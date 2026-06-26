# Subagentes del Guardián — Complemento de auditoría IA/LLM
### Extensión del Auditor Técnico (10.C) y del Auditor de PMF/Escala (10.E) para la capa de IA

> **Por qué existe:**
> Al sumar el subagente 6.F (Especialista IA/LLM) al Constructor, el Gate 4 quedó con un hueco: la skill `technical-mvp-audit` (10.C.1) audita arquitectura, código, tests, seguridad y docs, pero **no mira nada de la capa de IA** — ni los prompts, ni los evals, ni la seguridad LLM, ni el costo de tokens. Un MVP con IA podía pasar el Gate 4 sin que nadie auditara esa capa. Este complemento cierra ese hueco y, de paso, le da dueño al único umbral del sistema que estaba huérfano: **costo IA/LLM < 30% del precio**.

> **Relación con el Guardián:** este documento **extiende** `subagentes-guardian.md`. No reemplaza nada. El bloque de IA en 10.C solo se activa cuando el MVP tiene una feature de LLM (lo mismo que dispara a 6.F). Si el MVP no tiene IA, el bloque se marca N/A y el gate sigue con los criterios estándar.

---

## Principio rector (heredado del Guardián)

La calidad de la capa de IA tampoco es subjetiva. Cada criterio mapea uno a uno con un output verificable de 6.F. El Guardián no opina sobre si "el prompt está bueno" — verifica que los evals existan, que pasen el umbral, que la seguridad LLM esté revisada y que el costo proyectado entre en el margen.

**Regla de oro (heredada): un criterio bloqueante = RECHAZADO. Sin negociación.**

---

# EXTENSIÓN DE 10.C — AUDITOR TÉCNICO (Gate 4)

## SKILL 10.C.1 (extendida) — bloque AUDITORÍA DE CAPA IA/LLM

**Trigger:** Gate 4, cuando el MVP incluye al menos una feature de LLM. Se ejecuta junto con el resto de `technical-mvp-audit`.

**INPUT adicional obligatorio (solo si hay IA):** Matriz de ruteo (6.F.1) + Prompt y contexto (6.F.2) + Batería de evals y su reporte (6.F.3) + Security review LLM (6.F.4) + Controles de costo y confiabilidad (6.F.5).

**OUTPUT — se anexa al output de 10.C.1:**
```
AUDITORÍA TÉCNICA — BLOQUE IA/LLM | Gate: 4

─── APLICABILIDAD ───
✅/❌ ¿El MVP llama a un modelo de lenguaje?
  → Si NO: bloque N/A. El gate continúa con los 31 criterios estándar.
  → Si SÍ: aplicar los 17 criterios siguientes.

─── SELECCIÓN DE MODELO (6.F.1) ───
✅/❌ Cada tarea de IA con tier justificado + modelo primario + fallback
✅/❌ Costo IA proyectado < 30% del precio del producto
✅/❌ Capa de abstracción: 0 llamadas directas al SDK del proveedor en la lógica de negocio

─── PROMPT Y CONTEXTO (6.F.2) ───
✅/❌ Prompt del sistema versionado en repo (prompt-id@versión)
✅/❌ Hard cap de tokens aplicado al 100% de las llamadas
✅/❌ Salida estructurada validada contra schema antes de uso

─── EVALS (6.F.3) — BLOQUEANTE ───
✅/❌ Golden dataset ≥20 casos por tarea (happy + edge + adversarial)
✅/❌ Los evals existían ANTES del prompt (evidencia en historial o doc)
✅/❌ Harness ejecutable en CI, con umbral numérico y casos críticos al 100%
✅/❌ El prompt en producción pasa el umbral definido

─── SEGURIDAD LLM (6.F.4) — BLOQUEANTE ───
✅/❌ OWASP Top 10 for LLM: 0 issues críticos
✅/❌ OWASP Top 10 for LLM: 0 issues altos
✅/❌ Input del usuario aislado del system prompt + output tratado como no confiable
✅/❌ Casos de injection del golden set pasan al 100%

─── COSTO Y CONFIABILIDAD (6.F.5) ───
✅/❌ Cada tarea de IA con timeout + reintento + fallback determinista
✅/❌ 0 rutas que terminen en error crudo al usuario (siempre degradación)
✅/❌ Telemetría de costo/latencia activa con alerta de presupuesto

Resultado bloque IA: [N]/17 | Veredicto del bloque: GO / ITERAR
Correcciones: [qué] → [6.F.1 / 6.F.2 / 6.F.3 / 6.F.4 / 6.F.5 según corresponda]
```

**REGLAS críticas (bloqueantes, heredan el estándar de 10.C):**
- Evals ausentes o que no pasan el umbral = ❌ bloqueante. Sin evals no hay aprobación de feature de IA. (Espejo de la regla "tests existían antes del código".)
- Issue de seguridad LLM CRÍTICO o ALTO = ❌ bloqueante. Mismo estándar que OWASP de aplicación.
- Costo IA proyectado > 30% del precio = ❌ bloqueante → vuelve a 6.F.1 a rebajar tier o rediseñar la tarea.
- Tarea de IA sin fallback determinista = ❌ bloqueante.
- El bloque N/A solo es válido si se verificó que el MVP no llama a ningún LLM. "Tiene IA pero no la auditamos" no es N/A — es RECHAZADO.

**CRITERIO DE CALIDAD (medible):** Si el MVP tiene IA, el veredicto del Gate 4 no se emite sin los 5 inputs de 6.F. Los 17 criterios verificables con evidencia, no con opinión.

---

# EXTENSIÓN DE 10.E — AUDITOR DE PMF Y ESCALA (Gate 6 continuo)

## SKILL 10.E.1 (extendida) — vigilancia del costo IA en producción

**Por qué:** El costo IA proyectado en el Gate 4 es una estimación. En producción el costo real puede dispararse (más tokens por usuario, prompts que crecen, caché que no rinde). Si nadie lo vigila, se come el margen en silencio. El Gate 6 lo monitorea como una métrica de salud más.

**INPUT adicional (si el producto tiene IA):** Telemetría de costo IA del período (de 6.F.5, instrumentada por el Medidor) + precio vigente del producto.

**OUTPUT — se anexa al SEMÁFORO CORE de 10.E.1:**
```
─── SEMÁFORO IA (anexo al core) ───
Costo IA/LLM (% del precio): 🟢 <20% / 🟡 20-30% / 🔴 >30% (revienta margen)
  🔴 → optimizar ruteo (6.F.1) y caché/fallbacks (6.F.5), o revisar precio (Agente 4)

─── TENDENCIA IA (3 meses) ───
Costo IA % : [mes-2] → [mes-1] → [actual] — Tendencia: [subiendo/estable/bajando]
Costo por usuario activo: [mes-2] → [mes-1] → [actual]
```

**REGLA:** Costo IA > 30% del precio durante 2 meses consecutivos = señal de alerta CRÍTICA → revisión obligatoria de selección de modelo (6.F.1) y controles de costo (6.F.5) antes de escalar adquisición. No se aumenta presupuesto de growth con el costo IA en rojo.

**CRITERIO DE CALIDAD (medible):** El costo IA real se reporta en cada auditoría mensual de escala. Ningún veredicto de "ESCALAR" se emite con el costo IA en 🔴.

---

# HANDOFF DE LA RAMA IA (instancia de la skill transversal 10.0)

La skill 10.0 `inter-agent-handoff-validation` se instancia para la transferencia 6.F → 10.C con estos campos obligatorios:

```
VALIDACIÓN DE HANDOFF — Rama IA
De: Constructor 6.F | Para: Guardián 10.C

─── CAMPOS OBLIGATORIOS ───
✅/❌ Matriz de ruteo con costos proyectados (6.F.1)
✅/❌ Prompt versionado + estrategia de contexto (6.F.2)
✅/❌ Reporte de ejecución de evals (6.F.3)
✅/❌ Security review LLM (6.F.4)
✅/❌ Plan de costo y fallbacks (6.F.5)

COMPLETO: 10.C puede auditar el bloque IA
INCOMPLETO: falta [campo] → vuelve a 6.F antes del gate
```

---

## Definition of Done — Guardián con capa IA (addendum)

> Se suma a la Definition of Done de `subagentes-guardian.md`.

```
─── COBERTURA IA ───
□ 10.C audita las 5 dimensiones de 6.F cuando el MVP tiene IA
□ Evals (6.F.3) y seguridad LLM (6.F.4) son BLOQUEANTES en Gate 4
□ Costo IA < 30% auditado en Gate 4 (proyectado) y Gate 6 (real)
□ Handoff 6.F → 10.C validado con la skill 10.0
□ Si el MVP no tiene IA, el bloque se marca N/A sin penalizar el gate
□ "Tiene IA pero sin auditar" nunca cuenta como N/A — es RECHAZADO
```

---

## Pendiente de coordinación con el Medidor (Agente 9)

El costo IA en producción lo **audita** el Guardián (10.E, este complemento), pero lo **instrumenta** el Medidor. Para cerrar el circuito hay que sumar la métrica `costo_ia_por_usuario` y `costo_ia_pct_precio` a la skill de instrumentación del Medidor (9.A / 9.1 `metrics-framework`). Queda anotado para cuando se abra el archivo del Medidor — sin esto, 10.E no recibe el dato que necesita para el semáforo IA.

---

*SiriusLabs — miko.siriuslabs@gmail.com*
*Complemento de `subagentes-guardian.md`. El bloque IA de 10.C se activa solo cuando el MVP tiene una feature de LLM. Resuelve los hallazgos 1 y 2 de la auditoría de cobertura (Gate 4 sin auditoría de IA + umbral de costo IA sin dueño).*
