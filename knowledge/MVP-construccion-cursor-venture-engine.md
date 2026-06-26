# MVP de Validación en Cursor — SiriusLabs Venture Engine
## Documento de construcción: monorepo de agentes ejecutados a mano, gradual y escalable

> **Para qué sirve este documento:** Es la entrada de Cursor para construir el MVP. Cursor lee este documento + la documentación de los agentes (carpeta `knowledge/`) y construye el monorepo agente por agente. Define qué validamos, la estructura, los contratos, el formato de cada agente, el orden de construcción y las métricas de éxito.
>
> **Filosofía:** barato, gradual, escalable. Cero infraestructura al principio (sin Postgres, sin Inngest, sin ClickUp). El estado vive en archivos versionados por git. Lo que se construye hoy se reusa entero cuando el sistema pase a autónomo — solo cambia quién invoca a los agentes.

---

## 1. Qué valida este MVP (y qué NO)

El riesgo no es "¿la skill produce buen output?" — eso ya lo sabemos, las skills están bien escritas. El riesgo es el **encadenamiento**. Por eso el MVP está diseñado para estresar tres cosas:

**Validación 1 — Encadenamiento técnico.** ¿El output de un agente entra limpio al siguiente sin edición manual? Métrica brutal: **cuántas veces hay que editar a mano un handoff** para que el siguiente agente lo entienda. Meta: ≤1 por fase. Si son 5, el contrato de handoff está mal y es mejor saberlo ahora que con infra montada.

**Validación 2 — Gate e input humano.** ¿El Guardián produce un veredicto accionable que permite decidir GO/ITERAR/KILL en ≤2 minutos? Cuando un agente necesita un input del mundo real, ¿el pedido es claro y autocontenido? Lucía hace de CEO y de operador.

**Validación 3 — Viabilidad económica.** ¿Cuántos dólares de tokens cuesta llevar un venture de Fase 0 a Fase 3? Si un proyecto cuesta ~$15, el negocio cierra. Si cuesta $400, hay un problema de arquitectura de costos antes de escribir infra. Esta valida el **negocio**, no solo la técnica.

**Lo que el MVP NO hace:** no construye la app real (el Constructor llega en MVP-2), no monta infraestructura, no conecta servicios externos. Llega hasta Fase 3 (UX) en el primer run.

---

## 2. Principio de escalabilidad: el contrato I/O del agente no cambia nunca

La clave de que esto sea gradual: cada agente tiene un **protocolo de entrada** y un **protocolo de salida** fijos. Hoy el "transporte" son archivos en `runs/` y el invocador sos vos en Cursor. Mañana el transporte es Postgres y el invocador es Inngest. **El agente no se entera del cambio** — lee su input y escribe su output igual.

```
HOY (MVP):     Vos en Cursor → lee runs/ → ejecuta → escribe runs/
PASO 2:        Script run-phase.py → API Claude → escribe runs/ (sin copiar a mano)
PASO 3:        + ClickUp (MCP) como plano humano para gates e inputs
PASO 4:        Inngest invoca → Postgres reemplaza runs/ → autónomo
```

Cada paso reusa todo lo anterior. El monorepo, los SKILL.md y los contratos no se tiran nunca.

> **Sobre "hacer las conexiones dentro de la skill":** en el MVP NO. La skill produce su output + su handoff como archivos. La sincronización con ClickUp/servicios es un paso aparte (Paso 3). Fundirlas ahora te ata temprano y rompe la separación de planos. La skill se mantiene pura: entra contexto, sale output.

---

## 3. Estructura del monorepo

```
venture-engine/
├── README.md                        ← cómo correr un proyecto a mano
├── knowledge/                       ← la doc de agentes, cargada una vez (de Drive)
│   ├── equipo-agentes-venture-studio.md
│   ├── skills-especificacion-venture-engine.md
│   ├── subagentes-analista.md
│   ├── subagentes-arquitecto-ux.md
│   ├── subagentes-constructor-mvp.md
│   ├── subagentes-constructor-IA-LLM.md
│   ├── subagentes-motor-crecimiento.md
│   ├── subagentes-narrador.md
│   ├── subagentes-medidor.md
│   ├── subagentes-guardian.md
│   ├── subagentes-guardian-IA-LLM.md
│   ├── subagentes-medidor-IA-LLM.md
│   ├── patrones-estrategicos-tech.md
│   ├── ui-ux-design-patterns-2026.md
│   └── modelos-de-negocio-decision.md
├── agents/                          ← un SKILL.md por agente (lo que Cursor construye)
│   ├── 0-shifu/SKILL.md
│   ├── 1-explorador/SKILL.md
│   ├── 2-cartografo/SKILL.md
│   ├── 3-analista/SKILL.md
│   ├── 5-arquitecto-ux/SKILL.md
│   ├── 6-constructor/SKILL.md          (MVP-2)
│   └── 10-guardian/SKILL.md
├── contracts/                       ← los contratos que hacen funcionar el encadenamiento
│   ├── handoff-v2.schema.json
│   ├── state.schema.json
│   └── skill-io.md                  ← qué input obligatorio espera cada skill destino
├── runs/                            ← el "estado" del sistema = archivos versionados
│   ├── proyecto-001-nubia/
│   │   ├── _seed.md
│   │   ├── _state.json
│   │   ├── fase-0/ output.md, handoff.json
│   │   ├── fase-1/ ...
│   │   └── _cost-log.md
│   └── proyecto-002-girasol/
├── scripts/
│   ├── new-project.py               ← crea runs/proyecto-NNN/ desde un seed
│   ├── validate-handoff.py          ← simula la skill 10.0 a mano
│   └── cost-report.py               ← suma tokens/costo por corrida
└── docs/
    └── MVP-construccion-cursor.md   ← este documento
```

---

## 4. Los contratos (el corazón del MVP)

### 4.1 — `state.schema.json`: el estado del proyecto

```json
{
  "project_id": "proyecto-001-nubia",
  "mode": "create",                  // "create" | "audit"
  "current_phase": 0,
  "status": "in_progress",           // in_progress | awaiting_gate | awaiting_input | done | killed
  "phases": {
    "0": { "agent": "explorador", "status": "pending", "output_ref": null, "gate": null }
  },
  "pending_input_requests": [],
  "gate_decisions": [],
  "updated_at": "2026-06-23T00:00:00Z"
}
```

### 4.2 — `handoff-v2.schema.json`: el handoff entre agentes (referencias, no contenido inline)

```json
{
  "handoff_version": "2.0",
  "project_id": "proyecto-001-nubia",
  "from_agent": "explorador",
  "to_agent": "cartografo",
  "required_by_destination": ["1.1", "1.2"],
  "outputs": [
    { "skill_id": "1.1", "output_ref": "fase-0/output.md#problema", "type": "document" },
    { "skill_id": "1.2", "output_ref": "fase-0/output.md#poblacion", "type": "document" }
  ],
  "context_summary": "Resumen de 2-3 líneas de lo esencial que el siguiente agente necesita.",
  "flags": [],
  "created_at": "2026-06-23T00:00:00Z"
}
```

### 4.3 — `skill-io.md`: qué espera cada destino

Tabla que lista, por cada skill, su INPUT obligatorio. Se extrae directo de `skills-especificacion-venture-engine.md` y los subagentes. Es lo que `validate-handoff.py` usa para confirmar que un handoff trae lo que el destino necesita. Ejemplo:

```
SKILL 2.1 (Cartógrafo) requiere de la fase anterior:
  - 1.1 problema validado
  - 1.2 perfil de población
SKILL 3.A (Analista Mercado) requiere:
  - 2.1 landscape competitivo
  - 2.2 research de soluciones
```

---

## 5. Formato de cada agente — `agents/N-nombre/SKILL.md`

Cursor construye cada agente con esta plantilla uniforme. El contenido de identidad y skills se copia de la doc de `knowledge/`; los protocolos de entrada/salida son lo que hace que el agente "tome tareas".

```markdown
# AGENTE [N] — [Nombre]

## IDENTIDAD (system prompt del agente)
[Rol, objetivo, tono. Copiado de equipo-agentes-venture-studio.md]

## SKILLS QUE EJECUTA
[Lista de skills/subagentes con referencia a knowledge/. Para agentes con
subagentes, el agente los corre internamente en secuencia y entrega un solo
output consolidado — NO son tareas separadas.]

## PROTOCOLO DE ENTRADA (cómo toma su tarea)
1. Leer runs/[project_id]/_state.json → confirmar que esta fase está "pending"
2. Leer el handoff.json de la fase anterior
3. Leer los output.md referenciados en el handoff
4. Cargar de knowledge/ los documentos base que la skill necesita
5. VALIDAR input obligatorio (contracts/skill-io.md):
   - Si falta algo del mundo real (acceso, dato, decisión) → NO ejecutar.
     Escribir un INPUT_REQUEST en _state.json y parar. (Validación 2)

## PROTOCOLO DE SALIDA (cómo entrega)
1. Escribir el output en runs/[project_id]/fase-[N]/output.md
   (respetando la plantilla exacta de la skill, con secciones ─── ───)
2. Escribir runs/[project_id]/fase-[N]/handoff.json (contrato v2.0)
3. Actualizar _state.json: fase actual → "done", siguiente → "pending"
4. Registrar tokens usados en _cost-log.md (Validación 3)
5. Si la fase cierra un gate → status "awaiting_gate", invocar al Guardián

## REGLAS NO NEGOCIABLES
[De la skill]

## CRITERIO DE CALIDAD (medible)
[De la skill — el output no está "done" hasta cumplirlo]
```

---

## 6. El piloto: Nubia (modo "create", de cero)

### `runs/proyecto-001-nubia/_seed.md`

```
SEED DE PROYECTO — Nubia
─── PROBLEMA / SECTOR ───
App móvil para que sexólogos y psicólogos gestionen pacientes y les envíen
ejercicios y propuestas terapéuticas entre sesiones.
─── MODO ───
create (producto nuevo, de cero — pipeline completo desde Fase 0)
─── ALINEACIÓN ODS ───
ODS 3 — Salud y bienestar
─── MERCADO INICIAL ───
LATAM, foco inicial Uruguay
─── RESTRICCIÓN CRÍTICA ───
Datos de salud mental = altamente sensibles. El Analista de Riesgo (3.D) y la
capa de seguridad (6.D / 6.F.4) deben tratar privacidad y cumplimiento como
condición crítica desde Fase 0, no como detalle posterior.
─── INPUTS HUMANOS PROBABLES (a anticipar) ───
- Entrevistas con psicólogos/sexólogos reales (Explorador / Analista)
- Marco legal de datos de salud en UY/LATAM (Analista de Riesgo)
```

### Recorrido del primer run (MVP-1)

```
Fase 0  Shifu        → plan maestro + primera tarea
Fase 0  Explorador   → problema validado + perfil de población
        ↓ handoff (validado)
Fase 1  Cartógrafo   → landscape competitivo + research de soluciones
        ↓ handoff
Fase 2  Analista     → mercado + unit economics + viabilidad técnica + riesgo
        ↓ GATE 0-2 → Guardián 10.A audita → Lucía (CEO) decide GO/ITERAR/KILL
Fase 3  Arq. UX      → user journeys + IA + wireframes (sin construir)
        ↓ GATE 3 → Guardián 10.B audita → decisión
[FIN MVP-1]
```

El MVP-1 termina en Fase 3. No se construye la app. Se valida que el análisis y el diseño encadenan, que los gates funcionan y cuánto cuesta.

---

## 7. El segundo run: Girasol (modo "audit", producto existente)

Girasol ya tiene un prototipo web en desarrollo, hecho por proceso manual, sin análisis de mercado ni validación de modelo. El sistema entra en **modo auditoría**: no construye de cero, audita lo que existe contra los gates que se saltó.

### `runs/proyecto-002-girasol/_seed.md`

```
SEED DE PROYECTO — Girasol
─── MODO ───
audit (producto en desarrollo — entrada a mitad de pipeline)
─── ESTADO ACTUAL ───
Prototipo de app web existe. Proceso de construcción manual.
Sin análisis de mercado, sin validación de modelo de negocio, sin gates.
─── QUÉ SE PIDE ───
Auditoría retroactiva: correr Fase 1 (mercado) y Fase 2 (modelo) sobre el
producto existente, evaluar el prototipo contra el Gate 3 (UX), e identificar
los gaps que el proceso manual se saltó. Output: informe de gaps + recomendación.
─── ENTRADA ───
[Link/descripción del prototipo web actual — input humano del operador]
```

**Qué valida Girasol:** que Shifu sabe generar un plan que arranca a mitad de pipeline, que los agentes pueden auditar un artefacto existente (no solo crearlo), y que el Guardián produce un informe de gaps útil. Es el modo que vas a usar con clientes que ya tienen algo a medio hacer.

> Girasol corre **después** del primer run de Nubia. Primero validamos el pipeline completo de cero; después el modo auditoría.

---

## 8. Scripts de validación

**`validate-handoff.py`** — simula la skill 10.0. Toma un `handoff.json`, valida contra `handoff-v2.schema.json`, y confirma contra `skill-io.md` que todos los `required_by_destination` están presentes y referenciados. Devuelve PASA / FALLA con el campo faltante. **Se corre antes de cada cambio de fase.** Es el guardarraíl que mide la Validación 1.

**`cost-report.py`** — lee los `_cost-log.md` de un proyecto y suma tokens y dólares por fase y total. Es la Validación 3. (Cursor muestra el costo por mensaje; se registra a mano o se parsea del log.)

**`new-project.py`** — crea `runs/proyecto-NNN/` con su `_seed.md` y `_state.json` inicial.

---

## 9. Orden de construcción en Cursor (uno por uno)

```
PASO 1 — Base
  □ Esqueleto del monorepo (estructura §3)
  □ Cargar knowledge/ desde Drive
  □ contracts/ (los 3 archivos §4)
  □ scripts/ (los 3 §8)

PASO 2 — Agentes mínimos para el primer gate (en este orden)
  □ Agente 0 — Shifu (versión MVP: lee seed, genera plan maestro, crea tarea)
  □ Agente 1 — Explorador
  □ Agente 2 — Cartógrafo
  □ Agente 3 — Analista (con sus 4 subagentes internos)
  □ Agente 10 — Guardián (10.0 handoff + 10.A gates 0-2)

PASO 3 — Primer run de Nubia, Fase 0→2
  □ Correr a mano en Cursor, fase por fase
  □ Tras cada fase: validate-handoff.py
  □ Registrar: ediciones manuales de handoff, costo por fase
  □ Gate 2: Lucía decide como CEO

PASO 4 — Extender a Fase 3
  □ Agente 5 — Arquitecto UX (5 subagentes internos)
  □ Agente 10 — Guardián 10.B (gate 3)
  □ Correr Nubia Fase 3, medir

PASO 5 — Cierre de validación
  □ Reporte de las 3 validaciones
  □ Decisión: ¿seguimos a MVP-2 (Constructor) y a automatización (Paso 2 del §2)?
```

---

## 10. MVP-2 (después de validar el núcleo)

Solo si MVP-1 valida bien:
- **Agente 6 — Constructor** en sandbox (contenedor aislado, sin red interna, credenciales mínimas — según `arquitectura-mejorada-venture-engine.md` §7).
- Genera el código del MVP de Nubia en un repo de GitHub.
- Valida la parte cara y riesgosa: que un LLM genere código real, con tests, pasando el Gate 4 (incluido el bloque IA/LLM si Nubia usa IA).
- Acá también se valida el costo real de la fase más cara.

---

## 11. Métricas de éxito del MVP

```
─── VALIDACIÓN 1: ENCADENAMIENTO ───
□ Ediciones manuales de handoff por fase: ≤1 (meta)
□ Handoffs que pasan validate-handoff.py a la primera: ≥80%
□ Cada output cumple el criterio de calidad de su skill

─── VALIDACIÓN 2: GATE E INPUT HUMANO ───
□ Decisión de gate con el paquete del Guardián: ≤2 min
□ Input-requests autocontenidos (se entienden sin contexto extra): sí
□ El veredicto del Guardián es accionable (GO/ITERAR/KILL claro)

─── VALIDACIÓN 3: VIABILIDAD ECONÓMICA ───
□ Costo de tokens Fase 0→3 de un proyecto: registrado en $
□ Costo por fase: identificado (cuál fase es la más cara)
□ Proyección: ¿el costo por venture cierra contra el valor que genera?

─── DECISIÓN DE SALIDA ───
□ ¿El encadenamiento aguanta? → seguir a automatización (run-phase.py)
□ ¿Los gates funcionan? → seguir a ClickUp (plano humano)
□ ¿El costo cierra? → seguir a MVP-2 (Constructor) e infra
```

Si las tres validaciones pasan, validaste la estructura entera **sin haber gastado en infraestructura ni comprometido ninguna decisión de arquitectura**.

---

## 12. Definition of Done del MVP

```
□ Monorepo montado con la estructura del §3
□ knowledge/ cargado, contracts/ y scripts/ funcionando
□ Agentes 0,1,2,3,5,10 construidos como SKILL.md con protocolos I/O
□ Nubia corrió Fase 0→3 con handoffs validados
□ Las 3 validaciones medidas y registradas
□ Decisión informada sobre MVP-2 y automatización
□ (Opcional) Girasol corrió en modo auditoría
```

---

*SiriusLabs — miko.siriuslabs@gmail.com*
*Entrada de construcción para Cursor. Construir agente por agente siguiendo el §9. El contrato I/O de cada agente es portable: lo que se construye acá se reusa cuando el sistema pase a autónomo (Inngest + Postgres + ClickUp). Piloto: Nubia (create). Segundo run: Girasol (audit).*
