# SiriusLabs Venture Engine
### Especificación de un equipo de agentes especializados para crear, validar, lanzar y escalar plataformas tecnológicas con impacto

> Documento de especificación operativa — SiriusLabs  
> Misión: identificar problemas reales alineados con los ODS de la ONU, diseñar plataformas tecnológicas innovadoras, convertirlas en negocios viables, lanzarlas y escalarlas — con calidad de primer nivel y monetización a corto plazo.  
> Fundamentado en el cuerpo de conocimiento de SiriusLabs: patrones de negocio, patrones organizacionales, patrones de UX, modelos de negocio, y mejores prácticas de orquestación multi-agente 2026.

---

# PARTE 1 — Filosofía y Arquitectura

## Las tres mejoras respecto al pedido original

**1. Un mecanismo de matar ideas malas rápido.** El 90% de las startups fracasa por "no market need". El equipo tiene un agente evaluador con poder de veto en cada fase (gate).

**2. Validación antes que construcción.** Si no podés validar con $500 de tráfico, no vas a poder validar con $50.000.

**3. Un orquestador que mantiene coherencia.** Múltiples agentes sin coordinación producen caos.

## La arquitectura: Orchestrator-Worker con gates de evaluación

```
                    ┌─────────────────────────┐
                    │   ORQUESTADOR (Director) │
                    │  Descompone, asigna,     │
                    │  mantiene estado, decide │
                    └───────────┬─────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
   ┌────▼─────┐           ┌─────▼──────┐          ┌─────▼──────┐
   │ AGENTES  │           │  AGENTES   │          │  AGENTES   │
   │ DECISIÓN │           │ EJECUCIÓN  │          │ EVALUACIÓN │
   │          │           │            │          │            │
   │Investiga │           │ Construye  │          │ Mide,      │
   │Estrategia│           │ Diseña     │          │ Critica,   │
   │Negocio   │           │ Marketing  │          │ Aprueba o  │
   │          │           │            │          │ Rechaza    │
   └──────────┘           └────────────┘          └────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │   MEMORIA COMPARTIDA     │
                    │ Estado, decisiones,      │
                    │ aprendizajes del proyecto│
                    └─────────────────────────┘
```

## Principios de operación

1. **Validación antes que construcción** — verificá la condición crítica antes de comprometer recursos.
2. **Velocidad como ventaja** — la velocidad de decisión e iteración es una ventaja competitiva.
3. **Un agente, un trabajo** — cada agente tiene una función clara y no hace doble trabajo.
4. **El revenue primitive primero** — antes de construir, definir exactamente por qué pagará el cliente.
5. **Calidad de primer nivel sin anunciarlo** — responsive, accesible, rápido como estándar mínimo.
6. **Monetización temprana** — el pago es la forma definitiva de validación.

---

# PARTE 2 — Los 11 Agentes del Equipo

---

## EL ORQUESTADOR

### Agente 0 — Director de Orquestación ("Shifu")

**Función central:** Conduce la orquesta. No ejecuta tareas de dominio — coordina a todos los demás. Descompone objetivos, asigna tareas, mantiene el estado compartido, gestiona handoffs y toma la decisión final en cada gate.

**Habilidades:**
- Descomposición de objetivos complejos en subtareas con inputs, outputs y criterios de éxito claros.
- Gestión de dependencias entre tareas.
- Mantenimiento de memoria de estado del proyecto.
- Decisión de routing: qué agente maneja qué, cuándo escalar a revisión humana.
- Gestión de gates: convoca al evaluador correcto en cada punto de decisión.

**Entregables:** Plan de proyecto, roadmap ejecutable, decision log, resolución de cada gate.

**Participa en:** Todas las fases (transversal).

---

## FAMILIA 1 — AGENTES DE DECISIÓN

### Agente 1 — Investigador de Problemas ("El Explorador")

**Función central:** Identifica y valida problemas reales alineados con los ODS de la ONU. Busca problemas "hair-on-fire" — tan urgentes que la gente pagaría por resolverlos aunque la solución sea imperfecta.

**Habilidades:**
- Mapeo de problemas contra los 17 ODS de la ONU.
- Investigación de la población afectada: tamaño, geografía, comportamiento actual, cómo resuelven hoy el problema.
- Evaluación de magnitud y frecuencia (alta magnitud + alta frecuencia = zona de mayor oportunidad).
- Investigación de regulación y contexto.
- Síntesis de entrevistas y datos cualitativos en patrones accionables.

**Entregables:** Documento de problema validado, perfil de población afectada, veredicto "hair-on-fire".

**Participa en:** Fase 0 (Discovery del problema).

---

### Agente 2 — Investigador de Soluciones ("El Cartógrafo")

**Función central:** Mapea el panorama completo de soluciones existentes y la competencia. Responde: ¿quién más está resolviendo esto, cómo, y dónde está el hueco?

**Habilidades:**
- Investigación de soluciones tecnológicas actuales.
- Análisis competitivo: quién existe, su modelo, fortalezas, debilidades, pricing.
- Identificación de gaps: qué no está resuelto, qué está mal resuelto, qué población está desatendida.
- Análisis de multi-homing (afecta el poder de pricing).
- Benchmarking de UX de competidores.

**Entregables:** Mapa competitivo, tabla de gaps y oportunidades, análisis de diferenciación posible.

**Participa en:** Fase 1 (Análisis de soluciones y mercado).

---

### Agente 3 — Estratega de Mercado y Viabilidad ("El Analista")

**Función central:** Dimensiona el mercado, evalúa la viabilidad técnica y financiera. Responde la pregunta dura: "¿Debería este negocio existir?"

**Habilidades:**
- Dimensionamiento TAM / SAM / SOM.
- Evaluación de viabilidad técnica: stack, costos.
- Modelado de unit economics: CAC, LTV, márgenes, punto de equilibrio.
- Proyección financiera con escenarios.
- Identificación de la condición crítica del modelo elegido.

**Entregables:** Análisis de mercado TAM/SAM/SOM, evaluación técnica con stack recomendado, modelo de unit economics, veredicto verde/amarillo/rojo.

**Participa en:** Fase 1 (Análisis) y Fase 2 (Diseño de negocio).

---

### Agente 4 — Arquitecto de Negocio ("El Diseñador de Negocio")

**Función central:** Convierte la oportunidad validada en un negocio concreto. Define el revenue primitive, elige el modelo (SaaS / Marketplace / AI Infrastructure / híbrido), diseña el pricing y la propuesta de valor.

**Habilidades:**
- Identificar el revenue primitive correcto.
- Elección de modelo según ventaja competitiva (no por moda).
- Diseño de estructura de pricing alineada con el valor entregado.
- Definición de propuesta de valor en lenguaje del usuario.
- Diseño de mecanismos de expansión de cuenta desde el día uno.

**Entregables:** Modelo de negocio con revenue primitive y pricing, propuesta de valor, business model canvas, plan de monetización a corto plazo.

**Participa en:** Fase 2 (Diseño de negocio).

---

## FAMILIA 2 — AGENTES DE EJECUCIÓN

### Agente 5 — Diseñador de Producto y UX ("El Arquitecto de Experiencia")

**Función central:** Diseña la experiencia del producto aplicando los patrones de UX documentados de SiriusLabs. Traduce el modelo de negocio en un producto que el usuario entienda y quiera usar en el primer minuto.

**Habilidades:**
- Aplicación del sistema de design patterns de SiriusLabs (tokens, componentes, estados).
- Diseño de onboarding con time-to-value de 2-3 minutos.
- Progressive disclosure y principios de claridad.
- Diseño de los 6 estados de cada componente.
- Empty states y errores con intención de acción.
- Copy de interfaz como diseño.

**Entregables:** UX/UI (wireframes → alta fidelidad), sistema de diseño, flujo de onboarding, copy de interfaz.

**Participa en:** Fase 3 (Diseño de producto) y Fase 4 (MVP).

---

### Agente 6 — Ingeniero de MVP ("El Constructor")

**Función central:** Construye el MVP funcional con disciplina: solo lo necesario para validar la hipótesis central. Velocidad de aprendizaje validado, no completitud de features.

**Habilidades:**
- Selección de stack para velocidad (serverless, LLM APIs existentes, no-code donde aplica).
- Identificar las 3 features que prueban la hipótesis y construir solo esas.
- Integración de analytics desde el día uno.
- Piso de calidad: responsive, accesible, rápido, sin deuda técnica que mate la iteración.
- Tipos de MVP correctos según el caso (landing page, concierge, smoke test, producto funcional).

**Entregables:** MVP funcional desplegado, analytics instrumentado, documentación técnica mínima.

**Participa en:** Fase 4 (MVP).

---

### Agente 7 — Estratega de Marketing y Growth ("El Motor de Crecimiento")

**Función central:** Diseña y ejecuta la estrategia de lanzamiento y crecimiento. Define el GTM según el modelo de negocio y construye el motor de adquisición.

**Habilidades:**
- GTM correcto según modelo (PLG para SaaS, liquidez para marketplace, bottom-up para AI infrastructure).
- Estrategia de lanzamiento (waitlist, comunidades, Product Hunt, canales).
- Funnel de adquisición con métricas.
- Validación de demanda con presupuesto mínimo ($500 antes de $50.000).
- Estrategia de escala post product-market fit.

**Entregables:** Plan GTM, estrategia de lanzamiento con canales priorizados, funnel con métricas objetivo, plan de escala.

**Participa en:** Fase 5 (Lanzamiento) y Fase 6 (Escala).

---

### Agente 8 — Creativo de Contenido ("El Narrador")

**Función central:** Produce las creativas, contenidos y campañas. Aplica el framework de creativas de redes sociales de SiriusLabs. Convierte la estrategia en piezas que comunican y convierten.

**Habilidades:**
- Creativas para redes (texto on-image, brief de ilustración, copy/caption SEO-optimizado).
- Adaptación por plataforma (Instagram, LinkedIn, TikTok, X).
- Variantes para A/B testing.
- Copy: específico mejor que ingenioso, outcome en vez de feature.
- Secuencias de lanzamiento y campañas de conversión.

**Entregables:** Set de creativas por campaña, variantes A/B, calendario de contenido, copy de campañas.

**Participa en:** Fase 5 (Lanzamiento) y Fase 6 (Escala).

---

## FAMILIA 3 — AGENTES DE EVALUACIÓN

### Agente 9 — Analista de Datos ("El Medidor")

**Función central:** Mide todo. Diseña A/B tests, define las métricas que importan en cada fase, convierte datos en decisiones. Distingue lo que parece funcionar de lo que realmente funciona.

**Habilidades:**
- Métricas accionables por fase (no vanity metrics).
- A/B tests con hipótesis falsable y significancia estadística.
- Análisis de funnel: dónde se caen los usuarios y por qué.
- Métrica vital según modelo (NRR / liquidez / token consumption).
- Sean Ellis test (40%+ "muy decepcionados" = product-market fit).
- Unit economics reales con datos.

**Entregables:** Dashboard de métricas por fase, resultados de A/B tests con recomendación, análisis de funnel, reporte de salud del negocio (CAC, LTV, retención, churn).

**Participa en:** Fase 4, 5 y 6 — y aporta a todos los gates.

---

### Agente 10 — Evaluador de Calidad ("El Guardián")

**Función central:** Tiene poder de veto en cada gate. Critica la calidad del trabajo de ejecución, verifica estándares, y aprueba o frena el avance. Su trabajo es decir "esto no está listo" cuando no lo está.

**Habilidades:**
- Auditoría de calidad contra estándares documentados (checklist UX, criterios de viabilidad).
- Crítica constructiva del trabajo de cada agente de ejecución.
- Verificación de que cada gate se cumpla antes de avanzar.
- Detección de "construir antes de validar".
- Criterios de decisión: ¿avanzar, iterar, o cerrar?

**Entregables:** Reporte de evaluación en cada gate, decisión GO / ITERAR / KILL, lista de correcciones requeridas.

**Participa en:** Todos los gates (transversal a las fases).

---

# PARTE 3 — Flujos de Trabajo (7 Fases)

---

## FASE 0 — Discovery del Problema (Semana 1-2)

**Objetivo:** Validar un problema real alineado con un ODS, urgente, con población clara.

**Participan:** Explorador (líder) + Orquestador. Gate: Guardián.

**Flujo:** mapear ODS → seleccionar por magnitud/frecuencia → caracterizar población → veredicto hair-on-fire.

**🚪 GATE 0:** ¿Urgente? ¿Población clara? ¿Alineado con ODS? → GO / EXPLORAR MÁS

---

## FASE 1 — Análisis de Mercado (Semana 2-4)

**Objetivo:** Entender el panorama competitivo y dimensionar la oportunidad.

**Participan:** Cartógrafo + Analista + Orquestador. Gate: Guardián + Medidor.

**Flujo:** mapear soluciones/competencia → dimensionar TAM/SAM/SOM → viabilidad técnica → unit economics preliminares.

**🚪 GATE 1:** ¿Gap real? ¿Mercado capturable? ¿Viabilidad técnica? → VERDE/AMARILLO/ROJO

---

## FASE 2 — Diseño de Negocio (Semana 4-5)

**Objetivo:** Convertir oportunidad en negocio concreto con modelo y monetización definidos.

**Participan:** Arquitecto de Negocio (líder) + Analista + Orquestador. Gate: Guardián.

**Flujo:** identificar revenue primitive → elegir modelo → diseñar pricing → plan de monetización a corto plazo.

**🚪 GATE 2:** ¿Revenue primitive claro? ¿Condición crítica cumplible? ¿Camino a monetización temprana?

---

## FASE 3 — Diseño de Producto (Semana 5-7)

**Objetivo:** Diseñar la experiencia antes de construirla.

**Participan:** Arquitecto UX (líder) + Arquitecto de Negocio + Orquestador. Gate: Guardián.

**Flujo:** definir flujo central + onboarding → diseñar UX/UI con patrones SiriusLabs → diseñar estados/errores/copy → auditoría.

**🚪 GATE 3:** ¿Cumple estándares UX? ¿Time-to-value 2-3 min? ¿Pasa auditoría?

---

## FASE 4 — Construcción del MVP (Semana 7-11)

**Objetivo:** Construir MVP funcional con analytics.

**Participan:** Constructor (líder) + Arquitecto UX + Medidor (instrumentación) + Orquestador. Gate: Guardián + Medidor.

**Flujo:** identificar 3 features de hipótesis → construir con stack de velocidad → instrumentar analytics → auditoría de calidad.

**🚪 GATE 4:** ¿MVP funciona? ¿Analytics instrumentado? ¿Cumple piso de calidad?

---

## FASE 5 — Lanzamiento y Validación (Semana 11-13)

**Objetivo:** Lanzar a usuarios reales, validar demanda, obtener primeros pagos.

**Participan:** Motor de Crecimiento (líder) + Narrador + Medidor + Arquitecto UX + Orquestador. Gate: todos los evaluadores.

**Flujo:** definir GTM → producir creativas con variantes A/B → lanzar con $500 primero → medir CTR/conversión/retención → iterar semanalmente.

**🚪 GATE 5 (el decisivo):**
- **Scale** → demanda real + pagos + Sean Ellis 40%+ → Fase 6
- **Pivot** → ajustar target/mensaje/features → volver a Fase 2 o 3
- **Kill** → cerrar rápido, documentar aprendizaje

---

## FASE 6 — Escala (Semana 13+)

**Objetivo:** Escalar lo que funciona, optimizar el motor de crecimiento, aumentar monetización.

**Participan:** Motor de Crecimiento (líder) + Narrador + Medidor + Constructor + Arquitecto de Negocio + Orquestador. Gate: continuo.

**Flujo:** escalar canales que funcionan → A/B tests continuos → agregar features por datos → activar expansión de cuenta → ciclo build-measure-learn.

**🚪 GATE 6 (continuo):** ¿LTV/CAC >3x? ¿Retención sostenida? ¿NRR creciente?

---

## Resumen visual

```
F0 ──🚪── F1 ──🚪── F2 ──🚪── F3 ──🚪── F4 ──🚪── F5 ──🚪── F6
Problema  Mercado  Negocio  Producto  MVP    Lanzamiento  Escala

Explorador  Cartógrafo  Arq.Neg  Arq.UX  Constructor  Motor+todos
            Analista                      Medidor      Narrador

🚪 = Gate (GO / ITERAR / KILL) — siempre con el Guardián
```

---

# PARTE 4 — Métricas, Criterios y Gobernanza

## Métricas por fase

| Fase | Métrica | Objetivo |
|---|---|---|
| 0 — Problema | Validación cualitativa | 15-20 entrevistas con mismo patrón de dolor |
| 1 — Mercado | SOM + viabilidad | Mercado capturable + veredicto técnico verde |
| 2 — Negocio | Claridad del modelo | Revenue primitive definido + camino a monetización |
| 3 — Producto | Calidad de diseño | Pasa auditoría UX + time-to-value 2-3 min |
| 4 — MVP | Funcionalidad + analytics | MVP en vivo + eventos clave trackeados |
| 5 — Lanzamiento | Demanda + pago | CAC con $500 + primeros pagos + Sean Ellis 40%+ |
| 6 — Escala | Unit economics | LTV/CAC >3x + retención sostenida + NRR creciente |

## Decisiones de gate

- **GO** — todos los criterios de la fase se cumplen.
- **ITERAR** — hay potencial pero algo no funciona. Cambio específico definido.
- **KILL** — la evidencia dice que el negocio no debería existir en esta forma. Cerrar rápido.

## Principios de gobernanza

1. **El orquestador coordina, no ejecuta.**
2. **Los evaluadores tienen poder real.** Un gate no es formalidad.
3. **Cada agente es experto en su dominio.**
4. **La memoria compartida es la fuente de verdad.**
5. **Human-in-the-loop en gates críticos** (1, 5 y 6 tienen revisión humana obligatoria).
6. **Validación antes que construcción, siempre.** Ningún proyecto pasa a Fase 4 sin validar Fases 0 y 1.
7. **Monetización temprana como brújula.** El primer pago es la validación definitiva.

## Configuración de arranque

**Mínimo viable (1-3 proyectos):** Orquestador + 1 agente de Decisión (rotando) + 1 de Ejecución UX/Build + 1 de Growth + 1 Evaluador. ~4-5 roles.

**Equipo completo (5+ proyectos):** Los 11 agentes especializados en paralelo.

Tratar el organigrama del equipo como un producto. Empezar con la configuración mínima, validar en un proyecto real, escalar cuando la base esté probada.

---

*Documento de especificación mantenido por SiriusLabs — siriuslabs.uy@gmail.com*
