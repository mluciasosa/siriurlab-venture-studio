# PLAN MAESTRO DEL PROYECTO — QA Fase B

Proyecto: proyecto-901-qa
Modo: create
Fecha: 2026-06-26
ODS objetivo: 3 — Salud y bienestar

## Seed interpretado

─── PROBLEMA / SECTOR ───
Clínicas pequeñas y consultorios independientes en LATAM gestionan citas de forma
manual (WhatsApp, planillas, llamadas), con fricción operativa y no-shows que
afectan ingresos y calidad de atención. Se explora si el dolor es urgente y
pagable para una solución digital accesible.

─── RESTRICCIONES ───
- Geografía: LATAM (foco UY/BR en research secundario)
- Tiempo: exploración; QA de pipeline sin entrevistas primarias
- Presupuesto: no definido
- Riesgos conocidos: privacidad de datos de salud; resistencia al cambio en recepción; conectividad en zonas rurales

## Hipotesis central

"Creemos que consultorios independientes con 1–3 profesionales en LATAM tienen el
problema de perder citas y horas administrativas por agendamiento manual caótico
y pagarían entre USD 15–40/mes por recordatorios y agenda online integrada a
WhatsApp porque el no-show y la recepción saturada les cuesta pacientes e ingresos."

## Fases MVP-1

| Fase | Agente | Output esperado | Gate |
|---|---|---|---|
| 0 | Explorador | Problema + población + hair-on-fire | Consolidado 0-2 |
| 1 | Cartógrafo | Landscape + research de soluciones | Consolidado 0-2 |
| 2 | Analista + Negocio | Viabilidad + modelo + scope producto | Consolidado 0-2 |
| 3 | Arquitecto UX | User journeys + wireframes | Gate 3 reducido |

## Riesgos identificados

1. Validación primaria ausente: alta — mitigación: INPUT_REQUEST de entrevistas; veredicto INCIERTO hasta resolver
2. Sensibilidad de datos clínicos: media — mitigación: Cartógrafo debe mapear cumplimiento en Fase 1
3. Mercado fragmentado (clínicas muy pequeñas vs. volumen): media — mitigación: perfilar segmento mínimo viable en Fase 0

## Primer routing

ASIGNACION DE TAREA
Agente: 1 — Explorador
Tarea: validar problema y perfilar población afectada.
Input: este plan maestro + `_seed.md`.
Output esperado: `fase-0/output.md` con anclas `#problema`, `#poblacion`, `#hair-on-fire`, `#fuentes`; `fase-0/handoff.json`.
Dependencias: ninguna.
Criterio de aceptacion: output completo y handoff `0->1` valido.

## Decision log

| fecha | decision | razon | alternativas descartadas |
|---|---|---|---|
| 2026-06-26 | Inicio de proyecto QA Fase B | Validar encadenamiento Shifu → Explorador sin edición manual | Usar Nubia real antes de QA sintético |
| 2026-06-26 | Foco clínicas pequeñas LATAM | Alineado con ODS 3 y seed de prueba | Sector genérico "salud digital" |
