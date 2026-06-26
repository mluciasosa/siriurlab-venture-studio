# Bitacora de Construccion

Log cronologico de como construimos el SiriusLabs Venture Engine.

## Reglas

- Registrar una nota corta cada vez que se construya una pieza relevante.
- Marcar checkboxes en `development/ROADMAP.md` cuando una pieza quede implementada.
- No cerrar una fase hasta que Lucía corra y apruebe su QA.
- Registrar el resultado aprobado en `development/qa/fase-X.md`.
- Si cambia el plan, actualizar `development/ROADMAP.md`; no dejar decisiones solo en el chat.
- Las decisiones estables van en `development/DECISIONES.md`.

---

## 2026-06-26 — Setup de bitacora y roadmap

**Hecho:**

- Se definio `development/` como carpeta de bitacora del proceso de construccion.
- Se separo explicitamente `development/` de `runs/`.
- Se formalizo el roadmap de build del MVP-1 en cinco fases:
  - Fase A: esqueleto y contratos.
  - Fase B: Shifu + Explorador.
  - Fase C: cadena de decision + Gate 0-2.
  - Fase D: UX + Gate 3 reducido.
  - Fase E: piloto Nubia + medicion.
- Se registraron las decisiones de implementacion tomadas hasta ahora.
- Se crearon Cursor Rules del proyecto en `.cursor/rules/` para mantener las convenciones.

**Decision relevante:**

El primer paso de construccion real sera Fase A del roadmap. Antes de eso, esta carpeta deja fijado el plan y la forma de documentar avances, QA y cambios.

**Estado:**

Roadmap inicial creado. Pendiente: iniciar Fase A cuando Lucía lo apruebe.

---

## 2026-06-26 — Fase A: esqueleto, contratos y scripts

**Hecho:**

- Se creo la estructura base `agents/`, `contracts/`, `runs/`, `scripts/`.
- Se agregaron contratos:
  - `contracts/state.schema.json`
  - `contracts/handoff-v2.schema.json`
  - `contracts/skill-io.md`
  - `contracts/plantillas-por-fase.md`
- Se implementaron scripts con Python estandar:
  - `scripts/new-project.py`
  - `scripts/validate-handoff.py`
  - `scripts/cost-report.py`
- Se agregaron fixtures para QA:
  - handoff valido
  - handoff con skill faltante
  - handoff con ancla faltante
  - cost log de ejemplo
- Se creo `README.md` con instrucciones de QA manual para Fase A.
- Se marcaron en `development/ROADMAP.md` las piezas construidas de Fase A.

**Decision relevante:**

Los scripts se implementaron sin dependencias externas. La validacion de handoff cubre forma minima, required skills, alias canonicos y existencia de anclas en markdown.

**Estado:**

Fase A construida. Pendiente: ejecutar QA completo, registrar resultado en `development/qa/fase-A.md` y aprobacion de Lucía para cerrar la fase.

**QA tecnico intentado:**

Se intentaron ejecutar los comandos de QA con `python` y `py`, pero el entorno local no tiene Python disponible en PATH. La Fase A queda construida, pero no aprobada. Para cerrar la fase, instalar/habilitar Python 3 o correr los comandos documentados en una terminal con Python disponible.

---

## 2026-06-26 — Fase B: Shifu + Explorador

**Hecho:**

- Se creo `agents/0-shifu/SKILL.md`.
- Shifu quedo documentado como orquestador sin carpeta de fase.
- Shifu ejecuta en MVP-1:
  - `0.1 project-kickoff`
  - `0.3 task-routing`
- Se dejo fuera de scope `0.2 gate-decision`, diferido a automatizacion.
- Se definio la plantilla de `plan-maestro.md` dentro del `SKILL.md` de Shifu.
- Se creo `agents/1-explorador/SKILL.md`.
- El Explorador quedo documentado con skills:
  - `1.1 problem-discovery`
  - `1.2 population-profiling`
- Se creo `agents/1-explorador/plantilla-output.md` con anclas:
  - `#problema`
  - `#poblacion`
  - `#hair-on-fire`
  - `#fuentes`
- Se creo `agents/1-explorador/plantilla-handoff.json` para el handoff `0->1`.
- Se documento el comportamiento ante falta de entrevistas primarias: `INPUT_REQUEST`, `awaiting_input`, hair-on-fire `INCIERTO/NO-VALIDADO`.
- Se marcaron en `development/ROADMAP.md` las piezas construidas de Fase B.

**Decision relevante:**

El handoff de Fase 0 usa referencias relativas al archivo `fase-0/handoff.json`, por ejemplo `output.md#problema`, para que `scripts/validate-handoff.py` pueda resolver las anclas desde la carpeta de la fase.

**Estado:**

Fase B construida. Pendiente: ejecutar QA de Fase B cuando Python este disponible y registrar resultado en `development/qa/fase-B.md`. Fase B no queda aprobada hasta que Lucía corra y apruebe ese QA.
