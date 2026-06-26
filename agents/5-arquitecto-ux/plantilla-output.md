# FASE 3 — ARQUITECTO UX

Proyecto: [project_id] | Fecha: [YYYY-MM-DD] | Fuente Fase 2: `fase-2/output.md#scope-producto`

## User journeys y arquitectura de informacion {#user-journeys}

─── INPUTS USADOS ───

Problema: [resumen desde `fase-0/output.md#problema`]

Poblacion: [resumen desde `fase-0/output.md#poblacion`]

Modelo de negocio: [resumen desde `fase-2/output.md#modelo-negocio`]

Scope de producto: [resumen desde `fase-2/output.md#scope-producto`]

─── USER JOURNEY MAP ───

Usuario: [segmento primario] | Escenario: [situacion especifica]

Etapa 1: [nombre]

- Qué está haciendo: [accion concreta]
- Qué está pensando: "[cita/parafraseo en vocabulario del usuario]"
- Qué está sintiendo: [emocion]
- Punto de contacto: [canal/pantalla/persona]
- Friccion: [qué dificulta avanzar]
- Oportunidad de diseño: [decision concreta]

Etapa 2: [nombre]

- Qué está haciendo: [accion concreta]
- Qué está pensando: "[cita/parafraseo]"
- Qué está sintiendo: [emocion]
- Punto de contacto: [canal/pantalla/persona]
- Friccion: [qué dificulta avanzar]
- Oportunidad de diseño: [decision concreta]

Etapa 3: [nombre]

- Qué está haciendo: [accion concreta]
- Qué está pensando: "[cita/parafraseo]"
- Qué está sintiendo: [emocion]
- Punto de contacto: [canal/pantalla/persona]
- Friccion: [qué dificulta avanzar]
- Oportunidad de diseño: [decision concreta]

─── MOMENTOS CRITICOS ───

1. [momento] — Por que es critico: [razon] — Decision UX: [decision]
2. [momento] — Por que es critico: [razon] — Decision UX: [decision]
3. [momento] — Por que es critico: [razon] — Decision UX: [decision]

─── ARQUITECTURA DE INFORMACION ───

Inventario de contenido:

| Seccion | Contenido | Prioridad | Fuente |
|---|---|---|---|
| [nombre] | [qué contiene] | [alta/media/baja] | [scope/journey/modelo] |

Estructura de navegacion:

```text
Inicio / Dashboard
├── [Seccion principal]
│   ├── [Vista]
│   └── [Vista]
├── [Segunda seccion]
└── Configuracion
```

Nomenclatura:

| Lo que el equipo llama | Lo que el usuario llama | Decision final |
|---|---|---|
| [termino interno] | [termino usuario] | [label final] |

Jerarquia de acciones:

- Accion principal: [un solo CTA global o de flujo]
- Acciones frecuentes: [lista priorizada]
- Acciones raras/destructivas: [donde quedan, minimo 2 pasos]

Principios aplicados:

1. [principio]
2. [principio]
3. [principio]

## Wireframes baja fidelidad {#wireframes}

─── REGLAS DEL SET ───

Fidelidad: baja (gris / estructura textual / sin visual design)

Pantallas cubiertas: [lista]

Estados obligatorios por pantalla: default, loading, error, vacio, exito

Time-to-value objetivo: [minutos desde scope]

─── PANTALLA 1: [nombre] ───

Proposito: [qué debe lograr]

CTA primario: [un solo CTA]

Pregunta que responde: [pregunta del usuario]

Layout (ASCII):

```text
┌─────────────────────────────┐
│ [NAV / HEADER]              │
├─────────────────────────────┤
│ [Titulo claro]              │
│ [Contexto breve]            │
│                             │
│ [Contenido principal]       │
│                             │
│ [CTA PRIMARIO]              │
└─────────────────────────────┘
```

Anotaciones:

- [por qué este orden]
- [qué friccion reduce]

Estados:

- Default: [descripcion]
- Loading: [descripcion]
- Error: [mensaje accionable]
- Vacio: [estado vacio + CTA de salida]
- Exito: [feedback]

─── PANTALLA 2: [nombre] ───

Proposito: [qué debe lograr]

CTA primario: [un solo CTA]

Pregunta que responde: [pregunta del usuario]

Layout (ASCII):

```text
┌─────────────────────────────┐
│ [NAV / HEADER]              │
├─────────────────────────────┤
│ [Titulo claro]              │
│ [Contenido principal]       │
│ [CTA PRIMARIO]              │
└─────────────────────────────┘
```

Anotaciones:

- [por qué este orden]
- [qué friccion reduce]

Estados:

- Default: [descripcion]
- Loading: [descripcion]
- Error: [mensaje accionable]
- Vacio: [estado vacio + CTA de salida]
- Exito: [feedback]

─── PANTALLA 3: [nombre] ───

Proposito: [qué debe lograr]

CTA primario: [un solo CTA]

Pregunta que responde: [pregunta del usuario]

Layout (ASCII):

```text
┌─────────────────────────────┐
│ [NAV / HEADER]              │
├─────────────────────────────┤
│ [Titulo claro]              │
│ [Contenido principal]       │
│ [CTA PRIMARIO]              │
└─────────────────────────────┘
```

Anotaciones:

- [por qué este orden]
- [qué friccion reduce]

Estados:

- Default: [descripcion]
- Loading: [descripcion]
- Error: [mensaje accionable]
- Vacio: [estado vacio + CTA de salida]
- Exito: [feedback]

─── COBERTURA DEL SCOPE ───

| Item del scope | Pantalla / flujo que lo cubre | Estado |
|---|---|---|
| [feature] | [pantalla] | [cubierto/parcial/falta] |

─── FUERA DE SCOPE MVP-1 ───

- Alta fidelidad visual
- Design system
- Auditoria WCAG
- Design handoff para Constructor
- Prototipo interactivo en Figma

## Gate esperado

Este output alimenta `fase-3/gate-audit.md` del Guardian 10.B reducido.

Skills cubiertas:

- `5.A.1` — user journeys / arquitectura de informacion
- `5.B.1` — wireframes baja fidelidad
