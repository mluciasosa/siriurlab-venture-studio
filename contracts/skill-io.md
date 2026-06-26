# Skill I/O — Contratos de Entrada del MVP-1

Este archivo define que debe recibir cada destino del pipeline manual.

Regla canonica:

- Si existe subagente, el ID canonico es el del subagente (`3.A.1`, `5.A.1`, `10.A.1`).
- Si no existe subagente, se usa el ID plano (`1.1`, `2.1`, `4.1`).
- Los aliases existen para resolver documentacion vieja sin duplicar contratos.

## IDs canonicos por fase

| Fase | Agente | Skills canonicas en output |
|---|---|---|
| 0 | Explorador | `1.1`, `1.2` |
| 1 | Cartografo | `2.1`, `2.2` |
| 2 | Analista + Arquitecto de Negocio | `3.A.1`, `3.B.1`, `3.C.1`, `3.D.1`, `4.1`, `4.2`, `4.scope` |
| 3 | Arquitecto UX | `5.A.1`, `5.B.1` |

## Transiciones MVP-1

| Transicion | Destino | Requiere |
|---|---|---|
| `0->1` | Cartografo | `1.1`, `1.2` |
| `1->2` | Analista + Negocio | `2.1`, `2.2` |
| `2->3` | Arquitecto UX | `1.1`, `1.2`, `4.1`, `4.scope` |

## Bloque machine-readable

`scripts/validate-handoff.py` lee el bloque JSON entre los marcadores siguientes.

<!-- skill-io:start -->
```json
{
  "aliases": {
    "3.1": "3.A.1",
    "3.2": "3.B.1",
    "3.3": "3.C.1",
    "3.D": "3.D.1",
    "5.1": "5.A.1",
    "5.2": "5.B.1",
    "6.1": "4.scope",
    "10.1": "10.A.1"
  },
  "transitions": {
    "0->1": {
      "destination": "cartografo",
      "required": ["1.1", "1.2"]
    },
    "1->2": {
      "destination": "analista-negocio",
      "required": ["2.1", "2.2"]
    },
    "2->3": {
      "destination": "arquitecto-ux",
      "required": ["1.1", "1.2", "4.1", "4.scope"]
    }
  },
  "skills": {
    "1.1": {
      "name": "problem-discovery",
      "anchors": ["problema", "hair-on-fire", "fuentes"]
    },
    "1.2": {
      "name": "population-profiling",
      "anchors": ["poblacion"]
    },
    "2.1": {
      "name": "competitive-landscape",
      "anchors": ["mapa-competitivo"]
    },
    "2.2": {
      "name": "solution-research",
      "anchors": ["research-soluciones"]
    },
    "3.A.1": {
      "name": "market-sizing-rigorous",
      "anchors": ["mercado"]
    },
    "3.B.1": {
      "name": "unit-economics-rigorous",
      "anchors": ["unit-economics"]
    },
    "3.C.1": {
      "name": "technical-feasibility-rigorous",
      "anchors": ["viabilidad-tecnica"]
    },
    "3.D.1": {
      "name": "risk-analysis",
      "anchors": ["riesgos"]
    },
    "4.1": {
      "name": "business-model-design",
      "anchors": ["modelo-negocio"]
    },
    "4.2": {
      "name": "go-to-market-strategy",
      "anchors": ["gtm"]
    },
    "4.scope": {
      "name": "product-scope",
      "anchors": ["scope-producto"]
    },
    "5.A.1": {
      "name": "user-journey-mapping",
      "anchors": ["user-journeys"]
    },
    "5.B.1": {
      "name": "wireframes",
      "anchors": ["wireframes"]
    }
  }
}
```
<!-- skill-io:end -->

## Notas de validacion

- `required_by_destination` del handoff debe usar IDs canonicos o aliases resolubles.
- `outputs[].skill_id` debe cubrir todos los skills requeridos.
- Cada `outputs[].output_ref` debe incluir una ancla existente en el markdown referenciado.
- La existencia de una ancla se valida literalmente como un heading markdown con `{#ancla}` o como texto `#ancla` en el documento.
