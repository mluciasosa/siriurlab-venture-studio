# SiriusLabs Venture Engine

Monorepo del MVP de validacion manual del SiriusLabs Venture Engine.

El objetivo del MVP-1 es validar el encadenamiento entre agentes antes de montar infraestructura. El estado vive en archivos versionados por git.

## Estructura

- `knowledge/` — documentacion fuente de agentes, skills y subagentes.
- `development/` — bitacora de construccion del Venture Engine.
- `agents/` — agentes ejecutables como `SKILL.md` (se construyen desde Fase B).
- `contracts/` — contratos de estado, handoff y skill I/O.
- `runs/` — proyectos procesados por el motor (Nubia, Girasol, fixtures manuales).
- `scripts/` — utilidades de validacion del MVP.

## Fase A — QA manual

Todos los comandos se ejecutan desde la raiz del repo.

Prerequisito: Python 3 disponible como `python` en la terminal.

### 1. Parsear contratos JSON

```powershell
python -m json.tool contracts/state.schema.json
python -m json.tool contracts/handoff-v2.schema.json
```

### 2. Crear proyecto de prueba

```powershell
python scripts/new-project.py --project-id proyecto-900-test --name Test --mode create
```

Debe crear:

- `runs/proyecto-900-test/_seed.md`
- `runs/proyecto-900-test/_state.json`
- `runs/proyecto-900-test/_cost-log.md`
- `runs/proyecto-900-test/fase-0/` a `fase-3/`

### 3. Validar handoff correcto

```powershell
python scripts/validate-handoff.py scripts/fixtures/valid/handoff.json
```

Resultado esperado:

```text
PASA: handoff valido
```

### 4. Validar error por skill faltante

```powershell
python scripts/validate-handoff.py scripts/fixtures/missing-skill/handoff.json
```

Resultado esperado: `FALLA` nombrando `1.2`.

### 5. Validar error por ancla faltante

```powershell
python scripts/validate-handoff.py scripts/fixtures/missing-anchor/handoff.json
```

Resultado esperado: `FALLA` nombrando `#poblacion`.

### 6. Reporte de costos

```powershell
python scripts/cost-report.py scripts/fixtures/cost-log/_cost-log.md
```

Debe imprimir costo por fase y `TOTAL`.

## Regla operativa

No avanzar a Fase B hasta que Lucía corra el QA de Fase A, apruebe los resultados y se registre en `development/qa/fase-A.md`.
