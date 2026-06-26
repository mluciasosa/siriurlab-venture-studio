# Decisiones de Diseno

Registro vivo de decisiones de implementacion del MVP-1.

Formato:

- **Decision:** que se decidio.
- **Razon:** por que.
- **Impacto:** que cambia en el monorepo o en el flujo.

---

## 2026-06-26 — D001 — `development/` como bitacora separada de `runs/`

**Decision:** crear `development/` para documentar la construccion del Venture Engine.

**Razon:** `runs/` procesa proyectos como Nubia o Girasol; `development/` documenta como construimos el motor.

**Impacto:** roadmap, contexto, decisiones, bitacora y QA viven en `development/`.

---

## 2026-06-26 — D002 — Raiz del monorepo

**Decision:** construir dentro del repo actual `siriurlab-venture-studio`, no dentro de una subcarpeta `venture-engine/`.

**Razon:** el repo actual ya es la raiz real del proyecto.

**Impacto:** `agents/`, `contracts/`, `runs/`, `scripts/` y `development/` van al mismo nivel que `knowledge/`.

---

## 2026-06-26 — D003 — Estado en archivos

**Decision:** en MVP-1, el estado vive en archivos versionados por git.

**Razon:** evita infraestructura temprana y valida primero el contrato I/O.

**Impacto:** `_state.json`, `output.md`, `handoff.json`, `gate-audit.md`, `_cost-log.md` son la fuente de verdad.

---

## 2026-06-26 — D004 — Fases del MVP-1

**Decision:** `fase-N/` representa la fase del sistema, no un indice de corrida.

**Razon:** mantiene legible el pipeline manual.

**Impacto:**

- `fase-0/` = Explorador.
- `fase-1/` = Cartografo.
- `fase-2/` = Analista + Arquitecto de Negocio.
- `fase-3/` = UX reducido.

---

## 2026-06-26 — D005 — Shifu no tiene carpeta de fase

**Decision:** Shifu produce `plan-maestro.md` en la raiz del proyecto y actualiza `_state.json`.

**Razon:** Shifu orquesta; no es una fase de contenido.

**Impacto:** Fase 0 queda limpia como Explorador. `plan-maestro.md` es input inicial para la Fase 0.

---

## 2026-06-26 — D006 — Agente 4 entra en MVP-1 dentro de Fase 2

**Decision:** Arquitecto de Negocio entra en MVP-1, absorbido en `fase-2/` junto al Analista.

**Razon:** el modelo de negocio y GTM son inputs necesarios para UX y para estrategia futura; no se pueden saltear.

**Impacto:** no tiene carpeta ni gate propio. Corre despues del Analista y su output se consolida en `fase-2/output.md`.

---

## 2026-06-26 — D007 — Scope de producto lo produce Negocio

**Decision:** el scope de producto equivalente a 6.1 lo produce el Arquitecto de Negocio en `fase-2/`.

**Razon:** UX lo necesita antes del Constructor; el Constructor despues consume el scope, no lo crea.

**Impacto:** ancla canonica `fase-2/output.md#scope-producto`.

---

## 2026-06-26 — D008 — Gate 0-2 consolidado

**Decision:** en MVP-1 hay un solo paquete y una sola firma CEO para Gate 0-2.

**Razon:** en ejecucion manual, tres firmas seguidas agregan ceremonia sin ahorrar costo real.

**Impacto:** el Guardian corre 10.A.1, 10.A.2 y 10.A.3 por separado, pero el CEO firma una decision consolidada.

---

## 2026-06-26 — D009 — Auditorias internas no se colapsan

**Decision:** aunque el gate sea consolidado, las auditorias 10.A.1, 10.A.2 y 10.A.3 se mantienen separadas.

**Razon:** cada gate tiene criterios especificos; colapsarlos debilita el veredicto.

**Impacto:** `fase-2/gate-audit.md` contiene tres auditorias internas + recomendacion consolidada.

---

## 2026-06-26 — D010 — `gate_decisions[]` portable

**Decision:** modelar decisiones como una lista donde cada decision puede agrupar varias fases con `covers_phases`.

**Razon:** el mismo schema sirve para MVP manual y sistema autonomo.

**Impacto:** en MVP-1 se usa `covers_phases: [0, 1, 2]`; en autonomo podran existir decisiones separadas `[0]`, `[1]`, `[2]`.

---

## 2026-06-26 — D011 — Gate manual lo cierra CEO

**Decision:** en MVP-1 el Guardian recomienda, Lucía como CEO firma y registra la decision.

**Razon:** usar Shifu 0.2 para formalizar el gate agrega ceremonia en el modo manual.

**Impacto:** Shifu `gate-decision` queda diferido a automatizacion.

---

## 2026-06-26 — D012 — UX reducido en MVP-1

**Decision:** Fase 3 corre solo subagentes 5.A y 5.B.

**Razon:** alta fidelidad, accesibilidad completa y handoff solo tienen sentido si despues hay Constructor.

**Impacto:** 5.C, 5.D y 5.E quedan fuera de scope. Gate 3 reducido no audita WCAG ni design system.

---

## 2026-06-26 — D013 — IDs canonicos de skills

**Decision:** usar ID de subagente cuando existe; usar ID plano solo para agentes sin subagentes.

**Razon:** el subagente es la unidad que realmente ejecuta.

**Impacto:** `contracts/skill-io.md` debe incluir tabla de alias plano -> canonico para resolver documentacion vieja.

---

## 2026-06-26 — D014 — Handoffs con anclas verificables

**Decision:** cada fase produce un `output.md` consolidado con anclas, y `handoff.json` referencia esas anclas.

**Razon:** validar solo que un `skill_id` esta listado seria una validacion debil.

**Impacto:** `validate-handoff.py` debe verificar schema, skill requerido y existencia de ancla.

---

## 2026-06-26 — D015 — Cartografo 2.2 obligatorio

**Decision:** en MVP-1, Cartografo ejecuta 2.1 y 2.2.

**Razon:** el Analista necesita saber no solo quien compite, sino que hacen las soluciones existentes.

**Impacto:** el handoff 1->2 requiere landscape competitivo y research de soluciones.

---

## 2026-06-26 — D016 — INPUT_REQUEST en `_state.json`

**Decision:** input humano pendiente se registra en `_state.json` con envelope JSON minimo.

**Razon:** el agente no debe inventar datos del mundo real.

**Impacto:** cuando faltan entrevistas, accesos, decisiones o datos reales, el agente se detiene con `status: awaiting_input`.

---

## 2026-06-26 — D017 — Research secundario si, entrevistas no inventadas

**Decision:** los agentes pueden hacer research web y citar fuentes, pero entrevistas primarias son input humano.

**Razon:** fingir validacion primaria rompe la honestidad del sistema.

**Impacto:** para Nubia, hair-on-fire puede quedar INCIERTO/NO-VALIDADO hasta recibir entrevistas.

---

## 2026-06-26 — D018 — Idioma

**Decision:** outputs en espanol neutro LATAM; citas de usuarios Uruguay pueden ir en rioplatense.

**Razon:** el piloto apunta a LATAM con foco inicial Uruguay.

**Impacto:** agentes y outputs deben mantener ese registro.

---

## 2026-06-26 — D019 — `_cost-log.md` manual

**Decision:** registrar costos manualmente por fase.

**Razon:** es suficiente para distinguir si un venture cuesta USD 15 o USD 400; parsear logs de Cursor no aporta ahora.

**Impacto:** `cost-report.py` lee el formato manual y suma por fase + total.

---

## 2026-06-26 — D020 — Modo audit para Girasol

**Decision:** Girasol produce `gap-report.md` por fase, no el output normal.

**Razon:** en modo audit se compara lo que deberia existir contra lo que tiene el prototipo.

**Impacto:** `_state.json` arranca en la fase indicada por el seed; el prototipo debe entrar como archivo en `runs/`, no solo como link.

---

## 2026-06-26 — D021 — Duplicados de Drive

**Decision:** los archivos `knowledge/*(1).md` no son canonicos.

**Razon:** son artefactos de descarga de Drive.

**Impacto:** cuando toque limpieza, borrar duplicados `(1).md` y usar los nombres limpios.
