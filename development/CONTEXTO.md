# Contexto de Construccion del MVP

## Proposito

Esta carpeta documenta como construimos el SiriusLabs Venture Engine a si mismo.

No es parte del pipeline de proyectos. `runs/` es donde el motor procesa ventures como Nubia o Girasol. `development/` es la bitacora de construccion del motor: roadmap, decisiones de diseno, notas de avance y resultados de QA.

## MVP-1

El MVP-1 es una validacion manual en Cursor. El objetivo no es montar infraestructura ni construir la app real, sino probar si los agentes pueden encadenarse con contratos claros.

El transporte inicial son archivos versionados en git:

- `agents/` contiene los agentes ejecutables como `SKILL.md`.
- `contracts/` contiene los contratos que validan entradas y salidas.
- `runs/` contiene el estado de cada proyecto procesado.
- `development/` contiene la memoria de construccion del sistema.

## Que valida

### Validacion 1: encadenamiento

El output de una fase debe entrar limpio a la siguiente sin edicion manual.

Metas:

- Ediciones manuales de handoff por fase: <= 1.
- Handoffs que pasan `validate-handoff.py` a la primera: >= 80%.
- Cada output respeta la plantilla exacta de su skill.

### Validacion 2: gate e input humano

El Guardian debe producir un paquete de decision accionable, y los pedidos de input humano deben ser autocontenidos.

Metas:

- Decision CEO con paquete del Guardian: <= 2 minutos.
- `INPUT_REQUEST` entendible sin contexto extra.
- Veredicto claro: GO, ITERAR o KILL.

### Validacion 3: viabilidad economica

El MVP debe medir cuanto cuesta en tokens llevar un venture de fase 0 a fase 3.

Metas:

- Costo total Fase 0->3 registrado en USD.
- Costo por fase identificado.
- Decision informada sobre si el costo cierra contra el valor del venture.

## Scope MVP-1

El MVP-1 llega hasta Fase 3 del sistema:

- Fase 0: Explorador.
- Fase 1: Cartografo.
- Fase 2: Analista + Arquitecto de Negocio.
- Fase 3: Arquitecto UX, solo 5.A + 5.B.

No incluye:

- Construccion de la app real.
- Agente 6 Constructor.
- Agentes 7, 8 y 9.
- Infraestructura autonoma.
- ClickUp, Postgres o Inngest.
- UX de alta fidelidad, accesibilidad completa o design handoff.

## Principios

- Barato: validar con archivos y ejecucion manual antes de montar infraestructura.
- Gradual: cada fase debe ser construible y testeable de forma aislada.
- Escalable: el contrato I/O del agente no cambia cuando pasemos a automatizacion.
- Estado en archivos: si no esta registrado en archivo, no existe para el siguiente agente.
- Validacion antes que construccion: no pasar de fase sin QA aprobado.

## Fuentes

- `knowledge/MVP-construccion-cursor-venture-engine.md`
- `knowledge/equipo-agentes-venture-studio.md`
- `knowledge/skills-especificacion-venture-engine.md`
- `.cursor/rules/venture-engine-core.mdc`
- `.cursor/rules/venture-engine-agent-io.mdc`
- `.cursor/rules/venture-engine-handoffs-gates.mdc`
- `.cursor/rules/venture-engine-build-order.mdc`
