# UI/UX Design Patterns 2026
### Guía de referencia para desarrolladores y diseñadores

> Basado en el análisis de Linear, Notion, Figma, Superhuman, Raycast, Arc, Stripe, Vercel, Perplexity y Loom.  
> Mantener este documento como referencia antes de tomar decisiones de diseño o arquitectura de interfaz.

---

## Cómo usar esta guía

Este documento está organizado en capas: desde los principios más fundamentales hasta decisiones técnicas específicas. Un desarrollador puede saltar directamente a la sección de componentes. Un diseñador puede empezar por los principios visuales. Un founder puede leer solo la sección de filosofía y las preguntas de control.

Cada sección termina con una **Pregunta de control** — úsala para auditar cualquier decisión de diseño antes de implementarla.

---

## 01 — Filosofía: Lo que estas interfaces tienen en común

Las mejores interfaces de 2026 no compiten en features. Compiten en **claridad de propósito**. Cada elemento en pantalla ganó su lugar — o fue eliminado.

### Los tres principios que no se negocian

**1. Velocidad como decisión de diseño**
Si el usuario puede percibir latencia, el diseño falló. Regla: si una acción tarda más de 100ms en dar feedback visual, agregá un estado de loading. Si tarda más de 300ms en completarse, rediseñá el flujo.

**2. Progresión de complejidad (Progressive Disclosure)**
Simple para nuevos usuarios, poderoso para expertos. No muestres todo de entrada — revelá complejidad cuando el usuario demuestra que está listo.

**3. Cada elemento tiene un solo trabajo**
Un label etiqueta. Un botón ejecuta una acción. Un estado vacío invita a actuar. Cuando un elemento intenta hacer dos cosas, falla en las dos.

---

## 02 — Sistema Visual: Tokens y Variables

### Estructura de tokens recomendada

```
tokens/
├── primitivos/
│   ├── color.json
│   ├── spacing.json    # 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px
│   ├── radius.json
│   └── typography.json
│
└── semanticos/
    ├── color/
    │   ├── background.json   # bg-default, bg-subtle, bg-muted, bg-emphasis
    │   ├── border.json
    │   ├── text.json         # text-primary, text-secondary, text-disabled
    │   └── interactive.json  # action-primary, action-hover, action-pressed
    ├── spacing.json
    └── elevation.json
```

### Paleta base recomendada (2026)

```
-- Neutros (el 90% de la interfaz)
neutral-50:   #FAFAFA
neutral-100:  #F4F4F5
neutral-200:  #E4E4E7
neutral-400:  #A1A1AA
neutral-600:  #52525B
neutral-800:  #27272A
neutral-950:  #09090B

-- Acento (el 10% — con extrema restricción)
accent-400:   [color de marca]
accent-500:   [versión hover]
accent-600:   [versión pressed]

-- Semánticos
success:  #22C55E
warning:  #F59E0B
error:    #EF4444
```

### Escala tipográfica

```
text-xs:   11px / lh: 1.4  — labels, captions
text-sm:   13px / lh: 1.5  — body secundario
text-base: 15px / lh: 1.6  — body principal
text-lg:   19px / lh: 1.4  — subtítulos
text-xl:   24px / lh: 1.3  — títulos de sección
text-2xl:  30px / lh: 1.2  — títulos de página
text-3xl:  38px / lh: 1.1  — hero, display
```

| Tipo de producto | Display | Body | Mono |
|---|---|---|---|
| SaaS / Productividad | Inter, Geist | Inter | Geist Mono |
| Consumer / B2C | Plus Jakarta Sans | Inter | — |
| Developer-first | — | Geist | Geist Mono (protagonista) |
| Enterprise | Inter | Inter | IBM Plex Mono |

---

## 03 — Layout y Espaciado

### Sistema de 4px (todo espaciado es múltiplo de 4)

```
4px   — separación mínima entre elementos relacionados
8px   — padding interno de chips, badges
12px  — gap entre iconos y labels
16px  — padding estándar de contenedores
24px  — separación entre grupos de elementos
32px  — separación entre secciones
48px  — separación entre secciones mayores
64px  — separación entre bloques de página
96px  — espaciado hero
```

### Grid

```
Mobile:  4 col, gutter 16px, margin 16px
Tablet:  8 col, gutter 24px, margin 24px
Desktop: 12 col, gutter 24px, margin 32px

max-width: 1280px (marketing) / 960px (formularios) / 720px (texto)
```

### Densidad por audiencia

| Audiencia | Densidad | Ejemplo |
|---|---|---|
| Developer / power user | Alta | Linear, Raycast, Vercel |
| Knowledge worker | Media | Notion, Figma |
| Consumer / casual | Baja | Apps mobile |
| C-Suite | Muy baja | Dashboards ejecutivos |

---

## 04 — Componentes: Patrones de Alta Aceptación

### Buttons

```
Primary     — fondo acento — 1 por pantalla
Secondary   — borde sutil, texto primario
Ghost       — sin borde, texto
Destructive — rojo, solo para acciones irreversibles

Tamaños:
sm: height 28px, padding 0 10px
md: height 36px, padding 0 14px  (default)
lg: height 44px, padding 0 18px
```

Copy: verbo + objeto siempre. "Guardar cambios", "Crear proyecto". Nunca "OK" o "Confirmar".

### Inputs

```
Label:       text-sm, font-medium
Input:       height 36px, border 1px, radius 6px
             focus: border-accent, ring 2px accent/20
             error: border-error, ring 2px error/20
Helper text: text-xs, text-secondary
Error text:  text-xs, color error
```

Validar al blur, no al typing. Mínimo de campos siempre.

### Navigation

```
Sidebar contraída: 56px
Sidebar expandida: 240–280px

Nav item: text-sm, padding 6px 8px, radius 6px
Activo:   bg-accent/10, text-accent, font-medium
```

### Command Palette (Cmd+K)

```
Trigger: Cmd+K / Ctrl+K
Apertura: < 50ms
Container: width 560px, max-height 400px
Input: placeholder "Buscar o ejecutar..."
Resultados: agrupados por categoría con highlight de query
```

### Estados de componentes (los 6 obligatorios)

```
1. Default
2. Hover
3. Focused (teclado — accesibilidad)
4. Active
5. Disabled
6. Loading
```

### Elevación

```
Nivel 0: sin sombra, borde 1px — listas
Nivel 1: shadow-sm + border — cards
Nivel 2: shadow-md — dropdowns, tooltips
Nivel 3: shadow-lg — modals, sheets
```

---

## 05 — Interacción y Feedback

### Timing

```
< 50ms:   sin feedback necesario
50-100ms: estado activo visual
100-300ms: skeleton o spinner ligero
> 300ms:  loading state explícito
> 1000ms: proceso en background con notificación
```

### Microinteracciones

```css
--duration-fast:   100ms
--duration-normal: 200ms
--duration-slow:   300ms
--ease-out:    cubic-bezier(0, 0, 0.2, 1)
--ease-in:     cubic-bezier(0.4, 0, 1, 1)
--ease-inout:  cubic-bezier(0.4, 0, 0.2, 1)
--ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1)
```

Solo animar `transform` y `opacity`. Nunca `width`, `height`, `top`, `left`, `margin`.

### Empty States

```
1. Icono contextual
2. Título específico (no "Sin resultados")
3. Descripción de UNA oración
4. CTA primario
5. (opcional) Link secundario
```

---

## 06 — Onboarding

Flujo recomendado:
```
Paso 1: Email + password — nada más
Paso 2: Una pregunta de routing
Paso 3: Primer momento de valor (template / demo / acción guiada)
Paso 4: Micro-wins (checklist 3-5 items)
Paso 5: Datos adicionales (nombre, empresa — cuando ya está enganchado)
```

---

## 07 — Dark Mode

```
/* Dark Mode — sistema propio, no inversión */
--bg-page:        #0A0A0A
--bg-subtle:      #141414
--bg-muted:       #1A1A1A
--text-primary:   #FAFAFA
--text-secondary: #A1A1AA
--border:         #27272A

/* Elevación por luminancia (no por sombras) */
bg-page:    #0A0A0A  (base)
bg-card:    #141414  (+1 nivel)
bg-popover: #1A1A1A  (+2 niveles)
bg-tooltip: #27272A  (+3 niveles)
```

---

## 08 — Accesibilidad (los 5 no-negociables)

1. **Contraste:** texto normal 4.5:1, texto grande 3:1
2. **Focus visible:** más obvio que el hover
3. **Touch targets:** mínimo 44×44px en mobile
4. **Alt text:** descriptivo para imágenes informativas, `alt=""` para decorativas
5. **Reduced motion:** siempre respetar `prefers-reduced-motion`

---

## 09 — Performance como UX

```
LCP:  < 2.5s
INP:  < 200ms
CLS:  < 0.1
TTFB: < 800ms
```

- Imágenes con dimensiones definidas (evita CLS)
- WebP o AVIF en 2026
- Máximo 2 familias tipográficas
- Skeleton screens > spinners cuando el layout es predecible

---

## 10 — Patrones por Tipo de Producto

**SaaS / Productividad** (Linear, Notion): sidebar siempre visible, Cmd+K obligatorio, dark mode primero, densidad media-alta.

**Developer Tool** (Vercel, Raycast): mono prominente, densidad alta, paleta reducida, errores técnicos precisos.

**Consumer / Mobile** (Loom, Arc): densidad baja, bottom nav, gestos nativos, onboarding 3 pasos máximo.

**Dashboard / Analytics**: mostrar solo datos que llevan a acción, jerarquía clara, colores semánticos consistentes.

---

## 11 — Copy de Interfaz

```
✓ Activo:    "Guardá los cambios"
✗ Pasivo:    "Los cambios serán guardados"

✓ Específico: "Eliminá el proyecto"
✗ Genérico:   "Confirmar eliminación"

✓ Sentence case: "Nueva tarea"
✗ Title Case:    "Nueva Tarea"
```

**Errores:** título (qué falló) + descripción (por qué, si aporta) + acción (qué hacer ahora).

**Confirmaciones destructivas:** nunca "¿Estás seguro?". Sí: "Eliminar 'Proyecto X' — esta acción no se puede deshacer y eliminará 47 archivos."

---

## Auditoría Rápida

**Claridad**
- [ ] ¿Qué hace cada elemento? (si no podés responder en < 3 palabras, simplificá)
- [ ] ¿La acción principal está visualmente clara?
- [ ] ¿Los estados vacíos tienen CTA de salida?

**Consistencia**
- [ ] ¿Todos los colores vienen de tokens?
- [ ] ¿Todos los espaciados son múltiplos de 4?
- [ ] ¿Los errores tienen siempre la misma estructura?

**Accesibilidad**
- [ ] ¿Todos los elementos interactivos son alcanzables por teclado?
- [ ] ¿El focus visible es obvio?
- [ ] ¿El contraste mínimo es 4.5:1?

**Performance**
- [ ] ¿Las imágenes tienen dimensiones definidas?
- [ ] ¿Las animaciones usan solo transform/opacity?

**Mobile**
- [ ] ¿Los touch targets tienen al menos 44×44px?
- [ ] ¿El contenido se ve bien en 375px?

---

*Documento mantenido por SiriusLabs — siriuslabs.uy@gmail.com*
