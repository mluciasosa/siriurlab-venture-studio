# FASE 0 — EXPLORADOR

Proyecto: proyecto-901-qa | Fecha: 2026-06-26 | ODS: 3 — Salud y bienestar

## Problema validado {#problema}

─── EL PROBLEMA ───

Qué es: consultorios pequeños y clínicas de baja escala en LATAM pierden citas y
horas de recepción porque coordinan turnos por WhatsApp, planillas o llamadas,
con errores de horario, doble reserva y pacientes que no aparecen.

Cuándo ocurre: al abrir agenda semanal, ante picos de llamadas, cuando el
paciente olvida la cita o intenta reprogramar fuera de horario de recepción.

Cómo se ve (síntomas): teléfono saturado, mensajes de WhatsApp sin responder,
agenda en papel/planilla con solapamientos, quejas de dificultad para conseguir
turno, no-shows recurrentes.

Solución actual del usuario: recepcionista o el mismo profesional atiende
llamadas/WhatsApp manualmente; algunos usan Google Calendar o planilla Excel;
recordatorios manuales si hay tiempo.

─── MAGNITUD Y FRECUENCIA ───

Frecuencia: diario en consultorios con agenda activa (varias citas por día).

Gravedad (1-5): 4 — afecta ingresos directos (citas perdidas) y calidad de
atención (recepción colapsada).

Zona: alta magnitud + alta frecuencia = URGENTE (según literatura secundaria;
validación primaria pendiente).

─── EVIDENCIA VS INFERENCIA ───

Evidencia confirmada:

- Hasta 42% de pacientes pueden faltar a citas; ~23% olvidan sin recordatorio
  (LatamList, acceso 2026-06-26).
- Recepción saturada y doble reserva cuando conviven teléfono y sistemas online
  (LatamList, acceso 2026-06-26).
- Clínicas pequeñas pueden gastar 2–4 h/día en llamadas, WhatsApp y remarcaciones;
  no-shows >10–15% señalan problema operativo (blog Jefte Juan, acceso 2026-06-26).

Inferencias:

- Consultorios 1–3 profesionales en UY/BR comparten el patrón (inferido de
  mercado regional; no validado con entrevistas locales).

## Perfil de poblacion afectada {#poblacion}

─── QUIENES SON ───

Nombre del segmento: "Consultorio independiente LATAM — recepción manual"

Demografia: profesionales de salud 30–55 años; recepcionistas/administrativas
25–45 años; pacientes adultos que agendan por teléfono o WhatsApp.

Geografía: urbano/suburbano LATAM; foco inicial Uruguay y Brasil en research
secundario.

Acceso tecnologico: smartphone en recepción; WhatsApp como canal dominante;
conectividad variable en zonas periféricas.

Idioma(s): español y portugués según país.

Tamano estimado: mercado de software de agendamiento médico en Brasil proyectado
USD 320M (2025) → USD 645M (2031); segmento clínicas pequeñas con restricción de
costo (Mobility Foresights, acceso 2026-06-26) — estimación agregada, no
validada para UY.

─── JOBS TO BE DONE ───

Job funcional: llenar la agenda sin errores y reducir no-shows.

Job emocional: sentir control sobre la operación diaria sin estar "apagando
incendios" todo el día.

Job social: proyectar profesionalismo y accesibilidad al paciente.

─── POR QUE FALLA HOY ───

Solución actual: WhatsApp + planilla/papel + llamadas.

Fricción 1: respuestas tardías → paciente busca otro profesional.

Fricción 2: sin recordatorios automáticos → olvido y no-show.

Fricción 3: doble canal (teléfono + online informal) → solapamientos.

─── MOMENTOS DE MAYOR DOLOR ───

Momento 1: lunes por la mañana con cola de mensajes acumulados del fin de semana.

Momento 2: paciente no aparece en horario reservado sin aviso previo.

─── LENGUAJE ───

Para describir el problema: "NO DISPONIBLE — falta entrevista primaria"

Para la solución ideal: "NO DISPONIBLE — falta entrevista primaria"

Palabras que usan: INCIERTO (research secundario sugiere "faltas", "remarcar",
"agenda llena", "WhatsApp")

Palabras que NO usan: INCIERTO

─── DISPOSICION A PAGAR ───

¿Paga por algo parecido hoy? incierto — fuentes secundarias citan planes
USD 15–40/mes en BR para agenda básica (blog Jefte Juan, acceso 2026-06-26).

¿Cuanto valdria resolverlo? INCIERTO sin entrevistas.

## Veredicto hair-on-fire {#hair-on-fire}

¿Es urgente? INCIERTO — Evidencia: literatura y blogs sectoriales describen dolor
operativo frecuente, pero no hay entrevistas con el segmento objetivo.

¿Pagarían por resolverlo? INCIERTO — Evidencia: mercado de scheduling en crecimiento
en BR sugiere demanda, sin confirmación primaria de disposición a pagar en UY/LATAM
pequeño.

Estado de validacion primaria: INCIERTO-NO-VALIDADO

INPUT_REQUEST pendiente: si — request_id ir-001

Conclusion: el research secundario respalda un problema plausible y recurrente en
clínicas pequeñas LATAM, pero sin entrevistas no se puede afirmar hair-on-fire ni
disposición a pagar. El handoff documenta el estado para Cartógrafo con flag
explícito de validación pendiente.

## Fuentes {#fuentes}

- https://latamlist.com/why-the-healthcare-industry-should-automate-their-customer-service/ — acceso: 2026-06-26 — uso: no-shows, saturación recepción, doble reserva
- https://blog.jeftejuan.com.br/automacao-agendamento-clinicas-pequenas/ — acceso: 2026-06-26 — uso: tiempo administrativo, umbrales de no-show, rangos de precio BR
- https://mobilityforesights.com/product/brazil-medical-scheduling-software-market — acceso: 2026-06-26 — uso: tamaño mercado scheduling BR, adopción en clínicas pequeñas

## Handoff esperado

Este output alimenta el handoff `0->1` hacia Cartógrafo.

Skills cubiertas:

- `1.1` — problema validado (research secundario; primaria pendiente)
- `1.2` — perfil de población (segmento nombrado; lenguaje usuario NO DISPONIBLE)
