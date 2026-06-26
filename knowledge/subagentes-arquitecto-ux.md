# Subagentes del Arquitecto de Experiencia
### Equipo especializado de UX/UI para productos de primer nivel

> **Por qué existen:**  
> Entre una idea de producto y un archivo Figma listo para que el Constructor implemente existe un proceso completo: investigación, arquitectura de información, wireframes, sistema de diseño, prototipado, testing con usuarios, y handoff documentado. Si alguna de esas etapas falla, el Constructor construye lo incorrecto — y eso cuesta 10x más arreglar en código que en diseño.

---

## Principio rector

El diseño no es decoración. Es la traducción del modelo de negocio en comportamiento de usuario. Cada decisión de diseño debe justificarse con una razón de negocio, evidencia de usuario, o restricción técnica. "Se ve bien" no es una justificación.

**Proceso siempre:** investigar → arquitectura de información → wireframes (baja fidelidad) → diseño visual (alta fidelidad) → prototipo → testing → handoff documentado.

---

## Los 5 Subagentes

```
┌──────────────────────────────────┐
│  AGENTE 5 — ARQUITECTO UX        │
└───────────────┬──────────────────┘
                │
   ┌────────┬───┴──┬────────┬────────┐
   5.A      5.B    5.C      5.D      5.E
  IA/Inv.  Wire  Visual   Access   Hand-
           frames Design   ibility  off
```

**Flujo obligatorio:**
```
INVESTIGACIÓN+IA (5.A) → WIREFRAMES (5.B) → TEST USABILIDAD (5.B.2)
→ DISEÑO VISUAL (5.C) → ACCESIBILIDAD (5.D) → HANDOFF (5.E) → GATE 3
```

---

# SUBAGENTE 5.A — INVESTIGADOR / INFORMATION ARCHITECTURE

**Función:** Investigar la experiencia actual del usuario, mapear su journey completo, y diseñar la arquitectura de información del producto.

---

## SKILL 5.A.1 — user-journey-mapping

**Propósito:** Mapear la experiencia completa del usuario con el problema — antes, durante y después de usar el producto. Identificar momentos de mayor fricción y mayor oportunidad.

**Trigger:** Inicio de Fase 3. "user journey", "mapear el journey", "experiencia del usuario", "cómo vive el usuario el problema".

**INPUT obligatorio:** Perfil de población (1.2) + Documento de problema (1.1) + Modelo de negocio (4.1).

**OUTPUT:**
```
USER JOURNEY MAP — [Proyecto]
Usuario: [nombre del segmento] | Escenario: [situación específica]

─── ETAPAS ───
ETAPA [N]: [nombre]
  Qué está haciendo: [acción concreta]
  Qué está pensando: "[cita en su idioma, no el nuestro]"
  Qué está sintiendo: [emoción — frustración / ansiedad / esperanza]
  Puntos de contacto: [dónde interactúa]
  Fricción: [qué le dificulta avanzar]
  Oportunidad: [qué podría hacer mejor el producto aquí]

─── MAPA EMOCIONAL ───
[Curva: alto = positivo, bajo = negativo por etapa]
Etapa 1: 😟 → Etapa 2: 😐 → Etapa 3: 😊 → ...

─── MOMENTOS CRÍTICOS (Top 3) ───
Momento 1: [etapa] — [por qué es crítico] — [decisión de diseño]
Momento 2: ... | Momento 3: ...

─── OPORTUNIDADES DE DISEÑO ───
[insight] → [implicancia de diseño concreta]
```

**REGLAS:**
- El journey usa el lenguaje del usuario, no el de la empresa.
- Las emociones son reales, no idealizadas.
- Cada oportunidad termina con una implicancia concreta y accionable.

---

## SKILL 5.A.2 — information-architecture

**Propósito:** Diseñar cómo se organiza y navega el contenido. Qué existe, cómo se llama, cómo se agrupa, en qué orden aparece.

**Trigger:** Después del user journey. "arquitectura de información", "estructura del producto", "navegación", "mapa del sitio".

**INPUT obligatorio:** User journey (5.A.1) + Scope MVP (6.1) + Modelo de negocio (4.1).

**OUTPUT:**
```
ARQUITECTURA DE INFORMACIÓN — [Proyecto]

─── INVENTARIO DE CONTENIDO ───
Sección: [nombre] — Contenido: [qué hay] — Prioridad: [alta/media/baja]

─── ESTRUCTURA DE NAVEGACIÓN ───
Nivel 1 (máximo 5-7 items):
  • [Item] → [qué contiene]
Nivel 2 (sub-items si aplica):
  [Item] └── [sub-item]

─── MAPA DEL PRODUCTO (ASCII) ───
HOME / DASHBOARD
├── [Feature 1]
│   ├── [Vista]
│   └── [Vista]
├── [Feature 2]
└── CONFIGURACIÓN

─── NOMENCLATURA ───
| Lo que el equipo llama | Lo que el usuario llama | Decisión final |
| "Dashboard" | "Inicio" | [decisión] |

─── JERARQUÍA DE ACCIONES ───
Acción principal: [la más importante — un solo CTA global]
Acciones frecuentes: [lista ordenada por frecuencia]
Acciones raras / destructivas: [enterrar en segundo nivel]

─── PRINCIPIOS APLICADOS ───
1. [ej: "La navegación refleja el flujo de trabajo del usuario, no la estructura técnica"]
2. [ej: "Los nombres usan el vocabulario del usuario confirmado en las entrevistas"]
```

**REGLAS:**
- La navegación refleja cómo piensa el usuario, no cómo está organizado el código.
- Los nombres vienen del vocabulario del usuario (de skill 1.2).
- Máximo 5-7 items en navegación principal.
- Acciones destructivas: nunca en primer nivel, siempre 2 pasos mínimo.

---

## SKILL 5.A.3 — usability-criteria

**Propósito:** Definir criterios de usabilidad específicos y medibles para el producto.

**Trigger:** Al finalizar la IA. "criterios de usabilidad", "métricas de experiencia", "cómo medimos el UX".

**OUTPUT:**
```
CRITERIOS DE USABILIDAD — [Proyecto]

─── MÉTRICAS ───
Time-to-value: [minutos — restricción dura]
Task completion rate: [% objetivo]
Error rate máximo: [%]
SUS score objetivo: [>68 usable, >80 bueno]

─── HEURÍSTICAS DE NIELSEN APLICADAS ───
1. Visibilidad del estado: [cómo el producto muestra qué está pasando]
2. Mundo real: [vocabulario y metáforas a usar]
3. Control y libertad: [cómo el usuario puede deshacer / salir]
4. Consistencia: [qué patrones seguimos]
5. Prevención de errores: [qué errores comunes prevenimos con diseño]
6. Reconocimiento: [qué siempre está visible]
7. Flexibilidad: [atajos para usuarios expertos]
8. Diseño minimalista: [principio de reducción aplicado]
9. Recuperación de errores: [cómo son los mensajes]
10. Ayuda y documentación: [si existe, dónde]

─── FLUJOS CRÍTICOS CON CRITERIO ───
Flujo [nombre]: ≤[N] pasos | ≤[N] minutos | Abandono permitido: 0
Error más probable: [qué] → Prevención: [con diseño, no con texto]
```

---

# SUBAGENTE 5.B — WIREFRAMER

**Función:** Diseñar todos los flujos y pantallas en baja fidelidad antes de tocar el visual. Los wireframes son grises — validan estructura y flujo, no estética.

**Por qué es necesario:** Un wireframe toma el 10% del tiempo de un diseño de alta fidelidad y descubre el 60% de los problemas de usabilidad. Se atrapa lo estructural antes de que el Visual Designer lo embellezca.

---

## SKILL 5.B.1 — wireframe-set

**Propósito:** Set completo de wireframes de baja fidelidad. Cada pantalla, cada estado, cada variante mobile.

**Trigger:** Después de la IA. "wireframes", "bocetos de pantallas", "baja fidelidad", "estructura de pantallas".

**INPUT obligatorio:** User journey (5.A.1) + Arquitectura IA (5.A.2) + Criterios de usabilidad (5.A.3) + Scope MVP (6.1) + Flujo de usuario (5.1).

**OUTPUT por pantalla:**
```
─── PANTALLA: [nombre] ───
PROPÓSITO: [qué debe lograr en la mente del usuario]
ACCIÓN PRINCIPAL: [único CTA primario]
PREGUNTA QUE RESPONDE: [qué pregunta del usuario responde esta pantalla]

LAYOUT (ASCII):
┌─────────────────────────────┐
│  NAV: Logo      [CTA]       │
├─────────────────────────────┤
│                             │
│  [Headline — propuesta de   │
│   valor en una línea]       │
│                             │
│  [Sub-headline sin jerga]   │
│                             │
│      [ CTA PRIMARIO ]       │
│                             │
├─────────────────────────────┤
│  [Prueba social / contexto] │
└─────────────────────────────┘

ANOTACIONES:
- [justificación de cada decisión de layout]
- [por qué este orden de elementos]

ESTADOS:
- Default: [descripción]
- Mobile (375px): [cambios específicos]
- Loading: [qué se muestra]
- Error: [qué se muestra]
- Vacío: [qué se muestra con CTA de salida]
```

**REGLAS:**
- Wireframes son grises. Sin colores de marca, sin tipografía final, sin íconos reales.
- Cada pantalla tiene exactamente UN CTA primario.
- Mobile-first: versión 375px primero, luego desktop.
- Los estados (loading, error, vacío, éxito) se especifican en el wireframe — si no están aquí, el Developer los inventa.
- El layout refleja jerarquía de contenido, no estética final.

---

## SKILL 5.B.2 — wireframe-usability-test

**Propósito:** Testear los wireframes con usuarios reales antes de pasar al diseño visual.

**Trigger:** Después de tener los wireframes. "testear el wireframe", "test de usabilidad", "mostrarle a usuarios".

**INPUT obligatorio:** Wireframe set (5.B.1) + Criterios de usabilidad (5.A.3) + Perfil de usuario (1.2).

**OUTPUT:**
```
REPORTE DE TEST DE USABILIDAD — Wireframes

Participantes: [N] — Método: think-aloud protocol

─── RESULTADOS POR TAREA ───
TAREA: "[texto exacto pedido al usuario]"
  Completación: [N/N] ([%]) | Tiempo promedio: [min]
  Fricción observada: [dónde] — [qué hizo] — [qué esperaba]
  Cita: "[lo que dijo el usuario]"

─── PATRONES (aparece en 3+ de 5 usuarios = señal crítica) ───
Patrón 1: [problema] → [causa] → [corrección recomendada]

─── CAMBIOS ANTES DE PASAR A VISUAL ───
BLOQUEANTE: [problema] → [corrección específica]
IMPORTANTE: [fricción] → [recomendación]
OPCIONAL: [mejora de pulido]

─── VEREDICTO ───
APROBADO / NO APROBADO para visual
Cambios requeridos: [lista] | Re-test: [sí/no]
```

**REGLAS:**
- Mínimo 5 usuarios para identificar patrones (Nielsen: 85% de problemas detectados con 5).
- Las tareas son escenarios, no instrucciones: "Imaginá que querés [objetivo]" — no "hacé click en X".
- Se documenta lo que el usuario HACE, no lo que dice que haría.
- Un patrón en 3+ usuarios = señal. En 4-5 = problema crítico. Bloquea el avance a visual.

---

# SUBAGENTE 5.C — VISUAL DESIGNER

**Función:** Diseñar la alta fidelidad del producto. Traduce los wireframes aprobados en pantallas visuales completas, con el sistema de diseño aplicado. Todo componente en todos sus estados.

---

## SKILL 5.C.1 — visual-design-system

**Propósito:** Construir el sistema de diseño completo. Tokens, componentes, variantes y reglas de uso. Es el documento del que se derivan todas las pantallas.

**Trigger:** Inicio del diseño visual. "sistema de diseño", "design system", "componentes", "tokens", "paleta".

**INPUT obligatorio:** Tipo de producto + audiencia y densidad + tono de marca (3 adjetivos) + ¿dark mode?

**OUTPUT:**
```
SISTEMA DE DISEÑO — [Proyecto] v1.0

─── DECISIÓN VISUAL ESTRATÉGICA ───
Tipo: [SaaS / Consumer / Developer / Dashboard]
Densidad: [alta/media/baja] — Razón: [por audiencia]
Tono: [adj 1], [adj 2], [adj 3]
Riesgo visual asumido: [la decisión más diferenciadora y su justificación]

─── TOKENS SEMÁNTICOS — LIGHT MODE ───
Background: bg-page #[hex] | bg-subtle #[hex] | bg-card #[hex]
Text: text-primary #[hex] | text-secondary #[hex] | text-disabled #[hex]
Border: border-default #[hex] | border-subtle #[hex]
Accent: accent-default #[hex] | accent-hover #[hex] | accent-pressed #[hex]
Semantic: success #22C55E | warning #F59E0B | error #EF4444

─── TOKENS — DARK MODE (sistema propio, NO inversión) ───
bg-page: #0A0A0A (negro casi puro, no #000)
bg-subtle: #141414 (+1 nivel luminancia)
bg-card: #1F1F1F (+2 niveles)
text-primary: #FAFAFA (blanco suavizado, no #FFF)
text-secondary: #A1A1AA
border-default: #27272A
accent-default: [misma matiz que light, más luminoso sobre fondo oscuro]

─── TIPOGRAFÍA ───
Display: [familia] | Heading: [familia] | Body: [familia] | Mono: [si aplica]
Escala:
  3xl: 38px/1.05 | 2xl: 30px/1.10 | xl: 24px/1.20
  lg: 19px/1.35 | md: 15px/1.60 | sm: 13px/1.55 | xs: 11px/1.45
Regla: máximo 2 familias. Bold (700) solo para énfasis crítico.

─── ESPACIADO ───
Todo múltiplo de 4px.
4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 48 / 64 / 80 / 96px

─── ELEVACIÓN ───
LIGHT: shadow-sm / shadow-md / shadow-lg (sombras reales)
DARK: elevación por luminancia (bg-page → bg-subtle → bg-card — no sombras)

─── COMPONENTES CORE (con todos los estados) ───

BUTTON Primary:
  padding: 0 16px | height: 36px (md) / 28px (sm) / 44px (lg)
  bg: accent-default | color: text-inverse | radius: [del proyecto]
  :hover → accent-hover | :active → accent-pressed + scale(0.98)
  :focus-visible → 2px ring accent-default, offset 2px
  :disabled → opacity 40%, no pointer-events
  loading → spinner + "Cargando..."

BUTTON Secondary: bg transparent + border 1px border-default
BUTTON Ghost: bg transparent, no border, text-secondary → text-primary on hover
BUTTON Destructive: bg error-default + confirmación obligatoria

INPUT:
  height: 36px | padding: 0 12px | border: 1px solid border-default
  :hover → border-strong
  :focus → border-accent + ring 2px accent/20
  .error → border-error + ring 2px error/20
  :disabled → bg-subtle, opacity 60%
  Nunca: placeholder como único label (el placeholder desaparece al escribir)

CARD: padding space-4/space-6 | border 1px border-default | radius-xl | shadow-sm
BADGE: padding 4px 8px | radius-full | variantes: default/success/warning/error/info
TOOLTIP: delay 500ms | max-width 200px | trigger: hover + focus (nunca solo hover)
MODAL: overlay 50% | radius-xl | header+footer | cierra: ESC, click overlay, botón X

─── ICONOGRAFÍA ───
Sistema: [Lucide / Heroicons / Phosphor] — Tamaños: 16 / 20 / 24px
Color: currentColor (nunca hardcodeado) | Siempre con label de texto

─── REGLAS INNEGOCIABLES ───
accent-default ÚNICAMENTE en: CTA primario | focus visible | progreso activo
error-default ÚNICAMENTE en: mensajes de error | bordes de error | íconos de error
bold (700) ÚNICAMENTE en: títulos de sección grandes | datos críticos
Dark mode: implementado via data-theme="dark" | Sin colores hardcodeados en código
```

**REGLAS:**
- Todos los colores pasan contraste WCAG AA antes de entrar al sistema (herramienta, no a ojo).
- El sistema vive en Figma como variables. Ningún componente tiene valores hardcodeados.
- Cada componente tiene TODOS sus estados antes de usarse en pantallas.

---

## SKILL 5.C.2 — high-fidelity-screens

**Propósito:** Diseñar cada pantalla del MVP en alta fidelidad con el sistema de diseño aplicado.

**Trigger:** Después de sistema de diseño aprobado y wireframes aprobados.

**CHECKLIST por pantalla (todo en verde antes de entregar):**
```
─── ESTRUCTURA ───
□ Sigue el wireframe aprobado (cambios = re-aprobación)
□ CTA primario único y usando button-primary
□ Jerarquía visual refleja jerarquía de contenido
□ Espaciado múltiplo de 4px en todos los elementos

─── SISTEMA DE DISEÑO ───
□ Todos los colores de tokens semánticos (sin hardcodeados)
□ Tipografía de la escala definida (sin tamaños arbitrarios)
□ Componentes del sistema (sin componentes únicos de pantalla)
□ 6 estados de todos los componentes interactivos diseñados

─── ESTADOS OBLIGATORIOS ───
□ Default | Hover | Focus visible | Active | Disabled | Loading
□ Error | Success | Empty (con CTA de salida, nunca pantalla en blanco)

─── MOBILE FIRST ───
□ 375px diseñado primero
□ Touch targets ≥44×44px en mobile
□ Desktop diseñado segundo

─── COPY ───
□ Todo el copy del documento de copy (skill 5.3) — sin Lorem ipsum
□ Empty states: título + descripción + CTA
□ Errores: específicos y accionables
```

---

## SKILL 5.C.3 — prototype-interactive

**Propósito:** Conectar las pantallas en un prototipo interactivo navegable. Testear el flujo antes de que el Constructor escriba código.

**OUTPUT:**
```
PROTOTIPO — [Proyecto]

Flujos prototipados: [lista]
Interacciones: [click en X → pantalla Y con transición Z]

Transiciones:
  Navegación: Smart Animate / Slide / Push
  Modals: scale(0.95)+opacity(0) → scale(1)+opacity(1), 200ms ease-out
  Hover: 100ms ease-out (siempre ease, nunca linear)

Link Figma: [URL view-only]
Instrucciones: [cómo navegar el prototipo]
Limitaciones: [qué no está interactivo]
```

---

# SUBAGENTE 5.D — ACCESSIBILITY AUDITOR

**Función:** Garantizar que el producto puede ser usado por la mayor cantidad de personas posible. Audita contra WCAG 2.2 AA. Es BLOQUEANTE para el handoff.

**Por qué es necesario:** Solo el 30% de los sitios cumplen estándares básicos de accesibilidad. Los que los cumplen tienen 23% más de tráfico. El 16% de la población mundial tiene algún tipo de discapacidad. Y en 2026, en muchas jurisdicciones es legalmente obligatorio.

---

## SKILL 5.D.1 — accessibility-audit

**Propósito:** Auditar el diseño de alta fidelidad contra WCAG 2.2 AA. Issues críticos/importantes = RECHAZADO para handoff.

**Trigger:** Después del diseño de alta fidelidad, ANTES del handoff.

**INPUT obligatorio:** Pantallas de alta fidelidad (5.C.2) + Sistema de diseño (5.C.1).

**OUTPUT:**
```
ACCESSIBILITY AUDIT — [Proyecto]
Estándar: WCAG 2.2 AA | Fecha: [fecha]

Resumen: CRÍTICOS: [N] | IMPORTANTES: [N] | RECOMENDADOS: [N]

─── CONTRASTE (verificado con herramienta, no a ojo) ───
| Elemento | Color texto | Color fondo | Ratio | Meta | Estado |
| Body text | #hex | #hex | X:1 | ≥4.5:1 | ✅/❌ |
| Secondary | #hex | #hex | X:1 | ≥4.5:1 | ✅/❌ |
| Botones | #hex | #hex | X:1 | ≥3:1 | ✅/❌ |
| Íconos | #hex | #hex | X:1 | ≥3:1 | ✅/❌ |

─── CHECKLIST WCAG 2.2 AA ───
PERCEIVABLE:
□ 1.1.1 Alt text en imágenes informativas (decorativas: alt="")
□ 1.3.1 Estructura semántica comunicada
□ 1.4.1 Color no es el único medio para comunicar (+ ícono/texto en errores)
□ 1.4.3 Contraste texto normal ≥4.5:1
□ 1.4.4 Contraste texto grande (≥18px) ≥3:1
□ 1.4.11 Contraste elementos UI (botones, inputs, íconos) ≥3:1

OPERABLE:
□ 2.1.1 Todo accesible con teclado (diseño: focus visible en todos los elementos)
□ 2.4.3 Orden de foco lógico = orden visual
□ 2.4.6 Encabezados descriptivos (no "Sección 1")
□ 2.4.7 Focus visible diseñado (con ring de acento — más visible que hover)

UNDERSTANDABLE:
□ 3.3.1 Errores identifican el ítem + describen el problema (no "campo inválido")
□ 3.3.2 Labels visibles en todos los inputs (no solo placeholder)

ROBUST:
□ 4.1.2 Íconos sin texto → aria-label especificado en el diseño

─── ISSUES ───
CRÍTICO [N]: [criterio] | [pantalla] | [descripción exacta] | [corrección específica]
IMPORTANTE [N]: [misma estructura]
RECOMENDADO [N]: [descripción] | [recomendación]

─── SPECS DE ACCESIBILIDAD PARA DEVELOPER ───
Íconos sin texto:
  [ícono de cerrar]: aria-label="Cerrar"
  [lista completa]

Inputs:
  Todos: aria-required="true/false"
  Con helper: aria-describedby="[id]"
  Con error: aria-describedby="[id]" + aria-invalid="true"

Regiones dinámicas:
  Toasts/notificaciones: aria-live="polite"
  Errores críticos: aria-live="assertive"

─── VEREDICTO ───
APROBADO: 0 críticos + 0 importantes → pasar a handoff
RECHAZADO: resolver issues críticos/importantes + re-auditar
```

**REGLAS:**
- Issues críticos = handoff bloqueado. Sin excepción.
- El contraste se verifica con herramienta (WebAIM, Figma plugin). Nunca a ojo.
- Focus visible es un diseño real en Figma — no algo que "el developer verá".
- Inputs nunca con solo placeholder como label (desaparece al escribir).
- Aria-labels son responsabilidad del Diseñador especificar, no del Developer inventar.

---

# SUBAGENTE 5.E — DESIGN HANDOFF SPECIALIST

**Función:** Preparar y entregar el diseño al Constructor con cero ambigüedad. El Constructor no debería tener que hacer preguntas — todo está en el handoff.

---

## SKILL 5.E.1 — design-handoff-document

**Propósito:** Documento de handoff completo. El Constructor recibe esto + el link de Figma y puede implementar.

**Trigger:** Después de auditoría de accesibilidad aprobada. "handoff", "entregar al developer", "specs de diseño".

**INPUT obligatorio:** Pantallas aprobadas (5.C.2) + Auditoría aprobada (5.D.1, 0 críticos/importantes) + Sistema de diseño (5.C.1) + Copy (skill 5.3).

**OUTPUT:**
```
DESIGN HANDOFF — [Proyecto] v1.0
Figma (Dev Mode habilitado): [URL]
Design System Figma: [URL]

─── TOKENS EN CSS (pegar en globals.css) ───
:root {
  /* Background */
  --bg-page: #[hex];    --bg-subtle: #[hex];    --bg-card: #[hex];
  /* Text */
  --text-primary: #[hex];  --text-secondary: #[hex];  --text-disabled: #[hex];
  /* Border */
  --border-default: #[hex];  --border-subtle: #[hex];
  /* Accent */
  --accent-default: #[hex];  --accent-hover: #[hex];  --accent-pressed: #[hex];
  /* Semantic */
  --success: #22C55E;  --warning: #F59E0B;  --error: #EF4444;
  /* Spacing */
  --space-1: 4px;  --space-2: 8px;  --space-3: 12px;  --space-4: 16px;
  --space-6: 24px;  --space-8: 32px;  --space-12: 48px;  --space-16: 64px;
  /* Transitions */
  --duration-fast: 100ms;  --duration-normal: 200ms;  --duration-slow: 300ms;
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
}
[data-theme="dark"] {
  --bg-page: #0A0A0A;  --bg-subtle: #141414;  /* ... */
}

─── SPECS DE COMPONENTES ───

BUTTON Primary:
  display: inline-flex | align-items: center | gap: 8px
  padding: 0 16px | height: 36px(md) / 28px(sm) / 44px(lg)
  background: var(--accent-default) | border-radius: var(--radius-lg)
  :hover → var(--accent-hover)
  :active → var(--accent-pressed) + transform: scale(0.98)
  :focus-visible → outline: 2px solid var(--accent-default); outline-offset: 2px
  :disabled → opacity: 0.4; pointer-events: none

INPUT:
  width: 100% | height: 36px | padding: 0 12px
  border: 1px solid var(--border-default) | border-radius: var(--radius-md)
  :hover → border-color: var(--border-strong)
  :focus → border-color: var(--accent-default); box-shadow: 0 0 0 2px accent/20
  .error → border-color: var(--error); box-shadow: 0 0 0 2px error/20
  :disabled → background: var(--bg-subtle); opacity: 0.6

[repetir para cada componente]

─── COMPORTAMIENTOS E INTERACCIONES ───

MODALS:
  Apertura: overlay fade-in 200ms + modal scale(0.95)+opacity(0)→scale(1)+opacity(1) 200ms ease-out
  Cierre (ESC/click overlay/botón): 150ms ease-in
  Focus trap: foco queda dentro del modal mientras está abierto
  Primer foco: primer elemento interactivo del modal

TOASTS:
  Entrada: slide desde arriba/derecha, 300ms ease-out
  Auto-dismiss: 4000ms (success) | permanente (error)
  Salida: fade-out 200ms ease-in

ANIMACIONES GLOBALES:
  Solo transform + opacity (nunca width, height, top, left, margin)
  Hover: 100ms ease-out — nunca linear
  prefers-reduced-motion: { animation-duration: 0.01ms; transition-duration: 0.01ms }

─── ACCESIBILIDAD PARA IMPLEMENTACIÓN ───
(Ver también SKILL 5.D.1 checklist)

Íconos sin texto:
  Cerrar: aria-label="Cerrar"
  [lista completa de la auditoría]

Inputs:
  aria-required="true/false" en todos
  aria-describedby="[id-helper]" cuando tiene helper text
  aria-describedby="[id-error]" + aria-invalid="true" cuando hay error

Regiones dinámicas:
  Notificaciones/toasts: aria-live="polite"
  Errores críticos: aria-live="assertive"

─── ASSETS EXPORTADOS ───
SVGs: [lista de íconos e ilustraciones]
Imágenes: [lista en WebP 1x + 2x + PNG fallback]
Favicon: 16 / 32 / 180 / 192 / 512px
OG Image: 1200×630px
Fuentes: [archivos + formato de carga si son custom]

─── CHECKLIST DE HANDOFF ───
□ Figma con Dev Mode habilitado y link compartido
□ Tokens exportados en CSS variables
□ Todos los componentes con todos sus estados en Design System
□ Anotaciones en cada pantalla completa
□ Assets exportados (SVG, WebP, PNG, favicon, OG)
□ Specs de interacción con timing exacto
□ Aria-labels y atributos de accesibilidad documentados
□ Documento de copy (skill 5.3) vinculado
□ Auditoría de accesibilidad aprobada (0 críticos/importantes)
□ Constructor confirmó que puede implementar sin preguntas adicionales
```

---

## Definition of Done — Diseño UX/UI completo

```
DEFINITION OF DONE — DISEÑO

─── INVESTIGACIÓN Y ARQUITECTURA ───
□ User journey map con momentos críticos identificados
□ Arquitectura de información aprobada con vocabulario del usuario
□ Criterios de usabilidad con métricas concretas

─── WIREFRAMES ───
□ Set completo (todas las pantallas + todos los estados)
□ Mobile-first (375px primero)
□ Test de usabilidad con ≥5 usuarios
□ 0 problemas bloqueantes en el test

─── DISEÑO VISUAL ───
□ Sistema de diseño completo en Figma (tokens + componentes)
□ Todos los componentes con 6 estados (default/hover/focus/active/disabled/loading)
□ Pantallas en alta fidelidad (mobile + desktop)
□ Dark mode si fue requerido
□ Copy final aplicado (sin Lorem ipsum)
□ Prototipo interactivo navegable

─── ACCESIBILIDAD ───
□ Auditoría WCAG 2.2 AA completada
□ 0 issues críticos + 0 issues importantes
□ Contraste verificado con herramienta (no a ojo)
□ Focus visible diseñado para todos los elementos interactivos
□ Labels visibles en todos los inputs (no solo placeholder)
□ Alt text especificado para imágenes informativas
□ Aria-labels documentados para íconos sin texto

─── HANDOFF ───
□ Figma con Dev Mode + acceso compartido
□ Tokens exportados en CSS variables
□ Anotaciones en cada pantalla
□ Assets exportados (SVG, WebP, PNG, favicon, OG)
□ Especificaciones de interacción con timing exacto
□ Accesibilidad documentada para implementación
□ Copy final vinculado

─── GATE 3 ───
□ Aprobado por el Guardián (Agente 10)
□ Aprobado por revisión humana
□ Constructor confirmó que puede implementar sin preguntas
```

---

## Cuándo agregar subagentes adicionales

| Situación | Subagente adicional |
|---|---|
| Datos de salud/financieros sensibles | Agente de Privacy UX |
| Audiencia principal con discapacidades visuales severas | Accesibilidad Avanzada (WCAG AAA) |
| IA / LLM conversacional en el producto | Conversational UX |
| Mobile nativo (iOS / Android) | Mobile UX (HIG + Material) |
| Onboarding presencial / training | Learning Experience Design |

---

*SiriusLabs — siriuslabs.uy@gmail.com  
Actualizar cuando se detecte un patrón de error recurrente en los diseños entregados.*
