# PLAN MAESTRO DEL PROYECTO — QA Fase C

Proyecto: proyecto-902-qa
Modo: create
Fecha: 2026-06-26
ODS objetivo: 3 — Salud y bienestar

## Seed interpretado

─── PROBLEMA / SECTOR ───
Consultorios pequeños y clínicas independientes en LATAM operan agendas con
WhatsApp, llamadas y planillas. El problema a validar para QA técnico es si la
reducción de no-shows y carga administrativa justifica una solución SaaS simple.

─── RESTRICCIONES ───
- Geografía: LATAM, foco Uruguay.
- Tiempo: QA técnico de Fase C.
- Presupuesto: sin gasto real; corrida manual en Cursor.
- Riesgos conocidos: privacidad de datos de salud; adopción en negocios chicos.

## Hipotesis central

"Creemos que consultorios independientes con 1-3 profesionales tienen el problema
de perder turnos e ingresos por agenda manual y pagarían USD 29/mes por agenda,
recordatorios y reprogramación vía WhatsApp porque cada no-show representa ingreso
perdido y desorden operativo."

## Fases MVP-1

| Fase | Agente | Output esperado | Gate |
|---|---|---|---|
| 0 | Explorador | Problema + poblacion + hair-on-fire | Consolidado 0-2 |
| 1 | Cartografo | Landscape + research de soluciones | Consolidado 0-2 |
| 2 | Analista + Negocio | Viabilidad + modelo + scope producto | Consolidado 0-2 |
| 3 | Arquitecto UX | User journeys + wireframes | Gate 3 reducido |

## Riesgos identificados

1. Evidencia simulada: alta — mitigacion: tratar esta corrida como QA técnico, no como decisión comercial real.
2. Pricing bajo con CAC alto: media — mitigacion: Guardian debe simular bloqueante en 10.A.3 si GTM no cuadra.
3. Privacidad de datos de salud: media — mitigacion: Analista debe acotar el MVP a agenda y recordatorios sin historia clínica.

## Primer routing

ASIGNACION DE TAREA
Agente: 1 — Explorador
Tarea: producir Fase 0 validada como fixture para QA Fase C.
Input: este plan maestro + `_seed.md`.
Output esperado: `fase-0/output.md` con anclas `#problema`, `#poblacion`, `#hair-on-fire`, `#fuentes`; `fase-0/handoff.json`.
Dependencias: fixture de entrevistas simuladas disponible.
Criterio de aceptacion: handoff `0->1` valido.

## Decision log

| fecha | decision | razon | alternativas descartadas |
|---|---|---|---|
| 2026-06-26 | Crear proyecto-902-qa | QA Fase C necesita Fase 0 validada, no bloqueada | Reusar proyecto-901-qa con INPUT_REQUEST pendiente |
