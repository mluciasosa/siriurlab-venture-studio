# Plantillas por Fase — MVP-1

Este documento lista las secciones y anclas esperadas por fase. Las plantillas completas de contenido se construyen en las fases B-D; en Fase A solo fijamos el contrato de anclas para validar handoffs.

## Convencion de anclas

Cada seccion que pueda ser referenciada desde `handoff.json` debe incluir un heading markdown con ancla explicita:

```markdown
## Problema validado {#problema}
```

`validate-handoff.py` tambien acepta la forma literal `#problema` dentro del markdown para facilitar fixtures manuales, pero las plantillas reales deben preferir `{#ancla}`.

---

## Fase 0 — Explorador

Archivo: `runs/[project]/fase-0/output.md`

Anclas requeridas:

- `#problema` — Documento de problema validado (skill 1.1)
- `#poblacion` — Perfil de poblacion afectada (skill 1.2)
- `#hair-on-fire` — Veredicto hair-on-fire
- `#fuentes` — Fuentes y fecha de acceso

Handoff principal:

- `0->1` hacia Cartografo
- Requiere `1.1`, `1.2`

---

## Fase 1 — Cartografo

Archivo: `runs/[project]/fase-1/output.md`

Anclas requeridas:

- `#mapa-competitivo` — Landscape competitivo (skill 2.1)
- `#research-soluciones` — Research de soluciones / estado del arte (skill 2.2)
- `#gaps` — Gaps y oportunidades

Handoff principal:

- `1->2` hacia Analista + Negocio
- Requiere `2.1`, `2.2`

---

## Fase 2 — Analista + Arquitecto de Negocio

Archivo: `runs/[project]/fase-2/output.md`

Anclas requeridas:

- `#mercado` — Analisis de mercado (3.A.1)
- `#unit-economics` — Finanzas / unit economics (3.B.1)
- `#viabilidad-tecnica` — Viabilidad tecnica (3.C.1)
- `#riesgos` — Riesgos y kill criteria (3.D.1)
- `#modelo-negocio` — Modelo de negocio (4.1)
- `#gtm` — Go-to-market (4.2)
- `#scope-producto` — Scope de producto equivalente a 6.1, producido por Negocio

Handoff principal:

- `2->3` hacia Arquitecto UX
- Requiere `1.1`, `1.2`, `4.1`, `4.scope`

Gate:

- `fase-2/gate-audit.md`
- Contiene auditorias 10.A.1, 10.A.2 y 10.A.3 separadas

---

## Fase 3 — Arquitecto UX reducido

Archivo: `runs/[project]/fase-3/output.md`

Anclas requeridas:

- `#user-journeys` — User journeys / arquitectura de informacion (5.A.1)
- `#wireframes` — Wireframes baja fidelidad (5.B.1)

Gate:

- `fase-3/gate-audit.md`
- Gate 3 reducido: coherencia journeys/wireframes vs problema, poblacion y scope
- No audita WCAG, design system ni design handoff en MVP-1
