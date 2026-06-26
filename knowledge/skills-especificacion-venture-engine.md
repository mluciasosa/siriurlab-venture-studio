# Especificación de Skills — SiriusLabs Venture Engine
### Skills por agente para operación con máxima autonomía y calidad

> Cada skill está definida con: nombre, trigger, inputs, outputs, flujo, reglas y criterios de calidad.  
> Se implementan como archivos SKILL.md en la carpeta del agente correspondiente.

---

## Anatomía de cada skill

```
SKILL: nombre-de-la-skill
AGENTE: a qué agente pertenece
TRIGGER: cuándo se activa
INPUT: qué necesita (obligatorio y opcional)
OUTPUT: qué produce exactamente (formato, estructura)
FLUJO: pasos en orden, sin saltos
REGLAS: lo que no se negocia
CRITERIO DE CALIDAD: cómo saber si el output es de primer nivel
```

---

# AGENTE 0 — ORQUESTADOR ("Shifu")

---

## SKILL 0.1 — project-kickoff

**Propósito:** Inicializar un proyecto nuevo. Descomponer el objetivo en fases, asignar agentes, crear el plan maestro y el decision log.

**Trigger:** "nuevo proyecto", "explorar problema", "empezar con", "tenemos una oportunidad de".

**INPUT obligatorio:**
- Descripción del problema o área de oportunidad
- ODS de la ONU que se quiere abordar (si se conoce)
- Restricciones conocidas (presupuesto, tiempo, geografía)
- Nivel de urgencia: exploración / validación / construcción

**INPUT opcional:** investigación previa, competidores conocidos, tamaño de mercado estimado.

**OUTPUT:**
```
PLAN MAESTRO DEL PROYECTO — [Nombre]
ODS objetivo: [número y nombre]

FASES Y TIMELINE:
Fase 0: Discovery — Semanas 1-2 — Agente: Explorador
Fase 1: Mercado — Semanas 2-4 — Cartógrafo + Analista
Fase 2: Negocio — Semanas 4-5 — Arquitecto de Negocio
Fase 3: Producto — Semanas 5-7 — Arquitecto UX
Fase 4: MVP — Semanas 7-11 — Constructor + Medidor
Fase 5: Lanzamiento — Semanas 11-13 — Motor + Narrador
Fase 6: Escala — Semana 13+ — Motor de Crecimiento

HIPÓTESIS CENTRAL:
"Creemos que [población] tiene el problema de [problema] y pagaría [precio] por [solución] porque [razón]."

RIESGOS IDENTIFICADOS:
1. [riesgo]: [probabilidad] — [mitigación]

DECISION LOG:
[fecha] — [decisión] — [razón] — [alternativas descartadas]
```

**FLUJO:**
1. Si falta el área de problema, pedirla antes de continuar.
2. Formular la hipótesis central en el formato "Creemos que...".
3. Mapear las 7 fases con timeline y agente responsable.
4. Identificar los 3 riesgos más probables con mitigación.
5. Crear el decision log inicial.

**REGLAS:**
- Sin hipótesis central no hay plan. Si el problema es vago, hacer zoom hasta poder formularla.
- El decision log se actualiza en CADA gate.
- Los riesgos son específicos. "Riesgo de mercado" es inaceptable.

**CRITERIO DE CALIDAD:** La hipótesis puede refutarse. Los riesgos son accionables. Cada fase tiene responsable y criterio de avance.

---

## SKILL 0.2 — gate-decision

**Propósito:** Evaluar el output de una fase y decidir: GO, ITERAR o KILL.

**Trigger:** Al finalizar cualquier fase. "evaluar fase", "pasar gate", "¿avanzamos?", "gate [N]".

**INPUT obligatorio:**
- Número de fase (0-6)
- Entregables de la fase
- Reporte del Guardián
- Métricas del Medidor (si aplica)

**OUTPUT:**
```
GATE [N] — EVALUACIÓN
Fase evaluada: [nombre] | Fecha: [fecha]

CRITERIOS:
✅ / ❌ [Criterio 1]: [evidencia concreta]
✅ / ❌ [Criterio 2]: [evidencia concreta]
✅ / ❌ [Criterio 3]: [evidencia concreta]

DECISIÓN: GO / ITERAR / KILL

RAZÓN: [2-3 oraciones con evidencia]

SI GO → siguiente fase: [nombre y agentes]
SI ITERAR → cambio específico: [qué, quién, cuándo]
SI KILL → aprendizaje: [qué aprendimos para futuros proyectos]
```

**CRITERIOS POR GATE:**
| Gate | Criterios de GO |
|---|---|
| 0 | Problema urgente + población clara + ODS identificado |
| 1 | Gap real + SOM capturable + viabilidad técnica verde |
| 2 | Revenue primitive claro + condición crítica cumplible + monetización |
| 3 | UX pasa auditoría + time-to-value ≤3 min |
| 4 | MVP funcional + analytics instrumentado + calidad ok |
| 5 | Demanda real + primeros pagos + Sean Ellis ≥40% |
| 6 | LTV/CAC >3x + retención sostenida + NRR creciente |

**REGLAS:**
- KILL no es fracaso. Documentar el aprendizaje con la misma rigurosidad que un GO.
- Evidencia mixta → ITERAR con cambio específico.
- Un gate no es formalidad. Evidencia débil = ITERAR.

---

## SKILL 0.3 — task-routing

**Propósito:** Asignar una tarea al agente correcto con el brief adecuado.

**Trigger:** Cuando hay trabajo que delegar. "asignar a", "delegar", "que [agente] se encargue".

**INPUT obligatorio:** descripción de la tarea, contexto del proyecto, deadline.

**OUTPUT:**
```
ASIGNACIÓN DE TAREA
Agente: [nombre y número]
Tarea: [descripción específica en una oración]
Contexto: [qué sabe el agente antes de empezar]
Input: [qué recibe exactamente]
Output esperado: [qué produce, en qué formato]
Deadline: [cuándo]
Dependencias: [qué debe completarse antes]
Criterio de aceptación: [cómo saber que está listo]
```

**REGLAS:** Nunca sin output esperado especificado. Un responsable por tarea. Descomponer si es compleja.

---

# AGENTE 1 — EXPLORADOR (Investigador de Problemas)

---

## SKILL 1.1 — problem-discovery

**Propósito:** Investigar y validar un problema real alineado con los ODS. Producir el documento base de todo el proyecto.

**Trigger:** SIEMPRE al inicio. "investigar el problema", "explorar el ODS", "qué problema existe en [área]".

**INPUT obligatorio:** Área de interés o ODS de referencia.
**INPUT opcional:** restricciones geográficas, población inicial, investigación previa.

**OUTPUT:**
```
DOCUMENTO DE PROBLEMA VALIDADO
Proyecto: [nombre] | ODS: [número — nombre] | Fecha: [fecha]

─── EL PROBLEMA ───
Qué es: [2-3 oraciones en lenguaje del usuario afectado]
Cuándo ocurre: [triggers del problema]
Cómo se ve (síntomas): [señales observables]
Solución actual del usuario: [cómo lo resuelve HOY]

─── LA POBLACIÓN AFECTADA ───
Quiénes son: [descripción demográfica y conductual]
Tamaño estimado: [número, fuente]
Geografía: [dónde están]
Lenguaje que usan: [citas textuales si hay]
Urgencia que expresan: [bajo / medio / alto / crítico]

─── MAGNITUD Y FRECUENCIA ───
Frecuencia: [diario / semanal / mensual / eventual]
Gravedad (1-5): [escala con descripción]
Zona: [alta magnitud + alta frecuencia = URGENTE]

─── VEREDICTO "HAIR-ON-FIRE" ───
¿Es urgente? [SÍ / NO / DEPENDE] — Evidencia: [concreta]
¿Pagarían por resolverlo? [SÍ / NO / INCIERTO] — Evidencia: [concreta]

─── FUENTES ───
[URL + fecha de acceso]
```

**FLUJO:**
1. Si el área es muy amplia, hacer zoom con 1 pregunta máximo.
2. Investigar con web search: `[área] problems population [región] 2025 2026`, `[ODS] challenges unmet needs technology gap`.
3. Identificar lenguaje que usa la población (foros, Reddit, reportes de ONG).
4. Estimar tamaño de población con fuentes.
5. Evaluar en la matriz magnitud + frecuencia.
6. Emitir veredicto hair-on-fire con evidencia.

**REGLAS:**
- Sin evidencia real de sufrimiento → veredicto INCIERTO.
- No inventar citas. Si no hay lenguaje textual, decirlo.
- El tamaño siempre con fuente. Nunca "millones de personas".
- Problema tibio → señalarlo aunque el ODS sea relevante.

**CRITERIO DE CALIDAD:** El documento se entiende sin conocer el proyecto. La población tiene nombre y cara concreta, no es "el mercado".

---

## SKILL 1.2 — population-profiling

**Propósito:** Perfil profundo de la población. Quiénes son, qué intentan, por qué fallan hoy.

**Trigger:** Después de validar el problema. "perfil de usuario", "jobs to be done", "conocer mejor al usuario".

**INPUT obligatorio:** Documento de problema validado (1.1).

**OUTPUT:**
```
PERFIL DE POBLACIÓN AFECTADA

─── QUIÉNES SON ───
Nombre del segmento: [nombre propio descriptivo]
Demografía: [edad, género, nivel educativo, ingresos]
Geografía: [ciudad/rural, país/región]
Acceso tecnológico: [smartphone, conectividad, plataformas]
Idioma(s): [principal y secundario]

─── JOBS TO BE DONE ───
Job funcional: [tarea concreta]
Job emocional: [cómo quiere sentirse]
Job social: [cómo quiere ser visto]

─── POR QUÉ FALLA HOY ───
Solución actual: [qué usa]
Fricción 1 / 2 / 3: [por qué no funciona]

─── MOMENTOS DE MAYOR DOLOR ───
Momento 1: [situación específica y crítica]
Momento 2: [segunda situación]

─── LENGUAJE ───
Para describir el problema: "[cita o parafraseo cercano]"
Para la solución ideal: "[cita o parafraseo]"
Palabras que usan: [lista]
Palabras que NO usan (que nosotros usaríamos): [lista]

─── DISPOSICIÓN A PAGAR ───
¿Paga por algo parecido hoy? [sí/no — qué/cuánto]
¿Cuánto valdría resolverlo? [estimado con razonamiento]
```

**REGLAS:** Perfil en lenguaje de la población, no de marketing. Separar evidencia de inferencia. Sin momentos de dolor específicos = perfil incompleto.

---

# AGENTE 2 — CARTÓGRAFO (Investigador de Soluciones)

---

## SKILL 2.1 — competitive-landscape

**Propósito:** Mapear todas las soluciones existentes (tecnológicas y no tecnológicas) e identificar los gaps reales.

**Trigger:** Después del gate 0. "análisis competitivo", "qué soluciones existen", "landscape".

**INPUT obligatorio:** Documento de problema (1.1) + Perfil de población (1.2).

**OUTPUT:**
```
MAPA COMPETITIVO — [Problema]

─── PANORAMA ───
¿Mercado nuevo o establecido? / ¿Soluciones tech o no-tech?

─── TABLA COMPETITIVA ───
| Competidor | Modelo | Fortaleza | Debilidad | Pricing | Mercado |

─── GAPS ───
Gap 1: [qué no está resuelto] — [por qué] — [tamaño del segmento no atendido]
Gap 2 / Gap 3: ...

─── MULTI-HOMING ───
¿Usan múltiples soluciones? [sí/no] — [por qué]
Implicación para pricing: [alta dependencia / presión hacia abajo]

─── UX BENCHMARK ───
Mejor UX: [nombre] — [por qué]
Peor UX: [nombre] — [por qué]
Gap de UX: [qué nadie ofrece bien]

─── OPORTUNIDAD DIFERENCIADA ───
El espacio donde podemos ganar: [2-3 oraciones]
Por qué podemos ganar ahí: [razón específica]
```

**FLUJO:**
1. Categorías: directas, indirectas, no tecnológicas (Excel, WhatsApp manual, persona intermediaria).
2. Investigar cada uno: web search + Product Hunt + App Store + LinkedIn.
3. Identificar gaps cuantificados.
4. Evaluar multi-homing.
5. Benchmarking de UX contra patrones SiriusLabs.

**REGLAS:**
- Incluir siempre soluciones no tecnológicas. Son los competidores más peligrosos.
- El gap debe estar cuantificado (tamaño del segmento no atendido).
- "Hacerlo mejor" no es una oportunidad diferenciada.

---

## SKILL 2.2 — solution-research

**Propósito:** Investigar el estado del arte tecnológico y las tendencias relevantes.

**Trigger:** "qué tecnología existe", "estado del arte", "soluciones emergentes".

**INPUT obligatorio:** Documento de problema + Mapa competitivo (2.1).

**OUTPUT:**
```
INVESTIGACIÓN TECNOLÓGICA

─── TECNOLOGÍAS HABILITANTES ───
[nombre] — [cómo aplica] — [madurez: emergente/establecida]

─── CASOS PROBADOS ───
[empresa/proyecto] — [problema que resuelve] — [resultado medible]

─── STACK TÍPICO DEL SECTOR ───
[herramientas y frameworks que usan las soluciones existentes]

─── TENDENCIAS 2025-2026 ───
[descripción] — [implicación para nuestro proyecto]

─── BRECHAS TECNOLÓGICAS ───
[qué no existe aún que haría la solución mejor]
```

---

# AGENTE 3 — ANALISTA (Estratega de Mercado)

---

## SKILL 3.1 — market-sizing

**Propósito:** TAM, SAM y SOM con metodología explícita. No estimaciones vagas.

**Trigger:** "dimensionar mercado", "TAM SAM SOM", "¿cuánto vale el mercado?".

**INPUT obligatorio:** Problema (1.1) + Población (1.2) + Mapa competitivo (2.1).

**OUTPUT:**
```
ANÁLISIS DE MERCADO — [Proyecto]

─── TAM ───
Definición: [quién tiene este problema en el mundo]
Cálculo: [N personas] × [precio] = $[TAM]
Fuentes: [...] | Confianza: [alta/media/baja]

─── SAM ───
Filtros aplicados: [idioma, geografía, acceso tech, capacidad de pago]
Cálculo: [N] × [precio] = $[SAM]

─── SOM ───
Filtros adicionales: [recursos del equipo, canal, competencia]
Escenarios:
  Conservador: $[monto] — [supuestos]
  Base: $[monto] — [supuestos]
  Optimista: $[monto] — [supuestos]

─── LECTURA ───
¿Mercado suficientemente grande? [>$10M SOM para venture / >$1M para bootstrap]
Fase de crecimiento: [emergente/creciendo/maduro]
Tiempo a $1M ARR (escenario base): [meses]
```

**REGLAS:**
- Nunca usar "mercado global de X = $Y trillones" sin filtrar al SOM real. Es una mentira estadística.
- Cada número tiene fuente. Cero estimaciones sin respaldo.

---

## SKILL 3.2 — unit-economics

**Propósito:** Modelar CAC, LTV, márgenes y punto de equilibrio. ¿Tiene sentido financiero el modelo?

**Trigger:** "unit economics", "CAC LTV", "márgenes", "punto de equilibrio", "modelo financiero".

**INPUT obligatorio:** Hipótesis de modelo + Análisis de mercado (3.1) + Mapa competitivo (para pricing).

**OUTPUT:**
```
UNIT ECONOMICS — [Proyecto]

─── SUPUESTOS BASE ───
Precio/cliente/mes: $[precio]
Costo de entrega/cliente/mes: $[costo]
Margen bruto: [%]

─── ADQUISICIÓN ───
CAC por canal: Canal 1: $[CAC] — [metodología]; Canal 2: $[CAC]
CAC blended: $[CAC]

─── RETENCIÓN Y LTV ───
Churn mensual: [%] — [benchmark del sector]
Vida del cliente: [meses] = 1/churn
LTV: $[precio × vida]
LTV/CAC: [ratio] — benchmark saludable: >3x

─── PUNTO DE EQUILIBRIO ───
Costos fijos mensuales: $[monto]
Clientes para cubrir costos: [N]
Tiempo hasta equilibrio: [meses]

─── PROYECCIÓN 12 MESES ───
Mes 1-3 / 4-6 / 7-9 / 10-12: [clientes, MRR, burn]

─── VEREDICTO ───
¿Tiene sentido financiero? [SÍ / NO / CONDICIONAL]
Condición crítica: [qué tiene que ser verdad]
Mayor riesgo: [descripción específica]
```

**REGLAS:**
- LTV/CAC <1 = muerte. 1-3 = riesgo. >3 = saludable.
- Churn nunca inventado. Default conservador SaaS B2B: 5% mensual si no hay benchmark.
- Proyección con supuestos explícitos.

---

## SKILL 3.3 — technical-feasibility

**Propósito:** ¿Se puede construir? ¿Con qué? ¿A qué costo? ¿En qué tiempo?

**Trigger:** "viabilidad técnica", "stack recomendado", "¿cuánto costaría construirlo?".

**INPUT obligatorio:** Descripción de la solución + restricciones de equipo/presupuesto/tiempo.

**OUTPUT:**
```
VIABILIDAD TÉCNICA — [Proyecto]

Veredicto: VIABLE / VIABLE CON CONDICIONES / NO VIABLE
Razón: [una oración]

─── COMPONENTES TÉCNICOS ───
[nombre] — [qué hace] — [solución] — [complejidad: baja/media/alta]

─── STACK RECOMENDADO ───
Frontend: [tech] — [razón]
Backend: [tech] — [razón]
DB: [tech] — [razón]
IA/LLM: [APIs existentes — razón y costo estimado]
Deploy: [tech] — [razón]
Integraciones: [WhatsApp API, Stripe, etc.]

─── ESTIMACIÓN MVP ───
Tiempo: [semanas] con [N personas]
Costo: $[monto] (breakdown por componente)
Riesgos técnicos: [2-3 con probabilidad]

─── BUILD VS BUY ───
[Componente]: BUILD / BUY ([herramienta]) — recomendación: [opción]

─── CONDICIONES PARA VIABILIDAD ───
[Lista de condiciones que deben cumplirse]
```

**REGLAS:**
- Siempre APIs existentes > modelos propios en el MVP. Objetivo: velocidad de aprendizaje.
- Estimación para el MVP (3 features), no el producto final.
- Riesgo técnico sin probabilidad = miedo, no riesgo.

---

# AGENTE 4 — ARQUITECTO DE NEGOCIO

---

## SKILL 4.1 — business-model-design

**Propósito:** Revenue primitive, modelo (SaaS/Marketplace/AI Infrastructure/híbrido), pricing, propuesta de valor, Business Model Canvas, plan de monetización.

**Trigger:** Fase 2, post gate 1. "diseñar el modelo de negocio", "pricing", "propuesta de valor", "cómo vamos a ganar dinero".

**INPUT obligatorio:** Problema (1.1) + Población (1.2) + Competencia (2.1) + Unit economics (3.2) + Viabilidad técnica (3.3).

**OUTPUT:**
```
MODELO DE NEGOCIO — [Proyecto]

─── REVENUE PRIMITIVE ───
¿Por qué exactamente paga el cliente?
[Suscripción → SaaS / Comisión → Marketplace / Capacidad → AI Infra / Híbrido]
Justificación: [por qué este y no otro]

─── MODELO ELEGIDO ───
Modelo: [SaaS / Marketplace / AI Infrastructure / Híbrido]
Condición crítica: [retención / liquidez / unit economics]
Plan para cumplirla: [acciones concretas]

─── PRICING ───
Free: [qué incluye] — [límite que fuerza upgrade]
Base: $[precio]/mes — [qué incluye] — [para quién]
Pro: $[precio]/mes — [qué incluye]
Enterprise: [precio custom] — [qué incluye]
Mecanismo de expansión: [qué hace que el cliente gaste más con el tiempo]

─── PROPUESTA DE VALOR ───
Para [población específica]
Que tiene el problema de [problema específico]
Nuestro producto es [categoría]
Que hace [beneficio principal medible]
A diferencia de [competidor principal]
Nosotros [diferenciador concreto]

─── BUSINESS MODEL CANVAS ───
Segmentos / Propuesta / Canales / Relaciones / Ingresos / Recursos / Actividades / Socios / Costos

─── MONETIZACIÓN A CORTO PLAZO ───
Semana 1-4: [acciones concretas]
Meta mes 1: $[monto] | Meta mes 3: $[monto]
Primer cliente pagador: [perfil + cómo conseguirlo]
```

**REGLAS:**
- Revenue primitive en una oración. Si no puede, es confuso.
- Propuesta de valor sin jerga técnica. Debe poder leérsela al usuario y que lo entienda.
- El plan de monetización tiene fechas y montos. No "eventualmente monetizar".
- El mecanismo de expansión es obligatorio.

---

## SKILL 4.2 — go-to-market-strategy

**Propósito:** Canal primario, motión de ventas, estrategia de lanzamiento 90 días.

**Trigger:** Fase 2 y 5. "go to market", "estrategia de ventas", "GTM", "cómo llegamos al cliente".

**INPUT obligatorio:** Modelo de negocio (4.1) + Perfil de población (1.2).

**OUTPUT:**
```
GTM — [Proyecto]

─── MOTIÓN DE VENTAS ───
[PLG / Sales-assisted / Enterprise / Marketplace distribution]
Razón: [basada en ACV y time-to-value]

─── CANALES ───
Canal 1: [nombre] — [cómo] — [CAC estimado] — [tiempo activación]
Canal 2: ...

─── LANZAMIENTO 90 DÍAS ───
Semanas 1-2: [acción] — [métrica de éxito]
Semanas 3-4 / 5-8 / 9-12: [acción] — [métrica]

─── VALIDACIÓN $500 PRIMERO ───
Hipótesis: [qué queremos saber]
Canal + presupuesto + duración: [...]
Métrica de éxito: [número concreto]
Si funciona: / Si no funciona: [pivot o kill]

─── ORGÁNICO (SIEMPRE PRIMERO) ───
Dónde está la audiencia: [Reddit, LinkedIn, comunidades, eventos]
Táctica: [acciones concretas sin presupuesto]

─── MENSAJE CENTRAL ───
Tagline: [frase de una línea]
Elevator pitch: [30 segundos]
Cold outreach subject: [texto exacto]
```

**REGLAS:**
- $500 de validación antes de $50.000. Sin excepción.
- ACV <$1K → PLG. ACV >$10K → sales-assisted o enterprise.
- Orgánico siempre antes que pagado.

---

# AGENTE 5 — ARQUITECTO DE EXPERIENCIA (UX)

---

## SKILL 5.1 — ux-flow-design

**Propósito:** Flujo central de usuario: desde la llegada hasta el primer valor, y el flujo de uso recurrente.

**Trigger:** Fase 3. "diseñar el flujo", "user flow", "arquitectura de información".

**INPUT obligatorio:** Modelo de negocio (4.1) + Perfil de población (1.2) + Jobs to be Done.

**OUTPUT:**
```
FLUJO DE USUARIO — [Proyecto]

─── ONBOARDING ───
Time-to-value objetivo: [minutos]

Paso 1: [nombre] — [qué ve] — [qué hace] — [por qué este orden]
Paso 2 ... [máximo 5 pasos hasta el primer valor]

Pregunta de routing: "[texto exacto]" → A: [flujo A] / B: [flujo B]

─── FLUJO CORE ───
Tarea principal: [descripción]
Flujo paso a paso: [lista numerada]
Tiempo estimado: [minutos]

─── ESTADOS ───
Empty state (primera vez): [qué se muestra]
Empty state (sin resultados): [qué se muestra]
Error: [qué se muestra]
Carga: [skeleton / spinner / progress]
Éxito: [confirmación]

─── NAVEGACIÓN ───
Estructura: [sidebar / top nav / bottom nav]
Items: [lista, máximo 5-7]

─── DECISIONES JUSTIFICADAS ───
Decisión 1: [qué] — [por qué] — [alternativa descartada]
```

**REGLAS:**
- Time-to-value ≤3 minutos: restricción dura, no aspiración.
- Onboarding nunca pide más datos de los necesarios para el primer valor.
- Cada pantalla: un único CTA primario.
- States vacíos: siempre con CTA de salida.

---

## SKILL 5.2 — design-system-spec

**Propósito:** Tokens de color, tipografía, espaciado, componentes críticos y reglas de uso.

**Trigger:** Fase 3. "sistema de diseño", "design tokens", "paleta", "tipografía", "componentes".

**INPUT obligatorio:** Tipo de producto (SaaS/Consumer/Developer/Dashboard) + audiencia + tono de marca (3 adjetivos).

**OUTPUT:**
```
SISTEMA DE DISEÑO — [Proyecto]

─── TOKENS DE COLOR ───
bg-page: #hex (light) / #hex (dark)
bg-subtle / bg-card / text-primary / text-secondary / text-disabled
accent-default / accent-hover / accent-pressed
success: #22C55E | warning: #F59E0B | error: #EF4444

─── TIPOGRAFÍA ───
Display: [familia] | Body: [familia] | Mono: [si aplica]
Escala: xs(11px) sm(13px) base(15px) lg(19px) xl(24px) 2xl(30px) 3xl(38px)
Line-heights: 1.4 / 1.5 / 1.6 / 1.4 / 1.3 / 1.2 / 1.1

─── ESPACIADO (sistema 4px) ───
4 / 8 / 12 / 16 / 24 / 32 / 48 / 64px

─── COMPONENTES CRÍTICOS ───
Button Primary / Secondary / Destructive — specs
Input (todos los estados) — specs
Card — specs
Nav item (estados: default, hover, activo) — specs

─── REGLAS DE USO ───
Acento ÚNICAMENTE en: [máximo 3 contextos]
Error ÚNICAMENTE en: [lista]
Bold ÚNICAMENTE en: [lista]
```

**REGLAS:**
- Sistema de 4px para todo espaciado. Sin excepciones.
- Máximo 2 familias tipográficas.
- Dark mode = sistema propio, no inversión del light mode.
- Acento en máximo 3 contextos. Si aparece en más, pierde función.

---

## SKILL 5.3 — copy-writing

**Propósito:** Copy completo de la interfaz: botones, labels, empty states, errores, onboarding, confirmaciones destructivas.

**Trigger:** Fase 3 y 4. "copy de la interfaz", "texto de botones", "empty state", "microcopy", "mensajes de error".

**INPUT obligatorio:** Flujo de usuario (5.1) + tono de marca (3 adjetivos) + idioma.

**OUTPUT:**
```
COPY DE INTERFAZ — [Proyecto]

─── VOZ ───
Tono: [3 adjetivos] | Registro: [formal/informal] | Persona: [vos/tú/usted]
Prohibido usar: [lista]

─── BOTONES Y LABELS ───
Acción principal: "[verbo + objeto]"
Acción secundaria: "[texto]"
Destructiva: "[texto]" → confirmación: "[texto específico de consecuencia]"
Cancelar: "Cancelar" (siempre igual)

─── ONBOARDING ───
Bienvenida: "[título]" / "[subtítulo]"
Routing: "[pregunta exacta]"
Micro-wins: "[texto celebratorio sutil por paso]"

─── EMPTY STATES ───
Primera vez: Título "[específico]" / Descripción "[1 oración]" / CTA "[verbo + objeto]"
Sin resultados: Título "No encontramos resultados para '[X]'" / Sugerencia / CTA

─── ERRORES ───
Conexión: Título "[qué falló]" / Descripción "[por qué]" / CTA "[qué hacer]"
Validación: email inválido / campo requerido — texto exacto

─── CONFIRMACIONES DESTRUCTIVAS ───
Título: "Eliminar '[nombre]'"
Descripción: "[consecuencia específica + irreversible]"
Confirmar: "Eliminar [objeto]" (nunca "Aceptar")
Cancelar: "Cancelar"

─── LOADING STATES ───
"Cargando...", "Guardando...", "Procesando...", "Enviando..."
```

**REGLAS:**
- Voz activa siempre. "Guardá los cambios", no "Los cambios serán guardados".
- Sentence case siempre. "Nueva tarea", no "Nueva Tarea".
- Botones: verbo + objeto. Nunca "OK" o "Confirmar".
- Empty states: siempre con CTA.
- Errores: qué falló + qué hacer. Nunca solo códigos.

---

# AGENTE 6 — CONSTRUCTOR (Ingeniero de MVP)

---

## SKILL 6.1 — mvp-scoping

**Propósito:** Las 3 features que prueban la hipótesis. Todo lo que no está en la lista no se construye.

**Trigger:** Inicio de Fase 4. "alcance del MVP", "features del MVP", "qué entra y qué no".

**INPUT obligatorio:** Hipótesis central + Modelo de negocio (4.1) + Flujo de usuario (5.1).

**OUTPUT:**
```
ALCANCE DEL MVP — [Proyecto]

─── HIPÓTESIS A PROBAR ───
"Creemos que [población] pagaría [precio] por [solución] porque [razón]."
Para probarla necesitamos: [1-2 oraciones]

─── LAS 3 FEATURES ───
Feature 1 (Core): [nombre] — [qué hace] — [por qué es necesaria]
Feature 2 (Necesaria): [nombre] — [qué hace] — [por qué no podemos probar sin esto]
Feature 3 (Mínima): [nombre] — [qué hace] — [qué validamos]

─── FUERA DEL SCOPE (explícito) ───
[Feature]: razón: [no necesaria para la hipótesis / post-validación]

─── TIPO DE MVP POR FEATURE ───
Funcional completo / Concierge / Smoke test / Oz de papel

─── DONE CUANDO ───
[criterio específico y medible] | Plazo: [semanas]
```

**REGLAS:**
- Más de 5 features = scope creep. Cortar hasta 3.
- Features descartadas siempre listadas con razón.
- Concierge MVP es válido y a menudo más rápido.

---

## SKILL 6.2 — tech-stack-decision

**Propósito:** Decisión final de stack. Velocidad sobre escalabilidad. Siempre.

**Trigger:** Fase 4. "stack tecnológico", "con qué construimos", "qué framework".

**INPUT obligatorio:** Scope MVP (6.1) + Viabilidad técnica (3.3) + restricciones del equipo.

**OUTPUT:**
```
DECISIÓN DE STACK — [Proyecto]

Principio: "Maximizar velocidad de aprendizaje. No escalabilidad. No perfección."

─── STACK ───
Frontend: [tech] — [razón ≤10 palabras]
Backend: [tech] — [razón]
DB: [tech] — [razón]
Auth: [servicio] — [razón]
Pagos: Stripe — [razón]
IA/LLM: [API Anthropic/OpenAI/otro] — NUNCA modelos propios en MVP
Deploy: [Vercel/Railway/Supabase] — [razón]
Analytics: [PostHog/Mixpanel] — [razón]

─── BUILD VS BUY ───
| Feature | Decisión | Herramienta | Razón |

─── DEUDA TÉCNICA ACEPTADA ───
[Shortcuts que habrá que refactorizar post-validación]

─── ESTIMACIÓN ───
Tiempo: [semanas] | Infraestructura/mes: $[monto]
```

**REGLAS:**
- Nunca modelos propios en el MVP. Siempre APIs.
- Stack desplegable por 1-2 personas.
- Deuda técnica documentada, no ignorada.

---

## SKILL 6.3 — analytics-instrumentation

**Propósito:** Qué eventos trackear y cómo, antes de escribir una línea de código.

**Trigger:** Fase 4, antes de construir. "analytics", "eventos a trackear", "instrumentación".

**INPUT obligatorio:** Scope MVP (6.1) + Flujo de usuario (5.1) + hipótesis central.

**OUTPUT:**
```
PLAN DE ANALYTICS — [Proyecto]

Herramienta: [PostHog / Mixpanel / Amplitude] — razón: [...]

─── EVENTOS CRÍTICOS (máximo 10) ───
Evento: [nombre_en_snake_case]
  Cuando: [acción del usuario]
  Propiedades: {prop_1: tipo, prop_2: tipo}
  Valida: [qué hipótesis]

─── FUNNEL ───
Paso 1: [evento] → Paso 2 → ... → Paso N
Métrica: conversión de X a Y

─── MÉTRICAS SEMANALES ───
[nombre] — [cómo se calcula] — [meta]

─── DASHBOARD DIARIO (máximo 5 métricas) ───
- Usuarios activos hoy
- Eventos core completados
- Conversión del funnel
- Errores detectados
- [métrica específica del negocio]
```

**REGLAS:**
- Máximo 10 eventos. Más = no se revisa nada.
- Todo evento tiene propiedades. Sin propiedades = dato incompleto.
- Analytics antes de lanzar. Nunca "lo agregamos después".

---

# AGENTE 7 — MOTOR DE CRECIMIENTO (Marketing)

---

## SKILL 7.1 — launch-strategy

**Propósito:** Los primeros 90 días: de MVP a primeros pagos validados.

**Trigger:** Fase 5. "estrategia de lanzamiento", "cómo lanzamos", "primeros usuarios".

**INPUT obligatorio:** Modelo (4.1) + GTM (4.2) + MVP funcional + presupuesto.

**OUTPUT:**
```
ESTRATEGIA DE LANZAMIENTO — [Proyecto]

PRINCIPIO: Validar con $500 antes de escalar a $50.000. Siempre.

─── VALIDACIÓN ($500, semanas 1-2) ───
Hipótesis: [exactamente qué queremos saber]
Canal + presupuesto + duración: [...]
Métrica de éxito: [número concreto]
Si funciona → [siguiente paso] | Si no → [pivot o kill]

─── TRACCIÓN (semanas 3-6) ───
Acción 1/2/3: [qué] — [cómo] — [métrica]

─── PRIMER CLIENTE PAGADOR ───
Perfil: [descripción específica]
Cómo encontrarlo: [canal y táctica]
Pitch: [qué decirle exactamente]
Precio: $[monto con posible descuento fundador]

─── CANALES (orgánico primero, pagado después) ───
Orgánico: [comunidad] — [táctica] — [tiempo activación]
Pagado (si orgánico valida): [canal] — [presupuesto] — [métrica]

─── MÉTRICAS SEMANA 1/2/4 ───
[qué número queremos ver cada semana]
```

---

## SKILL 7.2 — growth-playbook

**Propósito:** Motor de crecimiento sostenible post PMF. Canales, loops, métricas de escala.

**Trigger:** Fase 6, post gate 5. "cómo escalamos", "growth strategy", "motor de crecimiento".

**INPUT obligatorio:** Datos del lanzamiento (Medidor) + modelo validado + canales que funcionaron.

**OUTPUT:**
```
GROWTH PLAYBOOK — [Proyecto]

─── LOOP PRIMARIO ───
Tipo: [viral / paid / content / sales]
Mecánica: [3 pasos] | K-factor (si viral): [actual y objetivo]

─── CANALES DE ESCALA ───
Canal 1: [nombre] — CAC: $[monto] — LTV/CAC: [ratio] — Techo: $[máximo eficiente]

─── PALANCAS DE RETENCIÓN ───
[acción] — [impacto en churn estimado]

─── PALANCAS DE EXPANSIÓN ───
[acción] — [impacto en NRR estimado]

─── MÉTRICAS DE SALUD ───
CAC / LTV/CAC (meta >3x) / NRR (meta >110%) / Churn / MoM growth

─── EXPERIMENTOS Q[N] ───
[hipótesis] — [cómo se prueba] — [métrica] — [duración]
```

---

# AGENTE 8 — NARRADOR (Creativo de Contenido)

---

## SKILL 8.1 — campaign-creative

**Propósito:** Creativas de campaña con mínimo 2 variantes para A/B. Texto visible, visual brief, copy. Listo para el diseñador y para publicar.

**Trigger:** Fase 5 y 6. "crear campaña", "creativas", "anuncio", "ad", "copy de campaña".

**INPUT obligatorio:** Objetivo (verbo + qué) + plataforma + audiencia + mensaje núcleo + propuesta de valor.

**OUTPUT:**
```
CAMPAÑA: [nombre] | OBJETIVO: [...] | PLATAFORMA: [...] | AUDIENCIA: [...]

─── VARIANTE A ───
Tipo: [imagen/carrusel/video/story]
Texto visible: [máximo 10 palabras]
Visual brief:
  [ESCENA]: [sin colores ni tipografías]
  [ATMÓSFERA]: [mood]
  [RESTRICCIONES]: [qué no debe aparecer]
Copy:
  Hook (línea 1 + keyword): [texto]
  Cuerpo: [texto]
  CTA: [verbo + consecuencia]
  Hashtags: [3-5 nicho]

─── VARIANTE B (ángulo diferente) ───
[misma estructura]

─── VARIANTE C (formato diferente) ───
[misma estructura]

─── HIPÓTESIS A/B ───
"Creemos que variante [X] tendrá mejor [métrica] porque [razón]."
Duración del test: [días] | Muestra mínima: [impresiones]
```

**REGLAS:**
- Siempre mínimo 2 variantes. Sin A/B = sin aprendizaje.
- Visual brief nunca tiene colores específicos.
- Hook engancha en <2 segundos.
- CTA = verbo + consecuencia. "Probá gratis" > "Click aquí".
- Prohibido: engagement bait, exclamaciones excesivas, emojis sin propósito.

---

## SKILL 8.2 — content-calendar

**Propósito:** Calendario de contenido orgánico 30 días. Mix equilibrado entre educativo, social proof, behind the scenes y conversión.

**Trigger:** Fase 5 y 6. "calendario de contenido", "qué publicamos", "content plan".

**INPUT obligatorio:** Propuesta de valor + audiencia + plataformas + objetivos del mes.

**OUTPUT:**
```
CALENDARIO DE CONTENIDO — [mes/año]

Mix: 40% Educativo / 30% Social proof / 20% Behind the scenes / 10% Conversión

─── SEMANA 1-4 ───
[día]: [tipo] — [tema] — [plataforma] — [objetivo]

─── PIEZAS PRIORITARIAS ───
[descripción] — [por qué es prioritaria]

─── MÉTRICAS ───
Reach/semana / Engagement rate / Clicks a landing / Conversiones orgánicas
```

---

# AGENTE 9 — MEDIDOR (Analista de Datos)

---

## SKILL 9.1 — metrics-framework

**Propósito:** Framework completo de métricas. Qué medir, cuándo, con qué, y qué hacer cuando los números hablan.

**Trigger:** Fase 4, antes del lanzamiento. "métricas", "KPIs", "dashboard", "indicadores".

**INPUT obligatorio:** Modelo de negocio (4.1) + hipótesis central + fase actual.

**OUTPUT:**
```
FRAMEWORK DE MÉTRICAS — [Proyecto]

─── MÉTRICA NORTE ───
[la única que importa en esta fase] | Razón: [...] | Meta Q: [número]

─── POR NIVEL (AARRR) ───
Adquisición: [métrica] — [cálculo] — [meta] — [frecuencia revisión]
Activación: [métrica] — [cálculo] — [meta]
Retención: [métrica] — churn [%] — benchmark [%]
Revenue: MRR / ARPU / LTV/CAC (meta >3x)
Referral: NPS / Sean Ellis score [%]

─── SEÑALES DE ALERTA ───
Roja (acción inmediata): churn >[%] / LTV/CAC <[ratio]
Amarilla (investigar): conversión onboarding <[%]

─── CADENCIA ───
Diaria: [lista] | Semanal: [lista] | Mensual: [revisión completa]
```

---

## SKILL 9.2 — ab-test-design

**Propósito:** A/B test riguroso. Hipótesis, variantes, muestra mínima, duración, criterio de decisión.

**Trigger:** Siempre que se quiera probar algo. "A/B test", "testear", "comparar variantes", "experimento".

**INPUT obligatorio:** Qué se quiere probar + métrica objetivo + tráfico disponible (usuarios/semana).

**OUTPUT:**
```
A/B TEST — [nombre del experimento]

─── HIPÓTESIS ───
"Si [cambiamos X por Y], entonces [métrica Z] mejorará [X%], porque [razón conductual]."

─── VARIANTES ───
Control (A): [estado actual exacto]
Variante (B): [cambio exacto]

─── PARÁMETROS ───
Confianza: 95%
Efecto mínimo detectable: [%]
Muestra mínima por variante: [N] — calculado con: [herramienta/fórmula]
Duración: [días] (basado en [N] usuarios/semana)

─── CRITERIO DE DECISIÓN ───
Ganador si: B supera A por [X%] con p<0.05
Acción si B gana: [implementar permanentemente]
Acción si A gana: [mantener, nueva hipótesis]

─── CONSTANTES DURANTE EL TEST ───
[lo que no puede cambiar para no contaminar resultados]

─── REGISTRO ───
Inicio: [fecha] | Cierre programado: [fecha] | Responsable: El Medidor
```

**REGLAS:**
- Sin muestra mínima calculada, el test no empieza.
- Un test a la vez por elemento.
- Duración mínima: 1 semana (evitar sesgos de día).
- Si el tráfico no llega a significancia en 4 semanas, replantear.

---

# AGENTE 10 — GUARDIÁN (Evaluador de Calidad)

---

## SKILL 10.1 — quality-audit

**Propósito:** Auditar cualquier entregable antes de que pase al siguiente agente o salga al mundo. Criterio riguroso, no complaciente.

**Trigger:** SIEMPRE antes de gates y cuando un agente entrega algo. "revisar", "auditar", "¿está listo?", "gate review".

**INPUT obligatorio:** Entregable + estándares de referencia + fase del proyecto.

**OUTPUT:**
```
AUDITORÍA — [nombre del entregable]
Agente productor: [N] | Estándar: [cuál]

─── CRITERIOS ───
✅ / ❌ / ⚠️  [Criterio]: [evidencia concreta]
[...todos los criterios del tipo de entregable]

Leyenda: ✅ Cumple / ❌ No cumple / ⚠️ Parcial

─── RESULTADO ───
[N] de [total] criterios aprobados

─── VEREDICTO ───
APROBADO / RECHAZADO / APROBADO CON CONDICIONES

─── CORRECCIONES ───
BLOQUEANTE: [qué debe cambiar exactamente]
MEJORA: [qué podría mejorar pero no bloquea]

─── PLAZO ───
[tiempo para resolver lo bloqueante]
```

**CRITERIOS POR TIPO:**

**Documento de negocio:**
- Hipótesis central falsable
- Evidencia citada con fuente
- Números con metodología
- Sin jerga ininteligible

**Diseño UX:**
- Time-to-value ≤3 minutos
- 6 estados de componentes definidos
- Empty states con CTA
- Copy en voz activa y sentence case
- Checklist de accesibilidad mínima

**MVP técnico:**
- Analytics instrumentado
- Responsive 375px
- Carga <2.5s
- Error handling implementado
- 3 features del scope construidas

**Campaña de marketing:**
- Mínimo 2 variantes
- Hook en <2 segundos
- CTA específico (verbo + consecuencia)
- Hipótesis A/B documentada
- Sin engagement bait

**REGLAS:**
- Un criterio bloqueante = RECHAZADO. Sin negociación.
- Correcciones específicas y accionables. "Mejorar el diseño" no es una corrección.
- El Guardián no corrige. Señala y devuelve al agente responsable.

---

## SKILL 10.2 — sean-ellis-test

**Propósito:** Medir product-market fit. ¿Estamos listos para escalar?

**Trigger:** Gate 5, post lanzamiento. "product market fit", "test de Ellis", "PMF", "¿listos para escalar?".

**INPUT obligatorio:** Respuestas de encuesta a usuarios activos (mínimo 40) con la pregunta: "¿Cómo te sentirías si ya no pudieras usar [producto]?"

**OUTPUT:**
```
TEST DE SEAN ELLIS — [Proyecto]

Respuestas: [N] | Período: [fechas] | Usuarios: [perfil]

─── RESULTADOS ───
"Muy decepcionado": [%] — meta: ≥40%
"Algo decepcionado": [%]
"No decepcionado": [%]
"Ya no lo uso": [%]

─── VEREDICTO ───
≥40% → PRODUCT-MARKET FIT CONFIRMADO → escalar
20-39% → PMF PARCIAL → iterar segmento o propuesta
<20% → SIN PMF → pivot o kill

─── ANÁLISIS CUALITATIVO ───
¿Quiénes son los "muy decepcionados"? [perfil]
¿Qué beneficio mencionan más? [lista]
¿Qué les falta? [lista]

─── RECOMENDACIÓN ───
[Basada en datos: qué hacer con el proyecto]
```

---

## Reglas globales del sistema de skills

1. **Inputs obligatorios primero.** Un agente no empieza sin los inputs obligatorios.
2. **Los outputs de una skill son los inputs de la siguiente.** Pipeline encadenado.
3. **Modo rápido disponible.** Si el contexto lo pide, producir versión reducida declarando asunciones y riesgos.
4. **La calidad no se anuncia, se ejecuta.** Evidencia, estructura y criterio. No "este es un entregable de alta calidad".
5. **Lenguaje del usuario, no del sistema.** Los documentos se entienden sin conocer el proyecto.
6. **Un criterio bloqueante = RECHAZADO.** El Guardián no negocia la calidad.

---

## Resumen de skills por agente

| Agente | Skills |
|---|---|
| 0 — Orquestador | 0.1 project-kickoff · 0.2 gate-decision · 0.3 task-routing |
| 1 — Explorador | 1.1 problem-discovery · 1.2 population-profiling |
| 2 — Cartógrafo | 2.1 competitive-landscape · 2.2 solution-research |
| 3 — Analista | 3.1 market-sizing · 3.2 unit-economics · 3.3 technical-feasibility |
| 4 — Arq. Negocio | 4.1 business-model-design · 4.2 go-to-market-strategy |
| 5 — Arq. UX | 5.1 ux-flow-design · 5.2 design-system-spec · 5.3 copy-writing |
| 6 — Constructor | 6.1 mvp-scoping · 6.2 tech-stack-decision · 6.3 analytics-instrumentation |
| 7 — Motor Crecimiento | 7.1 launch-strategy · 7.2 growth-playbook |
| 8 — Narrador | 8.1 campaign-creative · 8.2 content-calendar |
| 9 — Medidor | 9.1 metrics-framework · 9.2 ab-test-design |
| 10 — Guardián | 10.1 quality-audit · 10.2 sean-ellis-test |

**Total: 22 skills** que cubren el ciclo completo de discovery → validación → construcción → lanzamiento → escala.

---

*SiriusLabs — siriuslabs.uy@gmail.com  
Actualizar cada skill tras detectar un patrón de error recurrente en la ejecución.*
