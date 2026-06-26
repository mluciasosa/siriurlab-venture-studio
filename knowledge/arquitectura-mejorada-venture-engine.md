# Arquitectura Mejorada — SiriusLabs Venture Engine
## Anexo de revisión a la propuesta de infraestructura autónoma

> **Estado:** Propuesta mejorada para decisión
> **Fecha:** Junio 2026
> **Base:** Anexo a "Propuesta de Arquitectura — Sistema autónomo de agentes" (Lucía / SiriusLabs)
> **Qué hace este documento:** Toma la propuesta original, aplica los 16 hallazgos de la revisión + el eje humano que faltaba, y resuelve la decisión de orquestación con una recomendación fundada. Mantiene lo que la propuesta tenía bien (cloud-agnostic, sin Kubernetes, sin AWS, Postgres como fuente de verdad, sin modelos locales).

---

## 1. La idea central: dos planos, no uno

La propuesta original modela el sistema como un flujo lineal disparado por mail, con el humano entrando solo en los gates. El problema estructural: colapsa la **capa de máquinas** y la **capa humana** en un solo plano, y descarta la operativa de 3 humanos + ClickUp que ya habíamos definido.

La mejora separa los dos planos:

```
┌─────────────────────────────────────────────────────────────┐
│  PLANO HUMANO  —  ClickUp (las 4 puertas)                    │
│  CEO: gates / deploys     Operadores: inputs / inicio / esc. │
└───────────────┬───────────────────────────▲─────────────────┘
                │ crea tarea (MCP)           │ resuelto → vuelve
                ▼                            │
┌───────────────────────────────────────────┴─────────────────┐
│  PLANO DE MÁQUINAS  —  Durable executor + Postgres + R2      │
│  cola · estado · handoffs agente↔agente · recuperación       │
│  workers (Claude API) · memoria · costos · observabilidad    │
└──────────────────────────────────────────────────────────────┘
```

**Regla de oro:** un agente nunca contacta a un humano por su cuenta. Cuando necesita una decisión o un input, el plano de máquinas **crea una tarea en ClickUp vía MCP** (el envelope que ya definimos en la operativa) asignada al rol correcto. Cuando el humano la resuelve, el control vuelve al plano de máquinas. Postgres hace lo que hace bien; ClickUp es la ventana por donde entran y salen los humanos. ClickUp **no** es la cola de máquinas (sus rate limits y su falta de transaccionalidad no sirven para eso).

Esto reconcilia las dos sesiones: la operativa humana (CEO + 2 operadores, 4 puertas) y la infraestructura autónoma.

---

## 2. La decisión de orquestación (la que pediste que resuelva)

La propuesta original elige construir el orquestador a mano (Shifu en Python puro + tabla de tareas + `enqueue_next`). El problema: todo lo difícil de un sistema distribuido —reintentos, recuperación tras caída, exactly-once, timers durables, dead-letter, idempotencia, detección de zombies— queda como código propio que hay que escribir, testear y mantener. Es exactamente el código donde más se sufre.

Esa categoría de problema ya está resuelta por los motores de **durable execution**. Comparo los dos caminos con honestidad.

### Opción A — Postgres + Python puro (la original, corregida)

| | |
|---|---|
| **A favor** | Cero dependencias nuevas. Visibilidad total del código. Curva cero (es Python que ya sabés). Suficiente para 1 proyecto serial. |
| **En contra** | Tenés que escribir vos: idempotencia, recuperación de tareas zombie, exactly-once en el enqueue, timers durables para SLAs/gates, dead-letter queue, detección de procesos caídos. Es el código más difícil de testear y el que más silenciosamente falla. |
| **Costo real** | Bajo en infra, **alto en tiempo de ingeniería y en bugs de recuperación** que aparecen recién en producción. |

### Opción B — Durable executor self-hosted (Temporal o Inngest)

| | |
|---|---|
| **A favor** | Reintentos, recuperación, exactly-once, timers durables, DLQ y visibilidad de ejecución vienen resueltos y battle-tested. Self-hostable → cero lock-in (cumple tu restricción). El flujo se modela como grafo con bifurcaciones, paralelismo y retrocesos (que es la forma real del Venture Engine), no como `next` lineal. |
| **En contra** | Un servicio más que operar. Curva de aprendizaje propia. Temporal es más pesado; Inngest es más liviano y arranca más rápido. |
| **Costo real** | Más setup inicial, **mucho menos código de sistema propio y muchos menos bugs de recuperación.** |

### Recomendación

**Para el MVP "probemos si anda": Opción B con Inngest, no Temporal.**

Razonamiento, dado que dijiste que no sabés el volumen y querés probar primero:

1. El cuello de botella de un sistema agéntico **no es el throughput, es la robustez de las ejecuciones largas** (un proyecto corre horas/días, con pausas humanas en el medio). Ahí un executor durable gana incluso a volumen 1: si el proceso cae a mitad de la fase 4, retoma exactamente donde estaba sin reprocesar ni regastar tokens. Con Python puro eso lo tenés que escribir vos y es lo más difícil de acertar.
2. **Inngest** sobre Temporal porque: arranca con mucho menos ceremonia, su modelo de "funciones con steps" encaja natural con "skills encadenadas", se self-hostea simple, y para tu volumen no necesitás la maquinaria pesada de Temporal. Si algún día tenés decenas de proyectos concurrentes y necesidades de control finas, migrar a Temporal es una decisión informada por datos reales — no una apuesta hoy.
3. **No construir el orquestador artesanal** te ahorra todo el Bloque 1-2 de bugs de recuperación. El tiempo que "ahorrás" con Python puro lo pagás con intereses ahí.

**Cuándo elegiría A en cambio:** si la prioridad absoluta es no aprender ninguna herramienta nueva y aceptás escribir la recuperación a mano con mucho cuidado y tests primero. Es viable a volumen 1, pero es la opción con más riesgo de bug silencioso.

> **Shifu se parte en dos**, en cualquiera de las opciones: el **Shifu-LLM** (skills 0.1/0.2/0.3, razonamiento: plan maestro, decisión de gate) y el **Shifu-runtime** (código: orquestación, recuperación, watchdog). La propuesta los mezclaba. El runtime es el workflow del executor; el LLM es invocado por ese workflow cuando hace falta razonar. Esto resuelve la pregunta abierta #5 de tu propuesta.

---

## 3. Topología de workers (resuelve puntos 9 y la pregunta de volumen)

La propuesta fija "1 proceso por agente", lo que con varios proyectos serializa cada agente y se vuelve cuello de botella; y usa `SKIP LOCKED`, que solo cobra sentido con varios workers compitiendo.

**Mejora — desacoplar la concurrencia del código:**
- El número de workers por agente es **configuración, no arquitectura**. Arrancás con concurrencia 1 (serial, que es lo que necesitás para "probar si anda") y subís el número cuando los proyectos concurrentes lo pidan — sin reescribir nada.
- Con un durable executor (Opción B) esto es un parámetro de concurrencia del workflow. Con Postgres puro (Opción A), ahí sí `SKIP LOCKED` + un pool configurable cobra sentido.
- Resultado: hoy corrés 1 proyecto serial; mañana subís un número y corrés 5 en paralelo. La decisión de volumen se difiere hasta tener datos reales, que es justo lo que pediste.

---

## 4. Storage (resuelve 7, 8, 12)

Separar lo que la propuesta mezclaba.

| Dato | Dónde | Cambio vs propuesta original |
|---|---|---|
| Estado: proyectos, tareas, gates | Postgres — tabla `tasks` **liviana** | Sacar los outputs grandes de la tabla de cola |
| Outputs de agentes (texto .md) | `outputs` como `TEXT` + ref, o R2 si >100KB | Era JSONB de 500KB en la tabla de cola → se infla y degrada el polling |
| Handoff entre agentes | Lleva **referencias**, no contenido inline | Era `content` inline + `storage_ref: null` → 3 copias del mismo texto |
| Archivos grandes / binarios | Cloudflare R2 | (igual que la propuesta) |
| Código del Constructor | GitHub | (igual) |
| Memoria semántica | pgvector, **particionada por cliente** | (ver §6) |
| Observabilidad | Langfuse | (igual, + alerting en §7) |

**Schema corregido (cola liviana + outputs aparte):**
```sql
CREATE TABLE tasks (
  task_id      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id   UUID NOT NULL REFERENCES projects(project_id),
  agent_id     TEXT NOT NULL,
  subagent_id  TEXT,
  status       TEXT NOT NULL DEFAULT 'pending',   -- pending|running|done|failed|dead
  depends_on   UUID[],                            -- grafo de dependencias, no 'next' lineal
  idempotency_key TEXT UNIQUE,                    -- enqueue exactly-once
  attempt      INT NOT NULL DEFAULT 0,
  lease_until  TIMESTAMPTZ,                        -- detección de zombies
  error_msg    TEXT,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
  started_at   TIMESTAMPTZ,
  completed_at TIMESTAMPTZ
);

CREATE TABLE outputs (
  output_id    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  task_id      UUID NOT NULL REFERENCES tasks(task_id),
  skill_id     TEXT NOT NULL,
  body         TEXT,            -- el .md; o NULL si vive en R2
  storage_ref  TEXT,            -- ref a R2 si es grande
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);
```
`depends_on`, `idempotency_key` y `lease_until` son los tres campos que faltaban para modelar el grafo, el exactly-once y la recuperación de zombies (puntos 6 y 11).

---

## 5. Contrato de handoff específico por destino (resuelve 12)

El schema genérico de la propuesta (`outputs[]` plano con contenido inline) no le permite a la skill 10.0 validar de verdad. La mejora: el contrato lleva **referencias** y declara qué espera el destino.

```json
{
  "handoff_version": "2.0",
  "project_id": "uuid",
  "from_agent": "explorador",
  "to_agent": "cartografo",
  "required_by_destination": ["1.1", "1.2"],
  "outputs": [
    { "skill_id": "1.1", "output_ref": "outputs/uuid-a", "type": "document" },
    { "skill_id": "1.2", "output_ref": "outputs/uuid-b", "type": "document" }
  ],
  "context_summary": "Problema validado: psicólogos LATAM, hair-on-fire, 45k profesionales.",
  "flags": [],
  "created_at": "2026-06-23T12:00:00Z"
}
```

La skill 10.0 valida que cada `skill_id` de `required_by_destination` esté presente y referenciado **antes** de que el executor encole la tarea destino. Si falta uno, no se encola y vuelve al origen. El `required_by_destination` se deriva del INPUT obligatorio de cada skill destino — ya está especificado en las skills, solo hay que codificarlo.

---

## 6. Memoria (resuelve 13 + engancha la Tarea 2 pendiente)

Tres tipos, con los aislamientos que faltaban:

- **De proyecto:** SELECT de los outputs anteriores del mismo `project_id`. Sin cambios.
- **De trabajo:** checkpoints intermedios por tarea para ejecuciones largas (con durable executor, esto es nativo del workflow). Sin cambios.
- **Semántica entre proyectos (la Tarea 2):** pgvector, pero con tres salvaguardas que la propuesta no tenía:
  1. **Partición por cliente** — los embeddings se filtran por `client_id`; nunca se inyecta contexto de un cliente en otro. (Riesgo de fuga: crítico.)
  2. **Scoring de confianza + filtro por sector** — no se inyecta "lo más similar" a secas; se filtra por relevancia de sector y se puntúa. Lo que funcionó en salud no se inyecta como verdad en fintech.
  3. **Validez temporal** — cada patrón tiene fecha y un mecanismo de caducidad; un aprendizaje viejo puede haber dejado de ser cierto. Esto se diseña en detalle en la Tarea 2.

---

## 7. Costos, seguridad y resiliencia (resuelve 1-5, 14)

**Costos (1) — el sistema se aplica su propio umbral.** Presupuesto de tokens por proyecto, hard cap, y kill-switch que pausa el pipeline y abre una tarea de ClickUp al CEO cuando se llega al límite. Langfuse observa; el cap controla. Coherente con 6.F.5 y el umbral "<30% del precio".

**Seguridad del Constructor (2).** Sandbox aislado: contenedor sin acceso a la red interna ni a Postgres, credenciales efímeras de alcance mínimo, output revisado antes de mergear. Aplica 6.D y 6.F.4 a la infra, no solo al MVP que el sistema construye.

**Secretos (3).** Gestor de secretos real (Infisical / Vault self-hosted, o secretos del runtime) con rotación. Las credenciales de clientes (Meta Ads, Stripe) nunca en texto plano ni en el repo.

**Trigger autenticado (4).** El disparo no confía en el `from` del mail: allowlist verificada + token firmado en el cuerpo. Mejor aún, en el modelo de dos planos el trigger natural es **una tarea de ClickUp** (un operador o el CEO inicia el proyecto), no un mail abierto al mundo. El mail queda como canal secundario, autenticado.

**Resiliencia (5, 14).** Backups automáticos de Postgres a R2 (diarios + WAL). Supervisión de procesos por el runtime/Docker `restart: always`, no por Shifu vigilándose a sí mismo. **Alerting** a operadores/CEO vía ClickUp/Gmail cuando: un worker muere, la cola se atasca, un proyecto lleva N horas bloqueado, o el costo llega al cap. Observar sin alertar es autopsia.

---

## 8. Plan de construcción reordenado (resuelve 15 — tests primero)

El principio del Venture Engine es "tests antes del código". La recuperación, la idempotencia y los reintentos son lo más difícil de testear → van primero, no en el Sprint 4.

```
SPRINT 0 — Decisión y esqueleto (2-3 días)
  · Validar Opción B (Inngest) con un spike: un workflow de 2 pasos que sobrevive una caída
  · Schema Postgres (tasks liviana + outputs + embeddings)
  · Tests de recuperación/idempotencia ANTES de los workers

SPRINT 1 — Un agente end-to-end (3-4 días)
  · Shifu-runtime (workflow) + Shifu-LLM (plan maestro)
  · Worker Explorador con el loop completo
  · Trigger autenticado (tarea ClickUp → arranca workflow)
  · Handoff v2.0 + validación 10.0

SPRINT 2 — Fase 0→2 + plano humano (1 semana)
  · Workers Cartógrafo y Analista (subagentes internos)
  · Gate 0 operativo: Guardián audita → crea tarea ClickUp al CEO → decisión vuelve al workflow
  · Pedido de input operativo: agente → tarea ClickUp a operador → resuelto → continúa
  · Kill-switch de costos + alerting

SPRINT 3 — Constructor sandboxeado + observabilidad (1 semana)
  · Worker Constructor en sandbox aislado, GitHub, secretos rotables
  · Langfuse en todos los workers
  · Backups Postgres → R2

SPRINT 4 — Sistema completo (2 semanas)
  · Workers restantes (UX, Motor, Narrador, Medidor)
  · Memoria semántica con pgvector (partición + scoring + validez) = Tarea 2
  · Deploy Hetzner + Docker Compose
  · Tests de integración del pipeline completo con caídas inyectadas
```

---

## 9. Deploy (mantiene lo bueno de la propuesta)

Sin cambios de fondo: **Hetzner + Docker Compose, cloud-agnostic, sin Kubernetes, sin AWS.** Se agrega al compose el durable executor (Inngest self-hosted) y el gestor de secretos. Costo infra estimado sigue en el orden de ~$25-30/mes + API variable (el executor self-hosted no agrega costo de licencia).

---

## 10. Tabla de resolución de los 16 hallazgos

| # | Hallazgo | Resuelto en |
|---|---|---|
| 0 | Eje humano desaparecido | §1 dos planos + §7 trigger |
| 1 | Sin control de costos | §7 kill-switch |
| 2 | Constructor inseguro | §7 sandbox |
| 3 | Secretos ausentes | §7 gestor de secretos |
| 4 | Trigger spoofeable | §7 trigger autenticado |
| 5 | SPOF sin recuperación | §7 backups + supervisión externa |
| 6 | Sin idempotencia/zombies | §2 executor + §4 idempotency_key, lease_until |
| 7 | Cola y outputs juntos | §4 tablas separadas |
| 8 | Texto en JSONB | §4 TEXT + ref |
| 9 | SKIP LOCKED vs topología | §3 concurrencia configurable |
| 10 | Polling | §2 executor push / LISTEN-NOTIFY |
| 11 | enqueue_next lineal | §4 depends_on (grafo) |
| 12 | Handoff inline genérico | §5 contrato por destino |
| 13 | Memoria sin aislamiento | §6 partición + scoring + validez |
| 14 | Observabilidad sin alerting | §7 alerting |
| 15 | Tests al final | §8 tests primero |
| 16 | Timeout de gate | §7 pausa sin costo + recordatorio SLA |

---

## 11. Lo que queda como decisión tuya

- **Inngest vs Temporal vs Python puro:** recomiendo **Inngest** para el MVP (§2). Si querés cero herramientas nuevas, Python puro es viable a volumen 1 pero con el riesgo de los bugs de recuperación. El spike del Sprint 0 confirma la decisión con poco costo antes de comprometerse.
- **Volumen:** diferido por diseño (§3). Arranca serial, escala por configuración.
- **Mail como trigger:** queda como secundario; el primario es una tarea de ClickUp.

---

*SiriusLabs — miko.siriuslabs@gmail.com*
*Anexo de revisión a la propuesta de arquitectura. Resuelve los 16 hallazgos + el eje humano de dos planos. Recomendación de orquestación: Inngest self-hosted, validado con un spike en el Sprint 0.*
