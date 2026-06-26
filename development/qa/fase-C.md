# QA Fase C — Cadena de decisión + Gate 0-2

Fecha: 2026-06-26
Proyecto: `proyecto-902-qa`
Ejecutado por: agente en Cursor
Estado: **CERRADA** — QA técnico PASA; aprobado por Lucía el 2026-06-26.

## Alcance

Se corrió una cadena limpia sobre `proyecto-902-qa` usando una Fase 0 validada
como fixture técnico. El objetivo no fue validar el negocio de clínicas, sino
probar el encadenamiento:

Fase 0 → Fase 1 Cartógrafo → Fase 2 Analista + Negocio → Guardian 10.A.

## Comandos ejecutados

```powershell
python scripts/new-project.py --project-id proyecto-902-qa --name "QA Fase C" --mode create --force
python scripts/validate-handoff.py runs/proyecto-902-qa/fase-0/handoff.json --transition 0->1
python scripts/validate-handoff.py runs/proyecto-902-qa/fase-1/handoff.json --transition 1->2
python scripts/validate-handoff.py runs/proyecto-902-qa/fase-2/handoff.json --transition 2->3
python -m json.tool runs/proyecto-902-qa/_state.json
python scripts/cost-report.py runs/proyecto-902-qa/_cost-log.md
```

## Artefactos producidos

| Fase | Agente | Artefacto |
|---|---|---|
| Kickoff | Shifu | `runs/proyecto-902-qa/plan-maestro.md` |
| 0 | Explorador | `runs/proyecto-902-qa/fase-0/output.md` |
| 0 | Explorador | `runs/proyecto-902-qa/fase-0/handoff.json` |
| 1 | Cartógrafo | `runs/proyecto-902-qa/fase-1/output.md` |
| 1 | Cartógrafo | `runs/proyecto-902-qa/fase-1/handoff.json` |
| 2 | Analista + Negocio | `runs/proyecto-902-qa/fase-2/output.md` |
| 2 | Analista + Negocio | `runs/proyecto-902-qa/fase-2/handoff.json` |
| Gate 0-2 | Guardián 10.A | `runs/proyecto-902-qa/fase-2/gate-audit.md` |
| Estado | Sistema | `runs/proyecto-902-qa/_state.json` |
| Costos | Sistema | `runs/proyecto-902-qa/_cost-log.md` |

## Resultados

- Handoff `0->1`: **PASA**.
- Handoff `1->2`: **PASA**.
- Handoff `2->3`: **PASA**.
- `fase-1/output.md` contiene `#mapa-competitivo`, `#research-soluciones` y `#gaps`.
- `fase-2/output.md` contiene secciones en orden: Analista completo → Negocio → scope.
- `fase-2/output.md#scope-producto` existe y es referenciable.
- `fase-2/handoff.json` referencia `#scope-producto` y también `../fase-0/output.md#problema` / `#poblacion`.
- `fase-2/gate-audit.md` contiene auditorías separadas 10.A.1, 10.A.2 y 10.A.3.
- Cada auditoría usa criterios binarios y bloqueantes propios.
- `_state.json` registra `gate_decisions[]` con `covers_phases: [0, 1, 2]` y `audits[]`.
- Se simuló blocker en 10.A.3:
  - falta diferenciación real de planes/pricing.
  - falta validación chica de USD 500 antes de gasto mayor.
- El gate no habilita GO automático: `ceo_decision` queda `ITERAR`.
- `_cost-log.md` registra fases 1, 2 y Guardian 10.A.

## Checklist Definition of Done

- [x] Handoff 0->1 ya aprobado sigue validando después de agregar fase 1 y fase 2.
- [x] Cartógrafo produce `fase-1/output.md` con 2.1 y 2.2 presentes.
- [x] `scripts/validate-handoff.py` valida handoff 1->2 a la primera.
- [x] `fase-2/output.md` incluye secciones de Analista y Negocio en orden.
- [x] `fase-2/output.md#scope-producto` existe y es referenciable.
- [x] `fase-2/handoff.json` hacia UX referencia `#scope-producto`.
- [x] `fase-2/gate-audit.md` contiene 10.A.1, 10.A.2 y 10.A.3 como auditorías separadas.
- [x] Cada auditoría mantiene criterios binarios y bloqueantes propios.
- [x] `_state.json` puede registrar una decisión con `covers_phases: [0, 1, 2]` y `audits[]`.
- [x] Al simular un bloqueante en 10.A.3, el paquete muestra el bloqueante y no habilita GO automático.
- [x] `_cost-log.md` registra costos de fase 1 y fase 2.
- [x] QA aprobado por Lucía (cierre formal).

## Veredicto técnico

**PASA.**

La Fase C queda técnicamente validada: la cadena produce outputs y handoffs
referenciables, y el Gate 0-2 consolidado detecta un blocker sin permitir GO
automático.

## Cierre

Aprobado por Lucía el 2026-06-26. Fase C cerrada.
