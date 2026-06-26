# GATE 3 REDUCIDO — GUARDIAN 10.B

Proyecto: [project_id] | Fecha: [YYYY-MM-DD] | Auditor: Guardian 10.B

## Resumen ejecutivo

Recomendacion: [GO / ITERAR / KILL]

Razon principal: [2-3 oraciones con evidencia]

Bloqueantes totales: [N]

Decision requerida de CEO: [aprobar GO / devolver a UX / volver a Fase 2 / matar proyecto]

## Alcance del Gate 3 MVP-1

Este gate audita solo coherencia UX de baja fidelidad:

- Problema validado `1.1`
- Poblacion `1.2`
- Modelo de negocio `4.1`
- Scope de producto `4.scope`
- User journeys / arquitectura de informacion `5.A.1`
- Wireframes baja fidelidad `5.B.1`

Fuera de scope:

- WCAG / accesibilidad completa
- Design system
- Alta fidelidad
- Prototipo interactivo
- Design handoff para Constructor

## Auditoria 10.B.1 — UX reducido

Gate: 3 | Fase auditada: 3 | Responsable si itera: Arquitecto UX (5)

─── COHERENCIA CON PROBLEMA Y POBLACION ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| Journey refleja el problema validado | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |
| Journey refleja poblacion y lenguaje del usuario | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |
| Momentos criticos conectan con dolor real | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |

─── COHERENCIA CON MODELO Y SCOPE ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| Wireframes cubren todas las funcionalidades incluidas en `#scope-producto` | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |
| Wireframes no agregan funcionalidades fuera de scope | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |
| Flujo apoya la metrica de exito del MVP | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |
| Time-to-value objetivo es visible en el flujo | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |

─── ARQUITECTURA DE INFORMACION ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| Navegacion maxima 5-7 items principales | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |
| Nombres usan vocabulario del usuario | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |
| Acciones destructivas o raras no estan en primer nivel | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |

─── WIREFRAMES BAJA FIDELIDAD ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| Cada pantalla tiene proposito claro | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |
| Cada pantalla tiene un solo CTA primario | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |
| Estados default/loading/error/vacio/exito especificados | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |
| Layouts son baja fidelidad, no alta fidelidad | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |

─── CONTROL DE ALCANCE MVP-1 ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| No evalua WCAG ni contraste | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |
| No exige design system | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |
| No exige handoff para Constructor | [PASS/FAIL/N/A] | [cita/seccion] | [si/no] |

Resultado 10.B.1: [pass/fail/partial]

Veredicto: [GO / ITERAR / KILL]

Blockers:

- [bloqueante o "ninguno"]

Correcciones requeridas:

- [que corregir] -> [como] -> [responsable]

## Recomendacion consolidada

Recomendacion Guardian: [GO / ITERAR / KILL]

Justificacion: [2-3 oraciones]

Si ITERAR:

- Fase objetivo: 3
- Skill objetivo: [5.A.1 / 5.B.1]
- Motivo: [razon concreta]
- Output esperado para destrabar: [entregable]

Si KILL:

- Hipotesis que fallo: [hipotesis]
- Fase a la que volver: [0/1/2/3]
- Aprendizaje reusable: [aprendizaje]

## Bloque sugerido para `_state.json`

```json
{
  "decision_id": "gate-3-reducido",
  "covers_phases": [3],
  "audits": [
    {
      "skill": "10.B.1",
      "phase": 3,
      "result": "[pass/fail/partial]",
      "blockers": ["[bloqueante o lista vacia]"]
    }
  ],
  "ceo_decision": "[GO/ITERAR/KILL]",
  "iterar_target": null,
  "decided_at": "[ISO8601]",
  "decided_by": "CEO"
}
```

## Cierre

Estado del gate: [PENDIENTE_FIRMA_CEO / FIRMADO]

Notas para CEO: [maximo 5 bullets, orientados a decision]
