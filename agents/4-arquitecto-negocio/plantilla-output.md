# FASE 2 — ANALISTA + ARQUITECTO DE NEGOCIO

Proyecto: [project_id] | Fecha: [YYYY-MM-DD] | Fuente Fase 1: `fase-1/output.md`

## Veredicto consolidado del Analista

─── RESUMEN ───

Mercado (3.A): [VERDE/AMARILLO/ROJO] — [razon en una oracion]

Financiero (3.B): [VERDE/AMARILLO/ROJO] — [razon en una oracion]

Tecnico (3.C): [VERDE/AMARILLO/ROJO] — [razon en una oracion]

Riesgo (3.D): [VERDE/AMARILLO/ROJO] — [razon en una oracion]

─── VEREDICTO ───

Estado: [GO / ITERAR / KILL]

Razon: [2-3 oraciones basadas en evidencia]

─── LOS 3 NUMEROS QUE MAS IMPORTAN ───

SOM: [monto] — escenario base — fuente/supuesto: [detalle]

LTV/CAC: [ratio] — escenario base — fuente/supuesto: [detalle]

Tiempo a break-even: [meses] — escenario conservador — fuente/supuesto: [detalle]

─── CONDICION CRITICA ───

"[supuesto mas fragil en formato de hipotesis verificable]"

Como validarlo antes de construir: [experimento especifico]

## Analisis de mercado {#mercado}

─── TAM ───

Universo base: [N empresas/personas con el problema] — fuente: [URL + acceso]

Precio de referencia: [monto/anio] — fuente: [benchmark / disposicion a pagar]

Calculo: [N] x [precio] = [TAM]

─── SAM ───

Filtros:

- Geografia: [N] -> [N] — [% reduccion] — fuente: [URL + acceso]
- Idioma/canal/acceso tecnologico: [N] -> [N] — [%] — fuente: [URL + acceso]
- Capacidad de pago: [N] -> [N] — [%] — fuente: [URL + acceso]

SAM: [N] x [precio] = [SAM]

─── SOM (18-24 MESES) ───

Restricciones reales:

- Capacidad comercial: [N clientes/mes]
- Presupuesto de adquisicion: [monto]
- Tiempo de adopcion: [justificacion]
- Friccion competitiva: [descripcion]

Escenario conservador: [monto] — supuestos: [lista]

Escenario base: [monto] — supuestos: [lista]

Escenario optimista: [monto] — supuestos: [lista]

─── DINAMICA Y REGULACION ───

CAGR / crecimiento: [porcentaje o INCIERTO] — fuente: [URL + acceso]

Regulacion relevante: [norma / riesgo / implicancia]

## Unit economics {#unit-economics}

─── PRECIO Y MARGEN ───

Precio mensual/cliente: [monto] — fuente: [benchmark / supuesto]

Costos de entrega/cliente/mes:

- Infraestructura: [monto]
- IA/LLM compute: [monto o NO APLICA] — calculo: [tokens si aplica]
- Soporte: [monto]
- Herramientas: [monto]

Margen bruto: [porcentaje]

─── ADQUISICION ───

Canal 1: [nombre]

- CPC/costo accion: [monto] — fuente: [URL + acceso]
- Conversion esperada: [porcentaje]
- CAC: [monto]

Canal 2: [nombre]

- CPC/costo accion: [monto] — fuente: [URL + acceso]
- Conversion esperada: [porcentaje]
- CAC: [monto]

CAC blended: [monto]

─── RETENCION Y LTV ───

Churn mensual: [porcentaje] — fuente/supuesto: [detalle]

Vida del cliente: [meses]

LTV: [monto]

LTV/CAC: [ratio] — semaforo: [VERDE >3x / AMARILLO 1-3x / ROJO <1x]

─── SENSIBILIDAD ───

| Variable | Base | -20% | -40% | LTV/CAC resultante |
|---|---:|---:|---:|---:|
| Precio | [monto] | [monto] | [monto] | [ratio] |
| Churn | [porcentaje] | [porcentaje] | [porcentaje] | [ratio] |
| Conversion | [porcentaje] | [porcentaje] | [porcentaje] | [ratio] |

Peor escenario combinado: [resultado]

## Viabilidad tecnica {#viabilidad-tecnica}

─── COMPONENTES DEL MVP ───

| Componente | Que hace | Complejidad | Decision BUILD/BUY | Costo | Riesgo |
|---|---|---|---|---:|---|
| [nombre] | [descripcion] | [baja/media/alta] | [BUILD/BUY] | [monto] | [riesgo] |

─── STACK RECOMENDADO ───

Frontend: [tech] — [razon] — costo: [monto]

Backend: [tech] — [razon] — costo: [monto]

DB: [tech] — [razon] — costo: [monto]

Auth: [servicio] — [razon] — costo: [monto]

Pagos: [servicio] — [razon] — costo: [monto]

Deploy: [servicio] — [razon] — costo: [monto]

IA/LLM: [API / NO APLICA] — costo variable: [monto]

─── ESTIMACION MVP ───

Setup y arquitectura: [dias]

Feature 1: [dias]

Feature 2: [dias]

Feature 3: [dias]

Tests e integracion: [dias]

Total con contingencia 20%: [dias/semanas]

## Riesgos y kill criteria {#riesgos}

─── RIESGOS POR CATEGORIA ───

Mercado:

- [riesgo] — Probabilidad: [alta/media/baja] — Impacto: [critico/alto/medio] — Mitigacion: [accion concreta]

Modelo de negocio:

- [riesgo] — Probabilidad: [alta/media/baja] — Impacto: [critico/alto/medio] — Mitigacion: [accion concreta]

Tecnico:

- [riesgo] — Probabilidad: [alta/media/baja] — Impacto: [critico/alto/medio] — Mitigacion: [accion concreta]

Regulatorio/equipo:

- [riesgo] — Probabilidad: [alta/media/baja] — Impacto: [critico/alto/medio] — Mitigacion: [accion concreta]

─── SUPUESTOS MAS FRAGILES ───

1. "[hipotesis verificable]" — Como validar: [experimento] — Si falla: [cambio]
2. "[hipotesis verificable]" — Como validar: [experimento] — Si falla: [cambio]
3. "[hipotesis verificable]" — Como validar: [experimento] — Si falla: [cambio]

─── KILL CRITERIA ───

- Gate 0: [criterio binario]
- Gate 1: [criterio binario]
- Gate 2: [criterio binario]

## Modelo de negocio {#modelo-negocio}

─── REVENUE PRIMITIVE ───

En una oracion: [quien paga] paga [monto/modelo] por [resultado medible] porque [valor].

─── MODELO ELEGIDO ───

Modelo: [SaaS / Marketplace / AI Infrastructure / hibrido]

Por que este modelo: [razon basada en problema, mercado y unit economics]

Alternativas descartadas:

- [modelo] — por que no
- [modelo] — por que no

─── PRICING ───

Plan inicial: [nombre] — [precio] — incluye: [limites/valor]

Expansion de cuenta: [como aumenta el revenue con uso, seats, volumen o modulos]

Condicion critica del pricing: [que debe ser verdad]

─── PROPUESTA DE VALOR ───

Para [segmento], que tiene [problema], [producto] entrega [resultado medible] sin [friccion actual].

Lenguaje prohibido: [jerga que no usa el usuario]

## Go-to-market {#gtm}

─── CANAL INICIAL ───

Canal 1: [nombre] — por que: [razon] — costo esperado: [monto] — metrica de exito: [metrica]

Canal 2: [nombre] — por que: [razon] — costo esperado: [monto] — metrica de exito: [metrica]

─── PRIMER CLIENTE PAGADOR ───

Perfil: [tipo de cliente]

Tactica de adquisicion: [pasos concretos]

Oferta inicial: [precio / piloto / condicion]

─── VALIDACION DE BAJO PRESUPUESTO ───

Experimento: [que se prueba]

Presupuesto maximo: [monto]

Resultado esperado: [metrica/umbral]

Decision si falla: [ITERAR/KILL y a que volver]

─── SECUENCIA 0-90 DIAS ───

Dias 0-30: [objetivo y accion]

Dias 31-60: [objetivo y accion]

Dias 61-90: [objetivo y accion]

## Scope de producto {#scope-producto}

─── USUARIO Y RESULTADO ───

Usuario primario: [segmento]

Resultado core: [resultado medible]

Time-to-value objetivo: [minutos]

─── FLUJO CORE ───

1. [paso]
2. [paso]
3. [paso]
4. [paso]

─── FUNCIONALIDADES INCLUIDAS ───

1. [feature] — por que entra: [razon vinculada al modelo/GTM]
2. [feature] — por que entra: [razon]
3. [feature] — por que entra: [razon]

─── EXCLUIDO DEL MVP ───

- [feature] — por que queda fuera
- [feature] — por que queda fuera

─── REQUISITOS PARA UX ───

Pantallas necesarias:

- [pantalla]
- [pantalla]

Estados obligatorios:

- Default
- Loading
- Error
- Vacio
- Exito

Metrica de exito del MVP: [metrica]

## Handoff esperado

Este output alimenta el handoff `2->3` hacia Arquitecto UX.

Skills cubiertas:

- `3.A.1` — mercado
- `3.B.1` — unit economics
- `3.C.1` — viabilidad tecnica
- `3.D.1` — riesgos
- `4.1` — modelo de negocio
- `4.2` — go-to-market
- `4.scope` — scope de producto
