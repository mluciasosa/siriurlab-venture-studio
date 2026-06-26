# Subagentes del Narrador
### Equipo especializado para producción de contenido y comunicación de lanzamiento

> **Por qué existen:**
> El Agente 8 (Narrador) es donde la propuesta de valor se convierte en palabras que mueven a la acción. Un solo agente generalista no puede hacer estrategia de mensajes, producción de piezas creativas, secuencias de email, calendario editorial y distribución bien al mismo tiempo — cada uno tiene un ritmo diferente, criterios de calidad distintos y relaciones de dependencia propias.

---

## Decisión de arquitectura: cuáles merecen subagente propio

Los 5 candidatos iniciales se colapsan en 4 subagentes. Aquí la justificación:

**Copy Strategist → subagente propio (8.A)**
Opera antes de que exista una sola pieza. Define el mensaje, no el contenido. Si el mensaje es incorrecto, todo lo que produce el resto del equipo amplifica el error. Necesita aislamiento para poder ser desafiado.

**Creative Producer → subagente propio (8.B)**
Transforma la estrategia en piezas concretas. Produce el output más voluminoso y más sujeto a variantes A/B. Su criterio de calidad (hook, visual brief, CTA) es distinto al de todos los demás.

**Email & Lifecycle Writer → subagente propio (8.C)**
El email opera con lógica completamente diferente a las redes sociales: tiene segmentación, secuencias en el tiempo, métricas propias (apertura, clic, conversión), y el copy de asunto es una disciplina en sí misma. Colapsarlo con otro subagente destruye la especialización que justifica su existencia.

**Content Strategist + SEO & Distribution Specialist → COLAPSADOS en 8.D**
La razón para mantenerlos separados sería si hay un equipo humano grande donde un rol no sabe de SEO y el otro no sabe de editorial. En el contexto del Venture Engine, donde el agente opera con autonomía, el calendario editorial y la distribución son la misma decisión: qué publicar, cuándo, dónde y con qué tags. Un documento produce el otro. Separarlos crea un handoff artificial.

```
┌──────────────────────────┐
│  AGENTE 8 — NARRADOR    │
│    (orquesta a los 4)   │
└───────────┬──────────────┘
            │
    ┌───────┼──────────┬──────────┐
    │       │          │          │
   8.A     8.B        8.C        8.D
  Copy   Creative   Email &    Content &
Strategist Producer Lifecycle Distribution
```

**Flujo obligatorio:**
```
INPUT (Agente 7) → MENSAJES (8.A) → CALENDARIO (8.D) → PIEZAS (8.B) + SECUENCIAS (8.C) → OUTPUT al Agente 7 + Agente 9
```

Los mensajes van primero. Nada se produce sin estrategia aprobada.

---

# SUBAGENTE 8.A — COPY STRATEGIST

**Función:** Definir el sistema de mensajes de la plataforma antes de que exista un solo titular. Determina qué decir, a quién, en qué etapa del funnel, y con qué tono. Es el único subagente que puede vetar una pieza del 8.B si el mensaje es incorrecto.

---

## SKILL 8.A.1 — message-architecture

**Trigger:** Inicio de Fase 5 (Lanzamiento). Antes de cualquier pieza creativa. "definir mensajes", "qué le decimos a", "propuesta de valor por audiencia".

**INPUT obligatorio:** Propuesta de valor validada (Agente 4) + perfil de audiencia (Agente 7) + canales activos (Agente 7).

**INPUT opcional:** Entrevistas de usuario (Agente 1) + datos de competidores (Agente 2).

**OUTPUT:**
```
MESSAGE ARCHITECTURE — [Proyecto] v1.0

─── CORE MESSAGE ───
Problema que resolvemos: [en las palabras exactas que usó la audiencia en entrevistas]
Solución: [mecanismo diferencial — qué hacemos que otros no]
Prueba: [dato, resultado, caso real]
CTA principal: [verbo + consecuencia]

─── AUDIENCIA PRIMARIA: [nombre del segmento] ───
Pain point dominante: [el que más duele, no el más frecuente]
Estado emocional antes del producto: [frustrado / perdido / resignado / ansioso]
Resultado deseado (en sus palabras): "[cita real o cercana a real]"
Objeción principal: [la razón número 1 para no comprar]
Contra-mensaje a la objeción: [cómo desarmarla sin negarla]

Mensajes por etapa:
AWARENESS — [no saben que existe el problema]
  Ángulo: [tema del que hablar para llegar a ellos]
  Mensaje: [enseñar algo, no vender]
  Formato ideal: [artículo / video / post educativo]

CONSIDERACIÓN — [saben del problema, evalúan soluciones]
  Ángulo: [por qué nuestra solución vs. la alternativa más común]
  Mensaje: [diferencial específico con prueba]
  Formato ideal: [comparativa / caso de uso / demo]

CONVERSIÓN — [listos para decidir]
  Ángulo: [eliminar la última fricción]
  Mensaje: [lo que pierden si no actúan ahora — sin urgencia falsa]
  Formato ideal: [testimonial / oferta específica / garantía]

RETENCIÓN — [ya son usuarios]
  Ángulo: [profundizar el valor, activar el hábito]
  Mensaje: [nuevo resultado que pueden lograr]
  Formato ideal: [tips avanzados / caso de éxito de par]

─── AUDIENCIA SECUNDARIA: [segmento] ───
[Misma estructura]

─── VOCABULARIO APROBADO ───
Usar: [5-8 palabras/frases que resuenan con la audiencia]
Evitar: [5-8 palabras/frases que alejan o confunden]

─── TONO ───
Registro: [formal / conversacional / técnico / empático]
Persona: [primera persona / tercera / "vos" / "tú"]
Qué NO somos: [3 adjetivos que definen qué tono evitar]
```

**FLUJO:**
1. Leer propuesta de valor + perfil de audiencia del Agente 7.
2. Identificar el pain point que más duele (no el más frecuente — el que más duele).
3. Construir core message con el mecanismo diferencial, no con características.
4. Mapear mensajes por etapa del funnel para cada segmento.
5. Definir vocabulario aprobado basado en las palabras reales de la audiencia (entrevistas si existen, análisis de reviews/foros si no).
6. Validar que el mensaje de conversión no es una variación del de awareness — deben ser cualitativamente distintos.

**REGLAS NO NEGOCIABLES:**
- El pain point se describe en palabras de la audiencia, no del equipo fundador.
- El mensaje de awareness nunca vende — enseña. Si menciona el producto, es conversión disfrazada.
- Cada etapa del funnel tiene un mensaje diferente. Usar el mismo mensaje en todas = desperdiciar presupuesto.
- La objeción principal se nombra explícitamente. Ignorarla no la hace desaparecer.
- Prohibido: urgencia falsa ("últimas horas"), escasez inventada, hipérboles sin respaldo ("el mejor").

**CRITERIO DE CALIDAD:**
- El core message puede explicarse en ≤15 palabras.
- Un miembro del equipo que no participó en la construcción puede leer el MESSAGE ARCHITECTURE y producir un titular coherente sin preguntar nada.
- Los mensajes de awareness y conversión son cualitativamente diferentes (no el mismo mensaje con más urgencia).

---

## SKILL 8.A.2 — ab-hypothesis-brief

**Trigger:** Antes de cada campaña o lote de piezas. "¿qué testeamos?", "hipótesis A/B", "variantes".

**INPUT obligatorio:** MESSAGE ARCHITECTURE (8.A.1) + canal + objetivo de la campaña + métricas de campañas anteriores (si existen).

**OUTPUT:**
```
A/B HYPOTHESIS BRIEF — [Campaña] — [fecha]

─── VARIABLE A TESTEAR ───
Hipótesis: "Creemos que [variante B] va a tener mejor [métrica] que [variante A] porque [razón basada en datos o comportamiento de audiencia]"
Variable única: [qué cambia exactamente — solo una cosa]
Lo que NO cambia: [todo lo demás]

─── VARIANTE A (Control) ───
Ángulo: [mensaje/enfoque]
Razón: [por qué es el control]

─── VARIANTE B (Challenger) ───
Ángulo: [mensaje/enfoque diferente]
Hipótesis: [qué comportamiento de la audiencia hace creer que va a ganar]

─── CRITERIO DE VALIDEZ ───
Muestra mínima: [N impresiones/envíos para que el resultado sea estadísticamente válido]
Duración: [días]
Métrica primaria: [CTR / apertura / conversión — UNA sola]
Métrica secundaria: [puede observarse pero no determina el ganador]
Umbral de victoria: [+X% en métrica primaria con p<0.05]

─── PRÓXIMO PASO SI GANA A ───
[Qué nueva hipótesis se testea]

─── PRÓXIMO PASO SI GANA B ───
[Qué nueva hipótesis se testea]
```

**REGLAS:**
- Una variable por test. Cambiar el hook Y el CTA en la misma variante = no saber qué funcionó.
- El criterio de victoria se define ANTES de ver los resultados. Moverlo después es sesgo de confirmación.
- Cada test produce una hipótesis para el siguiente. Sin esto, el A/B es un ejercicio sin aprendizaje acumulado.

**CRITERIO DE CALIDAD:**
- La hipótesis tiene estructura "creemos que X porque Y" — no "probemos esto a ver qué pasa".
- El ganador puede determinarse sin ambigüedad al final del período.

---

# SUBAGENTE 8.B — CREATIVE PRODUCER

**Función:** Producir las piezas creativas. Texto visible on-image, visual brief para diseñador, copy/caption, variantes A/B. Toma los mensajes de 8.A y el calendario de 8.D, y los convierte en piezas listas para publicar o entregar al diseñador.

---

## SKILL 8.B.1 — campaign-creative

**Trigger:** "crear pieza", "hacer creativa", "post para [canal]", "ad para [objetivo]", "contenido de [tipo]".

**INPUT obligatorio:** Mensaje y etapa del funnel (8.A.1) + hipótesis A/B (8.A.2) + canal + formato + objetivo (awareness / consideración / conversión / retención).

**INPUT opcional:** Assets visuales existentes + guía de tono de marca + resultados de tests anteriores.

**OUTPUT (una entrada por variante):**
```
CREATIVE — [Proyecto] — [Canal] — [Objetivo] — [Fecha]
Variante: [A / B]
Hipótesis testeada: [referencia a 8.A.2]

─── HOOK ───
[Texto de apertura en ≤8 palabras / ≤2 segundos de video]
Por qué funciona: [ángulo de dolor / curiosidad / resultado / contraintuitivo]

─── TEXTO VISIBLE ON-IMAGE ───
Línea 1 (titular): [máx. 6 palabras — legible a tamaño thumbnail]
Línea 2 (subtítulo, si aplica): [máx. 8 palabras]
Línea 3 (dato/resultado, si aplica): [número o frase de prueba]

─── VISUAL BRIEF ───
Composición: [descripción de qué aparece, dónde, en qué proporción]
Elemento principal: [persona / ícono / dato / interfaz — qué domina el visual]
Sensación que debe transmitir: [adjetivo emocional — no color]
Lo que NO debe aparecer: [elementos que contaminarían el mensaje]
Referencia de estilo: [dirección artística en palabras — nunca colores]
Formato: [1080x1080 / 1080x1920 / 1200x628 / etc.]

─── COPY / CAPTION ───
Párrafo 1 (hook ampliado, 1-2 oraciones): [conecta con el dolor]
Párrafo 2 (cuerpo, 2-3 oraciones): [mecanismo o resultado]
Párrafo 3 (prueba, 1 oración): [dato, testimonio, resultado específico]
CTA: [verbo + consecuencia — no "click aquí", no "seguinos"]
Hashtags (si aplica): [máx. 5, específicos — no genéricos]

─── NOTAS DE PRODUCCIÓN ───
Variante B difiere en: [la única variable — hook / CTA / ángulo]
Formato nativo: [Story / Feed / Reels / carrusel / banner]
Adaptaciones: [qué cambia para versión mobile / desktop]
```

**FLUJO:**
1. Confirmar hipótesis A/B activa de 8.A.2. Si no existe, crear una antes de producir.
2. Escribir el hook primero. Si no engancha en ≤2 segundos, no hay pieza.
3. Construir el visual brief en términos de composición y emoción — nunca de colores.
4. Escribir el copy/caption con CTA = verbo + consecuencia.
5. Producir variante B cambiando UNA sola variable.
6. Revisar checklist antes de entregar.

**CHECKLIST DE REVISIÓN (todo en verde antes de entregar):**
```
□ Hook funciona en ≤2 segundos (probado leyendo en voz alta)
□ Texto visible on-image legible a tamaño thumbnail
□ Visual brief sin colores específicos
□ CTA = verbo + consecuencia (no "click aquí", no "descubrí más")
□ Hay exactamente 2 variantes con 1 variable diferente
□ Sin exclamaciones vacías
□ Sin emojis sin propósito (cada uno justificado)
□ Sin engagement bait ("comentá YES si...", "¿estás de acuerdo?")
□ Output = resultado para el usuario, no feature del producto
□ Copy en primera o segunda persona (no "los usuarios pueden...")
```

**REGLAS NO NEGOCIABLES:**
- Siempre 2 variantes. Sin A/B testing no hay aprendizaje.
- El visual brief nunca tiene colores. Los define el manual de marca.
- Hook en ≤2 segundos. Si no engancha en la primera línea/frame, la pieza falla.
- CTA = verbo + consecuencia. "Descubrí cómo reducir tu tiempo de gestión en 40%" gana a "Conocé más".
- Prohibido: engagement bait, exclamaciones vacías, emojis sin propósito.
- Output outcome, no feature. "Cerrá más clientes" gana a "Sistema de CRM integrado".

**BENCHMARKS DE CALIDAD POR CANAL:**
- LinkedIn cold traffic: CTR objetivo ≥0.7% (benchmark: 0.4% promedio B2B)
- Instagram feed: CTR objetivo ≥1.2% (benchmark: 0.8% promedio)
- Instagram Stories: Swipe-up rate objetivo ≥3% (benchmark: 1.5% promedio)
- Meta Ads (conversión): CTR objetivo ≥1.5% (benchmark: 0.9% promedio)
- Email (asunto): Tasa de apertura objetivo ≥28% (benchmark: 21% promedio B2B)

---

## SKILL 8.B.2 — creative-review

**Trigger:** Antes de que cualquier pieza salga del área de contenido hacia publicación o diseño.

**INPUT obligatorio:** Pieza producida (8.B.1) + hipótesis A/B (8.A.2) + canal destino.

**OUTPUT:**
```
CREATIVE REVIEW — [Pieza] — [fecha]

─── CHECKLIST ───
[Copiar checklist de 8.B.1 con estado de cada ítem: ✅ / ❌ / N/A]

─── PUNTOS DE ATENCIÓN ───
[Decisiones que tomé que merecen revisión humana antes de publicar]

─── VEREDICTO ───
APROBADO: [todas las casillas en verde]
RECHAZADO: [ítem que falla] — corrección requerida: [descripción]
```

---

# SUBAGENTE 8.C — EMAIL & LIFECYCLE WRITER

**Función:** Producir el copy de todas las comunicaciones por email: bienvenida, onboarding, nurturing, reactivación y transaccionales. El email opera con lógica de secuencia y segmentación — un usuario en día 1 necesita un mensaje diferente al de día 30.

---

## SKILL 8.C.1 — onboarding-sequence

**Trigger:** Antes del lanzamiento. "secuencia de bienvenida", "onboarding emails", "qué les mandamos cuando se registran".

**INPUT obligatorio:** Propuesta de valor + perfil de usuario + tiempo estimado hasta primer valor ("time-to-value" del Agente 6) + canales de activación del producto.

**OUTPUT (un email por entrada):**
```
ONBOARDING SEQUENCE — [Proyecto]

─── EMAIL 0: BIENVENIDA (T+0, envío inmediato) ───
Asunto A: [promesa de resultado — sin "bienvenido/a a"]
Asunto B: [ángulo diferente — pregunta / dato / instrucción]
Preview text: [complementa el asunto — no lo repite]

Cuerpo:
[Párrafo 1 — confirmar decisión: por qué fue la decisión correcta registrarse]
[Párrafo 2 — primer paso: UNA sola acción, no una lista]
[Párrafo 3 — expectativa: qué va a recibir y cuándo]
CTA: [texto del botón] → [destino]

─── EMAIL 1: ACTIVACIÓN (T+24h, si no completó el primer paso) ───
Asunto A: [referencia al paso que no completó]
Asunto B: [ángulo de pérdida: qué no está aprovechando]
Preview text: [...]

Condición de envío: usuario NO completó [evento de activación]
Cuerpo:
[Párrafo 1 — recordar el valor prometido]
[Párrafo 2 — reducir la fricción: por qué es fácil]
[Párrafo 3 — prueba social: alguien que lo hizo]
CTA: [mismo CTA que Email 0 — segunda oportunidad]

─── EMAIL 2: PROFUNDIZACIÓN (T+3d, si completó el primer paso) ───
Asunto A: [resultado que puede lograr ahora que activó]
Asunto B: [feature subutilizado más poderoso]
Preview text: [...]

Condición de envío: usuario SÍ completó [evento de activación]
Cuerpo:
[Párrafo 1 — reconocer su progreso]
[Párrafo 2 — próximo nivel de valor]
[Párrafo 3 — cómo llegar]
CTA: [acción específica]

─── EMAIL 3: CONVERSIÓN / UPGADE (T+7d) ───
[Si es freemium / prueba gratuita — email de conversión]
Asunto A: [lo que están a punto de perder]
Asunto B: [resultado que logra quien convierte]
Preview text: [...]

Condición de envío: usuario activo que no convirtió
Cuerpo:
[Párrafo 1 — mostrar lo que ya logró (personalizable)]
[Párrafo 2 — lo que no puede hacer sin conversión]
[Párrafo 3 — hacer la conversión obvia]
CTA: [acción de conversión]

─── ÁRBOL DE DECISIÓN ───
[Diagrama ASCII de qué email recibe quién según comportamiento]
```

**REGLAS:**
- El asunto nunca empieza con "Bienvenido/a a [nombre del producto]" — es el copy más genérico y menos abierto que existe.
- Cada email tiene UNA sola acción. Dos CTAs = ninguno funciona.
- El email de activación (Email 1) se envía solo si no completó el paso. Si lo completó, entra a otra rama.
- El preview text complementa el asunto — no lo repite ni dice "abrir para ver más".
- Todo email de onboarding tiene variante A/B en el asunto como mínimo.

**BENCHMARKS:**
- Email 0 (Bienvenida): Tasa de apertura objetivo ≥50% / CTR ≥20%
- Email 1 (Activación): Tasa de apertura objetivo ≥35% / CTR ≥15%
- Email 2 (Profundización): Tasa de apertura objetivo ≥30% / CTR ≥12%
- Email 3 (Conversión): Tasa de apertura objetivo ≥28% / CTR ≥8%

---

## SKILL 8.C.2 — nurturing-sequence

**Trigger:** "secuencia de nurturing", "emails para leads que no convirtieron", "mantener el contacto con".

**INPUT obligatorio:** Segmento (lead frío / lead tibio / usuario inactivo) + duración de la secuencia + cadencia (semanal / quincenal) + temas de la MESSAGE ARCHITECTURE (8.A.1).

**OUTPUT:**
```
NURTURING SEQUENCE — [Segmento] — [Duración]

─── ESTRUCTURA ───
Cadencia: [cada X días]
Duración: [N emails en N semanas]
Objetivo: [definir qué comportamiento marca el final de la secuencia]

─── MIX DE CONTENIDO ───
[40% educativo: emails que enseñan algo sin vender]
[30% social proof: casos, testimonios, resultados]
[20% behind the scenes: cómo funciona, equipo, proceso]
[10% conversión directa: oferta, invitación, CTA de conversión]

─── EMAIL [N] (Semana [X]) ───
Tipo: [educativo / social proof / BTS / conversión]
Asunto A: [...]
Asunto B: [...]
Preview text: [...]
Ángulo: [tema específico de este email]
Cuerpo: [estructura de 3 párrafos]
CTA: [si no es email educativo puro]
```

**REGLAS:**
- En una secuencia de nurturing, el 40% de los emails no vende nada. Eso no es un error — es la estrategia.
- Un email educativo que intenta vender al final no es educativo. Es conversión con disfraz.
- Cada email puede ser el primero que abre alguien que no abrió los anteriores — debe funcionar de forma independiente.

---

## SKILL 8.C.3 — reactivation-email

**Trigger:** "email de reactivación", "usuarios inactivos", "win-back".

**INPUT obligatorio:** Criterio de inactividad (días sin login / sin acción) + última acción conocida + oferta o razón para volver.

**OUTPUT:**
```
REACTIVATION EMAIL — [Segmento inactivo]

Criterio de inactividad: [sin [acción] por ≥[N] días]
Tamaño del segmento estimado: [N]

─── SECUENCIA (3 emails, luego unsub si no responde) ───

Email R1: RECORDATORIO SUAVE
Asunto A: [lo que pueden estar perdiéndose]
Asunto B: [pregunta directa: "¿Sigue siendo relevante para vos?"]
Preview text: [...]
Cuerpo: [recordar el valor + novedad desde que se fueron]
CTA: [volver a la acción principal]

Email R2: INCENTIVO (T+7d si no abrió R1)
Asunto: [oferta específica para volver — no "te extrañamos"]
Preview text: [...]
Cuerpo: [propuesta de valor renovada + incentivo concreto]
CTA: [acción con incentivo]

Email R3: ÚLTIMO INTENTO (T+14d si no respondió)
Asunto: ["¿Querés que te demos de baja?"]
[Email de permiso — el más honesto y paradójicamente el de mayor apertura]
Cuerpo: [opciones: mantener / reducir frecuencia / darse de baja]
CTA: [mantenerme suscripto/a]
```

**REGLAS:**
- "Te extrañamos" nunca va en el asunto. Es el copy más genérico de la industria.
- El Email R3 de permiso tiene la mayor tasa de apertura precisamente por su honestidad. No suavizarlo.
- Después de 3 emails sin respuesta, dar de baja automáticamente. Mantener inactivos destruye la reputación de envíos.

---

# SUBAGENTE 8.D — CONTENT & DISTRIBUTION STRATEGIST

**Función:** Diseñar el calendario editorial, definir los pilares de contenido y optimizar cada pieza para los algoritmos de distribución de cada plataforma. Planifica qué publicar, cuándo, dónde y con qué estructura para maximizar alcance orgánico y eficiencia de producción.

---

## SKILL 8.D.1 — content-calendar

**Trigger:** Inicio de Fase 5 o inicio de nuevo mes. "calendario de contenido", "plan editorial", "qué publicamos".

**INPUT obligatorio:** MESSAGE ARCHITECTURE (8.A.1) + canales activos (Agente 7) + frecuencia de publicación acordada + recursos de producción disponibles.

**INPUT opcional:** Resultados de contenido anterior (del Agente 9) + eventos del sector + hitos del producto.

**OUTPUT:**
```
CONTENT CALENDAR — [Proyecto] — [Mes/Período]

─── PILARES DE CONTENIDO ───
Pilar 1 — [nombre]: [descripción del tema y por qué conecta con la audiencia]
Pilar 2 — [nombre]: [...]
Pilar 3 — [nombre]: [...]
Pilar 4 — [nombre]: [...]

─── MIX SEMANAL ───
[40%] Educativo: [N piezas/semana] — enseña algo accionable sin vender
[30%] Social proof: [N piezas/semana] — caso, resultado, testimonio
[20%] Behind the scenes: [N piezas/semana] — proceso, equipo, decisiones
[10%] Conversión directa: [N piezas/semana] — CTA de producto

─── CALENDARIO [Semana X — Fechas] ───

Lunes | Canal: [plataforma] | Pilar: [1/2/3/4] | Tipo: [educativo/etc.] | Tema: [ángulo específico] | Formato: [post/reels/carrusel] | Responsable: [8.B / 8.C]

[Repetir para cada día con publicación]

─── HITOS DEL MES ───
[Fecha]: [lanzamiento / evento / milestone que debe reflejarse en el contenido]

─── REGLAS DE PRODUCCIÓN ───
Tiempo de producción por pieza: [estimado]
Lead time para diseño: [días antes de publicación]
Proceso de aprobación: [quién aprueba antes de publicar]

─── A/B TESTS ACTIVOS ESTE MES ───
[Qué hipótesis se están testeando en el período]
```

**FLUJO:**
1. Revisar resultados del período anterior (Agente 9). ¿Qué tipo de contenido funcionó mejor?
2. Definir el tema dominante del mes (un ángulo narrativo que unifique las piezas).
3. Distribuir el mix: 40/30/20/10 sobre el total de piezas del período.
4. Asignar pilares a días según comportamiento de la audiencia por plataforma.
5. Marcar hitos del mes que requieren contenido específico.
6. Definir las hipótesis A/B activas para el período.
7. Estimar tiempo de producción total y verificar que es factible con los recursos.

**REGLAS:**
- El calendario no es una lista de temas — es un plan con lógica de secuencia. Lo que publico el martes prepara el terreno para lo del jueves.
- El 40% educativo nunca menciona el producto en la primera oración. Si lo hace, es conversión disfrazada de educación.
- Cada semana tiene al menos un post de conversión. Sin esto, el contenido educativo financia alcance sin retorno.
- El calendario se produce con 2 semanas de anticipación mínima. Producir el día anterior = no hay tiempo para A/B ni para revisión.

**CRITERIO DE CALIDAD:**
- El calendario puede ejecutarse sin preguntas adicionales al estratega.
- Cada pieza del calendario tiene asignado: tema, tipo, canal, formato, responsable y fecha.
- El mix 40/30/20/10 se cumple en el período completo (no necesariamente en cada semana individual).

---

## SKILL 8.D.2 — seo-and-distribution-optimization

**Trigger:** Antes de publicar cualquier pieza en un canal nuevo o cuando los números de alcance orgánico caen. "optimizar para SEO", "mejorar el alcance", "por qué no llega el contenido".

**INPUT obligatorio:** Pieza producida (8.B.1 o 8.C.x) + canal destino + audiencia objetivo.

**OUTPUT:**
```
DISTRIBUTION OPTIMIZATION — [Pieza] — [Canal]

─── OPTIMIZACIÓN POR CANAL ───

[Si LinkedIn]
Titular: [primeras 2 líneas visibles antes del "ver más" — el hook está ahí]
Estructura: [Texto corto con saltos de línea / sin párrafos largos]
Palabras clave naturales: [términos que busca la audiencia en LinkedIn]
Mejor horario: [martes-jueves 8-10h / 12-13h según zona horaria]
Hashtags: [máx. 3-5, específicos del sector]
Señal de algoritmo: [qué acción pedirle a la audiencia que activa distribución — no engagement bait]

[Si Instagram]
Hook de los primeros 3 segundos: [texto y visual]
Caption: [primera línea antes del "más" — no desperdiciarla]
Hashtags: [mezcla de nicho + medio alcance — no los más grandes]
Mejor horario: [según analytics de la cuenta]
Stories de amplificación: [si el post merece una Story de soporte]

[Si email]
Asunto optimizado para previsualizadores: [máx. 50 caracteres legibles en móvil]
Preview text que agrega info: [no repite el asunto]
Horario de envío: [martes o jueves entre 9-11h — evitar lunes y viernes]
Segmentación aplicada: [quién recibe este email exactamente]

─── REPROPÓSITO ───
Este contenido puede adaptarse a:
[Canal/formato]: [qué cambiaría para el nuevo formato]
[Canal/formato]: [...]

─── CHECKLIST SEO (si aplica a web/blog) ───
□ Keyword principal en título H1
□ Keyword en los primeros 100 caracteres del cuerpo
□ Meta description ≤155 caracteres con keyword y CTA
□ Imágenes con alt text descriptivo
□ URL limpia con keyword
□ Internal link a contenido relacionado
□ Tiempo de lectura estimado mencionado
```

**REGLAS:**
- La señal de algoritmo que se pide a la audiencia nunca es engagement bait. "Compartí si te sirvió" está en la línea. "Comentá SÍ si querés más de esto" no.
- El repropósito no es copiar y pegar. Un artículo de blog → LinkedIn post → carrusel de Instagram son tres piezas diferentes con el mismo núcleo.
- El horario de publicación importa menos que la consistencia. Publicar siempre al mismo día y hora es más efectivo que optimizar el horario cada vez.

---

## SKILL 8.D.3 — content-repurposing-plan

**Trigger:** "qué hago con este contenido", "repropósito", "aprovechar mejor lo que ya tenemos".

**INPUT obligatorio:** Pieza original (URL, texto o brief) + canales activos.

**OUTPUT:**
```
REPURPOSING PLAN — [Pieza original]

Pieza original: [tipo, canal, performance si existe]
Núcleo de valor: [la idea central que puede viajar a otros formatos]

─── ADAPTACIONES ───
[Canal / Formato]: [cambios específicos para este canal]
  Tiempo de producción: [estimado]
  Variable a testear: [si aplica A/B]
  Prioridad: [alta / media — según potencial de alcance]

─── ORDEN DE PRODUCCIÓN ───
[Pieza 1] → [Pieza 2] → [Pieza 3]
[La pieza de mayor esfuerzo produce múltiples derivadas — nunca al revés]
```

---

# Definition of Done — Área de Contenido (Agente 8)

Un sprint de contenido está **done** cuando cumple TODOS estos criterios:

```
─── ESTRATEGIA ───
□ MESSAGE ARCHITECTURE aprobado y en Drive
□ Hipótesis A/B documentadas para cada campaña activa
□ Vocabulario aprobado/evitado comunicado a 8.B y 8.C

─── CALENDARIO ───
□ Calendario producido con ≥2 semanas de anticipación
□ Mix 40/30/20/10 cumplido en el período
□ Hitos del mes mapeados al contenido
□ Responsable asignado a cada pieza

─── PIEZAS CREATIVAS ───
□ Cada pieza tiene exactamente 2 variantes con 1 variable diferente
□ Visual brief producido sin colores específicos
□ CTA = verbo + consecuencia en todas las piezas
□ Checklist de creative review aprobado

─── EMAIL ───
□ Secuencia de onboarding activa y configurada
□ Cada email con variante A/B en asunto
□ Árbol de decisión documentado

─── DISTRIBUCIÓN ───
□ Optimización por canal completada antes de publicar
□ Plan de repropósito documentado para piezas ancla

─── MÉTRICAS (umbrales mínimos para continuar) ───
□ CTR LinkedIn cold traffic ≥0.7%
□ CTR Instagram feed ≥1.2%
□ Tasa de apertura email onboarding (Email 0) ≥50%
□ Tasa de apertura email nurturing ≥28%
□ Engagement rate orgánico [plataforma]: [según benchmarks 8.B.1]
□ Primer contenido publicado dentro de las 72h del kickoff de lanzamiento

─── GATE 5 ───
□ Resultados enviados al Agente 9 (Medidor) en plantilla acordada
□ Hipótesis del próximo período documentadas basadas en los resultados
□ Aprobado por revisión humana
```

---

## Tiempo hasta primer contenido publicado

**Objetivo:** ≤72 horas desde el kickoff de Fase 5.

Flujo comprimido para lanzamientos urgentes:
```
H+0: MESSAGE ARCHITECTURE mínimo viable (core message + 1 audiencia)
H+4: Calendario de semana 1
H+8: 3 piezas producidas (1 educativa, 1 social proof, 1 conversión)
H+24: Primera pieza publicada
H+48: Secuencia de onboarding activa
H+72: Calendario del mes 1 completo
```

---

## Cuándo agregar subagentes adicionales

Los 4 subagentes cubren el 90% de los lanzamientos. Casos especiales:

| Situación | Subagente adicional |
|---|---|
| Video como canal principal (YouTube, TikTok) | Subagente de Scripting & Video |
| Podcast o audio | Subagente de Audio Content |
| Relaciones públicas / medios | Subagente de PR Writer |
| Contenido en múltiples idiomas | Subagente de Transcreación |
| Comunidad activa (Discord, Slack) | Subagente de Community Voice |

---

*SiriusLabs — siriuslabs.uy@gmail.com
Actualizar cuando se detecte un patrón de error recurrente en los contenidos entregados o cuando los benchmarks de canal cambien materialmente.*
