# FASE 1 — CARTOGRAFO

Proyecto: proyecto-902-qa | Fecha: 2026-06-26 | Fuente Fase 0: `fase-0/output.md`

## Mapa competitivo {#mapa-competitivo}

─── CATEGORIAS DE SOLUCION ───

Competidores directos: agendas médicas SaaS con recordatorios y reserva online
(Doctoralia, AgendaPro, Doctolib como benchmark global, soluciones regionales
de agenda clínica).

Competidores indirectos: WhatsApp Business, Google Calendar, Calendly, planillas
compartidas, software de gestión clínica más amplio con módulo de agenda.

Sustitutos manuales/no tecnológicos: cuaderno de agenda, llamadas de recepción,
mensajes manuales de confirmación, lista de espera en papel.

─── TABLA COMPETITIVA ───

| Solución | Tipo | Segmento | Propuesta | Modelo/pricing | Fortaleza | Debilidad | Fuente |
|---|---|---|---|---|---|---|---|
| Doctoralia | Directo | Profesionales y clínicas | Perfil + turnos online + visibilidad | SaaS/marketplace, precio no siempre público | Demanda y marca | Puede ser más marketplace que workflow interno | https://www.doctoralia.com/ — acceso 2026-06-26 |
| AgendaPro | Directo | Servicios con agenda | Reservas, pagos, recordatorios | SaaS por plan | Producto maduro de agenda | No verticaliza sólo consultorio pequeño | https://www.agendapro.com/ — acceso 2026-06-26 |
| Google Calendar + WhatsApp | Sustituto | Consultorios pequeños | Agenda básica y comunicación manual | Gratis/bajo costo | Ya lo usan | Sin automatización clínica ni trazabilidad | Fixture QA Fase C |
| Software clínico completo | Indirecto | Clínicas medianas | Gestión clínica, agenda y fichas | SaaS/instalado | Cobertura amplia | Sobredimensionado para 1-3 profesionales | Research secundario QA |

─── MULTI-HOMING Y PODER DE PRICING ───

¿El usuario puede usar varias soluciones a la vez? sí — puede mantener WhatsApp,
calendar y una agenda online en paralelo.

Costo de cambio: bajo/medio — los datos de turnos son simples, pero cambiar hábitos
de recepción cuesta.

Implicación para pricing: poder bajo/medio — el precio debe ser accesible y el
valor debe verse rápido, porque el sustituto manual es barato.

─── EVIDENCIA VS INFERENCIA ───

Evidencia confirmada:

- Fixture QA: WhatsApp es canal principal en 5/5 entrevistas simuladas.
- Fuentes secundarias describen no-shows, recordatorios y saturación de recepción.
- Existen soluciones con agenda online y recordatorios como categoría madura.

Inferencias:

- La oportunidad no está en "agenda online" genérica, sino en una versión liviana
  para recepción manual con integración WhatsApp y reprogramación simple.

## Research de soluciones {#research-soluciones}

─── PATRONES DE SOLUCION ───

Patrón 1: agenda online + link público — el paciente reserva sin llamar; ejemplos:
AgendaPro, Calendly, Doctoralia.

Patrón 2: recordatorios automáticos — mensajes previos por WhatsApp/SMS/email para
confirmar o cancelar.

Patrón 3: gestión clínica integral — agenda como parte de historia clínica, pagos,
fichas y administración.

─── ESTADO DEL ARTE ───

Capacidades comunes:

- Calendario con disponibilidad configurable — evidencia: benchmarks de AgendaPro/Calendly.
- Recordatorios automáticos — evidencia: LatamList y blogs sectoriales.
- Confirmación/cancelación de turno — evidencia: categoría de scheduling médico.

Capacidades emergentes:

- Automatización conversacional por WhatsApp con derivación a humano.

Limitaciones observadas:

- Herramientas completas pueden ser demasiado caras o pesadas para 1-3 profesionales.
- WhatsApp manual conserva contexto pero no reduce carga administrativa.

─── BENCHMARK UX ───

Onboarding: crear cuenta, configurar disponibilidad, cargar servicios/profesionales,
compartir link.

Momento de valor: primer turno reservado o confirmado automáticamente.

Fricciones visibles: configurar reglas de agenda, migrar hábitos de recepción,
conectar WhatsApp oficial y explicar privacidad de datos.

## Gaps y oportunidades {#gaps}

─── GAPS DEL MERCADO ───

Gap 1: agenda liviana para recepción manual, sin suite clínica completa.

- Evidencia: fixture QA muestra uso de WhatsApp + calendario, no software clínico.
- Usuario afectado: consultorios 1-3 profesionales.
- Por qué importa: reduce barrera de adopción y precio.

Gap 2: reprogramación simple por WhatsApp con mínima configuración.

- Evidencia: el dolor aparece en recordatorios y cambios de horario.
- Usuario afectado: recepcionistas y profesionales que coordinan fuera de consulta.
- Por qué importa: ataca no-show y huecos vendibles.

Gap 3: privacidad por diseño sin historia clínica en MVP.

- Evidencia: datos de salud sensibles elevan fricción si se pide ficha clínica completa.
- Usuario afectado: consultorios que quieren resolver agenda, no digitalizar todo.
- Por qué importa: reduce riesgo regulatorio inicial.

─── OPORTUNIDADES PARA ANALISTA ───

Oportunidad diferenciada: SaaS liviano de agenda y recordatorios WhatsApp para
consultorios pequeños que hoy operan manualmente.

Hipótesis de ventaja: onboarding en menos de 15 minutos y valor visible con el
primer recordatorio automático.

Datos que el Analista debe verificar:

- Número de consultorios independientes alcanzables en Uruguay.
- CAC viable para ticket USD 29/mes.
- Costo y complejidad de WhatsApp Business API.

## Fuentes

- https://www.doctoralia.com/ — acceso: 2026-06-26 — uso: benchmark de turnos online en salud.
- https://www.agendapro.com/ — acceso: 2026-06-26 — uso: benchmark SaaS de agenda y recordatorios.
- https://latamlist.com/why-the-healthcare-industry-should-automate-their-customer-service/ — acceso: 2026-06-26 — uso: no-shows y automatización de atención.
- Fixture interno QA Fase C — acceso: 2026-06-26 — uso: sustitutos actuales y fricciones.

## Handoff esperado

Este output alimenta el handoff `1->2` hacia Analista + Arquitecto de Negocio.

Skills cubiertas:

- `2.1` — mapa competitivo
- `2.2` — research de soluciones
