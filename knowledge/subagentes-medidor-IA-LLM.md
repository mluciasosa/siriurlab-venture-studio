# Subagentes del Medidor — Complemento de instrumentación IA/LLM
### Extensión del Ingeniero de Instrumentación (9.A) y del Comunicador de Insights (9.D) para el costo de tokens

> **Por qué existe:**
> El Guardián vigila el costo IA en producción (semáforo de 10.E, ver `subagentes-guardian-IA-LLM.md`) y el modelo financiero lo proyecta antes de construir (Analista 3.B y 3.C.2). Pero entre la proyección y la auditoría faltaba el dato real: **el Medidor no instrumenta el costo de tokens**. Sin esta captura, el semáforo IA de 10.E no tiene fuente y el umbral "costo IA/LLM < 30% del precio" queda sin verificación en producción. Este complemento cierra ese lazo.

> **Relación con el Medidor:** extiende `subagentes-medidor.md`. La instrumentación de costo IA solo aplica si el producto llama a un LLM. Si no hay IA, este complemento es N/A.

---

# EXTENSIÓN DE 9.A — INGENIERO DE INSTRUMENTACIÓN

## SKILL 9.A.1 (extendida) — evento de costo IA en el tracking plan

**Trigger:** Fase 4, junto con el resto del tracking plan, cuando el producto tiene una feature de LLM.

**OUTPUT — se anexa al PLAN DE TRACKING:**
```
─── EVENTO DE COSTO IA (solo si hay LLM) ───
Evento: llm_call_completed
  Cuándo: cada vez que se completa una llamada a un modelo de lenguaje
  Propiedades: {
    task_id: string,          // qué tarea de IA (mapea a la matriz de ruteo 6.F.1)
    model: string,            // modelo efectivamente usado (primario o fallback)
    input_tokens: int,
    output_tokens: int,
    cost_usd: float,          // costo real de esta llamada
    latency_ms: int,
    fallback_used: bool,      // si se activó la cadena de fallback (6.F.5)
    cache_hit: bool           // si la respuesta salió de caché
  }
  Pregunta de negocio: ¿el costo IA real se mantiene < 30% del precio?
  Prioridad: crítica (si la IA está en el core del producto)

─── MÉTRICAS DERIVADAS ───
costo_ia_por_usuario_mes = Σ(cost_usd) del usuario en el mes
costo_ia_pct_precio = costo_ia_por_usuario_mes / precio_mensual × 100
tasa_fallback = % de llm_call_completed con fallback_used = true
tasa_cache = % de llm_call_completed con cache_hit = true
```

**REGLAS (heredan el estándar del Medidor):**
- `llm_call_completed` no cuenta contra el límite de 10-15 eventos de negocio: es un evento de costo de infraestructura, en su propio namespace.
- El `cost_usd` se calcula con el precio vigente del modelo, no estimado una vez. Si el proveedor cambia precios, se actualiza.
- `task_id` debe mapear a una tarea de la matriz de ruteo (6.F.1), o no se puede atribuir el costo por tarea.
- Si el producto tiene IA y este evento no está instrumentado antes del lanzamiento, la verificación de datos (9.A.2) lo marca como dato crítico faltante.

**CRITERIO DE CALIDAD (medible):** Si el producto tiene IA, `llm_call_completed` está instrumentado y verificado antes del lanzamiento. El costo IA por usuario es trazable por tarea, modelo y mes.

---

# EXTENSIÓN DE 9.D — COMUNICADOR DE INSIGHTS

## SKILL 9.D.1 (extendida) — costo IA en los dashboards

**OUTPUT — se anexa al DISEÑO DE DASHBOARD:**
```
─── DIARIO (si hay IA) ───
Costo IA del día (total + por usuario activo) — tendencia

─── SEMANAL (si hay IA) ───
Costo IA por usuario: tendencia semana a semana
Tasa de caché y tasa de fallback (señales de eficiencia y de salud del modelo)

─── MENSUAL (si hay IA) — alimenta el Gate 6 ───
costo_ia_pct_precio: [%]  🟢 <20% / 🟡 20-30% / 🔴 >30%
  → este es el dato que consume el semáforo IA del Guardián (10.E)
Costo IA por tarea (top 3 tareas más caras) — para priorizar optimización
```

**REGLA:** El reporte mensual entrega `costo_ia_pct_precio` al Guardián (10.E) en cada cierre de mes. Si está en 🔴, el Comunicador de Insights emite un `insight-report` (9.D.2) dirigido al Constructor 6.F con la tarea más cara como foco de optimización.

**CRITERIO DE CALIDAD (medible):** El costo IA real aparece en los tres niveles de dashboard cuando el producto tiene IA. El Gate 6 nunca se queda sin el dato de costo IA del período.

---

# HANDOFF AL GUARDIÁN (cierre del circuito)

```
De: Medidor 9.D | Para: Guardián 10.E (mensual)
─── CAMPO OBLIGATORIO ───
✅/❌ costo_ia_pct_precio del período + tendencia 3 meses
INCOMPLETO → 10.E no puede emitir el semáforo IA → vuelve a 9.A a verificar instrumentación
```

---

## Definition of Done — Medidor con instrumentación IA (addendum)

```
─── INSTRUMENTACIÓN IA ───
□ Evento llm_call_completed instrumentado y verificado (si hay IA)
□ Costo IA atribuible por tarea, modelo y mes
□ Métricas derivadas (costo_ia_pct_precio, tasa_cache, tasa_fallback) calculadas
□ Costo IA presente en dashboards diario/semanal/mensual
□ costo_ia_pct_precio entregado al Guardián 10.E cada mes
□ Si no hay IA en el producto, el bloque es N/A sin penalizar
```

---

*SiriusLabs — miko.siriuslabs@gmail.com*
*Complemento de `subagentes-medidor.md`. Cierra el circuito del umbral "costo IA/LLM < 30%": el Analista (3.B/3.C.2) lo proyecta, el Medidor (este complemento) lo instrumenta, el Guardián (10.C/10.E) lo audita.*
