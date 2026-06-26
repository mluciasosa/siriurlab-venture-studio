# Los 3 Modelos de Negocio Top
### Guía de decisión para construcción de plataforma, producto y estrategia comercial

> Documento de decisión estratégica — SiriusLabs  
> Para uso en definición de modelo de negocio, arquitectura de plataforma y diseño de estrategia comercial y de marketing.  
> Basado en análisis de SaaS, Marketplace y AI Infrastructure (datos a junio 2026).

---

## Cómo usar este documento

Este no es un documento informativo — es una herramienta de decisión. Se usa al revés: empezás por tu situación específica (qué problema resolvés, qué cobrás, qué ventaja tenés), identificás cuál de los tres modelos calza, y recién entonces leés sus implicancias para stack técnico, go-to-market y compliance.

**La advertencia más importante:** la elección de modelo de negocio es la decisión arquitectónica de mayor peso del primer año. El error más común es imitar a una empresa admirada y elegir el modelo equivocado. Si elegís mal, el producto pasa 18 meses tratando de ser algo que no es.

---

## Parte 1 — Definiciones

### Modelo 1: SaaS (Software as a Service)

**Definición:** Vende acceso a una herramienta que el cliente usa para hacer su propio trabajo. Ingresos recurrentes por suscripción.

**El principio:** la empresa vende, el cliente usa. Relación bilateral directa.

**Ejemplos:** Slack, Notion, HubSpot, Linear, Figma, Cursor.

**Cómo gana dinero:** suscripción recurrente. El costo de servir un cliente adicional es casi cero.

---

### Modelo 2: Marketplace / Plataforma de dos lados

**Definición:** Conecta dos o más grupos de usuarios y toma una porción de las transacciones que facilita. No posee inventario propio.

**El principio:** el valor se crea por las interacciones entre participantes. La plataforma vale más cuanto más gente la usa (efecto de red).

**Ejemplos:** Airbnb, Uber, Etsy, Upwork, Mercado Libre.

**Cómo gana dinero:** comisión por transacción (take rate). Rango típico: 5-20%. Complementado con suscripciones premium para sellers.

---

### Modelo 3: AI Infrastructure (Inteligencia como Servicio)

**Definición:** Venta de acceso a capacidad de IA — API de modelos, herramientas de agente, infraestructura sobre la que otros construyen.

**El principio:** se vende capacidad, no producto terminado. Los datos de uso mejoran los modelos (efecto de red sobre el propio producto).

**Ejemplos:** Anthropic (Claude API), OpenAI (GPT API), Claude Code, productos verticales sobre modelos.

**Cómo gana dinero:** pricing por uso (por token, por llamada), más suscripciones de producto y contratos enterprise.

---

## Parte 2 — Las cuatro dimensiones que importan

| Dimensión | SaaS | Marketplace | AI Infrastructure |
|---|---|---|---|
| **Revenue primitive** | Suscripción recurrente | Comisión por transacción | Pago por uso / consumo |
| **Activo principal** | Software / IP | Red de usuarios (liquidez) | Modelos + datos + compute |
| **Efecto de red** | Débil | Muy fuerte (bilateral) | Fuerte (datos de uso) |
| **Margen bruto** | 70-85% | 40-70% | 40-60% |
| **Barrera de entrada** | Media | Alta (cold start brutal) | Muy alta |
| **Predictibilidad** | Alta | Media | Media-alta (enterprise) |
| **Tiempo a tracción** | Rápido-medio | Lento | Variable |
| **Riesgo principal** | Churn | Multi-homing / masa crítica | Commoditización |
| **Métrica vital** | NRR / ARR | GMV / Liquidez | Token consumption / ARR enterprise |

---

## Parte 3 — Cuándo usar cada modelo

### Elegí SaaS si:

- Tu producto resuelve un workflow recurrente (no una transacción puntual).
- Podés entregar valor a un solo usuario sin necesitar a nadie más.
- El cliente experimenta el valor central en menos de una hora (habilita PLG).
- Tu ventaja competitiva es la profundidad del software en sí.

**Condición crítica:** alta retención. El churn alto mata empresas SaaS. Si no retenés clientes más allá del mes seis, ninguna adquisición arregla el fondo.

**Caso ideal SiriusLabs:** producto que una empresa usa diariamente para una función específica, con mecanismos de expansión de cuenta desde el día uno.

---

### Elegí Marketplace si:

- Existe un problema real de descubrimiento o confianza entre dos grupos que hoy no se encuentran eficientemente.
- Hay valor desbloqueado al conectar oferta y demanda fragmentadas.
- Podés capturar valor sobre cada transacción alineado con el beneficio que generás.
- Tenés un plan concreto para el cold start problem.

**Condición crítica:** liquidez. No cuántos usuarios registrás, sino la probabilidad de que alguien que entra complete una transacción. Un marketplace con 100.000 usuarios y baja liquidez vale menos que uno con 5.000 y transacciones constantes.

**Advertencia clave:** migrar de SaaS a Marketplace raramente funciona. De Marketplace a SaaS, frecuentemente. Ante la duda, esto sesga la decisión.

**Caso ideal SiriusLabs:** nicho vertical con proveedores y clientes que hoy se encuentran ineficientemente, dominando primero una geografía o segmento.

---

### Elegí AI Infrastructure si:

- Tu valor central es capacidad de inteligencia que otros integran.
- Tu cliente principal es enterprise o developer, no consumidor masivo.
- Tenés talento técnico especializado y datos difíciles de replicar.
- Podés diseñar pricing por uso que refleje el costo real.

**Condición crítica:** unit economics sostenibles vs. costo de compute. Las empresas que cobran flat-rate cuando el costo es variable terminan subsidiando heavy users hasta quebrar. El pricing por token es la respuesta ganadora.

**Distinción clave 2026:** "empresa enterprise con producto de consumo" tiene mejores unit economics que "empresa de consumo construyendo enterprise". La concentración enterprise da camino a la rentabilidad.

**Caso ideal SiriusLabs:** capa de aplicación vertical sobre modelos existentes — herramientas específicas de industria que usan IA por debajo, cobradas por valor entregado. No construir modelos propios (imposible competir en capital).

---

## Parte 4 — Implicancias prácticas

### Stack técnico

| Aspecto | SaaS | Marketplace | AI Infrastructure |
|---|---|---|---|
| **Pagos** | Stripe Billing | Stripe Connect (split payouts, KYC) | Medición de uso + billing por consumo |
| **Arquitectura** | Multi-tenant, planes y límites | Matching, verificación, disputas | Orquestación de modelos, rate limiting |
| **Compliance** | Privacidad, SOC2 enterprise | KYC sellers, seguridad de transacciones | Privacidad, uso responsable IA |
| **Complejidad inicial** | Media | Alta (dos lados + confianza) | Alta (infraestructura + costos variables) |

### Go-To-Market

**SaaS → PLG cuando time-to-value < 1 hora.** El producto se vende solo. Para ticket bajo (<$1K ACV): distribución por marketplace de apps. Para ticket alto (>$10K ACV): venta directa.

**Marketplace → construir liquidez, no ventas.** Concentrar en un lado (supply primero), sembrar 2-3 categorías hero, probar liquidez con MVP 90 días. El marketing genera densidad en un nicho específico.

**AI Infrastructure → bottom-up enterprise.** Developer prueba → demuestra valor → adopción se expande → contrato enterprise. Marketing técnico, demostración de capacidad real.

### Financiamiento

- **SaaS:** valuado por predictibilidad. MRR, NRR y unit economics limpios.
- **Marketplace:** valuado por efectos de red. Upside mayor si hay liquidez. Inversores miran repeat usage y calidad del supply.
- **AI Infrastructure:** valuado por crecimiento + camino a rentabilidad. Concentración enterprise y proyección de cash flow positivo son diferenciadores.

---

## Parte 5 — El patrón híbrido y la convergencia

Los mejores negocios de 2026 son los tres modelos a la vez, en capas:

- **Stripe** = SaaS + Marketplace + AI Infrastructure
- **Amazon** = Marketplace + SaaS (AWS) + infraestructura
- **OpenAI** = AI Infrastructure + SaaS + semilla de marketplace

**Patrón de evolución natural:**
- E-commerce → Marketplace (Amazon)
- Marketplace → Integración vertical (Zillow)
- SaaS → Plataforma de extensión (Salesforce)

**Regla de secuenciación:** no intentar ser los tres desde el día uno. Elegí un modelo, alcanzá masa crítica, agregá capas adyacentes cuando la base sea sólida.

---

## Proceso de decisión para SiriusLabs

**Paso 1 — Identificá el revenue primitive.**
¿Por acceso continuo (SaaS)? ¿Por transacción facilitada (Marketplace)? ¿Por capacidad consumida (AI Infrastructure)?

**Paso 2 — Verificá la condición crítica.**
¿Podés retener? ¿Podés generar liquidez? ¿Son sostenibles tus unit economics?

**Paso 3 — Validá con experimento de 60-90 días.**
Hipótesis falsable: "Si este modelo es correcto, veremos X clientes convertir a precio Y con churn Z en 90 días."

**Paso 4 — Diseñá expansión desde el día uno.**
El revenue de expansión (más gasto de clientes existentes) es casi siempre más barato que adquirir nuevos.

**Recomendación para SiriusLabs:** modelo más natural es **AI Infrastructure en capa de aplicación vertical** — herramientas específicas de industria con IA por debajo, cobradas por valor entregado, que evolucionan hacia SaaS recurrente. Nodo3 ya tiene esta estructura híbrida.

---

*Documento mantenido por SiriusLabs — siriuslabs.uy@gmail.com*
