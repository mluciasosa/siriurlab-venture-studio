# Prompt — Construcción Agente 7: Motor de Crecimiento

> Copiar y pegar esto al inicio de un chat nuevo para continuar el Venture Engine.

---

## PROMPT

Estamos construyendo el **SiriusLabs Venture Engine** — un equipo de 11 agentes especializados para crear, validar, lanzar y escalar plataformas tecnológicas con impacto en los ODS de la ONU.

**Tu tarea en esta sesión:** Construir el **Agente 7 — Motor de Crecimiento ("El Motor")** siguiendo exactamente el mismo patrón con el que ya construimos los Agentes 5 y 6.

---

## Contexto del proyecto

**Drive de la Knowledge Base:** carpeta `1mdBwlVTaoEhCzXUw40cTUY9hyDJzM8b-` (miko.siriuslabs@gmail.com)

**Archivos de referencia obligatoria en Drive:**
- `CONTEXTO-PROYECTO-venture-engine.md` (ID: `12zEdW0GOOST392J5-SGU_k2n8g3sWHOH`) — estado completo del proyecto, leer primero
- `equipo-agentes-venture-studio.md` (ID: `1haBD8cDVkfSuBxd-xp-0abI_gydNNExc`) — spec del equipo completo con fases y gates
- `skills-especificacion-venture-engine.md` (ID: `1jmOyJXTOn29s-mIVfOZUpH-ZlG-S_RQZ`) — las 22 skills ya definidas, incluidas las del Agente 7
- `subagentes-constructor-mvp.md` (ID: `1TxgAFr0UwVi6_XCUzJAWCUczNHSm0FyC`) — referencia del patrón del Agente 6 (Constructor)
- `subagentes-arquitecto-ux.md` (ID: `1A8AJiDeJrB7qU6XVZ1OPO8oG0k22PMHN`) — referencia del patrón del Agente 5 (UX)

---

## El Agente 7 en el sistema

**Nombre:** Motor de Crecimiento ("El Motor")
**Familia:** Ejecución
**Fases:** Fase 5 (Lanzamiento) y Fase 6 (Escala)

**Función central:** Diseñar y ejecutar la estrategia de go-to-market, lanzamiento y crecimiento sostenible. Define el canal primario, construye el motor de adquisición, valida la demanda con $500 antes de escalar, y diseña el growth playbook post PMF.

**Skills ya definidas en el archivo maestro (punto de partida — ampliar y profundizar):**
- `7.1 — launch-strategy`: estrategia de lanzamiento 90 días, validación $500, primer cliente pagador, canales orgánicos antes de pagados
- `7.2 — growth-playbook`: motor de crecimiento post PMF, loops, canales de escala, palancas de retención y expansión

---

## Lo que tenés que construir

Seguir el mismo patrón que los Agentes 5 y 6:

### 1. Decidir si el Agente 7 necesita subagentes

**Áreas candidatas:**
- Especialista en canales orgánicos (SEO, comunidades, redes)
- Especialista en canales pagados (Meta Ads, Google Ads, LinkedIn Ads)
- Especialista en growth loops y retención (PLG, onboarding, activación)
- Especialista en email marketing y lifecycle (secuencias, automatizaciones)
- Analista de canales y experimentos de adquisición (A/B en canales, CAC por canal)

### 2. Para cada subagente, escribir con esta estructura:

```
SUBAGENTE [N.X] — NOMBRE

Función central: [2-3 oraciones]
Por qué es necesario: [justificación de la especialización]

SKILL [N.X.N] — nombre-skill

Propósito: [qué hace en una oración]
Trigger: [palabras clave exactas]

INPUT obligatorio:
- [campo — de dónde viene]

OUTPUT:
[plantilla exacta con secciones ─── NOMBRE ───]

FLUJO:
1. [paso específico]

REGLAS:
- [lo que no se negocia]

CRITERIO DE CALIDAD:
- [medible]
```

### 3. Definition of Done del área de crecimiento

```
DEFINITION OF DONE — CRECIMIENTO / LANZAMIENTO
─── VALIDACIÓN DE DEMANDA ───
□ [criterio verificable]
─── LANZAMIENTO ───
□ [criterio]
─── MÉTRICAS DE TRACCIÓN ───
□ [criterio]
─── GATE 5 ───
□ PMF confirmado: Sean Ellis ≥40% + primeros pagos reales
```

---

## Principios del sistema (no negociar)

1. Pipeline encadenado: el output de una skill es el input de la siguiente.
2. $500 antes de $50.000: toda validación de canal empieza con presupuesto mínimo.
3. Orgánico antes que pagado: el canal pagado amplifica lo que funciona, nunca valida.
4. Los criterios de calidad son medibles. "Buenas creativas" no es un criterio.
5. Subir siempre como `.md` a la carpeta Drive `1mdBwlVTaoEhCzXUw40cTUY9hyDJzM8b-`.
6. Actualizar `CONTEXTO-PROYECTO-venture-engine.md` al finalizar.

---

## Umbrales establecidos en el sistema

| Métrica | Umbral | Agente que la define |
|---|---|---|
| LTV/CAC | >3x | Agente 3 (Analista) |
| Sean Ellis test | ≥40% | Gate 5 — Agente 10 |
| NRR objetivo | >110% | Agente 9 (Medidor) |
| Churn máximo SaaS B2B | <5% mensual | Agente 9 |
| Validación de canal | $500 antes de $50.000 | Agente 7 (este) |

---

## Output esperado

1. Documento `.md` completo del Agente 7 con subagentes, skills y DoD
2. Subido a Drive como `subagentes-motor-crecimiento.md`
3. `CONTEXTO-PROYECTO-venture-engine.md` actualizado
4. Resumen en el chat de las decisiones tomadas

---

*SiriusLabs Venture Engine — sesión de construcción del Agente 7*
