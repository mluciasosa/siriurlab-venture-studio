# GATE 0-2 CONSOLIDADO — GUARDIAN 10.A

Proyecto: proyecto-902-qa | Fecha: 2026-06-26 | Auditor: Guardian 10.A

## Resumen ejecutivo

Recomendación consolidada: ITERAR

Razón principal: los handoffs validan y las tres fases tienen outputs referenciables,
pero el modelo de negocio deja un blocker intencional en 10.A.3: no hay planes con
diferenciación real y la validación de bajo presupuesto no fija el umbral USD 500.

Bloqueantes totales: 2

Decisión requerida de CEO: devolver a Fase 2 / skill 4.2 para completar pricing y GTM.

## Validacion 10.0 — Handoffs

| Handoff | Transición | Resultado | Evidencia / acción |
|---|---|---|---|
| `fase-0/handoff.json` | `0->1` | PASS | `PASA: handoff valido` |
| `fase-1/handoff.json` | `1->2` | PASS | `PASA: handoff valido` |
| `fase-2/handoff.json` | `2->3` | PASS | `PASA: handoff valido` |

Completo para decisión CEO: SI

## Auditoria 10.A.1 — Problema y poblacion

Gate: 0 | Fase auditada: 0 | Responsable si itera: Explorador (1)

─── CRITERIOS DE PROBLEMA ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| Descrito en lenguaje del usuario, no jerga de producto | PASS | `#problema` y lenguaje fixture | no |
| Magnitud y frecuencia estimadas con fuente | PASS | diaria, gravedad 4; fixture QA | no |
| Solución actual documentada | PASS | WhatsApp, Google Calendar, planilla | no |
| Veredicto hair-on-fire con evidencia concreta | PASS | fixture QA validado para pipeline | no |
| Indicación de disposición a pagar | PASS | USD 20-40/mes fixture | no |

─── CRITERIOS DE POBLACION ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| Segmento específico, no "el mercado" | PASS | consultorio independiente con recepción manual | no |
| Tamaño con fuente o incertidumbre explícita | PASS | tamaño Uruguay marcado INCIERTO | no |
| Jobs to be Done funcional, emocional y social | PASS | sección JTBD completa | no |
| Momentos de dolor específicos | PASS | no-show y doble reserva | no |
| Lenguaje documentado con citas o marcado como no disponible | PASS | citas fixture QA | no |

─── CRITERIOS ODS ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| ODS identificado por número y nombre | PASS | ODS 3 — Salud y bienestar | no |
| Conexión directa con el problema | PASS | acceso/gestión de atención médica | no |
| Afecta población real dentro del ODS | PASS | consultorios y pacientes | no |

Resultado 10.A.1: pass

Veredicto: GO

Blockers:

- ninguno

Correcciones requeridas:

- ninguna

## Auditoria 10.A.2 — Mercado y viabilidad

Gate: 1 | Fase auditada: 1 | Responsable si itera: Cartografo (2) / Analista (3)

─── MERCADO ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| TAM filtrado a SOM real, no top-down genérico | PASS | SOM explícito 80/200/400 clientes | no |
| SAM con filtros explícitos | PASS | geografía, acceso, capacidad de pago | no |
| SOM con conservador/base/optimista | PASS | tres escenarios presentes | no |
| SOM supera umbral mínimo o justifica bootstrap | PASS | QA trata oportunidad bootstrap chica | no |
| Números con fuente y fecha | PARTIAL | varios supuestos QA; no bloquea por ser fixture | no |

─── UNIT ECONOMICS ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| CAC calculado por canal con metodología | PASS | outbound y ads modelados | no |
| Churn con benchmark o supuesto justificado | PASS | default SaaS B2B 5% | no |
| LTV/CAC > 3x en escenario base | FAIL | 2,53x | no |
| Punto de equilibrio con costos fijos reales | PARTIAL | tiempo a break-even, sin tabla completa | no |
| Proyección/sensibilidad con supuestos verificables | PASS | tabla sensibilidad presente | no |

─── VIABILIDAD TECNICA ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| Stack desplegable por equipo disponible | PASS | Next.js/Supabase/Vercel | no |
| Estimación MVP limitada a 3 features core | PASS | agenda, recordatorios, reprogramación | no |
| Riesgos técnicos con probabilidad | PASS | WhatsApp API y privacidad | no |
| No propone modelos de IA propios en MVP | PASS | IA/LLM no aplica | no |

─── COMPETENCIA ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| Mapa incluye sustitutos no tecnológicos | PASS | cuaderno, llamadas, WhatsApp manual | no |
| Gaps específicos y accionables | PASS | tres gaps definidos | no |
| Diferenciación específica, no "hacerlo mejor" | PASS | SaaS liviano WhatsApp para recepción manual | no |

Semáforo financiero: AMARILLO

Resultado 10.A.2: partial

Veredicto: ITERAR LEVE

Blockers:

- ninguno bloqueante para QA; sí requiere mejorar fuentes antes de decisión real.

Correcciones requeridas:

- Reemplazar estimaciones QA por fuentes reales en 3.A.1 antes de piloto comercial.

## Auditoria 10.A.3 — Modelo de negocio y GTM

Gate: 2 | Fase auditada: 2 | Responsable si itera: Arquitecto de Negocio (4)

─── MODELO ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| Revenue primitive en una oración | PASS | consultorios pagan USD 29/mes por reducir no-shows | no |
| Modelo elegido con justificación de ventaja | PASS | SaaS vertical liviano | no |
| Condición crítica identificada y plan para cumplirla | PASS | CAC < USD 150 | no |

─── PRICING ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| Pricing justificado por valor para el usuario | PASS | un turno recuperado por mes | no |
| Mecanismo de expansión definido | PASS | más profesionales, mensajes o sedes | no |
| Planes con diferenciación real | FAIL | output dice "PENDIENTE — sólo hay un plan inicial" | sí |

─── PROPUESTA DE VALOR ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| Sin jerga técnica | PASS | propuesta en lenguaje simple | no |
| Legible por usuario del segmento | PASS | menciona WhatsApp, huecos y mensajes manuales | no |
| Menciona resultado medible, no sólo feature | PASS | menos no-shows y menos mensajes | no |
| Diferenciación específica y defendible | PASS | liviano y sin suite clínica | no |

─── MONETIZACION TEMPRANA ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| Fechas y montos específicos | PASS | 3 pilotos pagos en 30 días | no |
| Primer cliente pagador con perfil y táctica | PASS | consultorio 2 profesionales, 80+ turnos/mes | no |
| Ejecutable con recursos actuales | PASS | outbound manual | no |

─── GTM ───

| Criterio | Resultado | Evidencia | Bloqueante |
|---|---|---|---|
| Motion consistente con ACV | PASS | outbound/referral para ACV bajo | no |
| Validación chica planificada antes de gasto mayor | FAIL | presupuesto máximo dice PENDIENTE; no fija USD 500 | sí |
| Canales orgánicos antes de pagados o excepción justificada | PASS | outbound y referidos antes de ads | no |

Resultado 10.A.3: fail

Veredicto: ITERAR

Blockers:

- Falta diferenciación real de planes/pricing.
- Falta fijar validación chica de USD 500 antes de gasto mayor.

Correcciones requeridas:

- Completar `4.1` con al menos dos planes diferenciados o justificar un solo plan.
- Completar `4.2` con experimento de validación de USD 500 y umbrales de decisión.

## Recomendacion consolidada

Resultado por auditoría:

| Auditoría | Fase | Result | Blockers |
|---|---:|---|---|
| 10.A.1 | 0 | pass | 0 |
| 10.A.2 | 1 | partial | 0 |
| 10.A.3 | 2 | fail | 2 |

Recomendación Guardian: ITERAR

Justificación: el pipeline y los handoffs funcionan, pero el Gate 2 falla por
pricing/GTM incompletos. Esto prueba que un blocker en 10.A.3 no habilita GO
automático aunque `fase-2/handoff.json` sea técnicamente válido.

Si ITERAR:

- Fase objetivo: 2
- Skill objetivo: 4.2
- Motivo: completar validación de USD 500 y diferenciación de pricing.
- Output esperado para destrabar: `fase-2/output.md#modelo-negocio` y `#gtm` corregidos.

## Bloque sugerido para `_state.json`

```json
{
  "decision_id": "gate-0-2-consolidado",
  "covers_phases": [0, 1, 2],
  "audits": [
    {
      "skill": "10.A.1",
      "phase": 0,
      "result": "pass",
      "blockers": []
    },
    {
      "skill": "10.A.2",
      "phase": 1,
      "result": "partial",
      "blockers": []
    },
    {
      "skill": "10.A.3",
      "phase": 2,
      "result": "fail",
      "blockers": [
        "Falta diferenciación real de planes/pricing",
        "Falta fijar validación chica de USD 500 antes de gasto mayor"
      ]
    }
  ],
  "ceo_decision": "ITERAR",
  "iterar_target": {
    "phase": 2,
    "skill": "4.2",
    "reason": "Completar pricing y validación chica antes de habilitar UX"
  },
  "decided_at": "2026-06-26T23:00:00Z",
  "decided_by": "CEO"
}
```

## Cierre

Estado del gate: FIRMADO PARA QA

Notas para CEO:

- La cadena técnica 0→1→2→3 valida.
- El scope de producto es referenciable por UX.
- No hay GO automático por blocker en 10.A.3.
- La decisión correcta del QA es ITERAR Fase 2 / skill 4.2.
