# Subagentes Técnicos del Constructor
### Equipo especializado para desarrollo de MVP con calidad impecable

> **Por qué existen:**  
> El Agente 6 (Constructor) es donde las decisiones se convierten en código real. Es el único punto donde un error tiene consecuencias técnicas acumulativas. Un solo agente generalista no puede hacer arquitectura, desarrollo, testing, seguridad y documentación bien al mismo tiempo.

---

## Principio rector

La calidad del output no viene del modelo. Viene de la especificación. Un agente produce código de calidad senior cuando la spec es inequívoca, el plan de tests está bloqueado antes de que exista una línea de implementación, y el PR no puede abrirse sin pasar gates mecánicos.

**Spec primero → Tests antes del código → Gates automáticos antes del merge.**

---

## Los 5 Subagentes

```
┌──────────────────────────┐
│   AGENTE 6 — CONSTRUCTOR  │
│   (orquesta a los 5)      │
└───────────┬──────────────┘
            │
  ┌─────────┼──────────────┬──────────┬──────────┐
  │         │              │          │          │
 6.A       6.B            6.C        6.D        6.E
Arq.     Dev.Core        QA/Test    Security   Docs
Técnica                            DevSecOps   Tech
```

**Flujo obligatorio:**
```
SPEC → ARQUITECTURA (6.A) → TEST PLAN (6.C) → DESARROLLO (6.B) → REVIEW (6.D+6.C) → DOCS (6.E) → GATE 4
```

Los tests se escriben ANTES del código. Esta es la regla más importante del área técnica.

---

# SUBAGENTE 6.A — ARQUITECTO TÉCNICO

**Función:** Diseñar la arquitectura completa antes de que se escriba una línea de código. Produce Architecture Decision Records, diagrama de componentes, contratos de API y modelo de datos.

---

## SKILL 6.A.1 — architecture-design

**Trigger:** Inicio de Fase 4, antes de cualquier código.

**INPUT obligatorio:** Scope MVP (6.1) + Stack tecnológico (6.2) + Flujo de usuario (5.1) + restricciones no funcionales.

**OUTPUT:**
```
ARCHITECTURE DESIGN DOCUMENT — [Proyecto]

─── PATRÓN ARQUITECTÓNICO ───
Elegido: [monolito modular / serverless / híbrido]
Razón: [la arquitectura más simple que cumpla los requisitos]

─── DIAGRAMA DE COMPONENTES ───
[ASCII diagram de módulos y relaciones]

─── MÓDULOS Y RESPONSABILIDADES ───
Módulo [nombre]:
  Responsabilidad única: [en una oración]
  Expone: [interfaces/endpoints]
  Consume: [dependencias]

─── CONTRATOS DE API ───
[METHOD] /api/[recurso]
  Request: { campo: tipo }
  Response 200: { campo: tipo }
  Response 4xx: { error: string, code: string }
  Validaciones: [lista]

─── MODELO DE DATOS ───
Tabla [nombre]: { id, campos, created_at, updated_at }
Índices: [con razón]

─── ARCHITECTURE DECISION RECORDS (ADRs) ───
ADR-001: [título]
  Contexto: [por qué había que decidir]
  Decisión: [qué se eligió]
  Consecuencias: [positivas y negativas]
  Alternativas descartadas: [con razón]

─── DEUDA TÉCNICA PRE-ACEPTADA ───
[Decisiones buenas para MVP que hay que revisar al escalar]
```

**REGLAS:**
- La arquitectura más simple siempre gana sobre la más elegante.
- Monolito modular es correcto para el MVP en el 90% de los casos. Microservicios en MVP = sobreingeniería.
- Cada módulo tiene UNA responsabilidad. Si no podés describirla en una oración, dividir.
- Los contratos de API se definen antes de implementar. Cambiarlos después rompe el frontend.
- Cada ADR documenta alternativas descartadas. Sin esto, el equipo futuro repite las mismas decisiones malas.

---

## SKILL 6.A.2 — environment-setup

**Trigger:** Inmediatamente después de la arquitectura.

**OUTPUT:**
```
ENVIRONMENT SETUP GUIDE

─── ESTRUCTURA DE CARPETAS ───
project/
├── src/
│   ├── modules/        # Un folder por módulo de negocio
│   ├── shared/         # Tipos, utils, constantes compartidos
│   └── infrastructure/ # Config DB, auth, storage
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/
├── .env.example        # Todas las variables (sin valores reales)
└── README.md

─── .env.example ───
[Lista completa de variables con descripción y ejemplo]

─── SCRIPTS (package.json) ───
dev / test / test:unit / test:integration / build / lint / typecheck

─── INSTRUCCIONES SETUP LOCAL ───
Prerequisitos + pasos + comando de verificación

─── CONVENCIONES ───
Naming: camelCase para variables, PascalCase para tipos, kebab-case para archivos
Commits: Conventional Commits (feat/fix/chore/docs/test)
Branches: feature/nombre, fix/nombre
```

**REGLAS:**
- .env.example tiene TODAS las variables. Nunca una sin documentar.
- La estructura refleja módulos, no layers técnicos (no controllers/, models/ como raíz).
- Los 5 scripts fundamentales siempre presentes: dev, test, build, lint, typecheck.

---

# SUBAGENTE 6.B — DESARROLLADOR CORE

**Función:** Escribir el código del MVP. Solo las 3 features del scope. Código limpio, tipado, con manejo de errores, que hace pasar los tests de 6.C.

---

## SKILL 6.B.1 — feature-implementation

**Trigger:** Para cada feature. "implementar [feature]", "codear [feature]".

**INPUT obligatorio:** Architecture Design (6.A.1) + Contratos de API + **Tests de 6.C.1 (OBLIGATORIO — sin tests no hay implementación)** + Flujo de usuario (5.1).

**CHECKLIST DE IMPLEMENTACIÓN (todo en verde antes de entregar):**
```
─── CÓDIGO LIMPIO ───
□ Nombres descriptivos sin "y" (si hay "y", dividir la función)
□ Funciones ≤20 líneas
□ Complejidad ciclomática ≤10 por función
□ Sin números mágicos (usar constantes con nombre)
□ Comentarios solo para "por qué", nunca para "qué"

─── TIPOS ───
□ TypeScript strict mode activado
□ Tipos explícitos en todos los parámetros y returns
□ Sin `any` (usar `unknown` con type guard si necesario)
□ Interfaces para todos los objetos de dominio

─── MANEJO DE ERRORES ───
□ Sin catch vacíos
□ Errores de servidor logueados con contexto
□ Errores de cliente con mensaje actionable (no stack trace)
□ Timeouts en todas las llamadas externas

─── SEGURIDAD BÁSICA ───
□ Input validation en TODOS los endpoints (server-side)
□ Sin datos sensibles en logs
□ Sin credenciales hardcodeadas
□ Sanitización de outputs al DOM

─── TESTS ───
□ Todos los tests de 6.C pasan en verde
□ Cobertura de la feature ≥80%
□ Sin tests comentados o skipped sin razón
```

**FLUJO:**
1. Leer los tests de 6.C. Si no existen → NO empezar.
2. Implementar lógica de negocio (parte pura, sin side effects).
3. Conectar con infraestructura (DB, APIs externas).
4. Implementar endpoints según contratos de 6.A.1.
5. Implementar UI según flujo de 5.1.
6. Correr tests → si alguno falla, corregir el código (nunca el test).
7. Correr linter → 0 warnings.
8. Correr typecheck → 0 errores.
9. Completar el checklist → solo entregar con todo en verde.

**REGLAS:**
- `any` en TypeScript = error. Sin excepción.
- PR con `console.log` de debug = rechazado.
- El código se escribe para ser leído, no para funcionar.
- Cyclomatic complexity >10 = señal para dividir la función.

---

## SKILL 6.B.2 — code-review-self

**Trigger:** Antes de entregar cualquier feature al QA.

**OUTPUT:**
```
SELF-REVIEW — [Feature]

Archivos modificados: [N] | Líneas +[N] -[N] | Tests +[N]

Checklist: [copiado de 6.B.1 con estado de cada ítem]

Puntos de atención para el reviewer:
- "[decisión que tomé que merece revisión — por qué lo hice así]"

Deuda técnica nueva (si hay):
- [descripción] — issue: [link]

─── PR DESCRIPTION ───
## ¿Qué hace este PR?
[descripción en lenguaje simple]

## ¿Por qué?
[contexto: qué hipótesis valida]

## Cómo testear
1. [paso] 2. [paso] 3. [resultado esperado]

## Checklist
- [ ] Tests pasando | Linter pasando | Types pasando | Docs actualizadas
```

---

# SUBAGENTE 6.C — QA / TESTER

**Función:** Escribir el plan de tests ANTES del código. Ejecutar tests. Mantener cobertura ≥80%. Validar que el MVP hace exactamente lo que la hipótesis dice.

---

## SKILL 6.C.1 — test-plan-writing

**Propósito:** Tests escritos ANTES del código. El Developer Core no puede empezar hasta que este documento exista. Es BLOQUEANTE.

**Trigger:** Después de la arquitectura, ANTES del desarrollo.

**INPUT obligatorio:** Architecture Design (6.A.1) + Contratos de API + Flujo de usuario (5.1) + Scope MVP (6.1).

**OUTPUT:**
```
TEST PLAN — [Feature/Proyecto]
Estado: BLOQUEANTE para iniciar desarrollo

─── PIRÁMIDE DE TESTS ───
Unit: [N] — Integration: [N] — E2E: [N, mínimos en MVP]

─── UNIT TESTS ───
TEST: "debería [hacer X] cuando [condición Y]"
  Input: [valores exactos]
  Expected: [resultado exacto]
  Edge case: [input vacío/null/inválido]

TEST: "[error case]"
  Input: [input inválido]
  Expected error: [error específico]

[un test por comportamiento, no por función]

─── INTEGRATION TESTS ───
TEST: "POST /api/[recurso] debería [comportamiento] y devolver [status]"
  Arrange: [estado inicial de DB / mocks]
  Act: [request: método, URL, headers, body exactos]
  Assert: [status, response body, estado DB después]

TEST: "[error case: campo faltante/inválido]"
  [misma estructura]

─── EDGE CASES OBLIGATORIOS ───
□ Input vacío/null en cada campo obligatorio
□ Strings con caracteres especiales (XSS attempt)
□ Payload demasiado grande
□ Dos requests simultáneos al mismo recurso
□ Token expirado o inválido
□ Timeout de servicio externo (LLM API, Stripe)
□ Rate limiting

─── CRITERIO DE DONE ───
□ Cobertura total ≥80%
□ Cobertura de paths críticos (auth, pagos, core) = 100%
□ 0 tests failing | 0 tests skipped sin razón
□ Todos los edge cases tienen test
```

**REGLAS:**
- Tests escritos primero, código después. Sin excepciones.
- Un test por comportamiento, no por función.
- Los tests testean comportamiento observable, no implementación interna.
- Un test que no puede fallar no es un test. Verificar que falla antes de que exista el código.
- Mocks solo para servicios externos (DB, APIs). Nunca para la lógica propia.

---

## SKILL 6.C.2 — test-execution-report

**Trigger:** Después de que 6.B entrega una feature.

**OUTPUT:**
```
TEST EXECUTION REPORT — [Feature] — [fecha]

Totales: [N] | Passing: [N] ✅ | Failing: [N] ❌ | Skipped: [N] ⚠️

─── COBERTURA ───
Total: [%] — meta ≥80% [✅/❌]
Branches: [%] | Functions: [%] | Lines: [%]
Paths críticos: auth [%] / payments [%] / core [%] — meta 100%

─── TESTS FALLANDO ───
TEST: [nombre] | Error: [mensaje] | Causa: [análisis] | Acción: [de quién]

─── EDGE CASES SIN COBERTURA ───
[Lista de edge cases del plan sin test]

─── VEREDICTO ───
APROBADO: cobertura ≥80%, 0 failing, edge cases cubiertos
RECHAZADO: [razón] — devuelto a 6.B con lista de correcciones
```

**REGLAS:** Cobertura <80% = RECHAZADO automático. 1 test failing = RECHAZADO. Tests skipped sin razón = RECHAZADO.

---

## SKILL 6.C.3 — regression-testing

**Trigger:** Después de cualquier modificación al código aprobado.

**OUTPUT:**
```
REGRESSION REPORT — [fecha]
Cambio: [descripción del PR]
Tests corridos: [N] | Nuevos failing: [N]

[Si hay failing: qué se rompió, quién lo arregla, prioridad]

VEREDICTO: LIMPIO / REGRESIÓN DETECTADA
```

---

# SUBAGENTE 6.D — SECURITY / DEVSECOPS

**Función:** Seguridad en cada PR. Pipeline CI/CD configurado. Gestión de secretos. En 2026, la seguridad se construye desde el inicio — no es un paso final.

---

## SKILL 6.D.1 — security-review

**Trigger:** En cada PR antes del merge.

**INPUT obligatorio:** Código del PR + Architecture Design (para contexto) + sensibilidad de datos (baja/media/alta).

**OUTPUT:**
```
SECURITY REVIEW — PR: [nombre]

─── OWASP TOP 10 ───
A01 Broken Access Control:     [✅/❌/N/A]
A02 Cryptographic Failures:    [✅/❌/N/A]
A03 Injection:                 [✅/❌/N/A]
A04 Insecure Design:           [✅/❌/N/A]
A05 Security Misconfiguration: [✅/❌/N/A]
A06 Vulnerable Components:     [✅/❌/N/A]
A07 Auth/Session Mgmt:         [✅/❌/N/A]
A08 Data Integrity:            [✅/❌/N/A]
A09 Logging/Monitoring:        [✅/❌/N/A]
A10 SSRF:                      [✅/❌/N/A]

─── CHECKLIST ───
□ Sin credenciales/API keys/secretos en el código
□ Input validation en todos los endpoints (server-side)
□ Outputs sanitizados antes de ir al DOM
□ Queries con parámetros (nunca concatenación de strings)
□ Auth verificada en CADA endpoint protegido
□ Rate limiting en endpoints sensibles (auth, pagos)
□ Sin datos sensibles en logs (passwords, tokens, PII)
□ CORS configurado (no `*` en producción)
□ `npm audit` sin vulnerabilidades high/critical

─── ISSUES ENCONTRADOS ───
CRÍTICO — [descripción] — [archivo:línea] — [cómo corregir]
ALTO — [descripción] — [archivo:línea] — [cómo corregir]
MEDIO — [descripción] — [recomendación]

─── VEREDICTO ───
APROBADO: 0 issues críticos, 0 issues altos
RECHAZADO: [N] críticos / [N] altos — devuelto a 6.B
```

**REGLAS:**
- Issue CRÍTICO = merge bloqueado. Sin excepción.
- Issue ALTO = merge bloqueado. Sin excepción.
- `npm audit` con high/critical = merge bloqueado.
- Credenciales en código = KILL del PR + rotar credenciales inmediatamente.

---

## SKILL 6.D.2 — cicd-pipeline-setup

**Trigger:** Inicio de Fase 4, una vez. "configurar CI/CD", "pipeline", "GitHub Actions".

**OUTPUT: `.github/workflows/ci.yml`**

```yaml
# ESTRUCTURA:
# Push → CI (lint + typecheck + test)
# PR a main → CI + Security scan
# Merge a main → CI + Security + Deploy staging (automático)
# Tag release → CI + Security + Deploy producción (aprobación manual)

name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20', cache: 'npm' }
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck

  test:
    needs: quality
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run test:unit -- --coverage
      - run: npm run test:integration
        env:
          DATABASE_URL: ${{ secrets.TEST_DATABASE_URL }}
      - uses: codecov/codecov-action@v4
        with: { fail_ci_if_error: true, threshold: 80 }

  security:
    needs: quality
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm audit --audit-level=high
      - uses: trufflesecurity/trufflehog@main

  deploy-staging:
    needs: [test, security]
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    # [pasos de deploy a staging]

  deploy-production:
    needs: deploy-staging
    environment: production  # Requiere aprobación manual
    if: startsWith(github.ref, 'refs/tags/v')
    # [pasos de deploy a producción]
```

**REGLAS:**
- Ningún PR se mergea sin que un engineer apruebe el reporte de CI. El CI puede rechazar automáticamente, pero el approve siempre es humano.
- Deploy a staging = automático al mergear a main.
- Deploy a producción = SIEMPRE aprobación manual. Sin excepción.
- Si algún job falla, el pipeline se detiene. No hay "deployar igual".

---

## SKILL 6.D.3 — secrets-management

**Trigger:** Al inicio y cada vez que se agrega una integración nueva.

**OUTPUT:**
```
SECRETS MANAGEMENT PLAN

─── INVENTARIO ───
| Variable | Qué es | Entorno | Dónde vive | Rotación |
| DATABASE_URL | Conexión DB | prod/staging | GitHub Secrets | 90d |
| ANTHROPIC_API_KEY | API Claude | prod/staging | GitHub Secrets | 30d |
| STRIPE_SECRET_KEY | Pagos | prod | GitHub Secrets | 90d |

─── CHECKLIST ───
□ .env.example con todas las variables (sin valores)
□ .gitignore incluye .env y archivos de secretos
□ Sin secretos hardcodeados (verificado con secrets scan)
□ Todos los secretos en GitHub Secrets
□ Documentado quién tiene acceso a producción
```

---

# SUBAGENTE 6.E — TECH WRITER (Documentación)

**Función:** Documentación técnica que permite a cualquier developer entender, instalar, usar y mantener el MVP sin hablar con quien lo construyó. Es parte del Definition of Done — no un extra.

---

## SKILL 6.E.1 — readme-writing

**Trigger:** Al final de la Fase 4, antes del gate 4.

**Criterio de calidad:** El setup funciona en <15 minutos en una máquina limpia.

**OUTPUT estructura:**
```markdown
# [Nombre del Proyecto]
> [Qué hace, para quién, con qué tecnología — 1 oración]

## Qué hace este proyecto
[Problema que resuelve + cómo + quién lo usa]

## Requisitos
[Node.js ≥X, Docker, etc. — versiones exactas]

## Setup en 5 minutos
[Comandos ejecutables + verificación de que funcionó]

## Variables de entorno
| Variable | Descripción | Ejemplo | Requerida |

## Arquitectura
[ASCII diagram + link a docs/architecture.md]

## Scripts
npm run dev / test / build / lint / typecheck

## Tests
Cobertura: [X%] | Cómo correr

## Deploy
Staging: automático al merge a main
Producción: tag + aprobación manual

## Estructura del proyecto
[árbol de carpetas comentado]
```

**REGLAS:**
- Los comandos se prueban antes de documentarlos. Un comando roto en README es un bug.
- Los tiempos son reales (15 min). Si tarda más, el setup es demasiado complejo.
- El badge de coverage muestra el número real.

---

## SKILL 6.E.2 — api-documentation

**Trigger:** Al finalizar el desarrollo. "documentar la API", "API docs", "endpoints".

**OUTPUT por endpoint:**
```markdown
## [METHOD] /api/[recurso]
[Descripción de qué hace]

**Request**
```json
{ "campo": "tipo (required/optional) — descripción" }
```

**Response 200** / **Response 401** / **Response 400** / **Response 429** / **Response 500**
[con ejemplos en JSON]

**Ejemplo con curl** (ejecutable sin modificaciones)
```bash
curl -X POST https://[proyecto].vercel.app/api/[recurso] \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"campo": "valor"}'
```
```

**REGLAS:**
- Cada endpoint documenta TODOS los status codes posibles.
- Los ejemplos con curl son ejecutables sin modificaciones.
- Los tipos de campos son exactos (no "string" — "email válido", "UUID v4").

---

## SKILL 6.E.3 — runbook

**Trigger:** Antes del primer deploy a producción.

**OUTPUT estructura:**
```markdown
# Runbook — [Proyecto]

## Health check
[Comando + respuesta esperada]

## Deploys
Staging: merge a main → automático
Producción: tag vX.X.X → aprobación manual → verificar health check

## Rollback
[Pasos exactos para volver al deployment anterior]

## Problemas comunes
### [Síntoma] → [Pasos de diagnóstico] → [Solución]
### Deploy fallido / 502-503 / DB lenta / ...

## Contactos de emergencia
[Quién contactar + links a status pages de servicios externos]
```

---

## Definition of Done — MVP completo

Un MVP está **done** cuando cumple TODOS estos criterios:

```
─── FUNCIONALIDAD ───
□ Las 3 features del scope funcionan end-to-end
□ Time-to-value ≤3 minutos (medido, no estimado)

─── CÓDIGO ───
□ Linter: 0 warnings | Type checker: 0 errores
□ Cyclomatic complexity ≤10 en todas las funciones
□ Sin `any`, sin `console.log`, sin credenciales en código

─── TESTS ───
□ Cobertura total ≥80% | Paths críticos = 100%
□ 0 failing | 0 skipped sin razón documentada
□ Todos los edge cases del plan tienen test

─── SEGURIDAD ───
□ OWASP Top 10 review: 0 issues críticos/altos
□ Secrets scan: 0 secretos en código
□ npm audit: 0 vulnerabilidades high/critical

─── CI/CD ───
□ Pipeline corriendo | Deploy staging automático
□ Deploy producción requiere aprobación manual
□ Rollback documentado y probado

─── DOCUMENTACIÓN ───
□ README: setup <15 min en máquina limpia
□ API docs: todos los endpoints con curl ejecutable
□ ADRs: todas las decisiones arquitectónicas documentadas
□ Runbook: problemas comunes y procedimientos de rollback
□ .env.example: todas las variables documentadas

─── ANALYTICS ───
□ Eventos críticos instrumentados (skill 6.3)
□ Funnel de conversión trazable end-to-end

─── GATE 4 ───
□ Aprobado por el Guardián (Agente 10)
□ Aprobado por revisión humana (human-in-loop obligatorio)
```

---

## Cuándo agregar subagentes adicionales

Los 5 subagentes cubren el 95% de los MVPs. Casos especiales:

| Situación | Subagente adicional |
|---|---|
| Datos médicos o financieros | Agente de Compliance (HIPAA, PCI-DSS) |
| ML/IA propia (no solo APIs) | Agente de MLOps |
| Mobile nativo (iOS/Android) | Agente de Mobile Dev |
| Infraestructura custom (no serverless) | Agente de DevOps/Infra |
| Performance crítica (<50ms) | Agente de Performance |

---

*SiriusLabs — siriuslabs.uy@gmail.com  
Actualizar cuando se detecte un patrón de error recurrente en los MVPs entregados.*
