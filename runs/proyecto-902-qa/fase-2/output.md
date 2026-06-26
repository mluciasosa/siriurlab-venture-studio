# FASE 2 — ANALISTA + ARQUITECTO DE NEGOCIO

Proyecto: proyecto-902-qa | Fecha: 2026-06-26 | Fuente Fase 1: `fase-1/output.md`

## Veredicto consolidado del Analista

─── RESUMEN ───

Mercado (3.A): AMARILLO — oportunidad plausible, pero el tamaño Uruguay requiere fuente bottom-up real.

Financiero (3.B): AMARILLO — ticket USD 29/mes puede cerrar si CAC orgánico domina; CAC pago rompe el modelo.

Técnico (3.C): VERDE — MVP acotado sin historia clínica es construible con stack SaaS estándar.

Riesgo (3.D): AMARILLO — adopción y WhatsApp API son los supuestos más frágiles.

─── VEREDICTO ───

Estado: ITERAR

Razón: la cadena técnica funciona y el negocio es plausible para QA, pero el GTM
todavía no prueba un camino de adquisición suficientemente barato para un ticket
bajo. Se puede avanzar a auditoría, pero no debería haber GO automático.

─── LOS 3 NUMEROS QUE MAS IMPORTAN ───

SOM: USD 69.600 ARR — escenario base — 200 consultorios x USD 29/mes x 12.

LTV/CAC: 2,3x — escenario base — LTV USD 348 con CAC USD 150.

Tiempo a break-even: 10 meses — escenario conservador con 15 clientes nuevos/mes.

─── CONDICION CRITICA ───

"Si el CAC real supera USD 150 por consultorio, el ticket de USD 29/mes no sostiene el modelo."

Cómo validarlo antes de construir: campaña manual/outbound de 30 días con 50
consultorios y medición de demo agendada, prueba piloto y pago.

## Analisis de mercado {#mercado}

─── TAM ───

Universo base: 10.000 consultorios pequeños LATAM como estimación de trabajo —
fuente: inferencia QA desde mercado regional; requiere validación real.

Precio de referencia: USD 348/año — fuente: pricing objetivo QA (USD 29/mes).

Cálculo: 10.000 x USD 348 = USD 3.480.000 TAM operativo de prueba.

─── SAM ───

Filtros:

- Geografía Uruguay inicial: 10.000 -> 1.000 — 10% estimado — fuente: supuesto QA.
- Acceso tecnológico/WhatsApp: 1.000 -> 800 — 80% estimado — fuente: fixture QA.
- Capacidad de pago: 800 -> 500 — 62,5% estimado — fuente: fixture QA.

SAM: 500 x USD 348 = USD 174.000 ARR.

─── SOM (18-24 MESES) ───

Restricciones reales:

- Capacidad comercial: 15 clientes/mes con venta manual.
- Presupuesto de adquisición: USD 500/mes máximo en QA.
- Tiempo de adopción: 15 minutos de onboarding esperado.
- Fricción competitiva: sustituto gratuito WhatsApp + calendario.

Escenario conservador: 80 clientes = USD 27.840 ARR — supuestos: bajo referidos y CAC alto.

Escenario base: 200 clientes = USD 69.600 ARR — supuestos: canal orgánico + alianzas.

Escenario optimista: 400 clientes = USD 139.200 ARR — supuestos: WhatsApp como canal viral.

─── DINAMICA Y REGULACION ───

CAGR / crecimiento: INCIERTO — fuentes secundarias muestran crecimiento de scheduling médico, pero no bottom-up local.

Regulación relevante: datos de salud sensibles. MVP evita historia clínica y minimiza datos: nombre, contacto, turno y profesional.

## Unit economics {#unit-economics}

─── PRECIO Y MARGEN ───

Precio mensual/cliente: USD 29 — fuente: fixture QA y benchmark de herramientas simples.

Costos de entrega/cliente/mes:

- Infraestructura: USD 2
- WhatsApp/API mensajes: USD 3
- Soporte: USD 4
- Herramientas: USD 1

Margen bruto: 65,5%.

─── ADQUISICION ───

Canal 1: outbound manual a consultorios

- Costo accion: USD 2/contacto equivalente en tiempo operativo — fuente: supuesto QA.
- Conversión esperada: 5% a piloto pago.
- CAC: USD 120.

Canal 2: ads locales

- Costo accion: USD 1/click — fuente: benchmark genérico QA.
- Conversión esperada: 1% a pago.
- CAC: USD 300.

CAC blended: USD 150 si el canal orgánico/outbound pesa 80%.

─── RETENCION Y LTV ───

Churn mensual: 5% — fuente/supuesto: default SaaS B2B chico.

Vida del cliente: 20 meses.

LTV: USD 29 x 65,5% x 20 = USD 380.

LTV/CAC: 2,53x — semáforo: AMARILLO 1-3x.

─── SENSIBILIDAD ───

| Variable | Base | -20% | -40% | LTV/CAC resultante |
|---|---:|---:|---:|---:|
| Precio | 29 | 23 | 17 | 1,5x |
| Churn | 5% | 6% | 7% | 1,8x |
| Conversión | 5% | 4% | 3% | 1,6x |

Peor escenario combinado: LTV/CAC < 1,5x; viable sólo con CAC orgánico bajo.

## Viabilidad tecnica {#viabilidad-tecnica}

─── COMPONENTES DEL MVP ───

| Componente | Qué hace | Complejidad | Decisión BUILD/BUY | Costo | Riesgo |
|---|---|---|---|---:|---|
| Agenda multi-profesional | disponibilidad y turnos | media | BUILD | USD 0 infra incremental | bajo |
| Recordatorios WhatsApp | envía confirmaciones | media | BUY/API | USD 3/cliente/mes | medio |
| Reprogramación simple | link para cancelar/reagendar | media | BUILD | incluido | medio |
| Panel recepción | lista de turnos y estados | baja | BUILD | incluido | bajo |
| Pagos piloto | cobrar suscripción | baja | BUY Stripe/MercadoPago | comisión | bajo |

─── STACK RECOMENDADO ───

Frontend: Next.js — rápido para SaaS CRUD — costo: USD 0-20/mes

Backend: Next.js API o FastAPI — suficiente para MVP — costo: USD 0-20/mes

DB: Supabase Postgres — auth y DB gestionada — costo: USD 0-25/mes

Auth: Supabase Auth — reduce construcción — costo: incluido

Pagos: Stripe/MercadoPago — cobro recurrente o link — costo: comisión

Deploy: Vercel/Railway — despliegue simple — costo: USD 0-20/mes

IA/LLM: NO APLICA — no usar IA en MVP de QA.

─── ESTIMACION MVP ───

Setup y arquitectura: 2 días

Feature 1 agenda: 4 días

Feature 2 recordatorios: 3 días

Feature 3 reprogramación: 3 días

Tests e integración: 3 días

Total con contingencia 20%: 18 días-persona / 3-4 semanas.

## Riesgos y kill criteria {#riesgos}

─── RIESGOS POR CATEGORIA ───

Mercado:

- Consultorios prefieren seguir gratis con WhatsApp — Probabilidad: media — Impacto: alto — Mitigación: piloto con ROI por no-shows recuperados.

Modelo de negocio:

- CAC real supera USD 150 — Probabilidad: alta — Impacto: crítico — Mitigación: validar canal orgánico/outbound antes de ads.

Técnico:

- WhatsApp Business API suma fricción — Probabilidad: media — Impacto: alto — Mitigación: empezar con proveedor low-code o mensajes manuales asistidos.

Regulatorio/equipo:

- Manejo de datos de salud se vuelve más amplio — Probabilidad: media — Impacto: alto — Mitigación: no guardar historia clínica ni notas médicas en MVP.

─── SUPUESTOS MAS FRAGILES ───

1. "Recepción adopta una agenda nueva si setup <15 minutos" — Validar: prueba onboarding — Si falla: servicio de configuración asistida.
2. "Consultorio paga USD 29/mes por reducir no-shows" — Validar: cobrar piloto — Si falla: cambiar pricing por uso o setup fee.
3. "CAC outbound queda bajo USD 150" — Validar: 50 contactos — Si falla: buscar canal alianza/colegios.

─── KILL CRITERIA ───

- Gate 0: kill si entrevistas reales muestran dolor sólo "nice to have".
- Gate 1: kill si LTV/CAC <1 en canal más barato.
- Gate 2: kill si no hay camino a primer cobro en menos de 6 meses.

## Modelo de negocio {#modelo-negocio}

─── REVENUE PRIMITIVE ───

En una oración: consultorios pequeños pagan USD 29/mes por reducir no-shows y
tiempo de recepción con agenda y recordatorios WhatsApp.

─── MODELO ELEGIDO ───

Modelo: SaaS vertical liviano.

Por qué este modelo: el valor se entrega a un solo cliente sin necesitar red de
dos lados; el workflow es recurrente y el ticket debe ser predecible.

Alternativas descartadas:

- Marketplace — agrega cold start y no resuelve la operación interna.
- AI Infrastructure — no se vende capacidad de IA ni hay compute diferencial.

─── PRICING ───

Plan inicial: Básico — USD 29/mes — agenda, 1-3 profesionales, recordatorios y reprogramación.

Expansión de cuenta: más profesionales, más mensajes o múltiples sedes.

Condición crítica del pricing: el cliente debe percibir al menos 1 turno recuperado
por mes para justificar el pago.

Planes con diferenciación real: PENDIENTE — sólo hay un plan inicial definido.

─── PROPUESTA DE VALOR ───

Para consultorios chicos que coordinan turnos por WhatsApp, Agenda Clara entrega
menos huecos por no-show y menos mensajes manuales sin obligarlos a cambiar todo
su sistema de trabajo.

Lenguaje prohibido: CRM, workflow, engagement, omnicanalidad.

## Go-to-market {#gtm}

─── CANAL INICIAL ───

Canal 1: outbound manual a consultorios — por qué: ACV bajo y nicho local — costo esperado: bajo — métrica: pilotos pagos.

Canal 2: referidos entre profesionales — por qué: confianza local — costo esperado: bajo — métrica: referidos por cliente.

─── PRIMER CLIENTE PAGADOR ───

Perfil: consultorio con 2 profesionales, agenda de 80+ turnos/mes y recepción compartida.

Táctica de adquisición: lista de 50 consultorios, mensaje directo, demo de 15 minutos y piloto pago de USD 29.

Oferta inicial: primer mes pago con setup asistido.

─── VALIDACION DE BAJO PRESUPUESTO ───

Experimento: contactar 50 consultorios y conseguir 3 pilotos pagos.

Presupuesto máximo: PENDIENTE — no se fijó validación de USD 500 antes de ads.

Resultado esperado: 3 pagos en 30 días.

Decisión si falla: ITERAR canal o pricing antes de construir.

─── SECUENCIA 0-90 DIAS ───

Días 0-30: vender 3 pilotos pagos manuales.

Días 31-60: medir no-shows recuperados y soporte requerido.

Días 61-90: cerrar 10 clientes o iterar modelo.

## Scope de producto {#scope-producto}

─── USUARIO Y RESULTADO ───

Usuario primario: recepcionista o profesional que agenda manualmente.

Resultado core: reducir no-shows y mensajes manuales.

Time-to-value objetivo: 15 minutos.

─── FLUJO CORE ───

1. Crear cuenta de consultorio.
2. Configurar profesionales y horarios.
3. Cargar o recibir turnos.
4. Enviar recordatorios y recibir confirmación/cancelación.

─── FUNCIONALIDADES INCLUIDAS ───

1. Agenda semanal — entra porque centraliza turnos.
2. Recordatorios WhatsApp/email — entra porque ataca no-show.
3. Link de reprogramación — entra porque recupera huecos.

─── EXCLUIDO DEL MVP ───

- Historia clínica — reduce riesgo regulatorio.
- Marketplace de pacientes — agrega cold start.
- IA conversacional — no es necesaria para primer valor.

─── REQUISITOS PARA UX ───

Pantallas necesarias:

- Onboarding consultorio.
- Agenda semanal.
- Detalle de turno.
- Configuración de recordatorios.
- Estado de confirmaciones.

Estados obligatorios:

- Default
- Loading
- Error
- Vacío
- Éxito

Métrica de éxito del MVP: porcentaje de turnos confirmados automáticamente y no-shows reducidos por consultorio.

## Handoff esperado

Este output alimenta el handoff `2->3` hacia Arquitecto UX.

Skills cubiertas:

- `3.A.1` — mercado
- `3.B.1` — unit economics
- `3.C.1` — viabilidad técnica
- `3.D.1` — riesgos
- `4.1` — modelo de negocio
- `4.2` — go-to-market
- `4.scope` — scope de producto
