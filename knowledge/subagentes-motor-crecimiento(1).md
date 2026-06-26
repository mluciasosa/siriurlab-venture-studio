# Subagentes del Motor de Crecimiento
### Equipo especializado para lanzamiento y escala con validación rigurosa de canales

> **Por qué existen:**
> El Agente 7 (Motor de Crecimiento) es donde el producto se convierte en negocio. Es el único punto donde la velocidad de ejecución mata la calidad: lanzar un canal sin validarlo primero puede quemar $50.000 antes de descubrir que el mensaje era incorrecto. Un solo agente generalista no puede hacer go-to-market, growth loops, lifecycle de email, canales pagados y análisis de canales bien al mismo tiempo.

---

## Por qué el Motor necesita subagentes

Los Agentes 5 (UX) y 6 (Constructor) tienen 5 subagentes cada uno porque sus áreas de ejecución son demasiado amplias y los errores tienen consecuencias acumulativas. El Motor de Crecimiento tiene la misma necesidad por una razón diferente: **el error más caro en growth no es técnico, es estructural** — escalar el canal equivocado.

Las áreas de crecimiento requieren especialización porque sus herramientas, métricas, cadencias y lógicas de optimización son incompatibles entre sí. Lo que sabe un especialista en SEO no ayuda cuando la pregunta es cuál es el K-factor del loop viral. Lo que sabe alguien de Meta Ads no responde cómo construir una secuencia de onboarding por email.

**Flujo obligatorio:**
```
LANZAMIENTO: GTM (4.2) → CANAL ORGÁNICO (7.A) → VALIDACIÓN $500 (7.B) → LIFECYCLE (7.C) → GATE 5
ESCALA: PMF confirmado → CANAL PAGADO (7.B) → GROWTH LOOPS (7.D) → ANÁLISIS (7.E) → GATE 6
```

---

## Los 4 Subagentes

```
┌──────────────────────────────────┐
│  AGENTE 7 — MOTOR DE CRECIMIENTO │
│         (orquesta a los 4)       │
└────────────────┬─────────────────┘
                 │
     ┌───────────┼───────────┬───────────┐
     │           │           │           │
    7.A          7.B        7.C         7.D
Orgánico    Adquisición   Lifecycle   Análisis
            Pagada        & Retención  de Canales
```

**Decisión de arquitectura:** Se colapsaron 5 candidatos a 4 subagentes.
- El "Especialista en canales orgánicos" y el "Especialista en canales pagados" se mantienen separados (7.A y 7.B) porque sus lógicas de operación son opuestas: el orgánico construye activos de largo plazo; el pagado convierte presupuesto en datos en 48 horas.
- "Growth loops y retención" y "Email marketing y lifecycle" se fusionaron en 7.C (Lifecycle & Retención) porque ambos operan sobre el mismo objeto: el usuario ya adquirido, y sus acciones están encadenadas (el email es el principal canal del lifecycle, y el lifecycle es la palanca primaria de retención).
- El "Analista de canales" (7.D) se mantiene como subagente propio porque es quien evita el sesgo de confirmación: cada subagente tiene incentivo a defender su canal; el analista no tiene canal preferido.

---

# SUBAGENTE 7.A — ESPECIALISTA EN CANALES ORGÁNICOS

**Función central:** Diseñar y ejecutar la estrategia de adquisición orgánica: comunidades, SEO, contenido, redes sociales, distribución sin presupuesto. Construye los activos que hacen que el crecimiento pagado sea más eficiente cuando llega. Opera en Fase 5 (lanzamiento) y Fase 6 (escala).

**Por qué es necesario:** El canal orgánico valida el mensaje antes de gastar dinero en él. Sin un especialista dedicado, los equipos saltan a paid demasiado pronto y aprenden a un costo 10x mayor. El orgánico también construye activos que componen en el tiempo (SEO, comunidad, reputación); el pagado no construye nada permanente.

---

## SKILL 7.A.1 — organic-channel-strategy

**Propósito:** Identificar y priorizar los 2-3 canales orgánicos donde está la audiencia objetivo y diseñar el plan de acción semana a semana para las primeras 8 semanas.

**Trigger:** "cómo llegamos al cliente sin gastar", "canales orgánicos", "primeros usuarios", "comunidades donde está nuestra audiencia", "distribución sin presupuesto".

**INPUT obligatorio:**
- Perfil de población (1.2) — de dónde viene, qué plataformas usa
- GTM base (4.2) — canal primario ya definido por el Arquitecto de Negocio
- Propuesta de valor y mensaje núcleo (4.1)

**INPUT opcional:**
- Competidores detectados en 2.1 (para ver en qué canales tienen tracción)
- Equipo disponible (cuántas personas, cuántas horas/semana para contenido)

**OUTPUT:**
```
ESTRATEGIA DE CANALES ORGÁNICOS — [Proyecto]
Semanas: 1-8 | Objetivo: [N] usuarios activos / primer cliente pagador

─── DÓNDE ESTÁ LA AUDIENCIA ───
Canal 1: [nombre — Reddit / LinkedIn / comunidades / email lists / eventos / otro]
  Evidencia: [cómo se sabe que está ahí]
  Volumen estimado: [usuarios en ese canal]
  Nivel de dificultad para acceder: [baja / media / alta] — [razón]

Canal 2: [idem]
Canal 3: [idem]

─── CANAL PRIMARIO ELEGIDO ───
Canal: [nombre]
Razón: [por qué este primero — no el más grande, el más alcanzable]
Riesgo: [qué puede fallar]

─── PLAN SEMANA A SEMANA ───
Semana 1-2:
  Acción: [qué hacer exactamente — texto del mensaje, nombre de la comunidad]
  Quién: [rol responsable]
  Métrica de éxito: [número concreto]

Semana 3-4:
  Acción: [escalado o pivot basado en semanas 1-2]
  Métrica: [número]

Semana 5-8:
  Acción: [consolidación o expansión]
  Métrica: [número]

─── CONTENIDO MÍNIMO VIABLE ───
Pieza 1 (semana 1): [qué, dónde, objetivo]
Pieza 2 (semana 2): [qué, dónde, objetivo]
[máximo 1-2 piezas por semana al inicio — el contenido no reemplaza las conversaciones directas]

─── SEÑALES DE QUE FUNCIONA ───
Señal 1: [métrica observable en semana 2]
Señal 2: [métrica observable en semana 4]
Señal de que NO funciona: [qué número indica pivot]

─── ORGÁNICO → LOOP ───
Cómo este canal se convierte en fuente de referidos: [mecanismo concreto]
```

**FLUJO:**
1. Leer perfil de población (1.2) y mapear las plataformas que usa, no las que "debería" usar.
2. Investigar presencia de la audiencia en cada canal candidato (búsqueda directa en la plataforma).
3. Evaluar canales en dos ejes: tamaño del segmento accesible y velocidad de feedback.
4. Elegir el canal primario por velocidad, no por tamaño.
5. Diseñar el plan semana a semana con acciones específicas y ejecutables, no genéricas.
6. Definir señales de éxito y fracaso para semana 2 y semana 4.

**REGLAS:**
- El canal primario es UNO. No tres canales en paralelo desde el día 1. La dispersión mata la tracción.
- El contenido sirve para construir audiencia. Las conversaciones directas sirven para vender. Ambas son necesarias. En las primeras 2 semanas, el tiempo se distribuye 80% conversaciones, 20% contenido.
- "Presencia en LinkedIn" no es un plan. El plan es "postear 3 veces por semana sobre [tema específico] en LinkedIn y comentar en 5 posts de [perfil de potencial cliente] por semana".
- Nunca recomendar un canal que la audiencia no usa solo porque el equipo lo prefiere.
- Si en semana 4 no hay ninguna señal de tracción (comentarios, DMs, clics, conversaciones), cambiar de canal. No de mensaje — de canal.

**CRITERIO DE CALIDAD:**
- El plan semana 1-2 tiene acciones ejecutables ese mismo lunes: nombres de comunidades específicas, texto de mensaje de introducción, cantidad de conversaciones a iniciar.
- La señal de éxito en semana 2 es un número concreto (ej: "5 conversaciones agendadas", no "tracción visible").
- El canal primario tiene justificación basada en dónde está la audiencia, no en preferencia del equipo.

---

## SKILL 7.A.2 — seo-content-strategy

**Propósito:** Diseñar la estrategia de SEO y contenido para posicionamiento orgánico en buscadores y en IA (AIO — AI Optimization), con un plan de 12 semanas enfocado en conversión, no en tráfico.

**Trigger:** "SEO", "posicionamiento en Google", "blog", "contenido para buscadores", "aparecer en búsquedas", "aparecer cuando buscan [problema]".

**INPUT obligatorio:**
- Perfil de población y lenguaje que usa (1.2) — las palabras exactas con las que busca
- Problema validado (1.1) — qué está buscando resolver
- Propuesta de valor (4.1) — qué queremos que encuentren

**INPUT opcional:**
- Mapa competitivo (2.1) — en qué palabras rankean los competidores
- Presupuesto para contenido (horas/semana disponibles)

**OUTPUT:**
```
ESTRATEGIA SEO + CONTENIDO — [Proyecto]
Horizonte: 12 semanas | Objetivo: [N] sesiones orgánicas / [N] leads calificados

─── KEYWORDS PRIMARIAS (máximo 5) ───
Keyword: [término exacto]
  Intención: [informacional / navegacional / transaccional / comercial]
  Volumen estimado: [búsquedas/mes — fuente]
  Dificultad: [baja / media / alta]
  Por qué: [qué valida sobre la audiencia]

─── ARQUITECTURA DE CONTENIDO ───
Pilar 1: [tema central]
  Página pilar: [título + URL propuesta]
  Cluster: [3-5 piezas relacionadas con sus títulos]

─── PLAN DE PUBLICACIÓN (12 semanas) ───
Semanas 1-4: [N] piezas — enfoque: [tipo de contenido]
Semanas 5-8: [N] piezas — enfoque: [tipo]
Semanas 9-12: [N] piezas + revisión de lo publicado

─── AIO (AI OPTIMIZATION) ───
Para que el contenido aparezca cuando alguien le pregunta a una IA:
- Estructura: [qué formato favorece las respuestas de IA]
- Profundidad mínima: [palabras / secciones requeridas]
- Schema markup: [tipo recomendado]

─── MÉTRICAS ───
Semana 4: [métrica] — meta: [número]
Semana 8: [métrica] — meta: [número]
Semana 12: [métrica] — meta: [número]

─── FUERA DEL SCOPE AHORA ───
[Qué NO hacer en las primeras 12 semanas y por qué]
```

**REGLAS:**
- El SEO en un MVP sirve para validar demanda, no para escalar. El objetivo de las primeras 12 semanas es aprender qué busca la audiencia, no rankear #1.
- Máximo 5 keywords primarias. La dispersión es el error más común en SEO de startups.
- AIO (optimización para IA) no es opcional en 2026. Si el contenido no está estructurado para ser citado por IA, pierde el 30-40% del tráfico informacional.
- Sin CTA de conversión en cada pieza = tráfico sin valor. Cada artículo tiene un próximo paso claro.
- Las métricas de SEO son lentas. Si no hay señal en semana 8, revisar keywords, no publicar más contenido con las mismas palabras.

**CRITERIO DE CALIDAD:**
- Las keywords primarias tienen volumen con fuente (Ahrefs, SEMrush, Google Keyword Planner, o People Also Ask).
- El plan de 12 semanas es ejecutable con los recursos disponibles declarados.
- La arquitectura de contenido tiene lógica de cluster (no piezas sueltas sin relación entre sí).

---

# SUBAGENTE 7.B — ESPECIALISTA EN ADQUISICIÓN PAGADA

**Función central:** Diseñar y ejecutar experimentos de canales pagados con presupuesto mínimo primero. Valida hipótesis de canal con $500 antes de escalar. Opera sobre canales ya validados orgánicamente o bajo hipótesis específicas de demanda que requieren prueba rápida con presupuesto.

**Por qué es necesario:** El canal pagado amplifica lo que funciona — no valida lo que funciona. Un generalista sin foco en paid tiende a gastar el presupuesto de validación en configurar campañas complejas en lugar de aprender rápido. El especialista en paid sabe que la primera campaña no es para vender: es para medir el costo de un clic, una conversión, un lead.

---

## SKILL 7.B.1 — paid-channel-experiment

**Propósito:** Diseñar el experimento de canal pagado mínimo ($500 o menos) para validar una hipótesis de adquisición antes de escalar presupuesto.

**Trigger:** "validar canal pagado", "Meta Ads", "Google Ads", "LinkedIn Ads", "experimento de $500", "testear adquisición pagada", "probar anuncio".

**INPUT obligatorio:**
- Hipótesis de canal a validar (qué queremos saber exactamente)
- Propuesta de valor y mensaje núcleo (4.1)
- Perfil de audiencia (1.2) — para targeting
- Creativas disponibles o brief de creativas (output de Agente 8)
- Presupuesto disponible para el experimento

**INPUT opcional:**
- Resultados de canal orgánico (7.A) — qué mensaje resonó
- Benchmarks de CTR/CPL del sector (del Analista 7.D)

**OUTPUT:**
```
EXPERIMENTO DE CANAL PAGADO — [Proyecto] — [Canal]
Presupuesto: $[monto] | Duración: [días] | Hipótesis: [exactamente qué queremos saber]

─── HIPÓTESIS ───
"Si mostramos [mensaje X] a [audiencia Y] en [canal Z], obtendremos [métrica] de [número], lo que validaría que [conclusión]."

─── CONFIGURACIÓN ───
Canal: [Meta / Google / LinkedIn / TikTok / otro]
Razón de elección: [por qué este canal para esta audiencia]

Audiencia:
  Targeting: [parámetros exactos — demografía, intereses, comportamientos, lookalike]
  Exclusiones: [quiénes NO queremos ver el anuncio]
  Tamaño estimado: [N personas]

Creatividad:
  Variante A: [descripción de la creativa — viene de Agente 8]
  Variante B: [descripción de la creativa — viene de Agente 8]
  [mínimo 2 variantes — sin A/B no hay aprendizaje]

Estructura de campaña:
  Objetivo: [tráfico / leads / conversiones — elegir UNO]
  Presupuesto diario: $[monto] / [días]
  Puja: [automática / manual — con razón]

─── MÉTRICAS DE VALIDACIÓN ───
Métrica primaria: [CTR / CPL / CPA / ROAS] — meta: [número]
Métrica secundaria: [reach / frequency / quality score]

─── CRITERIO DE DECISIÓN ───
ESCALAR si: [métrica primaria] ≥ [umbral] después de [N] días
NO ESCALAR si: [métrica primaria] < [umbral] después de [N] días
PIVOTAR AUDIENCIA si: CTR < [%] (el mensaje no llega a la audiencia correcta)
PIVOTAR MENSAJE si: CTR ≥ [%] pero conversión < [%] (llega pero no convierte)

─── APRENDIZAJE ESPERADO ───
Si funciona: [qué concluimos sobre el canal y el mensaje]
Si no funciona: [qué descartamos y qué testear próximo]

─── PRESUPUESTO BREAKDOWN ───
$[monto]: [semana 1 — aprendizaje inicial]
$[monto]: [semana 2 — si semana 1 da señal positiva]
Reserva: $[monto] para creativas adicionales si se necesitan
```

**FLUJO:**
1. Confirmar que el canal orgánico ya fue probado (7.A). Si no, señalar que se está saltando un paso.
2. Definir la hipótesis exacta: qué queremos saber (no "si funciona" — eso es vago).
3. Diseñar el targeting con los datos de perfil de población (1.2).
4. Solicitar creativas al Narrador (Agente 8) con brief específico para el canal.
5. Estructurar la campaña con presupuesto mínimo y A/B obligatorio.
6. Definir la fecha de corte para leer resultados y el umbral de decisión.
7. Documentar el aprendizaje, no solo el resultado.

**REGLAS:**
- $500 antes de $50.000. Sin excepción. Aunque el CEO quiera "ir a escala desde el día 1".
- Nunca lanzar paid sin landing page con conversión probada orgánicamente primero.
- La primera campaña de paid no es para vender. Es para medir. El objetivo siempre es un aprendizaje, no un número de ventas.
- Sin A/B = sin aprendizaje. Cada experimento tiene mínimo 2 variantes de creativa.
- Si CTR < 1% en Meta o < 2% en LinkedIn después de 48 horas con $100, el problema es de audiencia o de creativa — no de presupuesto. No aumentar el presupuesto antes de entender la causa.
- No correr más de 2 experimentos de canal en paralelo. Más = imposible atribuir resultados.

**CRITERIO DE CALIDAD:**
- La hipótesis es refutable: hay un número específico y un umbral de decisión claro antes de lanzar.
- El targeting usa los datos del perfil de población (1.2), no suposiciones del equipo.
- El experimento tiene fecha de corte y criterio de decisión documentados antes de gastar el primer dólar.

---

## SKILL 7.B.2 — paid-channel-scaling

**Propósito:** Diseñar el plan de escalado de un canal pagado validado, con estructura de campañas, reglas de puja y lógica de expansión de presupuesto.

**Trigger:** "escalar paid", "aumentar presupuesto", "canal validado", "plan de medios", "scaling paid ads", "cómo escalamos [canal]".

**INPUT obligatorio:**
- Resultados del experimento de validación (7.B.1) — métricas reales, no estimadas
- Presupuesto mensual disponible para escala
- LTV/CAC objetivo (viene del Analista 3.2)

**INPUT opcional:**
- Lookalike audiences disponibles (si hay base de clientes suficiente)
- Datos de retargeting (si hay tráfico orgánico previo)

**OUTPUT:**
```
PLAN DE ESCALADO — [Canal] — [Proyecto]
Presupuesto mensual: $[monto] | LTV/CAC objetivo: [ratio]

─── ESTRUCTURA DE CAMPAÑAS ───
Campaña 1 (Prospección): $[%] del presupuesto
  Objetivo: [cold traffic — nueva audiencia]
  Audiencia: [cold + lookalike]
  Creativas: [N variantes activas en rotación]

Campaña 2 (Retargeting): $[%] del presupuesto
  Objetivo: [conversión — audiencia caliente]
  Audiencia: [visitantes + lista de emails]
  Creativas: [N variantes — mensaje diferente al de prospección]

─── REGLAS DE PUJA ───
Presupuesto diario inicial: $[monto]
Escalado semanal: [%] si CPA ≤ $[umbral]
Pausa automática si: CPA > $[umbral] por [N] días consecutivos

─── LÓGICA DE EXPANSIÓN ───
Semana 1-2: $[monto] — aprender con estructura base
Semana 3-4: $[monto] — si CPA es estable, +[%] de presupuesto
Mes 2: $[monto] — expandir a [audiencias adicionales / formatos adicionales]
Mes 3: $[monto] — techo eficiente estimado: $[monto]/mes

─── MÉTRICAS DE SALUD ───
CPA actual: $[monto] | Meta: $[monto] (= LTV / 3)
ROAS actual: [ratio] | Meta: [ratio]
Frecuencia máxima: [N] impresiones antes de rotar creativa
Señal de fatiga de creativa: CTR cae [%] semana a semana

─── CUÁNDO PARAR DE ESCALAR ───
Techo eficiente del canal: $[monto]/mes
Señal de saturación: CPA aumenta [%] sin explicación de temporalidad
Acción: [abrir nuevo canal vs optimizar el existente]
```

**REGLAS:**
- El escalado de presupuesto sigue la curva de aprendizaje del algoritmo: aumentos de máximo 20-30% por semana. Duplicar presupuesto en un día resetea el aprendizaje.
- El LTV/CAC objetivo (>3x) no es negociable. Si el CPA en el canal no permite ese ratio, el canal no escala aunque esté "funcionando".
- Retargeting siempre separado de prospección. Mezclarlos contamina los datos y destruye la atribución.
- Toda campaña tiene reglas de pausa automática. Nadie puede monitorear manualmente 24/7.

**CRITERIO DE CALIDAD:**
- El techo eficiente estimado del canal está calculado (no "escalamos hasta donde podamos").
- Las reglas de puja tienen umbrales numéricos concretos, no "si no funciona, paramos".
- La lógica de expansión respeta el algoritmo del canal elegido (meta: learning phase de Facebook, quality score de Google, etc.).

---

# SUBAGENTE 7.C — ESPECIALISTA EN LIFECYCLE & RETENCIÓN

**Función central:** Diseñar y ejecutar el ciclo de vida del usuario desde la activación hasta la expansión. Construye las secuencias de email que llevan al usuario del primer uso al hábito, y las palancas de retención que convierten churn en NRR positivo.

**Por qué es necesario:** El 60-70% del crecimiento sostenible viene de retener y expandir la base existente, no de adquirir nuevos usuarios. Sin un especialista en lifecycle, los equipos optimizan obsesivamente el canal de adquisición mientras ignoran que el balde tiene agujeros. El lifecycle specialist cierra los agujeros.

---

## SKILL 7.C.1 — onboarding-email-sequence

**Propósito:** Diseñar la secuencia de emails de onboarding (día 0 a día 30) que lleva al usuario del registro al primer valor real y establece el hábito de uso.

**Trigger:** "secuencia de onboarding", "emails de bienvenida", "activación de usuarios", "cómo llevar al usuario al primer valor".

**INPUT obligatorio:**
- Flujo de usuario (5.1) — qué es el "primer valor" (time-to-value) y cómo se llega
- Perfil de población (1.2) — idioma, tono, jobs to be done
- Analytics de onboarding (6.3) — en qué paso del funnel pierden usuarios

**INPUT opcional:**
- Copy de interfaz (5.3) — para mantener coherencia de voz
- Datos de comportamiento iniciales si el producto ya está live

**OUTPUT:**
```
SECUENCIA DE ONBOARDING — [Proyecto]
Duración: 30 días | Objetivo: [%] de activación en día 7

─── DEFINICIÓN DE ACTIVACIÓN ───
Un usuario está "activado" cuando: [acción específica en el producto]
Por qué esta acción: [qué predice que el usuario va a retener]
Time-to-activation objetivo: [horas desde el registro]

─── EMAIL 1 — BIENVENIDA (día 0, inmediato) ───
Trigger: registro completado
Asunto: [texto exacto — sin "Bienvenido a [Producto]"]
Preview: [texto]
Objetivo: llevar al usuario a completar [acción de activación]
Estructura:
  Apertura: [qué es lo primero que ve]
  CTA primario: "[texto exacto del botón]" → [URL]
Tiempo de lectura estimado: [segundos]

─── EMAIL 2 — PRIMER VALOR (día 1, si no activó) ───
Trigger: NO completó [acción de activación]
Asunto: [texto — ángulo diferente al email 1]
Objetivo: mostrar el valor antes de que el usuario lo descubra
CTA: "[texto]" → [URL directa a la feature, no al home]

─── EMAIL 3 — EDUCACIÓN (día 3) ───
Trigger: activó O no activó [condicional]
Asunto: [texto]
Objetivo: [segundo hábito a establecer]
CTA: "[texto]" → [URL]

─── EMAIL 4 — SOCIAL PROOF (día 7) ───
Trigger: día 7 post registro
Asunto: [texto con prueba social específica]
Objetivo: reforzar la decisión de seguir usando el producto
Estructura: [caso de uso real o resultado de otro usuario]

─── EMAIL 5 — EXPANSIÓN (día 14) ───
Trigger: usuario activado
Asunto: [texto — introduce una feature secundaria]
Objetivo: [segundo job to be done]

─── EMAIL 6 — WIN-BACK (día 21, si no activó) ───
Trigger: no completó [acción de activación] en 21 días
Asunto: [texto directo — no click-bait]
Objetivo: última oportunidad de activación o feedback
CTA alternativo: "[texto]" → [encuesta de 1 pregunta]

─── MÉTRICAS POR EMAIL ───
Email 1: open rate objetivo [%] / CTR objetivo [%]
Email 2: [métricas]
[...]

─── SEÑALES DE OPTIMIZACIÓN ───
Si open rate < [%]: problema de asunto o sender name
Si CTR < [%]: problema de copy o CTA
Si activación en día 7 < [%]: problema de producto, no de email
```

**FLUJO:**
1. Definir la acción de activación con el equipo de UX (5.A/5.B). Sin esto, la secuencia no tiene objetivo.
2. Mapear el funnel de onboarding con datos de analytics (6.3) — dónde pierden usuarios.
3. Diseñar cada email como respuesta a un comportamiento del usuario (trigger-based, no blast).
4. Escribir el asunto primero — es lo que determina si el email se lee.
5. El CTA de cada email lleva a una sola acción. Nunca múltiples CTAs.
6. Definir métricas objetivo antes de lanzar para poder evaluar.

**REGLAS:**
- La secuencia de onboarding no es newsletter. No tiene noticias de la empresa, updates de producto, ni "novedades". Solo acciones para que el usuario llegue al valor.
- Nunca "Bienvenido a [Nombre del producto]" como asunto del email 1. Es el asunto más ignorado del mundo.
- Cada email tiene un único CTA. Más de uno divide la atención y reduce la conversión.
- Los emails de onboarding son trigger-based (responden a comportamiento), no time-based. Ajustar la secuencia según lo que el usuario hizo o no hizo.
- Si la activación en día 7 es baja a pesar de buenos open rates y CTRs, el problema es el producto, no el email. No optimizar más el email hasta que el producto resuelva la fricción.

**CRITERIO DE CALIDAD:**
- La acción de activación está definida antes de escribir un solo asunto.
- Cada email tiene trigger específico (comportamiento), objetivo específico y un solo CTA.
- La secuencia diferencia entre usuario activado y no activado (condicional en día 3).

---

## SKILL 7.C.2 — retention-playbook

**Propósito:** Diseñar el conjunto de palancas de retención que reducen el churn y aumentan el NRR, organizadas por momento del ciclo de vida (riesgo de churn temprano, mid-life, expansión).

**Trigger:** "reducir churn", "retención", "NRR", "usuarios que se van", "cómo retener", "playbook de retención".

**INPUT obligatorio:**
- Datos de churn actuales o benchmark del sector (Agente 9 / 3.2)
- Razones de churn conocidas o hipótesis (feedback de usuarios, encuestas)
- Modelo de negocio y pricing (4.1) — para calcular impacto de retención en MRR

**INPUT opcional:**
- Segmentación de usuarios por nivel de activación (analytics 6.3)
- NPS o Sean Ellis score actual (Agente 10)

**OUTPUT:**
```
RETENTION PLAYBOOK — [Proyecto]
Churn actual: [%] mensual | Meta: [%] mensual | Impacto en MRR: $[monto]/mes

─── SEGMENTOS DE RIESGO ───
Riesgo alto (acción inmediata):
  Señal: [comportamiento o ausencia de comportamiento]
  Definición: [qué hace que un usuario caiga en este segmento]
  % de la base actual: [estimado]

Riesgo medio (nurturing):
  Señal: [comportamiento]

Activados (expansión):
  Señal: [comportamiento]

─── PALANCAS POR MOMENTO ───

RETENCIÓN TEMPRANA (días 0-30):
  Palanca 1: [acción] — [impacto estimado en churn] — [cómo medir]
  Palanca 2: [acción] — [impacto] — [cómo medir]

RETENCIÓN MID-LIFE (días 31-90):
  Palanca 1: [acción] — [impacto] — [cómo medir]
  Check-in proactivo: [cuándo / cómo / por quién]

EXPANSIÓN (día 90+):
  Palanca 1: [qué trigger dispara la conversación de upsell]
  Palanca 2: [feature o plan que aumenta el ACV]

─── EARLY WARNING SYSTEM ───
Señal roja (riesgo de churn inminente): [comportamiento — acción en 48h]
Señal amarilla (riesgo medio): [comportamiento — acción en 1 semana]
Quién actúa: [humano / automatización / ambos]

─── PROTOCOLO DE CHURN INEVITABLE ───
Cuando un usuario confirma que se va:
  1. [pregunta exacta para feedback]
  2. [oferta de rescate si aplica — condiciones]
  3. [off-boarding con dignidad — qué datos puede exportar]
  Aprendizaje: [cómo se documenta para el sistema]

─── MÉTRICAS ───
Churn mensual: [actual] → meta: [número] — plazo: [tiempo]
NRR actual: [%] → meta: >110% — plazo: [tiempo]
Expansión revenue % del MRR: [actual] → meta: [%]
```

**REGLAS:**
- El churn de los primeros 30 días es un problema de producto o de expectativas mal gestionadas, no de retención. No intentar "retener" a un usuario que nunca encontró el valor — buscar la causa raíz.
- Un check-in proactivo antes de que el usuario tenga un problema vale 10x más que un win-back después de que se fue.
- NRR > 100% significa que aunque pierdas usuarios, los que se quedan gastan más. Ese es el objetivo de la expansión.
- El protocolo de churn inevitable es obligatorio. Los usuarios que se van con buena experiencia refieren. Los que se van mal, escriben reviews negativos.
- Churn < 5% mensual en SaaS B2B es el umbral operativo. Sobre ese número, cualquier inversión en adquisición pagada se está llenando un balde con agujeros.

**CRITERIO DE CALIDAD:**
- El early warning system tiene señales observables en el producto (no "sentimiento del equipo").
- Las palancas de retención son específicas y medibles (no "mejorar la experiencia del usuario").
- El playbook diferencia entre churn de los primeros 30 días (problema de producto) y churn mid-life (problema de valor percibido).

---

# SUBAGENTE 7.D — ANALISTA DE CANALES Y EXPERIMENTOS

**Función central:** Medir el desempeño de todos los canales de adquisición, identificar cuáles tienen el mejor LTV/CAC, diseñar los experimentos de crecimiento y evitar el sesgo de confirmación que tienen los especialistas de canal. Es quien dice "este canal no está funcionando" cuando todos los demás tienen incentivo a defender el propio.

**Por qué es necesario:** Sin un analista independiente de los canales, el sesgo de atribución destruye los datos. El especialista en paid tiene incentivo a atribuir conversiones a su canal. El especialista en orgánico tiene incentivo a demostrar que el contenido convierte. Alguien tiene que medir sin sesgo y con metodología robusta.

---

## SKILL 7.D.1 — channel-attribution-analysis

**Propósito:** Medir el CAC real por canal (incluyendo tiempo de equipo, no solo gasto en medios), comparar LTV/CAC por canal y priorizar dónde invertir los recursos del siguiente mes.

**Trigger:** "qué canal está funcionando mejor", "CAC por canal", "atribución", "priorizar canales", "dónde invertir el próximo mes", "reporte de canales".

**INPUT obligatorio:**
- Datos de adquisición por canal (período: mínimo 4 semanas)
- Costos por canal (gasto en medios + tiempo de equipo estimado en horas × tarifa)
- Datos de conversión a cliente pagador por canal (del sistema de analytics / CRM)

**INPUT opcional:**
- LTV por cohorte si hay datos suficientes (Agente 9)
- Datos de retención por canal de adquisición (¿los usuarios de LinkedIn retienen mejor que los de Meta?)

**OUTPUT:**
```
ANÁLISIS DE CANALES — [Proyecto] — [período]

─── CAC REAL POR CANAL ───
Canal: [nombre]
  Gasto en medios: $[monto]
  Tiempo de equipo: [horas] × $[tarifa] = $[costo]
  CAC total: $[monto]
  Clientes adquiridos: [N]
  CAC por cliente: $[monto]

[repetir para cada canal activo]

─── LTV/CAC POR CANAL ───
Canal 1: LTV/CAC = [ratio] [✅ >3x / ⚠️ 1-3x / ❌ <1x]
Canal 2: LTV/CAC = [ratio] [veredicto]
[...]

─── CALIDAD DE USUARIO POR CANAL ───
(Si hay datos de retención por cohorte de adquisición)
Canal 1: retención 30d = [%] | 60d = [%] | 90d = [%]
Canal 2: [idem]
Conclusión: [qué canal trae usuarios que mejor retienen]

─── RANKING DE CANALES ───
1. [Canal] — LTV/CAC [ratio] — recomendación: [invertir más / mantener / reducir]
2. [Canal] — LTV/CAC [ratio] — recomendación: [...]
3. [Canal] — LTV/CAC [ratio] — recomendación: [...]

─── DECISIÓN PARA EL PRÓXIMO MES ───
Canal a escalar: [nombre] — razón: [LTV/CAC + señal de escalabilidad]
Canal a mantener: [nombre] — razón: [...]
Canal a reducir/pausar: [nombre] — razón: [LTV/CAC insuficiente o plateau]
Canal nuevo a testear: [nombre] — hipótesis: [...]

─── ALERTAS ───
[Canal]: CAC aumentó [%] respecto al mes anterior — posible saturación
[Canal]: datos insuficientes para decisión — necesita [N] semanas más
```

**FLUJO:**
1. Recopilar datos de todos los canales activos con el mismo período de referencia.
2. Calcular CAC incluyendo tiempo de equipo (el CAC solo con gasto en medios es una mentira).
3. Cruzar con datos de retención por canal si están disponibles.
4. Calcular LTV/CAC para cada canal.
5. Hacer el ranking.
6. Emitir recomendación de asignación de presupuesto para el próximo mes.

**REGLAS:**
- El CAC que no incluye tiempo de equipo es falso. En etapas tempranas, el costo de equipo es mayor al gasto en medios.
- Un canal con LTV/CAC < 1x está destruyendo valor aunque traiga usuarios. Pararlo de inmediato.
- 4 semanas es el mínimo de datos para una conclusión. Con menos, el análisis es ruido.
- No concluir sobre canales con menos de 10 conversiones. Muestra insuficiente.
- Si dos canales tienen LTV/CAC similares, priorizar el que trae usuarios con mayor retención.

**CRITERIO DE CALIDAD:**
- El CAC incluye costo de medios + tiempo de equipo (desagregado).
- La recomendación del próximo mes tiene razón específica para cada canal (no "escalar lo que funciona").
- Los canales sin datos suficientes están marcados como "no concluyente" — no se recomienda acción sobre ellos.

---

## SKILL 7.D.2 — growth-experiment-design

**Propósito:** Diseñar el backlog de experimentos de crecimiento para el próximo trimestre, priorizados por impacto estimado, facilidad de implementación y velocidad de aprendizaje.

**Trigger:** "experimentos de crecimiento", "growth experiments", "qué testear", "backlog de growth", "cómo aceleramos el crecimiento", "hipótesis de crecimiento".

**INPUT obligatorio:**
- Métricas actuales del negocio (Agente 9 — AARRR)
- Canales validados y sus métricas (7.D.1)
- Cuello de botella actual del funnel (dónde se pierde más usuario)

**INPUT opcional:**
- Resultados de experimentos anteriores
- Recursos disponibles (cuántas personas pueden correr experimentos en paralelo)

**OUTPUT:**
```
BACKLOG DE EXPERIMENTOS — [Proyecto] — Q[N] [año]

─── CUELLO DE BOTELLA ACTUAL ───
Etapa del funnel con mayor pérdida: [adquisición / activación / retención / revenue / referral]
Métrica que más impacta si mejora: [nombre] — impacto estimado en [métrica norte]: [%]

─── EXPERIMENTOS PRIORIZADOS ───

EXPERIMENTO 1 (ALTA PRIORIDAD)
Hipótesis: "Si [cambiamos X], entonces [métrica Y] mejorará [N%], porque [razón conductual]."
Cuello que ataca: [etapa del funnel]
Impacto potencial: [bajo / medio / alto] — [cómo se calcula]
Facilidad: [baja / media / alta]
Recursos necesarios: [horas de diseño / desarrollo / copy]
Duración: [días]
Métrica primaria: [nombre] — baseline: [valor] — meta: [valor]
Responsable: [subagente o rol]
Estado: [por empezar / en curso / completado]

EXPERIMENTO 2 (ALTA PRIORIDAD)
[misma estructura]

EXPERIMENTO 3 (MEDIA PRIORIDAD)
[misma estructura]

─── EXPERIMENTOS DESCARTADOS ───
[Hipótesis] — razón: [por qué no ahora]

─── REGLAS DE PRIORIZACIÓN ───
1. Atacar el cuello de botella, no el canal favorito.
2. Máximo 3 experimentos activos en paralelo.
3. Un experimento a la vez por elemento (no testear headline y CTA al mismo tiempo).

─── REGISTRO DE APRENDIZAJES ───
[Experimento anterior]: [hipótesis] → [resultado] → [conclusión] → [próximo paso]
```

**REGLAS:**
- Los experimentos atacan el cuello de botella del funnel. Si la activación es 15% y la retención es 80%, el experimento es de activación — aunque el equipo prefiera testear adquisición.
- Máximo 3 experimentos activos en paralelo. Más = contaminación de señales y equipo disperso.
- La hipótesis tiene razón conductual. "Creemos que CTR mejorará" no es una hipótesis — "Creemos que CTR mejorará porque el usuario busca prueba social antes de hacer clic" sí lo es.
- Los aprendizajes de experimentos fallidos son tan valiosos como los exitosos. Documentar siempre.

**CRITERIO DE CALIDAD:**
- El primer experimento ataca el cuello de botella identificado en los datos, no la intuición del equipo.
- Cada hipótesis tiene razón conductual (por qué creemos que el cambio tendrá ese efecto).
- El backlog distingue entre "alta prioridad — empezar este sprint" y "media prioridad — próximo sprint".

---

# Definition of Done — Crecimiento / Lanzamiento

Un ciclo de lanzamiento y crecimiento está **done** cuando cumple TODOS estos criterios:

```
─── VALIDACIÓN DE DEMANDA ───
□ Hipótesis de canal documentada antes de gastar el primer dólar
□ Experimento de $500 completado con aprendizaje documentado
□ Criterio de éxito/fracaso definido antes del lanzamiento del experimento
□ Resultado del experimento registrado con conclusión accionable

─── CANAL ORGÁNICO ───
□ Canal primario elegido con justificación basada en dónde está la audiencia
□ Plan semana a semana ejecutable (semanas 1-8) con acciones específicas
□ Señales de éxito y fracaso definidas para semana 2 y semana 4
□ Mínimo 10 conversaciones directas con potenciales usuarios en semana 1-2

─── LANZAMIENTO ───
□ Primer cliente pagador: perfil, canal, pitch y precio documentados
□ Canales orgánicos probados antes de lanzar paid
□ Creativas con mínimo 2 variantes (A/B) antes de activar paid
□ Landing page con conversión probada antes de lanzar tráfico pagado

─── LIFECYCLE & RETENCIÓN ───
□ Acción de activación definida (qué hace que un usuario esté "activado")
□ Secuencia de onboarding: mínimo 4 emails trigger-based
□ Early warning system de churn configurado con señales observables
□ Protocolo de churn inevitable documentado

─── MÉTRICAS DE TRACCIÓN ───
□ CAC por canal calculado incluyendo tiempo de equipo
□ LTV/CAC por canal ≥ 3x en al menos un canal antes de escalar
□ Churn mensual medido con baseline establecido
□ Funnel de conversión trazable end-to-end (analytics instrumentados — skill 6.3)

─── GATE 5 — PMF ───
□ Sean Ellis test completado con mínimo 40 respuestas de usuarios activos
□ ≥ 40% "muy decepcionados" — condición de GO para Fase 6
□ Perfil del usuario "muy decepcionado" documentado (quiénes son, qué beneficio mencionan)
□ Primeros pagos reales recibidos (no promesas, no LOIs — dinero en cuenta)
□ NRR actual documentado aunque sea con muestra pequeña

─── GATE 6 — ESCALA ───
□ LTV/CAC > 3x en el canal principal de escala
□ NRR > 110% (expansión supera el churn)
□ Churn mensual < 5% (SaaS B2B)
□ Backlog de experimentos Q[N+1] priorizado por cuello de botella
□ Al menos un canal validado con techo eficiente estimado
```

---

## Cuándo agregar subagentes adicionales

Los 4 subagentes cubren el 95% de los proyectos del Venture Engine. Casos especiales:

| Situación | Subagente adicional |
|---|---|
| Marketplace con dos lados (supply + demand) | Agente de Marketplace Growth (estrategia de bootstrap de liquidez) |
| Product-Led Growth con virality como canal principal | Agente de PLG / Viral Loops |
| Enterprise sales (ACV > $10.000) | Agente de Sales Development |
| Comunidad como canal primario (community-led growth) | Agente de Community Building |
| Contenido como motor principal (media company model) | Agente de Content / SEO especializado |

---

*SiriusLabs — siriuslabs.uy@gmail.com
Actualizar cuando se detecte un patrón de error recurrente en los lanzamientos ejecutados.*
