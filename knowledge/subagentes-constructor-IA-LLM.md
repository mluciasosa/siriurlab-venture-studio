# Subagente de IA/LLM del Constructor (6.F)
### Complemento técnico de `subagentes-constructor-mvp.md` — la capa de IA del MVP

> **Por qué existe:**
> El Constructor (Agente 6) tiene 5 subagentes (6.A a 6.E) que cubren arquitectura, desarrollo, testing, seguridad y documentación de software determinista. Pero cuando el MVP incluye una feature de IA/LLM, hay una capa entera que cae en tierra de nadie: el prompt del sistema, qué entra en la ventana de contexto, cómo se evalúa que el modelo responda bien, cuánto cuesta cada llamada en producción, qué pasa cuando el modelo falla, y cómo se defiende de prompt injection. 6.B no la cubre (no es código determinista), 6.C no la cubre (un test unitario no mide si una respuesta del modelo es buena), 6.D la cubre a medias (OWASP app, no OWASP LLM). 6.F es ese subagente.

> **Relación con el Constructor:** 6.F **extiende** a `subagentes-constructor-mvp.md`. No reemplaza nada. Solo se activa cuando el MVP tiene al menos una feature que llama a un modelo de lenguaje. Si el MVP no tiene IA, 6.F no corre.

---

## Principio rector

Una feature de IA no es código que funciona o no funciona — es un sistema probabilístico que funciona *la mayoría de las veces* y hay que medir cuánto. La calidad no viene del modelo elegido. Viene de tres cosas: un prompt especificado como contrato, una batería de evals que define "bueno" de forma medible **antes** de escribir el prompt, y controles de costo y fallback que asumen que el modelo va a fallar en producción.

**Evals primero → Prompt como contrato → Costos y fallbacks asumiendo que el modelo falla.**

Esto es el espejo exacto del principio del Constructor (spec → tests antes del código → gates). Los evals son a 6.F lo que el test plan (6.C.1) es a 6.B: bloqueantes, escritos antes, no negociables.

---

## Dónde encaja 6.F en el Constructor

```
┌──────────────────────────────────────┐
│        AGENTE 6 — CONSTRUCTOR         │
│          (orquesta a los 6)           │
└───────────────────┬──────────────────┘
                    │
  ┌────────┬────────┼────────┬────────┬────────┐
  │        │        │        │        │        │
 6.A      6.B      6.C      6.D      6.E      6.F
Arq.    Dev.Core  QA/Test  Security  Docs    IA/LLM
Técnica          DevSecOps Tech    (solo si
                                   hay IA)
```

**Flujo obligatorio cuando el MVP tiene IA** (se inserta en el flujo del Constructor):

```
SPEC → ARQUITECTURA (6.A) →
  ├── [rama software]   TEST PLAN (6.C) → DESARROLLO (6.B) → REVIEW (6.D+6.C) → DOCS (6.E)
  └── [rama IA]         6.F.1 modelo → 6.F.3 EVALS (bloqueante) → 6.F.2 prompt+contexto
                        → correr evals → 6.F.4 security LLM (bloqueante) → 6.F.5 costos+fallbacks
  → GATE 4
```

Las dos ramas convergen en el Gate 4. La rama de IA se escribe en paralelo a la de software, pero su orden interno es estricto: **no se diseña el prompt (6.F.2) hasta que existe la batería de evals (6.F.3)**, igual que no se escribe código (6.B) hasta que existe el test plan (6.C.1).

**Límites con otros subagentes (sin solapamiento):**
- **6.C** testea el código que rodea la llamada al modelo (parsing de la respuesta, manejo de errores, contratos). **6.F.3** evalúa la *calidad de la respuesta del modelo*. Son cosas distintas y ambas corren.
- **6.D** hace el OWASP Top 10 de la aplicación. **6.F.4** hace el OWASP Top 10 **para LLM** (prompt injection, fuga de datos, output handling). 6.F.4 le pasa a 6.D cualquier hallazgo que toque infra.
- **6.A** decide la arquitectura del sistema. **6.F.1** decide qué modelo va en cada tarea dentro de esa arquitectura.

---

# SUBAGENTE 6.F — ESPECIALISTA IA/LLM

**Función:** Diseñar, evaluar, asegurar y operar la capa de modelos de lenguaje del MVP. Produce la matriz de selección de modelo, el prompt del sistema como contrato, la batería de evals, la revisión de seguridad LLM y los controles de costo y fallback de producción.

**Por qué es necesario:** En 2026 casi todo MVP tiene al menos una feature de IA. Tratarla como "código que llama a una API" produce productos que funcionan en la demo y se rompen en producción: respuestas inconsistentes sin forma de medirlas, costos de tokens que se comen el margen, y vectores de prompt injection que ningún OWASP de aplicación detecta. 6.F convierte esa capa difusa en artefactos especificados y medibles.

---

## SKILL 6.F.1 — model-selection-and-routing

**Propósito:** Decidir qué modelo se usa en cada tarea de IA del MVP, con el tradeoff explícito entre capacidad, costo y latencia. Una sola tarea casi nunca necesita el modelo más caro; rutear bien es la primera palanca de costo.

**Trigger:** Inicio de la rama IA, después de la arquitectura (6.A.1). "qué modelo usamos", "selección de modelo", "routing de modelos".

**INPUT obligatorio:** Architecture Design (6.A.1) + lista de tareas de IA del MVP (qué hace cada llamada al modelo) + restricciones no funcionales (latencia tolerable, sensibilidad de datos) + precio objetivo del producto (para el techo de costo IA).

**INPUT opcional:** Benchmarks públicos relevantes a la tarea, restricciones de residencia de datos / compliance.

**OUTPUT:**
```
MODEL SELECTION & ROUTING — [Proyecto]

─── INVENTARIO DE TAREAS DE IA ───
Tarea [nombre]:
  Qué hace: [en una oración]
  Criticidad: [crítica / estándar / best-effort]
  Volumen estimado: [llamadas/día]
  Latencia tolerable: [ms o "asíncrona"]
  Sensibilidad de datos: [baja / media / alta]

─── MATRIZ DE RUTEO ───
| Tarea | Tier requerido | Modelo primario | Modelo fallback | Razón |
| [n]   | [razonamiento alto / medio / extracción simple] | [modelo] | [modelo más barato o más estable] | [por qué ese tier] |

─── DIMENSIONES DE DECISIÓN (por tarea) ───
Capacidad mínima: [qué tiene que poder hacer — razonamiento multi-paso, function calling, visión, ventana larga]
Costo por llamada estimado: [input tokens × precio + output tokens × precio]
Latencia p95 objetivo: [ms]
Por qué NO el modelo más caro: [justificación explícita del downgrade]

─── PRESUPUESTO DE COSTO IA ───
Precio del producto: [$X/mes por usuario o por unidad]
Techo de costo IA: [30% de $X = $Y] (umbral del sistema)
Costo IA proyectado por usuario activo: [$Z]
Margen contra el techo: [$Y - $Z] [✅ si Z < Y / ❌ si lo supera]

─── ADR DE MODELO ───
ADR-LLM-001: [decisión de modelo para tarea crítica]
  Contexto / Decisión / Consecuencias / Alternativas descartadas (con razón)

─── CONTRATO DE ABSTRACCIÓN ───
Interfaz única de invocación: [el código nunca llama al SDK del proveedor directo]
  → permite cambiar de modelo sin tocar la lógica de negocio
```

**FLUJO:**
1. Listar cada tarea de IA del MVP por separado (una llamada al modelo = una tarea).
2. Clasificar cada tarea por capacidad mínima real (no por "más es mejor").
3. Asignar el modelo más barato/rápido que cumpla la capacidad mínima. Documentar por qué NO se usa uno más caro.
4. Asignar un fallback por tarea (modelo más estable o más barato, ver 6.F.5).
5. Estimar costo por llamada y proyectar costo por usuario activo.
6. Validar contra el techo de costo IA (<30% del precio). Si lo supera → volver a 3 y bajar de tier o rediseñar la tarea.
7. Definir el contrato de abstracción para que el modelo sea reemplazable sin tocar negocio.

**REGLAS:**
- El modelo más caro nunca es el default. Cada uso de un tier alto se justifica por escrito.
- Toda tarea de IA tiene modelo primario **y** fallback. Sin fallback no pasa.
- El código nunca llama al SDK del proveedor directamente: siempre detrás de una interfaz propia (un cambio de modelo no debe tocar la lógica de negocio).
- No se hardcodea el nombre del modelo en la lógica: vive en configuración.
- Si el costo IA proyectado supera el 30% del precio, la selección está RECHAZADA hasta rediseñarla.

**CRITERIO DE CALIDAD (medible):** 100% de las tareas de IA tienen tier justificado, modelo primario, fallback y costo estimado. Costo IA proyectado por usuario < 30% del precio del producto. 0 llamadas al SDK del proveedor fuera de la capa de abstracción.

---

## SKILL 6.F.2 — system-prompt-and-context-design

**Propósito:** Escribir el prompt del sistema como un contrato y definir qué entra en la ventana de contexto, en qué orden y con qué presupuesto de tokens. El prompt es la spec de la feature de IA — la ambigüedad acá produce outputs inconsistentes que ningún modelo arregla.

**Trigger:** Después de que existe la batería de evals (6.F.3). "diseñar el prompt", "system prompt", "armar el contexto". **No arranca sin 6.F.3.**

**INPUT obligatorio:** Matriz de ruteo (6.F.1) + batería de evals (6.F.3 — OBLIGATORIO, sin evals no hay prompt) + flujo de usuario (5.1) + contratos de datos disponibles para el contexto.

**INPUT opcional:** Ejemplos few-shot curados, tono/voz del producto (Agente 8 si existe).

**OUTPUT:**
```
SYSTEM PROMPT & CONTEXT DESIGN — [Tarea de IA]

─── PROMPT DEL SISTEMA (contrato) ───
Rol / objetivo: [qué es el modelo en esta tarea, en una oración]
Tarea exacta: [qué produce, con qué formato]
Reglas no negociables: [lista — qué nunca debe hacer]
Formato de salida: [estructura exacta — JSON schema si es estructurado]
Manejo de incertidumbre: [qué dice cuando no sabe — nunca inventar]

─── ENSAMBLADO DE CONTEXTO ───
Presupuesto total de ventana: [N tokens]
| Sección | Fuente | Presupuesto tokens | Prioridad | Si excede → |
| sistema | fijo | [n] | 1 (nunca se trunca) | — |
| datos de usuario | [fuente] | [n] | 2 | resumir |
| historial | [fuente] | [n] | 3 | truncar más viejo primero |
| few-shot | curado | [n] | 4 | quitar ejemplos |

─── ESTRATEGIA DE TRUNCADO / RESUMEN ───
Orden de degradación: [qué se sacrifica primero cuando no entra]
Resumen de historial: [cuándo se resume, con qué modelo, cada cuántos turnos]
Guardarraíl de tokens: [hard cap por request — nunca enviar más de N]

─── SALIDA ESTRUCTURADA ───
Schema esperado: [JSON schema o formato]
Validación de salida: [qué se valida antes de confiar en la respuesta]
Qué pasa si el modelo no respeta el formato: [reintento / fallback — ver 6.F.5]

─── VERSIONADO DE PROMPT ───
Prompt-id: [nombre]@[versión]
Cambios desde la versión anterior: [qué y por qué]
Evals que tiene que pasar antes de promover: [link a 6.F.3]
```

**FLUJO:**
1. Leer la batería de evals (6.F.3). Si no existe → NO empezar.
2. Escribir el prompt del sistema como contrato: rol, tarea, reglas, formato, manejo de incertidumbre.
3. Definir el presupuesto de tokens de la ventana y repartirlo por sección con prioridad.
4. Definir la estrategia de truncado/resumen para cuando el contexto excede el presupuesto.
5. Definir el schema de salida y la validación post-respuesta.
6. Versionar el prompt (`prompt-id@versión`).
7. Correr la batería de evals contra este prompt. Si no pasa el umbral → iterar el prompt (nunca relajar los evals).

**REGLAS:**
- El prompt es un contrato versionado, no texto suelto. Vive en el repo con `prompt-id@versión`.
- La sección "sistema" nunca se trunca. La degradación siempre empieza por lo de menor prioridad.
- Todo request tiene un hard cap de tokens. Enviar la ventana entera "por las dudas" es la fuga de costo número uno.
- Salida estructurada siempre validada antes de confiar en ella. Una respuesta del modelo es input no confiable hasta que pasa validación.
- Un prompt nuevo no se promueve a producción hasta que pasa los evals de 6.F.3. El prompt se itera, los evals no se relajan.

**CRITERIO DE CALIDAD (medible):** El prompt pasa el umbral de la batería de evals (6.F.3) antes de promover. 100% de los requests respetan el hard cap de tokens. 100% de las salidas estructuradas se validan contra schema antes de uso. Prompt versionado en repo.

---

## SKILL 6.F.3 — llm-evaluation-harness

**Propósito:** Definir qué es una "buena respuesta" de forma medible, **antes** de escribir el prompt. Es el espejo del test plan (6.C.1): bloqueante, escrito primero, no negociable. Sin esto, "mejorar el prompt" es opinión.

**Trigger:** Después de seleccionar el modelo (6.F.1), **antes** de diseñar el prompt (6.F.2). "evals", "cómo medimos si responde bien", "golden set".

**INPUT obligatorio:** Inventario de tareas de IA (6.F.1) + flujo de usuario (5.1) + criterios de éxito de cada tarea (qué tiene que lograr la respuesta).

**INPUT opcional:** Casos reales de uso esperado, casos de fallo conocidos del dominio.

**OUTPUT:**
```
LLM EVALUATION HARNESS — [Tarea de IA]
Estado: BLOQUEANTE para diseñar el prompt (6.F.2)

─── GOLDEN DATASET ───
Total de casos: [N] (mínimo 20 por tarea en MVP)
| ID | Input | Output esperado / criterio de aceptación | Categoría |
| g01 | [input exacto] | [qué hace correcta a la respuesta] | happy path |
| g02 | [input borde] | [criterio] | edge case |
| g03 | [input adversarial] | [debe rechazar / no filtrar] | seguridad |

─── MÉTRICAS POR TAREA ───
Tipo de eval: [exact-match / schema-valid / LLM-as-judge con rúbrica / asserts programáticos]
Métrica primaria: [pass rate / exactitud / groundedness]
Umbral de aprobación: [≥ X% en el golden set total]
Casos críticos (safety / formato / no-alucinación): umbral 100%

─── RÚBRICA (si usa LLM-as-judge) ───
Criterio 1: [definición binaria — cumple/no cumple]
Criterio 2: [definición binaria]
Modelo juez: [cuál, distinto del evaluado si es posible]
Anti-sesgo: [cómo se evita que el juez premie su propio estilo]

─── EDGE / ADVERSARIAL OBLIGATORIOS ───
□ Input vacío / ambiguo
□ Input fuera de dominio (¿rechaza o alucina?)
□ Intento de prompt injection (entra a 6.F.4)
□ Pedido de información que no debe dar
□ Input en otro idioma / con caracteres especiales
□ Caso donde la respuesta correcta es "no sé"

─── GATE DE REGRESIÓN ───
Cada cambio de prompt o de modelo re-corre el harness completo.
Promoción a producción: solo si pass rate ≥ umbral y críticos = 100%.

─── CRITERIO DE DONE ───
□ ≥20 casos por tarea, con happy/edge/adversarial
□ Umbral de aprobación definido y medible
□ Casos críticos identificados con umbral 100%
□ Harness ejecutable de forma automática (no manual)
```

**FLUJO:**
1. Por cada tarea de IA, construir el golden dataset (mínimo 20 casos: happy + edge + adversarial).
2. Definir el tipo de eval más barato que sirva (asserts programáticos > schema-valid > LLM-as-judge; el juez se usa solo cuando no hay forma programática).
3. Definir métrica primaria y umbral medible. Marcar casos críticos con umbral 100%.
4. Si usa LLM-as-judge, escribir rúbrica binaria y elegir modelo juez con control de sesgo.
5. Hacer el harness ejecutable automáticamente (se corre en CI, no a mano).
6. Verificar que el harness puede fallar: correrlo contra un prompt malo a propósito y confirmar que reprueba.

**REGLAS:**
- Los evals se escriben antes del prompt. Sin excepción. (Espejo de 6.C.1.)
- Un eval que no puede fallar no es un eval: se valida contra un prompt malo antes de confiar en él.
- Preferir asserts programáticos sobre LLM-as-judge: el juez cuesta tokens y agrega varianza.
- Los casos críticos (safety, no filtrar datos, formato) son umbral 100%, nunca promediados con el resto.
- El prompt se itera para pasar los evals; los evals nunca se relajan para que pase el prompt.
- El harness corre en CI en cada cambio de prompt o modelo (gate de regresión).

**CRITERIO DE CALIDAD (medible):** ≥20 casos por tarea con cobertura happy/edge/adversarial. Umbral de aprobación definido numéricamente. Casos críticos con umbral 100%. Harness ejecutable en CI. Validado contra un prompt malo (falla cuando debe fallar).

---

## SKILL 6.F.4 — llm-security-review

**Propósito:** Revisión de seguridad específica de LLM en cada feature de IA, mapeada al OWASP Top 10 for LLM Applications. Complementa a 6.D (que cubre OWASP de aplicación) sin pisarlo. Es BLOQUEANTE, igual que 6.D.1.

**Trigger:** Después de diseñar el prompt (6.F.2) y antes del Gate 4. En cada PR que toque la capa de IA. "seguridad LLM", "prompt injection", "OWASP LLM".

**INPUT obligatorio:** Prompt y contexto (6.F.2) + flujo de datos hacia y desde el modelo + sensibilidad de datos + casos adversariales del golden set (6.F.3).

**OUTPUT:**
```
LLM SECURITY REVIEW — [Feature de IA] / PR: [nombre]

─── OWASP TOP 10 FOR LLM ───
LLM01 Prompt Injection (directa e indirecta): [✅/❌/N/A]
LLM02 Sensitive Information Disclosure: [✅/❌/N/A]
LLM03 Supply Chain (modelos/plugins de terceros): [✅/❌/N/A]
LLM04 Data & Model Poisoning: [✅/❌/N/A]
LLM05 Improper Output Handling: [✅/❌/N/A]
LLM06 Excessive Agency (permisos del modelo): [✅/❌/N/A]
LLM07 System Prompt Leakage: [✅/❌/N/A]
LLM08 Vector/Embedding Weaknesses (si hay RAG): [✅/❌/N/A]
LLM09 Misinformation / alucinación con consecuencia: [✅/❌/N/A]
LLM10 Unbounded Consumption (costo/DoS por tokens): [✅/❌/N/A]

─── CHECKLIST ───
□ Input del usuario aislado del prompt del sistema (delimitadores / estructura)
□ El output del modelo se trata como NO confiable (se valida antes de ejecutar/renderizar)
□ Sin datos sensibles innecesarios en el contexto enviado al modelo
□ El system prompt no expone secretos ni instrucciones que filtren lógica de negocio
□ Si el modelo dispara acciones (tools), permisos mínimos y confirmación humana en acciones sensibles
□ Contenido de fuentes externas (RAG, web) tratado como input adversarial
□ Rate limiting y hard cap de tokens por usuario (anti abuso de costo)
□ Logs sin PII ni contenido sensible de prompts
□ Casos de injection del golden set (6.F.3) pasan

─── ISSUES ENCONTRADOS ───
CRÍTICO — [descripción] — [dónde] — [cómo corregir]
ALTO — [descripción] — [dónde] — [cómo corregir]
MEDIO — [descripción] — [recomendación]

─── HANDOFF A 6.D ───
[Issues que tocan infra/app y los toma 6.D]

─── VEREDICTO ───
APROBADO: 0 críticos, 0 altos
RECHAZADO: [N] críticos / [N] altos — devuelto a 6.F.2 / 6.B
```

**FLUJO:**
1. Recorrer los 10 ítems de OWASP LLM marcando estado con evidencia.
2. Probar prompt injection directa e indirecta (incluyendo contenido de fuentes externas si hay RAG).
3. Verificar que el output del modelo se trata como input no confiable en todo el flujo.
4. Verificar Excessive Agency: si el modelo dispara herramientas, permisos mínimos + human-in-loop en lo sensible.
5. Verificar que el system prompt no filtra secretos ni se puede extraer.
6. Confirmar hard cap de tokens y rate limiting (Unbounded Consumption).
7. Pasar a 6.D lo que toque infra. Emitir veredicto.

**REGLAS:**
- Issue CRÍTICO o ALTO = merge bloqueado. Sin excepción. (Mismo estándar que 6.D.1.)
- El output del modelo es input no confiable: nunca se ejecuta, renderiza ni concatena a una query sin validar.
- El input del usuario nunca se mezcla sin delimitar con el prompt del sistema.
- Si el modelo tiene agencia (tools), el default es el permiso mínimo y la confirmación humana en acciones con efecto.
- Contenido externo (RAG, web, archivos del usuario) se trata siempre como adversarial.

**CRITERIO DE CALIDAD (medible):** 0 issues críticos/altos de OWASP LLM. 100% de los casos de injection del golden set pasan. 0 datos sensibles en logs. Hard cap de tokens y rate limiting verificados.

---

## SKILL 6.F.5 — cost-and-reliability-controls

**Propósito:** Definir los controles de producción que asumen que el modelo va a fallar y que los tokens cuestan plata real: presupuesto de tokens, caché, cadena de fallback, circuit breaker y degradación elegante. Es el runbook de la capa de IA.

**Trigger:** Antes del Gate 4, una vez que el prompt pasó evals y security. "control de costos", "fallbacks", "qué pasa si el modelo se cae".

**INPUT obligatorio:** Matriz de ruteo con fallbacks (6.F.1) + prompt y hard caps (6.F.2) + presupuesto de costo IA (6.F.1) + criticidad de cada tarea.

**OUTPUT:**
```
COST & RELIABILITY CONTROLS — [Proyecto]

─── CONTROL DE COSTO DE TOKENS ───
Presupuesto por llamada: [input cap + output cap por tarea]
Presupuesto por usuario/día: [N tokens o $N] → al superarlo: [degradar / cortar / avisar]
Caché: [qué respuestas se cachean — prompts idénticos, embeddings] → ahorro estimado [%]
Caché de contexto del proveedor: [si aplica — qué se cachea, TTL]
Telemetría de costo: [tokens y $ por tarea, por usuario, por día — dashboard]
Alerta de presupuesto: [se dispara al X% del techo mensual]

─── CADENA DE FALLBACK (por tarea) ───
Tarea [n]:
  1. Modelo primario [m] → si timeout/error/rate-limit →
  2. Reintento con backoff [N intentos, jitter]  →
  3. Modelo fallback [m2] →
  4. Respuesta degradada determinista [qué se muestra: cache vieja / mensaje honesto / flujo sin IA]
  Nunca: error 500 crudo al usuario.

─── CIRCUIT BREAKER ───
Se abre si: [error rate > X% en ventana de Y min]
Estado abierto: [no llama al modelo, sirve degradación]
Half-open: [reintenta después de Z, cierra si recupera]

─── DEGRADACIÓN ELEGANTE ───
Por tarea crítica: [qué ve el usuario cuando la IA no está disponible — siempre algo usable]
Regla: la feature de IA puede caer; el producto no.

─── TIMEOUTS Y LÍMITES ───
Timeout por llamada: [ms] | Reintentos máx: [N] | Concurrencia máx: [N]

─── RUNBOOK DE IA (para 6.E) ───
Síntoma: costo disparado → diagnóstico → acción
Síntoma: latencia alta → diagnóstico → acción
Síntoma: calidad cayó (evals en producción bajan) → diagnóstico → acción
Síntoma: proveedor caído → confirmar circuit breaker + degradación
```

**FLUJO:**
1. Fijar presupuesto de tokens por llamada y por usuario/día, con acción al superarlo.
2. Definir qué se cachea (prompts idénticos, embeddings, contexto del proveedor) y estimar el ahorro.
3. Diseñar la cadena de fallback por tarea: primario → reintento con backoff → fallback → degradación determinista.
4. Definir el circuit breaker (umbral de apertura, half-open, recuperación).
5. Definir la degradación elegante por tarea crítica: el producto siempre muestra algo usable.
6. Instrumentar telemetría de costo y latencia (entrega a 6.E para el runbook y a Agente 9 para medición).
7. Verificar que ninguna ruta termina en un error crudo al usuario.

**REGLAS:**
- Toda llamada al modelo tiene timeout, límite de reintentos y un fallback determinista. Sin las tres, no pasa.
- Ninguna falla del modelo llega como error 500 crudo al usuario: siempre hay degradación.
- La feature de IA puede caerse; el producto no. Si la IA es indispensable para que el producto funcione, eso es una decisión de arquitectura (6.A), no un default.
- El costo de tokens se mide en producción, no se estima una sola vez. Alerta automática al X% del techo mensual.
- El caché es la primera palanca de costo antes de bajar de modelo.

**CRITERIO DE CALIDAD (medible):** 100% de las tareas de IA tienen timeout + reintento + fallback determinista. 0 rutas que terminen en error crudo. Telemetría de costo activa con alerta. Costo IA real en producción < 30% del precio (verificado, no estimado).

---

## Definition of Done — Capa de IA/LLM (addendum a la DoD del MVP)

> Se suma a la Definition of Done de `subagentes-constructor-mvp.md`. Si el MVP tiene IA, estos criterios son parte del Gate 4.

```
─── SELECCIÓN DE MODELO ───
□ Cada tarea de IA con tier justificado, modelo primario y fallback
□ Costo IA proyectado < 30% del precio del producto
□ Capa de abstracción: 0 llamadas directas al SDK del proveedor en la lógica de negocio
□ Nombre de modelo en config, no hardcodeado

─── PROMPT Y CONTEXTO ───
□ Prompt del sistema versionado en repo (prompt-id@versión)
□ Presupuesto de tokens por sección definido, sistema nunca se trunca
□ Hard cap de tokens por request aplicado al 100% de las llamadas
□ Salida estructurada validada contra schema antes de uso

─── EVALS ───
□ Golden dataset ≥20 casos por tarea (happy/edge/adversarial)
□ Umbral de aprobación medible; casos críticos al 100%
□ Harness ejecutable en CI (gate de regresión en cada cambio de prompt/modelo)
□ Harness validado contra prompt malo (falla cuando debe)
□ El prompt en producción pasa el umbral

─── SEGURIDAD LLM ───
□ OWASP Top 10 for LLM: 0 críticos/altos
□ Input de usuario aislado del system prompt
□ Output del modelo tratado como no confiable (validado antes de ejecutar/renderizar)
□ Casos de injection del golden set pasan al 100%
□ Sin PII ni contenido sensible en logs

─── COSTO Y CONFIABILIDAD ───
□ Cada tarea con timeout + reintento + fallback determinista
□ Circuit breaker y degradación elegante por tarea crítica
□ 0 rutas que terminen en error crudo al usuario
□ Telemetría de costo/latencia activa con alerta de presupuesto
□ Costo IA real en producción < 30% del precio (medido)

─── GATE 4 ───
□ Aprobado por el Guardián (Agente 10 — auditor técnico 10.C)
□ Aprobado por revisión humana (human-in-loop obligatorio)
```

---

## Cuándo NO usar 6.F

- El MVP no llama a ningún modelo de lenguaje → 6.F no corre.
- La "IA" es una librería de ML clásica entrenada propia (no un LLM por API) → eso es MLOps, no 6.F (ver la tabla de subagentes adicionales del Constructor).

---

*SiriusLabs — miko.siriuslabs@gmail.com*
*Complemento de `subagentes-constructor-mvp.md`. 6.F se activa solo cuando el MVP tiene una feature de LLM.*
*Actualizar cuando se detecte un patrón de error recurrente en la capa de IA de los MVPs entregados.*
