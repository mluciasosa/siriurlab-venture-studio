# FASE 0 — EXPLORADOR

Proyecto: proyecto-902-qa | Fecha: 2026-06-26 | ODS: 3 — Salud y bienestar

## Problema validado {#problema}

─── EL PROBLEMA ───

Qué es: consultorios chicos pierden turnos e ingresos por agenda manual. La
recepción confirma, reprograma y persigue pacientes por WhatsApp o teléfono, y
los recordatorios dependen de memoria humana.

Cuándo ocurre: especialmente al inicio de semana, antes de feriados, cuando el
paciente pide reprogramar fuera de horario o cuando una recepcionista maneja más
de un profesional.

Cómo se ve (síntomas): mensajes sin responder, doble reserva ocasional, huecos
por no-show, pacientes que preguntan dos veces el horario y profesionales que
interrumpen consulta para coordinar turnos.

Solución actual del usuario: WhatsApp Business, Google Calendar o planilla, más
llamadas manuales de confirmación.

─── MAGNITUD Y FRECUENCIA ───

Frecuencia: diaria.

Gravedad (1-5): 4 — afecta ingresos, reputación y tiempo administrativo.

Zona: alta magnitud + alta frecuencia = URGENTE para consultorios con agenda
llena o recepción compartida.

─── EVIDENCIA VS INFERENCIA ───

Evidencia confirmada:

- Fixture QA: 4/5 entrevistados simulados reportan al menos 3 no-shows por semana.
- Fixture QA: 5/5 usan WhatsApp como canal principal de agenda.
- Fuente secundaria: LatamList reporta que los recordatorios reducen olvidos y
  que algunos proveedores LATAM tienen recepción saturada.

Inferencias:

- El dolor es más fuerte en consultorios con agenda de 40+ consultas mensuales.
- El segmento prefiere herramienta liviana integrada a WhatsApp antes que HIS/EHR completo.

## Perfil de poblacion afectada {#poblacion}

─── QUIENES SON ───

Nombre del segmento: consultorio independiente con recepción manual.

Demografía: dueños/profesionales de salud de 30-55 años y recepcionistas de
25-45 años; 1-3 profesionales por consultorio.

Geografía: Uruguay urbano como foco de entrada; LATAM como expansión.

Acceso tecnológico: smartphone, WhatsApp, calendario digital básico; bajo apetito
por software administrativo pesado.

Idioma(s): español rioplatense en foco inicial.

Tamaño estimado: INCIERTO para Uruguay; fuente secundaria de Brasil sugiere
mercado de scheduling médico en crecimiento, pero se requiere dimensionamiento
bottom-up en Fase 2.

─── JOBS TO BE DONE ───

Job funcional: llenar la agenda y reducir no-shows sin sumar trabajo manual.

Job emocional: sentir control operativo y dejar de "estar atrás del WhatsApp".

Job social: que el consultorio parezca ordenado y profesional frente al paciente.

─── POR QUE FALLA HOY ───

Solución actual: WhatsApp + calendario + memoria de recepción.

Fricción 1: mensajes fuera de horario quedan para después y se pierden.

Fricción 2: los recordatorios manuales son inconsistentes.

Fricción 3: confirmar, cancelar y reprogramar consume tiempo de atención.

─── MOMENTOS DE MAYOR DOLOR ───

Momento 1: paciente no aparece y el hueco ya no se puede vender.

Momento 2: dos pacientes reciben el mismo horario por error humano.

─── LENGUAJE ───

Para describir el problema: "me mata cuando me dejan plantada y no avisaron"
(fixture QA simulado).

Para la solución ideal: "que mande el recordatorio solo y me avise si cancela"
(fixture QA simulado).

Palabras que usan: agenda, confirmar, remarcar, hueco, paciente, WhatsApp, no vino.

Palabras que NO usan: workflow, CRM, engagement, revenue operations.

─── DISPOSICION A PAGAR ───

¿Paga por algo parecido hoy? sí/incierto — 2/5 entrevistados simulados pagan
herramientas administrativas simples o WhatsApp Business; ninguno paga software médico completo.

¿Cuánto valdría resolverlo? USD 20-40/mes como rango de fixture QA para consultorios chicos.

## Veredicto hair-on-fire {#hair-on-fire}

¿Es urgente? SI — Evidencia: fixture QA simulado reporta dolor semanal y pérdida
de ingreso por huecos.

¿Pagarían por resolverlo? SI CON RIESGO — Evidencia: rango declarado USD 20-40/mes
en fixture; requiere validación real fuera del QA.

Estado de validacion primaria: VALIDADO PARA QA TECNICO (fixture simulado)

INPUT_REQUEST pendiente: no

Conclusión: para el propósito del QA Fase C, la Fase 0 queda sin bloqueo y puede
alimentar Cartógrafo. Este documento no debe usarse como validación comercial real.

## Fuentes {#fuentes}

- Fixture interno QA Fase C — acceso: 2026-06-26 — uso: simular entrevistas primarias para pipeline.
- https://latamlist.com/why-the-healthcare-industry-should-automate-their-customer-service/ — acceso: 2026-06-26 — uso: no-shows y automatización de recordatorios en salud LATAM.
- https://blog.jeftejuan.com.br/automacao-agendamento-clinicas-pequenas/ — acceso: 2026-06-26 — uso: problemas operativos y pricing de herramientas simples en clínicas pequeñas.

## Handoff esperado

Este output alimenta el handoff `0->1` hacia Cartógrafo.

Skills cubiertas:

- `1.1` — problema validado
- `1.2` — perfil de población
