# Subagentes del Medidor
### Equipo especializado para convertir datos en decisiones

> **Por qué el Medidor necesita subagentes:**
> El Agente 9 hace cuatro trabajos distintos: decidir qué medir (instrumentación), entender qué dicen los datos (análisis), probar qué funciona mejor (experimentación), y comunicar para que se actúe (reporting). El Medidor es el sistema nervioso del Venture Engine — sin él, todos los demás agentes operan a ciegas: el Motor no sabe qué canal funciona, el Narrador no sabe qué mensaje convierte, el Guardián no tiene datos para sus gates.

---

## Principio rector

Los datos no son la verdad — son evidencia. Una métrica sin contexto engaña, una de vanidad distrae, y una mal instrumentada miente. El trabajo del Medidor no es producir dashboards bonitos: es producir las pocas métricas que importan, medirlas bien, y traducirlas en decisiones.

**Regla del Medidor: medí lo que lleva a una decisión. Si un número no cambia ninguna acción, no lo midas. Vanity metrics afuera.**

---

## Los 4 Subagentes

```
┌──────────────────────────────────┐
│   AGENTE 9 — MEDIDOR            │
└─────────────────┬────────────────┘
                  │
   ┌──────────┬───┴────┬──────────┐
  9.A        9.B      9.C        9.D
Ingeniero  Analista  Diseñador  Comunicador
Instrumen- de        de         de Insights
tación     Producto  Experimentos (Reporting)
```

**Flujo:**
```
ANTES DEL LANZAMIENTO: 9.A Instrumentación (qué medir + verificar)
DURANTE: 9.B Análisis (funnels, cohortes) → 9.C Experimentos (A/B) → 9.D Reporting
→ alimenta a: Motor (7), Narrador (8), Guardián (10), Orquestador (0)
```

---

# SUBAGENTE 9.A — INGENIERO DE INSTRUMENTACIÓN

**Función:** Definir qué eventos se trackean, con qué propiedades, y verificar que funciona antes del lanzamiento. Si los datos no se capturan bien desde el día uno, ningún análisis posterior sirve.

**Por qué es necesario:** El error más costoso en analítica es descubrir 3 meses después que un evento crítico no se trackeaba. Los datos perdidos no se recuperan.

---

## SKILL 9.A.1 — tracking-plan

**Trigger:** Fase 4, antes de instrumentar el código. "plan de tracking", "qué eventos medir", "analytics setup".

**INPUT obligatorio:** Hipótesis central + flujo de usuario (5.1) + modelo de negocio (4.1) + momento de valor (7.D.1).

**OUTPUT:**
```
PLAN DE TRACKING — [Proyecto]
Herramienta: [PostHog / Mixpanel / Amplitude]

─── IDENTIFICACIÓN DE USUARIO ───
Cómo identificamos: [user_id / email hash]
User properties: plan_type, signup_date, source_channel, segment

─── EVENTOS CRÍTICOS (máximo 10-15) ───
Evento: [nombre_snake_case]
  Cuándo: [acción exacta del usuario]
  Propiedades: { prop_1: tipo, prop_2: tipo }
  Pregunta de negocio: [qué queremos saber]
  Prioridad: [crítica / importante]

Típicos: signup_started/completed, onboarding_step_completed, activation_reached,
core_action_performed, payment_completed, feature_used, churned

─── FUNNEL PRINCIPAL ───
Paso 1 [evento] → Paso 2 [evento] → ... → Paso N [conversión]

─── NOMENCLATURA ───
Eventos: snake_case, verbo en pasado ("payment_completed")
Consistencia: mismo concepto, mismo nombre siempre

─── VERIFICACIÓN ───
Proceso de QA de datos + quién valida antes del lanzamiento (9.A + Constructor 6.C)
```

**REGLAS:**
- Máximo 10-15 eventos críticos. "Medir todo" produce ruido, no señal.
- Cada evento conectado a una pregunta de negocio. Si no informa una decisión, no se trackea.
- Todo evento con propiedades para segmentar.
- Nomenclatura consistente desde el día uno (cambiarla después rompe el histórico).
- Verificar antes del lanzamiento. "Lo revisamos después" = datos perdidos.

---

## SKILL 9.A.2 — data-quality-audit

**Trigger:** Después del lanzamiento y periódicamente. "verificar datos", "los números no cuadran", "data quality".

**OUTPUT:**
```
AUDITORÍA DE CALIDAD DE DATOS — [Proyecto]

─── VERIFICACIÓN DE EVENTOS ───
| Evento | ¿Se dispara? | Volumen esperado | Real | Estado |
[para cada evento crítico]

─── PROBLEMAS ───
Evento que no se dispara: [nombre] — causa — reportar a Constructor 6.B
Propiedad faltante / duplicados / discrepancia entre fuentes

─── CONFIABILIDAD ───
¿Confiables para decisiones? [sí/no/con reservas]
Métricas confiables: [lista] | A usar con cuidado: [lista + razón]

─── ACCIONES ───
[correcciones con responsable]
```

**REGLAS:** Auditar datos antes de confiar en ellos para una decisión importante. Discrepancias entre fuentes se investigan, no se ignoran.

---

# SUBAGENTE 9.B — ANALISTA DE PRODUCTO

**Función:** Analizar el comportamiento de usuarios. Funnels, cohortes, retención, segmentación. ¿Qué hacen realmente los usuarios y por qué?

**Por qué es necesario:** Tener datos no es entenderlos. El Analista convierte eventos crudos en insights: dónde se caen los usuarios, qué comportamiento predice retención, qué segmento es más valioso.

---

## SKILL 9.B.1 — funnel-and-cohort-analysis

**Trigger:** "análisis de funnel", "dónde se caen los usuarios", "cohortes", "análisis de retención", "por qué se van".

**INPUT obligatorio:** Datos verificados (9.A.2) + funnel principal (9.A.1) + métrica de activación.

**OUTPUT:**
```
ANÁLISIS DE FUNNEL Y COHORTES — [Proyecto]
Período: [rango] | Usuarios: [N]

─── FUNNEL ───
| Paso | Evento | Usuarios | % del anterior | Drop-off |
| 1 | signup_started | [N] | 100% | — |
| 2 | signup_completed | [N] | [%] | [%] ← |
| 3 | activation_reached | [N] | [%] | [%] |
| 4 | payment_completed | [N] | [%] | [%] |

Mayor caída: [paso X→Y] — [%] | Hipótesis: [por qué]
Recomendación: [a Arquitecto UX 5 / Motor 7 — qué investigar]

─── COHORTES (retención) ───
| Cohorte | Sem 0 | Sem 1 | Sem 2 | Sem 4 | Sem 8 |
| [fecha] | 100% | [%] | [%] | [%] | [%] |

Curva: [se estabiliza / decae continuamente]
Punto de estabilización: [cuándo se aplana — usuarios que encontraron valor real]
Si no se estabiliza: señal de falta de PMF

─── INSIGHT DE RETENCIÓN ───
"Usuarios que [acción X] en los primeros [N días] retienen [Y]% vs [Z]%."
→ Implicación: [qué hacer — al Especialista en Activación 7.D]

─── SEGMENTACIÓN ───
Más valioso: [cuál] — [mayor LTV / mejor retención]
Menor valor: [cuál] — [despriorizar o ajustar]

─── ACCIONES ───
[acción específica] → [agente]
```

**REGLAS:**
- Siempre identificar el mayor punto de caída — mayor oportunidad de mejora.
- Retención por cohortes, no promedio (el promedio esconde si mejora o empeora).
- El insight conecta un comportamiento con quedarse — eso es lo accionable.
- Curva que no se estabiliza = señal más importante de falta de PMF.

---

# SUBAGENTE 9.C — DISEÑADOR DE EXPERIMENTOS

**Función:** A/B tests rigurosos. Hipótesis falsable, muestra mínima calculada, significancia estadística, criterio definido antes de empezar.

**Por qué es necesario:** Sin rigor experimental, el equipo confunde ruido con señal. El Diseñador aporta la disciplina: no declarar ganador sin significancia, no correr tests con muestra insuficiente, no cambiar reglas a mitad.

---

## SKILL 9.C.1 — experiment-design

**Trigger:** "A/B test", "experimento", "probar una hipótesis", "comparar variantes".

**INPUT obligatorio:** Qué probar + métrica a impactar + tráfico disponible (usuarios/semana).

**OUTPUT:**
```
DISEÑO DE EXPERIMENTO — [nombre]

─── HIPÓTESIS ───
"Si [cambiamos X por Y], [métrica Z] mejorará [%], porque [razón conductual]."
Falsable: [sí]

─── VARIANTES ───
Control (A): [estado actual exacto]
Variante (B): [el cambio — UN solo cambio]

─── PARÁMETROS (antes de empezar) ───
Métrica primaria: [la única que decide]
Métricas secundarias (monitoreo): [otras a observar]
Baseline: [valor actual]
MDE (efecto mínimo detectable): [%]
Confianza: 95% (p<0.05) | Poder: 80%
Muestra mínima/variante: [N] — calculada con: [calculadora/fórmula]
Duración: [días] = muestra / tráfico semanal

─── CRITERIO DE DECISIÓN (antes de ver resultados) ───
B gana si: supera A con p<0.05 Y efecto ≥ MDE
Sin diferencia → mantener A
Acción si B gana: [implementar permanente]

─── CONTROL DE CALIDAD ───
Qué NO cambiar: [todo lo demás constante]
Asignación: aleatoria, consistente por usuario

─── REGISTRO ───
Inicio: [fecha] | Cierre: [no antes de muestra mínima]
```

**REGLAS:**
- Sin muestra mínima calculada, no empieza. n=50 no demuestra nada.
- Un experimento prueba UN cambio.
- Criterio de decisión definido antes de ver resultados (decidir después es p-hacking).
- Duración mínima 1 semana; nunca cortar antes de la muestra aunque "ya se vea el ganador".
- Tráfico insuficiente para significancia en 4 semanas → experimento inviable.

---

## SKILL 9.C.2 — experiment-analysis

**Trigger:** Cuando termina un experimento. "resultado del A/B test", "¿quién ganó?", "¿es significativo?".

**OUTPUT:**
```
ANÁLISIS DE EXPERIMENTO — [nombre]
Muestra alcanzada: [N por variante]

─── RESULTADOS ───
| Variante | Muestra | Métrica primaria | Dif vs control | p-value |
| A | [N] | [valor] | — | — |
| B | [N] | [valor] | [+/-%] | [p] |

¿Muestra mínima alcanzada? [sí/no]
¿Significativo? [sí p<0.05 / no] | ¿Supera MDE? [sí/no]

─── VEREDICTO ───
GANADOR: [A / B / sin diferencia significativa]

─── MÉTRICAS SECUNDARIAS ───
[¿Efectos inesperados? — ej: B mejoró conversión pero subió churn]

─── INTERPRETACIÓN Y RECOMENDACIÓN ───
Qué aprendimos: [el insight más allá del número]
Acción: [implementar B / mantener A / iterar]
Próximo experimento: [qué probar después]
```

**REGLAS:**
- No declarar ganador sin significancia estadística.
- Revisar siempre métricas secundarias (mejora en conversión que sube churn no es mejora).
- Experimento sin ganador igual produce aprendizaje.

---

# SUBAGENTE 9.D — COMUNICADOR DE INSIGHTS

**Función:** Traducir datos en reportes y dashboards que mueven decisiones. Cada agente necesita información distinta — entregar a cada uno lo que necesita en el formato que le permite actuar.

**Por qué es necesario:** Un insight que no se comunica bien es un insight desperdiciado. El mejor análisis es inútil si el equipo no sabe qué hacer con él.

---

## SKILL 9.D.1 — dashboard-design

**Trigger:** "dashboard", "panel de métricas", "qué mostramos".

**INPUT obligatorio:** Framework de métricas (9.1) + métricas confiables (9.A.2) + audiencia.

**OUTPUT:**
```
DISEÑO DE DASHBOARD — [Proyecto]

─── DIARIO (operativo — máximo 5 métricas) ───
Para: [quién lo revisa cada día]
[métrica] — [visualización: número grande / tendencia]
Regla: si no cambia una acción diaria, no va acá.

─── SEMANAL (tendencias) ───
Funnel completo con tendencia semana a semana
Retención por cohorte (últimas 8)
CAC y LTV/CAC por canal
Experimentos en curso

─── MENSUAL (salud del negocio) ───
Para: Orquestador + gate 6
MRR/ARR y crecimiento MoM | NRR y churn | Unit economics | Progreso vs metas

─── PRINCIPIOS ───
Cada gráfico responde una pregunta | Tendencia > snapshot
Contexto siempre (meta/benchmark/período anterior) | Color con significado
```

**REGLAS:**
- Diario máximo 5 métricas (sobrecarga = nadie revisa).
- Cada métrica con tendencia, no solo valor actual.
- Si no informa una decisión en ese nivel, no va en ese dashboard.

---

## SKILL 9.D.2 — insight-report

**Trigger:** Cuando hay un hallazgo que comunicar. "reporte", "insights", "qué dicen los datos".

**INPUT obligatorio:** Análisis (9.B.1) y/o experimentos (9.C.2) + audiencia.

**OUTPUT:**
```
REPORTE DE INSIGHTS — [tema] — [fecha]
Para: [agente que debe actuar]

─── EL HALLAZGO (una oración) ───
"[insight principal, sin jerga, accionable]"

─── LA EVIDENCIA ───
[datos que lo sostienen — concisos]
Confianza: [alto/medio/bajo según calidad de datos]

─── POR QUÉ IMPORTA ───
[impacto en el negocio — conectado a una métrica]

─── LA RECOMENDACIÓN ───
Acción: [qué hacer] | Responsable: [qué agente]
Impacto esperado: [métrica y cuánto] | Esfuerzo: [alto/medio/bajo]

─── PRIORIDAD ───
[crítica/alta/media — impacto × facilidad]
```

**REGLAS:**
- El hallazgo en una oración, sin jerga estadística.
- Cada reporte termina en recomendación accionable dirigida a un agente.
- Nivel de confianza explícito (no presentar muestra pequeña con certeza de dato robusto).
- Recomendación con impacto esperado y esfuerzo, para priorizar.

---

## Definition of Done — Medidor

```
DEFINITION OF DONE — MEDIDOR

─── INSTRUMENTACIÓN (9.A) ───
□ Plan de tracking con máximo 10-15 eventos críticos
□ Cada evento conectado a una pregunta de negocio
□ Propiedades que permiten segmentar
□ Nomenclatura consistente
□ Funnel principal medible end-to-end
□ Instrumentación verificada antes del lanzamiento

─── ANÁLISIS (9.B) ───
□ Funnel con el mayor punto de caída identificado
□ Retención por cohortes (no promedio)
□ Al menos un insight comportamiento → retención
□ Segmentación que identifica el segmento más valioso
□ Recomendaciones dirigidas a agentes específicos

─── EXPERIMENTACIÓN (9.C) ───
□ Muestra mínima calculada antes de empezar
□ Hipótesis falsable, un solo cambio por test
□ Criterio de decisión definido antes de ver resultados
□ Significancia verificada antes de declarar ganador
□ Métricas secundarias revisadas

─── COMUNICACIÓN (9.D) ───
□ Dashboard diario con máximo 5 métricas accionables
□ Dashboards semanal y mensual con tendencias y contexto
□ Reportes con hallazgo en una oración
□ Cada reporte termina en recomendación dirigida
□ Nivel de confianza explícito

─── INTEGRACIÓN ───
□ Alimenta al Motor (7): qué canal/campaña funciona
□ Alimenta al Narrador (8): qué mensaje convierte
□ Alimenta al Guardián (10): datos para los gates
□ Alimenta al Orquestador (0): salud general
□ Provee Sean Ellis al Gate 5 y métricas de escala al Gate 6
```

---

## Cuándo agregar subagentes adicionales

| Situación | Subagente adicional |
|---|---|
| Datos complejos con modelos predictivos | Data Scientist / ML Analyst |
| Atribución multi-touch sofisticada | Especialista en Atribución |
| Revenue analytics complejo | Analista Financiero de Producto |
| Volumen que requiere pipelines | Data Engineer |
| Research cualitativo además de cuantitativo | Investigador de Usuarios (qualitative) |

---

*SiriusLabs — siriuslabs.uy@gmail.com
El Medidor es el sistema nervioso del Venture Engine. Convierte la actividad en aprendizaje. Sin él, todos operan a ciegas.*
