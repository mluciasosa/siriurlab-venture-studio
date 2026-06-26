# FASE 2 — ANALISTA + ARQUITECTO DE NEGOCIO

Proyecto: proyecto-903-qa | Fecha: 2026-06-26 | Fuente Fase 1: `fase-1/output.md`

## Veredicto consolidado del Analista

Estado: GO

Razón: para QA Fase D, el modelo queda aprobado como fixture para habilitar UX. La oportunidad es un SaaS liviano con scope acotado y sin historia clínica.

## Analisis de mercado {#mercado}

SOM fixture: 200 consultorios en 18-24 meses.

Escenario base: USD 69.600 ARR.

## Unit economics {#unit-economics}

Precio: USD 29/mes.

LTV/CAC fixture: 3,2x.

Condición crítica: CAC menor a USD 120 por consultorio.

## Viabilidad tecnica {#viabilidad-tecnica}

MVP viable en 3-4 semanas con agenda, recordatorios y reprogramación. Stack sugerido: Next.js, Supabase, WhatsApp provider y pagos simples.

## Riesgos y kill criteria {#riesgos}

Riesgos principales: adopción por recepción, costos de WhatsApp y privacidad de datos. MVP no incluye historia clínica.

Kill criteria: LTV/CAC menor a 1, no aceptación de piloto pago o setup mayor a 15 minutos.

## Modelo de negocio {#modelo-negocio}

─── REVENUE PRIMITIVE ───

Consultorios pequeños pagan USD 29/mes por reducir no-shows y mensajes manuales con agenda, recordatorios y reprogramación.

─── MODELO ELEGIDO ───

SaaS vertical liviano.

Por qué: el cliente obtiene valor sin marketplace ni red de dos lados.

─── PRICING ───

Plan Básico: USD 29/mes para 1-3 profesionales.

Plan Plus: USD 49/mes con más mensajes y reportes simples.

## Go-to-market {#gtm}

Canal inicial: outbound manual y referidos locales.

Validación chica: USD 500 máximo para conseguir 3 pilotos pagos en 30 días.

Primer cliente pagador: consultorio con 2 profesionales y 80+ turnos/mes.

## Scope de producto {#scope-producto}

─── USUARIO Y RESULTADO ───

Usuario primario: recepcionista o profesional que agenda manualmente.

Resultado core: reducir no-shows y mensajes repetitivos.

Time-to-value objetivo: 15 minutos.

─── FLUJO CORE ───

1. Crear consultorio.
2. Configurar profesionales y horarios.
3. Ver agenda semanal y turnos de hoy.
4. Enviar recordatorios.
5. Ver confirmaciones, cancelaciones y reprogramaciones.

─── FUNCIONALIDADES INCLUIDAS ───

1. Agenda semanal.
2. Recordatorios automáticos.
3. Link de reprogramación.
4. Panel de estado de confirmaciones.

─── EXCLUIDO DEL MVP ───

- Historia clínica.
- Marketplace de pacientes.
- Alta complejidad de pagos.
- IA conversacional.

─── REQUISITOS PARA UX ───

Pantallas necesarias:

- Onboarding consultorio.
- Agenda semanal.
- Turnos de hoy.
- Detalle de turno.
- Configuración de recordatorios.

Estados obligatorios:

- Default
- Loading
- Error
- Vacío
- Éxito

Métrica de éxito del MVP: porcentaje de turnos confirmados automáticamente y reducción de no-shows.

## Handoff esperado

Skills cubiertas:

- `4.1` — modelo de negocio
- `4.2` — go-to-market
- `4.scope` — scope de producto
