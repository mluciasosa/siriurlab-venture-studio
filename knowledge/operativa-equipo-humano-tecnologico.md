# Operativa del Equipo Humano-Tecnológico — SiriusLabs Venture Engine
### Cómo se comunican los agentes, cómo delegan tareas, y cómo los 3 humanos operan junto a ellos

> **Propósito:** Define la capa operativa que convierte los 11 agentes (0-10) en un equipo que ejecuta de verdad, con tres humanos en el loop. Es el manual de operación: planos de comunicación, intervención humana, roles, formatos de mensaje, infraestructura y el plan de implementación por fases.

---

## 1. Configuración del equipo

**Humanos (3):**
- **CEO / Decisor** — aprueba los gates (GO / KILL / ITERAR), autoriza deploys a producción, decide pivots. Es el único que cierra un gate.
- **Operador A** y **Operador B** — resuelven los pedidos de input que los agentes no pueden conseguir solos (accesos, datos de cliente, entrevistas reales, decisiones de negocio menores, contenido aprobado), inician proyectos y tareas ad-hoc, y atienden escalaciones.

**Agentes (11 + subagentes):** operan en **modo autónomo bidireccional**:
- Corren el pipeline por sí mismos (una skill produce el input de la siguiente).
- Piden ayuda humana cuando la necesitan (emiten un pedido de input y esperan).
- También ejecutan tareas que un humano les indica directamente (trabajo ad-hoc fuera del pipeline).

**Orquestador (Agente 0 / Shifu):** el dispatcher. Asigna trabajo, fija dependencias, vigila bloqueos y escala a humanos. Ningún agente suelto contacta a un humano: lo hace a través de Shifu o publicando un pedido formal en el sistema.

---

## 2. Los tres planos de comunicación

```
┌─────────────────────────────────────────────────────────┐
│  PLANO 3 — HUMANO ↔ SISTEMA                              │
│  CEO (gates/deploys) · Operadores (inputs/inicio/escala) │
└───────────────────────────┬─────────────────────────────┘
                            │ (vía ClickUp)
┌───────────────────────────┴─────────────────────────────┐
│  PLANO 2 — ORQUESTADOR → AGENTES                         │
│  Shifu asigna, secuencia, vigila dependencias y bloqueos │
└───────────────────────────┬─────────────────────────────┘
                            │
┌───────────────────────────┴─────────────────────────────┐
│  PLANO 1 — AGENTE ↔ AGENTE                               │
│  Handoffs encadenados, validados por la skill 10.0       │
│  Artefacto → Drive · Estado → ClickUp                    │
└─────────────────────────────────────────────────────────┘
```

### Plano 1 — Agente ↔ Agente (handoff)
El contrato ya existe: el output en plantilla de una skill es el input de la siguiente, validado por `inter-agent-handoff-validation` (10.0). En la operativa:
- El **artefacto** (el .md producido) vive en **Drive** (fuente canónica).
- El **estado del handoff** vive como **tarea en ClickUp**: de quién, para quién, bloqueante o no, link al artefacto.
- **Mover la tarea de fase = ejecutar el handoff.** La validación 10.0 corre como checklist obligatorio antes de permitir el movimiento. Si falta un campo, la tarea no avanza.

### Plano 2 — Orquestador → Agentes (delegación)
Shifu (Agente 0):
- Crea las tareas de cada fase y asigna qué skill/subagente las ejecuta.
- Fija dependencias: no se entra a la fase N+1 sin el Done + el gate de la fase N aprobado.
- Vigila bloqueos y SLAs. Cuando una tarea queda en `BLOQUEADA-NECESITA-HUMANO`, Shifu enruta el pedido al humano correcto.
- Es el punto único de escalación: traduce un problema de un agente en una acción concreta para un humano.

### Plano 3 — Humano ↔ Sistema
Los humanos no "hablan con un agente" en abstracto: interactúan con **tareas en ClickUp**. Cuatro tipos de puerta (sección 3).

---

## 3. Los cuatro tipos de intervención humana

| Tipo | Quién | Bloqueante | Disparador |
|---|---|---|---|
| **Aprobación de gate** | CEO | Sí | El Guardián emite veredicto en un gate (0-6) o se pide deploy a producción |
| **Pedido de input** | Operador | A veces | Un agente necesita algo del mundo real que no puede generar solo |
| **Inicio de tarea/proyecto** | Operador / CEO | No | Arranca un proyecto nuevo o una solicitud ad-hoc |
| **Escalación / excepción** | Operador de guardia | Según caso | Un agente se traba, hay ambigüedad o vence un SLA |

**Pedido de input — ejemplos concretos:** acceso a la cuenta de Meta Ads del cliente, credenciales de un sistema, 5 entrevistas con usuarios reales, el presupuesto real de adquisición, aprobación de una creativa, una decisión de pricing, validación de un dato de campo.

**Inicio de tarea — bidireccional:** el sistema acepta trabajo que arranca el pipeline (un proyecto nuevo) y trabajo ad-hoc que un humano le encarga a un agente puntual ("Narrador, reescribime estos 3 emails"). Ambos entran como tarea en ClickUp.

---

## 4. Roles humanos — RACI por evento

> R = ejecuta · A = aprueba (única firma) · C = consultado · I = informado

| Evento | CEO | Operador A | Operador B | Agentes |
|---|---|---|---|---|
| Iniciar proyecto | A | R | R | I |
| Resolver pedido de input | I | R | R | R (solicita) |
| Gate 0-2 (negocio) | **A** | C | C | R (10.A audita) |
| Gate 3 (UX) | **A** | C | — | R (10.B audita) |
| Gate 4 (técnico + IA) | **A** | I | I | R (10.C audita) |
| Gate 5 (growth / PMF) | **A** | R | R | R (10.D audita) |
| Gate 6 (escala) | **A** | R | R | R (10.E audita) |
| Deploy a producción | **A** | R | — | R (6.D prepara) |
| Decisión KILL | **A** | C | C | R (Guardián + Analista) |

**Reparto sugerido de los 2 operadores** (a ajustar): Operador A en el eje negocio / growth / contenido (inputs de mercado, validaciones de canal, aprobación de creativas, entrevistas); Operador B en el eje técnico / datos / accesos (credenciales, integraciones, datos de cliente, instrumentación). Alternativa: turnos de guardia semanales donde uno es el "operador on-call" que atiende toda la cola.

---

## 5. Formato de mensaje estándar (envelopes)

Todo mensaje del sistema viaja en un sobre con campos fijos. Esto hace que la skill 10.0 pueda validar y que cualquier humano entienda una tarea sin contexto previo.

### 5.1 — Handoff entre agentes
```
HANDOFF
─── RUTA ───
Task-ID: [VE-PROY-FASE-NN]
De: [agente/skill origen]  →  Para: [agente/skill destino]
Fase: [0-6]  |  Bloqueante: [sí/no]
─── ARTEFACTO ───
Output: [link Drive al .md]  |  Plantilla: [nombre de skill]
─── VALIDACIÓN 10.0 ───
✅/❌ Campos obligatorios del input destino presentes
Si ❌ → la tarea no avanza, vuelve al origen
```

### 5.2 — Pedido de input humano (Human Input Request)
```
PEDIDO DE INPUT
─── ORIGEN ───
Task-ID: [...]  |  Agente que pide: [...]  |  Fase: [...]
─── QUÉ SE NECESITA ───
Pedido: [una oración clara — qué, no por qué técnico]
Por qué bloquea: [qué no puede continuar sin esto]
Formato esperado: [archivo / acceso / texto / decisión sí-no]
─── GESTIÓN ───
Asignado a: [Operador A/B]  |  Bloqueante: [sí/no]
SLA: [deadline]  |  Estado: [pendiente/resuelto]
─── RESPUESTA ───
[el operador completa acá o adjunta el recurso]
```

### 5.3 — Decisión de gate (para el CEO)
```
DECISIÓN DE GATE — Gate [N]
─── VEREDICTO DEL GUARDIÁN ───
Resultado auditoría: [N/total criterios]  |  Recomendación: [GO/ITERAR/KILL]
Bloqueantes abiertos: [lista o "ninguno"]
─── RESUMEN PARA DECIDIR (3 líneas) ───
[lo mínimo que el CEO necesita para firmar]
Los 3 números que importan: [ej. SOM / LTV-CAC / Sean Ellis]
─── FIRMA CEO ───
Decisión: [ GO / ITERAR / KILL ]  |  Fecha: [...]
Si KILL o ITERAR: [qué se documenta / qué se corrige]
```

### 5.4 — Escalación
```
ESCALACIÓN
Task-ID: [...]  |  Severidad: [alta/media]
Síntoma: [qué pasó]  |  Agente afectado: [...]
Acción pedida: [qué necesita el operador de guardia que se haga]
SLA vencido: [sí/no]
```

---

## 6. Infraestructura (sobre lo que ya está conectado)

| Capa | Herramienta | Rol |
|---|---|---|
| **Tareas + comunicación** | **ClickUp** (MCP) | Columna vertebral. Tareas, estados, asignados, comentarios (hilo humano↔agente), gates como milestones. Los agentes leen/crean/mueven/comentan tareas por MCP. |
| **Artefactos** | Google Drive | Repositorio canónico de los .md (ya lo es). Cada tarea linkea su artefacto. |
| **Notificaciones + agenda** | Gmail + Calendar | Avisos de gate y de SLA al CEO/operadores; agenda de reviews semanales. |
| **Estado + memoria** | Supabase | (Opcional) estado estructurado del pipeline y base de la memoria entre proyectos (Tarea 2). |
| **Ejecución de agentes** | Claude (API / Code / Cowork) | Donde corren las skills. Cowork con MCP de ClickUp permite el modo autónomo bidireccional. |

**Por qué ClickUp y no un tablero manual:** está conectado por MCP, así que los agentes son ciudadanos de primera del tablero — crean el pedido de input, mueven su propia tarea a "en review", comentan el resultado. El humano y el agente trabajan sobre el mismo objeto. No hay copia-pega ni sincronización a mano.

---

## 7. Máquina de estados de una tarea

```
BACKLOG
  │ (Shifu asigna)
  ▼
TODO ──► IN_PROGRESS ──► IN_REVIEW_GATE ──► AWAITING_CEO ──► DONE
              │  ▲              (Guardián)      (decisión)      │
              ▼  │                                              ├─► KILLED
       BLOQUEADA-NECESITA-HUMANO                                └─► ITERAR ──┐
              │  (pedido de input resuelto)                                  │
              └──────────────────────────────────────────────► IN_PROGRESS ◄┘
```

**Tipos de tarea (ClickUp task types / tags):** `FASE` · `SKILL_RUN` · `GATE` (milestone, approver = CEO) · `INPUT_REQUEST` (asignada a operador) · `ESCALATION` · `PROJECT_SEED`.

**Campos personalizados:** `agente_responsable` · `fase (0-6)` · `artefacto_drive` · `tipo_intervencion` · `bloqueante` · `sla_deadline` · `gate_veredicto`.

**Automatizaciones clave:**
- Tarea → `IN_REVIEW_GATE`: crea subtarea de auditoría para el Guardián correspondiente.
- Tarea → `AWAITING_CEO`: notifica al CEO (email + ClickUp) con el envelope 5.3.
- Se crea `INPUT_REQUEST`: asigna al operador de guardia + arranca el timer de SLA.
- SLA vencido: dispara `ESCALATION`.
- `FASE` → `DONE` con gate aprobado: desbloquea la fase siguiente (dependencia).

---

## 8. SLAs y cadencia

**SLAs:**
- Pedido de input bloqueante de pipeline: **< 4 h hábiles**.
- Pedido de input no bloqueante: **< 24 h hábiles**.
- Revisión de gate por el CEO: **< 48 h**.
- Escalación: **inmediata** (operador on-call).

**Cadencia:**
- **Diaria (async):** los operadores vacían la cola de `INPUT_REQUEST`; Shifu publica el estado del pipeline (qué proyecto, qué fase, qué bloqueos).
- **Por gate:** el CEO revisa el paquete de decisión y firma.
- **Semanal (30-45 min):** review de pipeline — proyectos × fase, bloqueos recurrentes, métricas de salud, y aprendizajes para la memoria entre proyectos.

---

## 9. Plan de trabajo — implementación por fases

```
F1  MODELO OPERATIVO        ← este documento
F2  INFRAESTRUCTURA CLICKUP
F3  PROTOCOLOS + SLAs + RUNBOOK
F4  PILOTO CON 1 PROYECTO REAL
F5  ITERACIÓN + FORMALIZACIÓN
```

**F1 — Modelo operativo** *(este documento)*
- Entregable: roles, RACI, planos de comunicación, envelopes, infraestructura. ✅ al aprobar este doc.

**F2 — Infraestructura ClickUp**
- Crear el Space del Venture Engine; estructura Folder = proyecto, List = fase (0-6).
- Configurar estados (sección 7), tipos de tarea, campos personalizados.
- Conectar cada tarea con su artefacto en Drive.
- Cargar las automatizaciones de gate, input-request y dependencias.
- Plantillas de tarea por tipo (SKILL_RUN, GATE, INPUT_REQUEST).
- Entregable: workspace operativo vacío listo para correr un proyecto.

**F3 — Protocolos + SLAs + runbook**
- Documento corto para los 3 humanos: qué hace cada uno, cómo responde un pedido de input, cómo firma un gate, cómo escala.
- Tabla de SLAs activa con timers en ClickUp.
- Entregable: runbook de 1-2 páginas por rol.

**F4 — Piloto con un proyecto real**
- Elegir un proyecto chico y acotado para correr el ciclo completo (sugerencia: un proyecto del Venture Engine de bajo riesgo, o un encargo ad-hoc).
- Correr de Fase 0 a un primer gate, midiendo: dónde se traba, cuántos input-requests salen, si los SLAs se cumplen.
- Entregable: bitácora del piloto con fricciones detectadas.

**F5 — Iteración + formalización**
- Ajustar estados, SLAs, reparto de operadores y automatizaciones según el piloto.
- Conectar con la memoria entre proyectos (Tarea 2): los aprendizajes del review semanal y de cada KILL/GO alimentan la base.
- Entregable: operativa formalizada + integrada al CONTEXTO maestro.

---

## 10. Definition of Done — Capa operativa

```
─── MODELO (F1) ───
□ Roles y RACI definidos y aceptados por los 3 humanos
□ Cuatro tipos de intervención humana con dueño y SLA
□ Envelopes estándar (handoff, input-request, gate, escalation)

─── INFRAESTRUCTURA (F2) ───
□ Space/Folders/Lists del Venture Engine montados en ClickUp
□ Estados, tipos de tarea y campos personalizados configurados
□ Automatizaciones de gate, input-request y dependencias activas
□ Cada tarea linkea su artefacto en Drive
□ Agentes pueden leer/crear/mover/comentar tareas vía MCP

─── PROTOCOLOS (F3) ───
□ Runbook por rol (CEO, Operador A, Operador B)
□ SLAs con timers activos
□ Ruta de escalación probada

─── VALIDACIÓN (F4-F5) ───
□ Un proyecto corrió de Fase 0 a un gate de punta a punta
□ Input-requests resueltos dentro de SLA en el piloto
□ Fricciones documentadas y ajustadas
□ Operativa integrada con la memoria entre proyectos
```

---

*SiriusLabs — miko.siriuslabs@gmail.com*
*Capa operativa del Venture Engine. Modo de ejecución: agentes autónomos bidireccionales + 3 humanos (1 CEO decisor + 2 operadores). Columna vertebral: ClickUp. Actualizar tras el piloto (F4) y al conectar la memoria entre proyectos.*
