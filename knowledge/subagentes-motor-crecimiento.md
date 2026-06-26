# Subagentes del Motor de Crecimiento
### Equipo especializado para validar demanda, lanzar y escalar con disciplina

> **Por qué el Motor necesita subagentes:**
> El Agente 7 hace dos trabajos distintos: validar que existe demanda (Fase 5) y construir un motor de crecimiento sostenible (Fase 6). Dentro de cada uno hay disciplinas separadas: adquisición orgánica, pagada, activación y retención. El error más caro del crecimiento es escalar un canal antes de validarlo. Los subagentes hacen ese error estructuralmente imposible.

---

## Principio rector

El crecimiento no es gastar más en publicidad. Es encontrar un mecanismo repetible donde meter $1 produce más de $1 de valor, y hacer ese mecanismo más grande.

**Regla del Motor: validar con $500 antes de escalar a $50.000. Orgánico antes que pagado. El canal pagado amplifica lo que funciona — nunca lo descubre.**

---

## Los 5 Subagentes

```
┌────────────────────────────────────┐
│   AGENTE 7 — MOTOR DE CRECIMIENTO  │
└─────────────────┬──────────────────┘
                  │
   ┌─────────┬────┴────┬─────────┬─────────┐
  7.A       7.B       7.C       7.D       7.E
Validador Orgánico  Pagado   Activación Retención
Demanda                              + Lifecycle
```

**Flujo:**
```
FASE 5: 7.A Validador ($500) → 7.B Orgánico → 7.D Activación → GATE 5
FASE 6: 7.C Pagado (escala) + 7.E Retención (mantiene y expande)
```

---

# SUBAGENTE 7.A — VALIDADOR DE DEMANDA

**Función:** El experimento de $500 que confirma que existe gente dispuesta a pagar antes de invertir en escalar. Protege contra el error más caro: escalar algo que no funciona.

---

## SKILL 7.A.1 — demand-validation-experiment

**Trigger:** Inicio de Fase 5, antes de gastar en marketing. "validar demanda", "experimento de $500", "¿hay demanda?", "prueba de mercado".

**INPUT obligatorio:** Modelo de negocio (4.1) + GTM (4.2) + MVP/landing + Perfil de población (1.2).

**OUTPUT:**
```
EXPERIMENTO DE VALIDACIÓN — [Proyecto]
Presupuesto: $500 | Duración: [días]

─── HIPÓTESIS FALSABLE ───
"Creemos que [población] está dispuesta a [acción de conversión]
cuando le mostramos [propuesta de valor] a través de [canal],
a un CAC menor a $[X]."
Lo que probamos: [pregunta central] | Lo que NO probamos: [fuera de alcance]

─── DISEÑO ───
Canal de prueba: [cuál] — razón: [donde la audiencia tiene mayor intención]
Audiencia: [segmentación específica]
Oferta: [producto / waitlist / pre-order]
Acción medida: [registro / pago / reserva / demo]

─── MÉTRICA DE ÉXITO (antes de empezar) ───
Primaria: [número concreto — ej: "20 registros con email real a CAC <$25"]
Umbral de éxito: [valor exacto] | Umbral de fracaso: [valor exacto]

─── CRITERIO DE DECISIÓN (antes de ver resultados) ───
CAC <$[X] y conv >[Y]% → VALIDADO → escalar
CAC $[X-Z] o conv [Y-W]% → MIXTO → iterar y re-probar
CAC >$[Z] o conv <[W]% → NO VALIDADO → pivot o kill

─── INSTRUMENTACIÓN ───
Herramienta: [UTM / pixel / PostHog] | Qué confirma conversión real (no bot): [criterio]

─── POST-EXPERIMENTO ───
Si VALIDADO: [pasar a 7.B o 7.C] | Si MIXTO: [qué variable cambiar — una sola] | Si NO: [fase/kill]
```

**REGLAS:**
- La métrica de éxito se define antes de ver resultados. Definirla después es trampa.
- Un experimento = una hipótesis. 3 canales = 3 experimentos.
- "Intención de pagar" en encuesta ≠ validación. La validación es una acción: registro, pago, demo.
- No cambiar las reglas a mitad del experimento.
- El canal se elige por intención de audiencia, no por costo.

---

## SKILL 7.A.2 — first-paying-customer

**Trigger:** Después de validar demanda. "primer cliente pagador", "primera venta", "primer pago real".

**INPUT obligatorio:** Resultado del experimento (7.A.1) + pricing (4.1) + perfil de población (1.2).

**OUTPUT:**
```
PRIMER CLIENTE PAGADOR — [Proyecto]

─── PERFIL IDEAL ───
Quién es: [específico — no "PYMES" sino "dueño de restaurante de 1-2 locales que ya usa WhatsApp para reservas"]
Por qué primero: [dolor más agudo / más fácil de alcanzar / más representativo]
Dónde está: [canal específico]

─── LA OFERTA ───
Precio: $[monto] (puede ser descuento fundador X%)
Qué incluye: [exactamente qué recibe]
Qué pedimos a cambio: [feedback / testimonio / caso de estudio]

─── EL PITCH ───
Apertura: "[referencia a su dolor específico]"
Propuesta: "[qué ofrecemos en una oración]"
Prueba: "[por qué creernos — demo, garantía, prueba social]"
Cierre: "[la pregunta que pide el sí]"

─── CANAL Y OBJECIONES ───
Cómo lo contactamos: [cold outreach / comunidad / referido]
Objeción esperada: "[lo que dirán]" → Respuesta: "[cómo respondemos]"

Meta: primer pago real en [N días] | Conversaciones estimadas para 1 pago: [N]
```

**REGLAS:** Perfil como persona real, no categoría demográfica. El pago es real — compromiso verbal no cuenta. Gratis no valida disposición a pagar.

---

# SUBAGENTE 7.B — ESPECIALISTA EN ORGÁNICO

**Función:** Conseguir usuarios sin presupuesto publicitario: comunidades, SEO, contenido, Product Hunt, partnerships. El orgánico va primero porque valida que el mensaje funciona antes de amplificarlo con dinero.

---

## SKILL 7.B.1 — organic-channel-strategy

**Trigger:** Después de validar demanda. "canales orgánicos", "comunidades", "Product Hunt", "SEO", "tracción sin presupuesto".

**INPUT obligatorio:** Perfil de población (1.2) + propuesta de valor (4.1) + resultado del experimento (7.A.1).

**OUTPUT:**
```
CANALES ORGÁNICOS — [Proyecto]

─── DÓNDE ESTÁ LA AUDIENCIA ───
Comunidades: [Reddit / Discord / grupos WhatsApp / foros]
Redes: [LinkedIn / X / Instagram / TikTok — donde el segmento es activo]
Búsqueda: [keywords que busca la audiencia]
Referentes del nicho: [quién tiene la atención del segmento]

─── CANAL 1 (prioritario) ───
Canal: [específico] — por qué primero: [mayor concentración de intención]
Táctica: [acciones concretas, no "estar presente"]
Acción semanal: [qué publicar / dónde participar]
Regla: aportar valor antes de promocionar (ratio 9:1)
Tiempo de activación: [cuándo esperamos resultados] | Métrica: [registros/semana]

─── CANAL 2 ───
[misma estructura]

─── PRODUCT HUNT (si aplica) ───
¿Tiene sentido? [sí/no] — Preparación: [audiencia previa + assets]
Día de lanzamiento: [táctica primeras horas] | Meta: [posición / registros]

─── SEO / CONTENIDO ───
¿Viable? [sí/no] — tiempo a resultados: [meses]
Keywords: [priorizadas por intención y volumen]
Nota: el SEO no valida demanda en Fase 5 — construye en Fase 6.

─── PARTNERSHIPS ───
Socios: [productos complementarios / comunidades] — qué ganan ellos: [...]

Métrica: registros orgánicos/semana | Canal con mejor conversión: [a identificar]
```

**REGLAS:**
- En comunidades: ratio 9:1 (nueve aportes genuinos por cada mención). Spamear quema el canal.
- El orgánico se mide en tiempo invertido. Si consume 20h/semana para 2 registros, no es viable.
- El SEO no valida demanda en Fase 5 (tarda meses). Es inversión de Fase 6.
- Product Hunt requiere preparación de semanas. No improvisar.

---

# SUBAGENTE 7.C — ESPECIALISTA EN PAGADO

**Función:** Escalar adquisición con canales pagados (Meta/Google/LinkedIn Ads) con CAC controlado. Solo entra DESPUÉS de que el orgánico validó el mensaje. El pagado amplifica lo que ya convierte.

---

## SKILL 7.C.1 — paid-acquisition-strategy

**Trigger:** Fase 6, después de validar el mensaje orgánicamente. "campañas pagadas", "Meta Ads", "Google Ads", "escalar con publicidad", "ads".

**INPUT obligatorio:** Mensaje validado (7.B.1) + CAC objetivo (3.B.1) + creativas (Agente 8) + LTV/CAC objetivo (>3x).

**OUTPUT:**
```
ADQUISICIÓN PAGADA — [Proyecto]

─── PRECONDICIÓN (verificar antes de gastar) ───
✅/❌ Mensaje validado orgánicamente
✅/❌ CAC objetivo definido (LTV/CAC >3x → CAC máx = $[X])
✅/❌ Creativas con variantes A/B (del Narrador)
✅/❌ Funnel instrumentado end-to-end
Si algún ❌ → no escalar todavía.

─── SELECCIÓN DE CANAL ───
Primario: [Meta / Google / LinkedIn]
  Google: alta intención (la gente busca la solución)
  Meta: descubrimiento (crear demanda con interrupciones)
  LinkedIn: B2B, ACV alto

─── CAMPAÑA INICIAL ───
Presupuesto de prueba: $[pequeño]/día durante [días]
Audiencias: [2-3 segmentos] | Creativas: [variantes A/B]
Objetivo: conversión (registro o pago) — nunca clicks ni impresiones

─── MÉTRICAS Y UMBRALES ───
CAC objetivo: <$[X] | CTR mínimo: [%] | Conversión landing: [%]
Regla de escala: escalar solo cuando CAC <$[X] durante [N] días consecutivos

─── ESCALA GRADUAL ───
Sem 1-2: $[X]/día — validar CAC por audiencia
Sem 3-4: escalar ganadoras a $[X×2]/día
Sem 5+: escalar mientras CAC <objetivo
Techo de eficiencia: cuando duplicar presupuesto sube CAC >[X]%

─── MATRIZ DE DECISIÓN ───
CAC <objetivo + volumen creciente → ESCALAR
CAC <objetivo + volumen estancado → MANTENER (techo de audiencia)
CAC >objetivo → PAUSAR y revisar (creativa/audiencia/landing)
```

**REGLAS:**
- No escalar pagado sin mensaje validado orgánicamente.
- Empezar pequeño y escalar gradual. Nunca volcar todo el presupuesto de entrada.
- Objetivo de campaña = conversión, nunca clicks/impresiones.
- CAC medido por canal Y campaña Y audiencia — no blended que esconde campañas malas.
- Techo de eficiencia definido — no "escalar infinitamente".

---

# SUBAGENTE 7.D — ESPECIALISTA EN ACTIVACIÓN

**Función:** Garantizar que los usuarios que llegan lleguen a su primer momento de valor rápido. La activación es el puente entre adquisición y retención.

**Por qué es necesario:** El mejor canal de adquisición es inútil si los usuarios no se activan. La activación es donde se pierde más valor silenciosamente — usuarios que se registran y nunca vuelven porque no llegaron al "momento aha".

---

## SKILL 7.D.1 — activation-optimization

**Trigger:** Cuando llegan usuarios pero la retención temprana es baja. "activación", "onboarding", "time-to-value", "los usuarios no vuelven", "aha moment".

**INPUT obligatorio:** Flujo de onboarding (5.1) + eventos de analytics (6.3) + comportamiento de usuarios.

**OUTPUT:**
```
OPTIMIZACIÓN DE ACTIVACIÓN — [Proyecto]

─── MOMENTO DE VALOR ───
El "momento aha": [acción específica donde el usuario entiende el valor]
Ej: chatbot de reservas → "ve la primera reserva gestionada automáticamente"
Métrica de activación: [% que llega al momento aha]
Tiempo objetivo: ≤3 minutos

─── FUNNEL DE ACTIVACIÓN ───
Paso 1 [registro]: % completa [%] — fricción: [qué los frena]
Paso 2 [setup]: % completa [%] — fricción: [...]
Paso 3 [primera acción]: % completa [%]
Paso 4 [momento aha]: % llega [%] ← MÉTRICA DE ACTIVACIÓN
Mayor abandono: [qué paso] — hipótesis: [por qué]

─── OPTIMIZACIONES ───
[qué cambiar] — [en qué paso] — [impacto esperado]

─── PRIMEROS 7 DÍAS ───
Día 0: [experiencia + comunicación]
Día 1: [seguimiento — qué dice, qué acción pide]
Día 3: [check-in — tip de uso]
Día 7: [¿volvió? qué hacer si no]

─── MÉTRICA NORTE ───
Activación actual: [%] → Meta: [%] | Benchmark sector: [%]
```

**REGLAS:**
- El momento de valor es una acción específica observable, no "el usuario entiende el producto".
- Activación = % que llega al momento aha, no % que se registra.
- Los primeros 7 días tienen comunicación planificada.
- Cada optimización se prueba con experimento medible.

---

# SUBAGENTE 7.E — ESPECIALISTA EN RETENCIÓN Y LIFECYCLE

**Función:** Mantener usuarios activos en el tiempo y expandir el valor que generan. Palancas de retención (reducir churn) y expansión de cuenta (aumentar NRR) + lifecycle de comunicación.

**Por qué es necesario:** Adquirir cuesta 5-7x más que retener. Un producto con churn alto es un balde con agujeros — no importa cuánta agua le eches.

---

## SKILL 7.E.1 — retention-and-expansion

**Trigger:** Fase 6, con base de usuarios que mantener. "retención", "reducir churn", "expansión de cuenta", "NRR", "upsell".

**INPUT obligatorio:** Datos de churn (9.1) + mecanismos de expansión (4.1) + comportamiento de usuarios.

**OUTPUT:**
```
RETENCIÓN Y EXPANSIÓN — [Proyecto]

─── DIAGNÓSTICO ───
Churn mensual: [%] — Meta: <[%]
Curva de retención: [cuándo se van — día 1 / semana 1 / mes 1 / mes 3]
Mayor abandono: [cuándo] — hipótesis: [por qué]
Cohorte insight: usuarios que [hicieron X] retienen [Y]% más → [qué comportamiento predice retención]

─── PALANCAS DE RETENCIÓN ───
Palanca 1: [acción concreta] — impacto en churn: [-X%] — implementación: [quién/qué/cuándo]
Palanca 2 [hábito]: [...]
Palanca 3 [valor acumulado que aumenta costo de irse]: [...]

─── PALANCAS DE EXPANSIÓN ───
Mecanismo 1 [upsell al llegar a un límite]: trigger [cuándo] — impacto NRR [+X%]
Mecanismo 2 [cross-sell / add-ons / asientos]: [...]
NRR objetivo: >110% (expansión supera churn)

─── LIFECYCLE DE COMUNICACIÓN ───
Onboarding (día 0-7): [secuencia de 7.D]
Engagement (sem 2-4): [refuerza el hábito]
Retención (mes 2+): [valor continuo — tips, novedades]
Win-back (inactivos): trigger [N días sin actividad] — mensaje [qué los trae de vuelta]
Expansión (power users): trigger [umbral de uso] — oferta de upgrade en momento de máximo valor

─── MÉTRICAS ───
Churn: [actual] → [meta] | NRR: [actual] → [>110%]
Retención día 7/30/90: [%]/[%]/[%] | Reactivación: [%]
```

**REGLAS:**
- Retención analizada por cohortes, no número agregado.
- Las palancas atacan el punto de mayor abandono de la curva — no mejoras genéricas.
- La expansión se ofrece en el momento de máximo valor percibido (límite alcanzado / hito), no aleatoriamente.
- El win-back tiene trigger definido, no es email masivo a todos.

---

## Definition of Done — Crecimiento

```
DEFINITION OF DONE — MOTOR DE CRECIMIENTO

─── VALIDACIÓN (7.A) ───
□ Experimento de $500 con hipótesis falsable
□ Métrica de éxito definida ANTES de empezar
□ Criterio de decisión definido antes de ver resultados
□ Al menos 1 pago real (dinero en la cuenta, no intención)
□ Primer cliente pagador con perfil específico

─── ORGÁNICO (7.B) ───
□ Mapa de dónde está la audiencia
□ Al menos 1 canal orgánico activado con táctica concreta
□ Mensaje validado orgánicamente antes de pagado
□ Métrica de registros orgánicos/semana

─── PAGADO (7.C) ───
□ Precondición verificada (mensaje + CAC + creativas + funnel)
□ Campaña con presupuesto pequeño y escala gradual
□ CAC por canal/campaña/audiencia (no solo blended)
□ Techo de eficiencia definido
□ LTV/CAC >3x en canales escalados

─── ACTIVACIÓN (7.D) ───
□ Momento de valor con acción específica observable
□ Funnel de activación con % por paso
□ Time-to-value ≤3 min verificado en la práctica
□ Plan de primeros 7 días
□ Tasa de activación medida con meta

─── RETENCIÓN (7.E) ───
□ Análisis de retención por cohortes
□ Palancas que atacan el punto de mayor abandono
□ Mecanismos de expansión de cuenta
□ Lifecycle de comunicación completo
□ NRR objetivo >110%

─── GATE 5 (decisivo) ───
□ Demanda validada con datos reales
□ Primeros pagos reales
□ CAC sostenible (LTV/CAC >3x con CAC real)
□ Retención temprana positiva
□ Sean Ellis ≥40% (si ≥40 respuestas)
□ Aprobado por Auditor de Growth (Guardián 10.D)
```

---

## Cuándo agregar subagentes adicionales

| Situación | Subagente adicional |
|---|---|
| E-commerce con catálogo grande | Performance Marketing / ROAS |
| Crecimiento por viralidad | Loops Virales / Referral |
| Enterprise con ciclos largos | Sales / Account-Based Marketing |
| SEO como canal principal | SEO / Content Engine |
| Producto con comunidad | Community-Led Growth |

---

*SiriusLabs — siriuslabs.uy@gmail.com
El Motor de Crecimiento no gasta dinero — encuentra mecanismos donde $1 produce más de $1. Esa es toda la diferencia.*
