# FASE 3 — ARQUITECTO UX

Proyecto: proyecto-903-qa | Fecha: 2026-06-26 | Fuente Fase 2: `fase-2/output.md#scope-producto`

## User journeys y arquitectura de informacion {#user-journeys}

─── INPUTS USADOS ───

Problema: consultorios pequeños pierden turnos e ingresos porque la agenda depende de WhatsApp, llamadas, calendario y memoria de recepción.

Población: consultorio independiente con recepción manual; profesionales y recepcionistas que usan WhatsApp y calendario básico.

Modelo de negocio: SaaS vertical liviano a USD 29/mes para reducir no-shows y mensajes manuales.

Scope de producto: onboarding, agenda semanal, turnos de hoy, detalle de turno, configuración de recordatorios y reprogramación.

─── USER JOURNEY MAP ───

Usuario: recepcionista de consultorio pequeño | Escenario: configurar el sistema y confirmar turnos de la semana.

Etapa 1: configurar consultorio

- Qué está haciendo: carga nombre del consultorio, profesionales y horarios.
- Qué está pensando: "si esto lleva mucho, vuelvo al WhatsApp".
- Qué está sintiendo: cautela y prisa.
- Punto de contacto: onboarding.
- Fricción: miedo a configurar mal horarios.
- Oportunidad de diseño: mostrar progreso simple y permitir editar después.

Etapa 2: revisar turnos de hoy

- Qué está haciendo: mira quién confirmó, quién está pendiente y quién canceló.
- Qué está pensando: "necesito saber a quién tengo que escribirle".
- Qué está sintiendo: necesidad de control.
- Punto de contacto: vista "Turnos de hoy".
- Fricción: no distinguir confirmados de pendientes.
- Oportunidad de diseño: estados visibles por turno.

Etapa 3: resolver un hueco

- Qué está haciendo: ve una cancelación y decide reprogramar o llenar hueco.
- Qué está pensando: "ojalá pueda recuperar ese horario".
- Qué está sintiendo: urgencia.
- Punto de contacto: detalle de turno.
- Fricción: tener que buscar mensajes viejos.
- Oportunidad de diseño: CTA único "Enviar link de reprogramación".

─── MOMENTOS CRITICOS ───

1. Setup inicial — crítico porque define adopción — Decisión UX: onboarding en tres pasos.
2. Primer turno confirmado — crítico porque muestra valor — Decisión UX: feedback de éxito visible.
3. Cancelación/reprogramación — crítico porque recupera ingreso — Decisión UX: acción directa desde detalle de turno.

─── ARQUITECTURA DE INFORMACION ───

Inventario de contenido:

| Sección | Contenido | Prioridad | Fuente |
|---|---|---|---|
| Inicio | resumen de turnos de hoy y pendientes | alta | scope/journey |
| Agenda | vista semanal de turnos | alta | scope |
| Turno | detalle, estado y acciones | alta | scope |
| Recordatorios | configuración de mensajes | media | scope |
| Configuración | profesionales y horarios | media | scope |

Estructura de navegación:

```text
Inicio / Turnos de hoy
├── Agenda semanal
│   └── Detalle de turno
├── Recordatorios
└── Configuración
    ├── Profesionales
    └── Horarios
```

Nomenclatura:

| Lo que el equipo llama | Lo que el usuario llama | Decisión final |
|---|---|---|
| Dashboard | Turnos de hoy | Turnos de hoy |
| Appointment | Turno | Turno |
| Reminder automation | Recordatorios | Recordatorios |
| Reschedule link | Link de reprogramación | Reprogramar |

Jerarquía de acciones:

- Acción principal: confirmar o recuperar turnos pendientes.
- Acciones frecuentes: ver agenda, abrir turno, enviar recordatorio, reprogramar.
- Acciones raras/destructivas: eliminar turno queda dentro de detalle y con confirmación.

Principios aplicados:

1. La primera pantalla responde "qué pasa hoy".
2. Los estados de turno son visibles antes que los datos administrativos.
3. Configuración queda fuera del flujo diario.

## Wireframes baja fidelidad {#wireframes}

─── REGLAS DEL SET ───

Fidelidad: baja (estructura textual / sin visual design).

Pantallas cubiertas: onboarding, turnos de hoy, agenda semanal, detalle de turno, recordatorios.

Estados obligatorios por pantalla: default, loading, error, vacío, éxito.

Time-to-value objetivo: 15 minutos.

─── PANTALLA 1: Onboarding consultorio ───

Propósito: configurar lo mínimo para enviar el primer recordatorio.

CTA primario: Guardar y ver agenda.

Pregunta que responde: "¿Qué tengo que cargar para empezar?"

Layout (ASCII):

```text
┌─────────────────────────────┐
│ Paso 1 de 3                 │
├─────────────────────────────┤
│ Nombre del consultorio      │
│ Profesionales               │
│ Horarios básicos            │
│                             │
│ [ Guardar y ver agenda ]    │
└─────────────────────────────┘
```

Anotaciones:

- El progreso reduce ansiedad de setup.
- Sólo pide lo necesario para time-to-value.

Estados:

- Default: formulario con tres bloques.
- Loading: "Guardando configuración..."
- Error: "Revisá el horario de atención: hay un solapamiento."
- Vacío: formulario inicial con ejemplo.
- Éxito: "Consultorio creado. Ahora cargá tu primer turno."

─── PANTALLA 2: Turnos de hoy ───

Propósito: mostrar qué requiere atención ahora.

CTA primario: Enviar recordatorios pendientes.

Pregunta que responde: "¿A quién tengo que escribirle hoy?"

Layout (ASCII):

```text
┌─────────────────────────────┐
│ Turnos de hoy               │
├─────────────────────────────┤
│ Confirmados: 8              │
│ Pendientes: 3               │
│ Cancelados: 1               │
│                             │
│ [ Enviar recordatorios ]    │
│                             │
│ Lista de turnos por estado  │
└─────────────────────────────┘
```

Anotaciones:

- Prioriza pendientes porque son accionables.
- Evita dashboard genérico.

Estados:

- Default: lista agrupada por estado.
- Loading: skeleton de tarjetas de turno.
- Error: "No pudimos cargar los turnos. Reintentar."
- Vacío: "No hay turnos hoy. Crear turno."
- Éxito: "Recordatorios enviados."

─── PANTALLA 3: Agenda semanal ───

Propósito: dar visión de ocupación y huecos.

CTA primario: Crear turno.

Pregunta que responde: "¿Dónde tengo lugar esta semana?"

Layout (ASCII):

```text
┌─────────────────────────────┐
│ Semana: [<] 24-30 Jun [>]   │
├─────────────────────────────┤
│ Lun | Mar | Mie | Jue | Vie │
│ bloques de turnos           │
│ huecos visibles             │
│                             │
│ [ Crear turno ]             │
└─────────────────────────────┘
```

Anotaciones:

- Muestra huecos como oportunidad de ingreso.
- Mantiene una sola acción primaria.

Estados:

- Default: grilla semanal.
- Loading: grilla en carga.
- Error: "No pudimos cargar la semana."
- Vacío: "Todavía no cargaste turnos. Crear turno."
- Éxito: "Turno creado."

─── PANTALLA 4: Detalle de turno ───

Propósito: resolver el estado de un turno específico.

CTA primario: Enviar link de reprogramación.

Pregunta que responde: "¿Qué hago con este turno?"

Layout (ASCII):

```text
┌─────────────────────────────┐
│ Turno: Ana Pérez            │
├─────────────────────────────┤
│ Fecha y hora                │
│ Profesional                 │
│ Estado: pendiente/cancelado │
│ Historial de recordatorios  │
│                             │
│ [ Enviar link reprogramar ] │
└─────────────────────────────┘
```

Anotaciones:

- Acciones de recuperación están cerca del estado.
- Eliminar turno no aparece como CTA primario.

Estados:

- Default: datos del turno y estado.
- Loading: "Cargando turno..."
- Error: "No pudimos actualizar este turno."
- Vacío: "Seleccioná un turno de la agenda."
- Éxito: "Link enviado."

─── PANTALLA 5: Recordatorios ───

Propósito: configurar mensaje y anticipación.

CTA primario: Guardar recordatorio.

Pregunta que responde: "¿Qué mensaje se manda y cuándo?"

Layout (ASCII):

```text
┌─────────────────────────────┐
│ Recordatorios               │
├─────────────────────────────┤
│ Enviar: 24h antes           │
│ Canal: WhatsApp/email       │
│ Mensaje editable            │
│                             │
│ [ Guardar recordatorio ]    │
└─────────────────────────────┘
```

Anotaciones:

- Configuración queda fuera del flujo diario.
- El copy usa "turno" y "recordatorio", no automatización.

Estados:

- Default: configuración actual.
- Loading: "Guardando recordatorio..."
- Error: "No se guardó. Probá de nuevo."
- Vacío: "Todavía no configuraste recordatorios."
- Éxito: "Recordatorio guardado."

─── COBERTURA DEL SCOPE ───

| Item del scope | Pantalla / flujo que lo cubre | Estado |
|---|---|---|
| Agenda semanal | Agenda semanal | cubierto |
| Recordatorios automáticos | Turnos de hoy + Recordatorios | cubierto |
| Link de reprogramación | Detalle de turno | cubierto |
| Panel de confirmaciones | Turnos de hoy | cubierto |

─── FUERA DE SCOPE MVP-1 ───

- Diseño visual final
- Sistema visual de componentes
- Auditoría normativa de accesibilidad
- Entrega técnica a desarrollo
- Prototipo interactivo externo

## Gate esperado

Este output alimenta `fase-3/gate-audit.md` del Guardian 10.B reducido.

Skills cubiertas:

- `5.A.1` — user journeys / arquitectura de información
- `5.B.1` — wireframes baja fidelidad
