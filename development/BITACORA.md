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

**QA tecnico ejecutado posteriormente:**

Python quedo disponible (`Python 3.13.14`) y se ejecuto el QA tecnico de Fase A. Resultado: PASA. Se registro el detalle en `development/qa/fase-A.md` y se marcaron los criterios tecnicos en `development/ROADMAP.md`. Pendiente: aprobacion explicita de Lucia para cerrar Fase A.

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

**QA tecnico ejecutado:**

Se corrio QA Fase B sobre `proyecto-901-qa`: Shifu produjo `plan-maestro.md` y `_state.json`; Explorador produjo `fase-0/output.md` y `handoff.json` con INPUT_REQUEST ir-001 y veredicto INCIERTO-NO-VALIDADO. `validate-handoff.py` devolvio PASA. Detalle en `development/qa/fase-B.md`; criterios tecnicos marcados en ROADMAP.

**Aprobacion Lucía (2026-06-26):** Fase B cerrada. Siguiente paso: Fase C (Cartógrafo, Analista, Arquitecto de Negocio, Guardián Gate 0-2).

---

## 2026-06-26 — Fase C: cadena de decision + Gate 0-2

**Hecho:**

- Se creo `agents/2-cartografo/SKILL.md`.
- El Cartografo quedo documentado con skills obligatorias:
  - `2.1 competitive-landscape`
  - `2.2 solution-research`
- Se crearon plantillas de Cartografo:
  - `agents/2-cartografo/plantilla-output.md`
  - `agents/2-cartografo/plantilla-handoff.json`
- Se creo `agents/3-analista/SKILL.md`.
- El Analista quedo documentado con subagentes internos:
  - `3.A.1 market-sizing-rigorous`
  - `3.B.1 unit-economics-rigorous`
  - `3.C.1 technical-feasibility-rigorous`
  - `3.D.1 risk-analysis`
- Se creo `agents/4-arquitecto-negocio/SKILL.md`.
- Se definio que Negocio cierra `fase-2/` con:
  - `4.1 business-model-design`
  - `4.2 go-to-market-strategy`
  - `4.scope product-scope`
- Se creo la plantilla consolidada `agents/4-arquitecto-negocio/plantilla-output.md` para `fase-2/output.md`.
- Se creo `agents/4-arquitecto-negocio/plantilla-handoff.json` para el handoff `2->3`.
- Se creo `agents/10-guardian/SKILL.md` con:
  - `10.0 inter-agent-handoff-validation`
  - `10.A.1 business-problem-audit`
  - `10.A.2 market-viability-audit`
  - `10.A.3 business-model-audit`
- Se creo `agents/10-guardian/plantilla-gate-audit.md` como paquete consolidado para CEO.
- Se marcaron en `development/ROADMAP.md` las piezas construidas de Fase C.

**Decision relevante:**

La Fase C se construyo sin ejecutar QA. El QA se correra en una sesion aparte sobre `proyecto-902-qa`, con Fase 0 validada, para probar una cadena limpia `0->1->2` y el Gate 0-2 consolidado.

**Estado:**

Fase C construida. Pendiente: ejecutar QA de Fase C, registrar resultado en `development/qa/fase-C.md` y aprobacion de Lucía para cerrar la fase.

**QA tecnico ejecutado:**

Se corrio QA Fase C sobre `proyecto-902-qa` con Fase 0 validada como fixture tecnico. Resultados:

- `0->1`, `1->2` y `2->3` devuelven `PASA: handoff valido`.
- `fase-1/output.md` contiene `#mapa-competitivo`, `#research-soluciones` y `#gaps`.
- `fase-2/output.md` contiene Analista completo, Negocio y `#scope-producto`.
- `fase-2/gate-audit.md` contiene 10.A.1, 10.A.2 y 10.A.3 separadas.
- Se simulo blocker en 10.A.3 y el gate quedo en `ITERAR`, sin GO automatico.
- `_state.json` registra `gate_decisions[]` con `covers_phases: [0, 1, 2]`.

Detalle en `development/qa/fase-C.md`; criterios tecnicos marcados en ROADMAP.

**Aprobacion Lucía (2026-06-26):** Fase C cerrada. Siguiente paso: Fase D (Arquitecto UX 5.A + 5.B y Gate 3 reducido).

---

## 2026-06-26 — Fase D: UX + Gate 3 reducido

**Hecho:**

- Se creo `agents/5-arquitecto-ux/SKILL.md`.
- El Arquitecto UX quedo documentado con alcance reducido MVP-1:
  - `5.A.1 user-journey-mapping`
  - `5.B.1 wireframe-set`
- Se documento explicitamente que quedan fuera de scope:
  - 5.C Visual Designer
  - 5.D Accessibility Auditor
  - 5.E Design Handoff
  - Agente 6 Constructor
- Se definio que UX lee el scope desde `fase-2/output.md#scope-producto`, no desde `6.1`.
- Se creo `agents/5-arquitecto-ux/plantilla-output.md` con anclas:
  - `#user-journeys`
  - `#wireframes`
- Se extendio `agents/10-guardian/SKILL.md` con `10.B.1 ux-design-audit-reducido`.
- Se creo `agents/10-guardian/plantilla-gate-audit-3.md` para `fase-3/gate-audit.md`.
- Se marcaron en `development/ROADMAP.md` las piezas construidas de Fase D.

**Decision relevante:**

Fase 3 es terminal en MVP-1: el Arquitecto UX produce `fase-3/output.md` y no genera handoff hacia Constructor. El Gate 3 reducido audita coherencia entre problema, poblacion, scope, journeys y wireframes; no audita WCAG, design system, alta fidelidad ni handoff.

El QA de Fase D se correra en una sesion aparte sobre `proyecto-903-qa`, con Fases 0-2 completas y Gate 0-2 en `GO`.

**Estado:**

Fase D construida. Pendiente: ejecutar QA de Fase D, registrar resultado en `development/qa/fase-D.md` y aprobacion de Lucía para cerrar la fase.

**QA tecnico ejecutado:**

Se corrio QA Fase D sobre `proyecto-903-qa` con Fases 0-2 como fixture tecnico y Gate 0-2 en `GO`. Resultados:

- `2->3` devuelve `PASA: handoff valido`.
- UX usa `fase-2/output.md#scope-producto` y no pide `6.1` al Constructor.
- `fase-3/output.md` contiene `#user-journeys` y `#wireframes`.
- No existe `fase-3/handoff.json`, correcto porque Fase 3 es terminal en MVP-1.
- `fase-3/gate-audit.md` contiene Gate 3 reducido 10.B y audita coherencia UX.
- Gate 3 reducido no evalua WCAG, design system ni handoff.
- `_state.json` registra `gate_decisions[]` con `covers_phases: [3]`.

Detalle en `development/qa/fase-D.md`; criterios tecnicos marcados en ROADMAP. Pendiente: aprobacion explicita de Lucia para cerrar Fase D.
