# FASE 0 — EXPLORADOR

Proyecto: proyecto-903-qa | Fecha: 2026-06-26 | ODS: 3 — Salud y bienestar

## Problema validado {#problema}

─── EL PROBLEMA ───

Qué es: consultorios pequeños pierden turnos e ingresos porque la agenda depende de WhatsApp, llamadas, calendario y memoria de recepción.

Cuándo ocurre: cuando pacientes olvidan el turno, piden reprogramar fuera de horario o la recepción maneja varios profesionales.

Cómo se ve: mensajes acumulados, doble reserva ocasional, huecos por no-show y profesionales interrumpiendo consulta para coordinar.

Solución actual del usuario: WhatsApp Business, Google Calendar, planilla y llamadas manuales.

─── MAGNITUD Y FRECUENCIA ───

Frecuencia: diaria.

Gravedad (1-5): 4 — impacta ingresos y carga operativa.

─── EVIDENCIA VS INFERENCIA ───

Evidencia confirmada:

- Fixture QA: 5/5 consultorios simulados usan WhatsApp como canal principal.
- Fixture QA: 4/5 reportan no-shows semanales.

Inferencias:

- El MVP debe reducir mensajes repetitivos y hacer visible el estado de cada turno.

## Perfil de poblacion afectada {#poblacion}

─── QUIENES SON ───

Nombre del segmento: consultorio independiente con recepción manual.

Demografía: profesionales de salud 30-55 años y recepcionistas 25-45 años; 1-3 profesionales por consultorio.

Geografía: Uruguay urbano, extensible a LATAM.

Acceso tecnológico: WhatsApp, smartphone y calendario digital básico.

Idioma(s): español.

Tamaño estimado: INCIERTO en fixture; suficiente para QA técnico.

─── JOBS TO BE DONE ───

Job funcional: confirmar turnos y reducir no-shows sin sumar trabajo manual.

Job emocional: sentir control de la agenda.

Job social: verse profesional frente al paciente.

─── MOMENTOS DE MAYOR DOLOR ───

Momento 1: paciente no aparece y el hueco queda perdido.

Momento 2: reprogramación fuera de horario genera mensajes pendientes.

─── LENGUAJE ───

Para describir el problema: "me quedan huecos y no me avisan".

Para la solución ideal: "que mande recordatorio solo y me diga si confirma".

## Veredicto hair-on-fire {#hair-on-fire}

¿Es urgente? SI — evidencia fixture QA.

¿Pagarían por resolverlo? SI — rango fixture USD 20-40/mes.

Estado de validación primaria: VALIDADO PARA QA TECNICO.

INPUT_REQUEST pendiente: no.

Conclusión: Fase 0 queda sin bloqueo para QA Fase D.

## Fuentes {#fuentes}

- Fixture interno QA Fase D — acceso: 2026-06-26 — uso: simular Fase 0 validada.

## Handoff esperado

Skills cubiertas:

- `1.1` — problema validado
- `1.2` — perfil de población
