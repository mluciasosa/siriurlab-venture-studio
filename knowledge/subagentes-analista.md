# Subagentes del Analista
### Equipo especializado para validar que el negocio tiene sentido antes de construirlo

> **Por qué el Analista necesita subagentes:**
> El Agente 3 toma las tres decisiones con mayor consecuencia financiera del sistema: si el mercado justifica la inversión, si los números cierran, y si el producto se puede construir con los recursos disponibles. Un error aquí no se detecta hasta 4 fases después.

---

## Principio rector

Los números no son la realidad — son un modelo de la realidad. Un modelo útil tiene supuestos explícitos, metodología verificable, y rango de escenarios que permite tomar decisiones aunque haya incertidumbre.

**Regla del Analista: cada número tiene fuente, cada supuesto tiene justificación, cada proyección tiene un escenario donde falla.**

---

## Los 4 Subagentes

```
┌──────────────────────────────┐
│   AGENTE 3 — ANALISTA        │
└──────────────┬───────────────┘
               │
   ┌───────────┼───────────┬───────────┐
  3.A         3.B         3.C         3.D
Analista    Modelador   Evaluador   Analista
Mercado     Financiero  Técnico     de Riesgo
```

**Flujo obligatorio:**
```
PROBLEMA (1.1) + POBLACIÓN (1.2) + COMPETENCIA (2.1)
→ 3.A Mercado → 3.B Finanzas → 3.C Técnica → 3.D Riesgos
→ VEREDICTO CONSOLIDADO → Gate 1 (Guardián 10.A)
```

---

# SUBAGENTE 3.A — ANALISTA DE MERCADO

**Función:** TAM/SAM/SOM con metodología bottom-up verificable. Dinámica de crecimiento. Contexto regulatorio. Poder de pricing.

**Por qué es necesario:** La mayoría de los análisis de mercado toman el tamaño total de una industria y lo llaman TAM. Eso no es un análisis. El Analista de Mercado produce un SOM real: cuántos clientes del segmento específico pueden alcanzarse con el canal disponible y el equipo actual, en los próximos 18-24 meses.

---

## SKILL 3.A.1 — market-sizing-rigorous

**Trigger:** "dimensionar el mercado", "TAM SAM SOM", "¿cuánto vale la oportunidad?".

**INPUT obligatorio:** Problema (1.1) + Perfil de población (1.2) + Mapa competitivo (2.1).

**OUTPUT:**
```
ANÁLISIS DE MERCADO — [Proyecto]
Metodología: bottom-up | Confianza: [alta/media/baja]

─── TAM ───
Universo base: [N personas/empresas con el problema] — fuente: [URL + fecha]
Precio de referencia: $[precio/año] — fuente: [benchmark / willingness-to-pay]
Cálculo: [N] × $[precio] = $[TAM]

─── SAM ───
Filtros (cada uno con % de reducción y fuente):
  Geografía [países]: [N] → [N] — [% reducción] — fuente: [...]
  Idioma: [N] → [N] — [%]
  Acceso tecnológico: [N] → [N] — [%]
  Capacidad de pago: [N] → [N] — [%]
SAM: [N] × $[precio] = $[SAM]

─── SOM (18-24 meses) ───
Restricciones reales:
  Capacidad del equipo de sales/growth: [N clientes/mes]
  Presupuesto de adquisición / CAC estimado: [N clientes]
  Tiempo de adopción: [justificación]
  Fricción competitiva: [descripción]

Escenario CONSERVADOR: $[monto] — supuestos: [lista]
Escenario BASE: $[monto] — supuestos: [lista]
Escenario OPTIMISTA: $[monto] — supuestos: [lista]

─── DINÁMICA ───
CAGR del mercado: [%] — fuente: [...] | Driver: [qué lo impulsa]
Fase: [emergente / creciendo / maduro / declinando]
Riesgo de contracción: [descripción]

─── REGULACIÓN ───
[Regulación relevante] — [qué implica] — [riesgo: alto/medio/bajo]
Oportunidad regulatoria: [¿hay regulación que crea una ventana?]

─── VEREDICTO ───
Bootstrap (>$1M SOM): [sí/no] | Venture (>$10M SOM): [sí/no]
Tiempo a $1M ARR en escenario base: [meses]
```

**REGLAS:**
- Nunca metodología top-down como fuente primaria.
- Cada filtro del SAM tiene su propia fuente.
- El SOM tiene restricciones de recursos reales — no es una aspiración.
- El escenario conservador asume que los 3 supuestos más optimistas fallan simultáneamente.

---

## SKILL 3.A.2 — competitive-dynamics

**Trigger:** "dinámica competitiva", "barreras de entrada", "poder de pricing", "¿podemos ganar?".

**INPUT obligatorio:** Mapa competitivo (2.1) + Análisis de mercado (3.A.1).

**OUTPUT:**
```
DINÁMICA COMPETITIVA — [Proyecto]

─── ESTRUCTURA DEL MERCADO ───
Tipo: [monopolio / oligopolio / fragmentado / atomizado]
Implicación para pricing: [poder alto/medio/bajo del vendedor]
Implicación para CAC: [estructuralmente alto/bajo]

─── FUERZAS DE PORTER ───
Poder de compradores: [alto/medio/bajo] — [razón en una oración]
Poder de proveedores: [alto/medio/bajo] — [razón]
Amenaza de sustitutos: [alta/media/baja] — [razón]
Amenaza de nuevos entrantes: [alta/media/baja] — [razón]
Rivalidad entre existentes: [alta/media/baja] — [razón]

─── BARRERAS DE ENTRADA ───
[barrera]: [descripción] — tiempo para superarla: [semanas/meses/años]
¿Hay ventana antes de que los incumbentes reaccionen? [sí/no] — [cuánto tiempo]

─── EFECTOS DE RED ───
¿Existen? [sí/no] | Tipo: [directos / indirectos / de datos]
Implicación: [el que llega primero tiene ventaja estructural / el mercado puede fragmentarse]

─── PODER DE PRICING ───
Precio actual del mercado: $[rango]
Nuestra posición: [premium / paridad / descuento] — [justificación]
Riesgo de commoditización: [alto/medio/bajo] — [razón]

─── VELOCIDAD DEL MERCADO ───
Ciclo de innovación del sector: [meses entre lanzamientos]
Riesgo de ser copiados: [alto/medio/bajo] — en [cuánto tiempo]
```

---

# SUBAGENTE 3.B — MODELADOR FINANCIERO

**Función:** Unit economics con rigor, proyección P&L a 18 meses, análisis de sensibilidad. El modelo no predice el futuro — crea un mapa de los supuestos que deben ser verdad para que el negocio funcione.

**Por qué es necesario:** Los unit economics mal modelados son la segunda causa más común de muerte de startups. Un buen modelo financiero no es el más optimista — es el que muestra exactamente qué supuesto hay que cambiar para que el negocio funcione.

---

## SKILL 3.B.1 — unit-economics-model

**Trigger:** "unit economics", "CAC LTV", "márgenes", "¿el modelo cierra?", "¿cuánto cuesta adquirir un cliente?".

**INPUT obligatorio:** Análisis de mercado (3.A.1) + Mapa competitivo (2.1, para pricing) + tipo de modelo de negocio.

**OUTPUT:**
```
UNIT ECONOMICS — [Proyecto] v[N]

─── PRECIO Y MARGEN BRUTO ───
Precio mensual/cliente: $[precio] — fuente: [benchmark / willingness-to-pay]
Costos de entrega/cliente/mes:
  Infraestructura (hosting, DB, CDN): $[X]
  IA compute (tokens × precio × sesiones): $[X] — [cálculo explícito]
  Soporte (% tiempo equipo): $[X]
  Herramientas: $[X]
  Total: $[X]
Margen bruto: [%] | Benchmark sector: [%] — fuente: [...]

─── ADQUISICIÓN ───
Canal 1: [nombre]
  Costo por click: $[X] — fuente: [benchmark plataforma]
  Conv. a trial: [%] | Conv. trial a pago: [%]
  CAC: $[X]
Canal 2: [misma estructura]
CAC blended: $[X]
Payback period: [meses] — benchmark aceptable: <12m venture / <6m bootstrap

─── RETENCIÓN Y LTV ───
Churn mensual: [%] — fuente: [benchmark sector / estimación] — justificación: [...]
Vida del cliente: [meses] = 1/churn
LTV: $[precio × margen × vida]
LTV/CAC: [ratio] 🟢 >3x / 🟡 1-3x / 🔴 <1x (muerte)

─── ANÁLISIS DE SENSIBILIDAD ───
| Variable | Base | -20% | -40% | LTV/CAC resultante |
|---|---|---|---|---|
| Precio | $[X] | $[X×0.8] | $[X×0.6] | [ratio] |
| Churn | [%] | [%×1.2] | [%×1.4] | [ratio] |
| Conv. trial | [%] | [%×0.8] | [%×0.6] | [CAC resultante] |

Peor escenario combinado (todo a -20%): LTV/CAC = [ratio]
¿Sigue siendo viable? [sí/no]

─── PUNTO DE EQUILIBRIO ───
Costos fijos: equipo $[X] + infra fija $[X] + tools $[X] = $[total]/mes
Clientes para equilibrio: $[costos fijos] / ($[precio] × [margen%]) = [N]
Con crecimiento de [N] clientes/mes → equilibrio en [meses]

─── VEREDICTO FINANCIERO ───
¿Tiene sentido el modelo? [SÍ / NO / CONDICIONAL]
Condición crítica: [supuesto más frágil]
Variable más sensible: [cuál tiene mayor impacto]
```

**REGLAS:**
- IA compute siempre calculado en tokens. Nunca "infraestructura" como línea única.
- Churn default SaaS B2B: 5%/mes si no hay benchmark mejor.
- Análisis de sensibilidad obligatorio — sin él no se sabe la holgura del modelo.
- LTV/CAC <1 = KILL automático. Sin argumentos que lo salven.

---

## SKILL 3.B.2 — financial-projections

**Trigger:** "proyección financiera", "P&L", "runway", "¿cuánto capital necesitamos?", "modelo a 18 meses".

**INPUT obligatorio:** Unit economics (3.B.1) + SOM (3.A.1).

**OUTPUT:**
```
PROYECCIÓN FINANCIERA — [Proyecto]
Horizonte: 18 meses

─── SUPUESTOS ───
Clientes mes 1: [N] — fuente: [waitlist / piloto / estimado]
Crecimiento MoM: [%] — fuente: [benchmark sector]
Churn mensual: [%] (de 3.B.1)
Expansión de cuenta: [%] (si aplica)

─── P&L MENSUAL (resumen) ───
| Mes | Clientes | MRR | Costos var. | Costos fijos | EBITDA | Cash acumulado |
| 1 | [N] | $[X] | $[X] | $[X] | $[X] | $[X] |
| 3 | ... |
| 6 | ... |
| 12 | ... |
| 18 | ... |

─── MILESTONES ───
Primer EBITDA positivo: Mes [N]
$1M ARR: Mes [N]
Break-even de caja: Mes [N]

─── NECESIDADES DE CAPITAL ───
Para llegar al break-even: $[monto]
Con holgura 20%: $[monto]
Runway con $[capital inicial] en escenario conservador: [meses]

Gate de decisión: si al mes [N] no llegamos a $[MRR] → revisar el modelo
```

**REGLAS:**
- Proyección en escenario conservador y base — nunca solo optimista.
- Milestones son gates de decisión reales, no aspiraciones.
- Runway siempre calculado en escenario conservador.

---

# SUBAGENTE 3.C — EVALUADOR TÉCNICO

**Función:** Viabilidad técnica del MVP. Stack óptimo. Costos de construcción con metodología explícita. Costos de IA/LLM detallados. Riesgos técnicos con probabilidad.

**Por qué es necesario:** Los costos de IA/LLM son el driver de costo más subestimado de los MVPs del Venture Engine en 2026. Un Evaluador Técnico especializado puede calcular si el modelo de negocio es viable con IA en el core antes de construir nada.

---

## SKILL 3.C.1 — technical-viability-assessment

**Trigger:** "viabilidad técnica", "¿se puede construir?", "stack recomendado", "estimación técnica".

**INPUT obligatorio:** Descripción de la solución + restricciones (presupuesto, equipo, tiempo) + modelo de negocio tentativo.

**OUTPUT:**
```
VIABILIDAD TÉCNICA — [Proyecto]
Equipo disponible: [descripción] | Veredicto: VIABLE / CON CONDICIONES / NO VIABLE

─── COMPONENTES DEL MVP ───
[Componente]: [qué hace] | Complejidad: [baja/media/alta] | Decisión: BUILD / BUY
  Si BUY: [herramienta] → $[costo/mes]
  Si BUILD: [días-persona estimados]
  Riesgo técnico: [bajo/medio/alto] — [razón]

[repetir para cada componente — máximo 6-8]

─── STACK RECOMENDADO ───
Frontend: [tech] — [razón ≤10 palabras] — $[costo/mes]
Backend: [tech] — [razón] — $[costo]
DB: [tech] — [razón] — $[costo]
Auth: [servicio] — [razón] — $[costo]
IA/LLM: [API Anthropic/OpenAI] — SIEMPRE APIs en MVP — $[costo variable]
Pagos: Stripe — 2.9% + $0.30/transacción
Deploy: [Vercel/Railway] — [razón] — $[costo]
Analytics: PostHog — gratis hasta 1M eventos
Total infra/mes con [N] usuarios: $[total]

─── COSTOS DE IA/LLM (si aplica) ───
Tokens entrada/llamada: [N] | Tokens salida/llamada: [N]
Llamadas/usuario/mes: [N]
Costo/usuario/mes = ([tokens_entrada × precio] + [tokens_salida × precio]) × llamadas = $[X]
Como % del precio: [%] — meta: <30% para mantener margen saludable

─── ESTIMACIÓN MVP ───
Desglose:
  Setup y arquitectura: [días]
  Feature 1 [nombre]: [días]
  Feature 2 [nombre]: [días]
  Feature 3 [nombre]: [días]
  Tests e integración: [días]
  Total: [días] × [N personas] = [semanas]

Costo: [días-persona] × $[costo/día] × 1.2 (contingencia) = $[total]

─── RIESGOS TÉCNICOS ───
[Riesgo]: Prob. [alta/media/baja] | Impacto: [retraso X sem / costo $X]
  Mitigación: [acción concreta]

─── DEUDA TÉCNICA PRE-ACEPTADA ───
[Ítem]: refactorizar cuando: [condición]

─── CONDICIONES PARA VIABILIDAD ───
[Lista de lo que tiene que ser verdad]
```

**REGLAS:**
- Nunca modelos de IA propios en el MVP. Siempre APIs existentes.
- Costo de IA/LLM calculado en tokens reales, no "estimado por uso".
- Estimación de tiempo incluye siempre 20% de contingencia.
- Si existe solución comprable que hace el 80% de lo necesario → BUY.

---

## SKILL 3.C.2 — ai-cost-modeling

**Trigger:** Cuando el producto usa LLMs como componente central. "costos de IA", "cuánto cuesta usar Claude/GPT", "tokens", "IA compute".

**OUTPUT:**
```
MODELO DE COSTOS IA — [Proyecto]

─── USO POR SESIÓN ───
Prompt de sistema: ~[N] tokens | Contexto usuario: ~[N] | Respuesta: ~[N]
Total por llamada: [N entrada] + [N salida]
Llamadas/sesión: [N] | Sesiones/usuario/mes: [N]

─── COSTO/USUARIO/MES ───
Modelo: [Claude Sonnet / otro]
Precio entrada: $[X]/M tokens | Precio salida: $[X]/M tokens
Costo = ([tokens_e × $p_e] + [tokens_s × $p_s]) × llamadas/mes = $[X]

─── PROYECCIÓN POR ESCALA ───
| Usuarios | Costo IA/mes | % del MRR | Margen restante |
| 100 | $[X] | [%] | [%] |
| 1.000 | $[X] | [%] | [%] |
| 5.000 | $[X] | [%] | [%] |

─── UMBRALES ───
Meta: costo IA <30% del precio para mantener margen saludable
Precio mínimo viable con este uso de IA: $[X/mes/usuario]
¿El precio actual es suficiente? [sí/no] — margen: [%]

─── OPTIMIZACIONES ───
Mejor prompt engineering: -[%] tokens | Modelo más pequeño para baja complejidad: -[%] costo
Caché de respuestas frecuentes: [% de llamadas cacheables]
```

---

# SUBAGENTE 3.D — ANALISTA DE RIESGO

**Función:** Mapa de riesgos del negocio, stress-test de supuestos frágiles, criterios de kill definidos antes del lanzamiento.

**Por qué es necesario:** Todo análisis de negocio tiene sesgo de confirmación. El Analista de Riesgo es la voz del escepticismo estructurado — no para hundir proyectos buenos, sino para identificar los supuestos más frágiles antes de que el mercado los exponga.

---

## SKILL 3.D.1 — risk-framework

**Trigger:** "análisis de riesgos", "qué puede salir mal", "risk assessment", "supuestos más frágiles".

**INPUT obligatorio:** Análisis de mercado (3.A.1) + Unit economics (3.B.1) + Viabilidad técnica (3.C.1) + Mapa competitivo (2.1).

**OUTPUT:**
```
FRAMEWORK DE RIESGOS — [Proyecto]

─── RIESGOS POR CATEGORÍA ───

MERCADO:
  [Riesgo]: Prob. [alta/media/baja] | Impacto: [crítico/alto/medio]
    Señal de alerta: [dato concreto que indica que se está materializando]
    Mitigación: [acción concreta — no "monitorear"]

MODELO DE NEGOCIO:
  [ej: "CAC real es 3x el estimado"]: Prob. media | Impacto: crítico
    Señal: CAC supera $[X] en el primer mes de lanzamiento
    Mitigación: canal orgánico funcionando antes de escalar pagado

TÉCNICO:
  [ej: "Costo LLM supera 30% del revenue"]: Prob. media | Impacto: alto
    Señal: costo LLM >$[X]/usuario en los primeros 100 usuarios
    Mitigación: optimizar prompts + caché antes de escalar

COMPETITIVO / REGULATORIO / EQUIPO:
  [misma estructura]

─── MATRIZ DE RIESGO ───
CRÍTICO (prob. alta × impacto crítico): [lista — plan de mitigación obligatorio antes de Gate 1]
ALTO (prob. media × impacto crítico): [lista — monitorear activamente]
MEDIO: [lista — revisar mensualmente]

─── LOS 3 SUPUESTOS MÁS FRÁGILES ───
Supuesto 1: "[en formato de hipótesis verificable]"
  Por qué es frágil: [razón]
  Cómo validar antes de construir: [experimento con presupuesto y timeline]
  Si falla: [qué cambiaría en el modelo]

Supuesto 2 / 3: [misma estructura]
```

---

## SKILL 3.D.2 — kill-criteria

**Propósito:** Definir las condiciones de cierre ANTES del lanzamiento, cuando el equipo no está emocionalmente invertido en los resultados. Previene el sunk cost fallacy.

**Trigger:** "criterios de kill", "cuándo cerramos", "cuándo pivotar", "condiciones de salida".

**OUTPUT:**
```
CRITERIOS DE KILL — [Proyecto]
Definidos: [fecha — antes del lanzamiento] | Son un contrato del equipo consigo mismo.

─── POR GATE ───

GATE 0: KILL si:
□ Problema sin evidencia de urgencia real (entrevistas muestran "bueno tenerlo" no "lo necesito ya")
□ Sin disposición a pagar en ninguna conversación de validación

GATE 1: KILL si:
□ SOM <$1M (bootstrap) / <$10M (venture) con supuestos razonables
□ LTV/CAC <1x con el CAC más barato disponible
□ Costo IA/LLM >50% del precio sin optimización posible

GATE 2: KILL si:
□ Revenue primitive incomprensible en una oración después de 2 iteraciones
□ Sin camino a primer cobro en menos de 6 meses

GATE 5 (los más importantes): KILL si:
□ Sin pago real tras [N] semanas con canal validado con $500
□ Sean Ellis <20% tras ajustes de mensaje y segmento
□ CAC real >3x CAC estimado sin mecanismo de reducción claro

GATE 6: KILL si:
□ LTV/CAC <1x por 3 meses consecutivos sin mejora
□ Churn >10% mensual durante 3 meses sin causa identificable

─── PROCESO DE KILL ───
1. Guardián emite veredicto KILL
2. Equipo tiene 48h para presentar evidencia contradictoria
3. Sin evidencia → KILL ejecutado
4. Orquestador documenta el aprendizaje
5. Equipo tiene 1 semana para decidir: pivot viable o cierre

─── LO QUE TODO KILL PRODUCE ───
□ Qué hipótesis falló y por qué
□ Dónde falló: problema / mercado / modelo / producto / go-to-market / ejecución
□ Recomendación para el próximo proyecto
□ Actualización del sistema si hay patrón repetido
```

**REGLA CRÍTICA:** Los criterios de kill se definen ANTES del lanzamiento. No se agregan después. Son binarios y objetivos — "el equipo no está entusiasmado" no es un criterio.

---

## Veredicto consolidado del Analista

```
VEREDICTO CONSOLIDADO — VIABILIDAD
Proyecto: [nombre] | Fecha: [fecha]

─── RESUMEN ───
Mercado (3.A): 🟢/🟡/🔴 — [razón en una oración]
Financiero (3.B): 🟢/🟡/🔴 — [razón]
Técnico (3.C): 🟢/🟡/🔴 — [razón]
Riesgo (3.D): 🟢/🟡/🔴 — [razón]

─── VEREDICTO ───
🟢 VERDE — GO: todas las áreas verdes o amarillo con mitigación
🟡 AMARILLO — ITERAR: al menos un área roja con corrección posible
🔴 ROJO — KILL: área crítica en rojo sin corrección viable

─── LOS 3 NÚMEROS QUE MÁS IMPORTAN ───
SOM: $[monto] — escenario base
LTV/CAC: [ratio] — escenario base
Tiempo a break-even: [meses] — escenario conservador

─── CONDICIÓN CRÍTICA ───
"[supuesto más frágil en formato de hipótesis verificable]"
Cómo validarlo antes de construir: [experimento específico]
```

---

## Definition of Done — Análisis completo

```
DEFINITION OF DONE — ANÁLISIS (Agente 3)

─── MERCADO (3.A) ───
□ TAM con metodología bottom-up y fuentes verificables
□ SAM con filtros explícitos y fuente por cada filtro
□ SOM con 3 escenarios y supuestos documentados
□ SOM supera umbral ($1M bootstrap / $10M venture)
□ Dinámica de mercado y regulación documentadas

─── FINANCIERO (3.B) ───
□ Margen bruto con IA compute desglosado (si aplica)
□ CAC por canal con conversiones benchmarkeadas
□ Churn con fuente de benchmark del sector
□ LTV/CAC en semáforo (🟢 >3x / 🟡 1-3x / 🔴 <1x)
□ Análisis de sensibilidad con 3 variables críticas
□ Proyección 12-18 meses con supuestos explícitos
□ Necesidades de capital y runway calculados

─── TÉCNICO (3.C) ───
□ Componentes con decisión BUILD vs BUY justificada
□ Stack con costo mensual por componente
□ Costo IA/LLM en tokens si el producto usa LLMs
□ Estimación de tiempo con desglose por feature
□ Riesgos técnicos con probabilidad y mitigación

─── RIESGO (3.D) ───
□ Framework de riesgos con matriz probabilidad × impacto
□ 3 supuestos más frágiles con experimento de validación
□ Criterios de kill definidos por gate

─── VEREDICTO ───
□ Veredicto consolidado (Verde/Amarillo/Rojo) producido
□ Condición crítica en formato de hipótesis verificable
□ Los 3 números entregados al Gate 1 (Guardián 10.A)
```

---

*SiriusLabs — siriuslabs.uy@gmail.com
El Analista es el agente que separa los proyectos que tienen sentido de los que se sienten bien. Son cosas distintas.*
