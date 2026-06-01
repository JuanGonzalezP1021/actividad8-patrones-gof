# Manual de Pruebas Unitarias - Patrones GoF

## Descripcion general

Se implementaron 14 pruebas unitarias (2 por cada patron) en el archivo `tests/test_patrones.py`. Las pruebas se ejecutan con el runner integrado sin dependencias externas.

## Comando de ejecucion

```bash
python tests/test_patrones.py
```

---

## Detalle de cada prueba

### Singleton

| # | Test | Que verifica | Resultado esperado |
|---|------|-------------|-------------------|
| 1 | `test_singleton_misma_instancia` | Que `ConfiguracionApp()` siempre devuelve el mismo objeto (identidad con `is`) | Las dos referencias apuntan al mismo objeto en memoria |
| 2 | `test_singleton_estado_compartido` | Que al modificar un atributo desde una referencia, se refleja en otra | Cambiar `idioma` a `"fr"` es visible desde cualquier llamada a `ConfiguracionApp()` |

### Factory Method

| # | Test | Que verifica | Resultado esperado |
|---|------|-------------|-------------------|
| 3 | `test_factory_pdf` | Que `FabricaPDF().publicar()` genera un reporte con marcador `[PDF]` | La cadena retornada contiene `"PDF"` |
| 4 | `test_factory_excel` | Que `FabricaExcel().publicar()` genera un reporte con marcador `[EXCEL]` | La cadena retornada contiene `"EXCEL"` |

### Builder

| # | Test | Que verifica | Resultado esperado |
|---|------|-------------|-------------------|
| 5 | `test_builder_campos` | Que el builder asigna correctamente nombre, carrera y semestre al Estudiante | `e.nombre == "Maria"` y `e.carrera == "Sistemas"` |
| 6 | `test_builder_director` | Que `DirectorMatricula.construir_nuevo_ingreso()` crea un estudiante de semestre 1 | `e.semestre == 1` |

### Decorator

| # | Test | Que verifica | Resultado esperado |
|---|------|-------------|-------------------|
| 7 | `test_decorator_bono` | Que `ConBono` suma correctamente el bono a la nota base | `CalificacionBase(3.5) + bono(0.5) = 4.0` |
| 8 | `test_decorator_penalidad` | Que `ConPenalidad` resta correctamente la penalidad | `CalificacionBase(4.0) - penalidad(0.3) = 3.7` |

### Facade

| # | Test | Que verifica | Resultado esperado |
|---|------|-------------|-------------------|
| 9 | `test_facade_instancia` | Que `SistemaAcademico` inicializa correctamente sus subsistemas internos | `_notas` y `_asistencia` no son `None` |
| 10 | `test_facade_registrar` | Que `registrar_calificacion()` produce salida con el marcador del modulo de notas | La salida a consola contiene `"NOTAS"` |

### Command

| # | Test | Que verifica | Resultado esperado |
|---|------|-------------|-------------------|
| 11 | `test_command_agregar` | Que `AgregarEstudiante` anade el nombre a la lista al ejecutarse | `"Sofia"` aparece en `lista.listar()` |
| 12 | `test_command_deshacer` | Que `deshacer()` revierte la ultima operacion de agregar | `"Miguel"` ya no aparece en `lista.listar()` |

### Strategy

| # | Test | Que verifica | Resultado esperado |
|---|------|-------------|-------------------|
| 13 | `test_strategy_promedio` | Que `EvaluacionPromedio` calcula correctamente el promedio de [4.0, 3.0, 5.0] | Resultado contiene `"4.00"` y `"APROBADO"` |
| 14 | `test_strategy_cambio_dinamico` | Que se puede cambiar de estrategia en tiempo de ejecucion a `EvaluacionMejorN(2)` | Con notas [2.0, 4.5, 3.5], las mejores 2 dan `"4.00"` y el nombre de estrategia es `"Mejores 2"` |

---

## Evidencia de ejecucion

```
==================================================
  PRUEBAS - Actividad 8: Patrones GoF
==================================================
  OK   Singleton - misma instancia
  OK   Singleton - estado compartido
  OK   Factory Method - PDF
  OK   Factory Method - Excel
  OK   Builder - campos
  OK   Builder - director
  OK   Decorator - bono
  OK   Decorator - penalidad
  OK   Facade - instancia
  OK   Facade - registrar
  OK   Command - agregar
  OK   Command - deshacer
  OK   Strategy - promedio
  OK   Strategy - cambio dinamico
==================================================
  14/14 pruebas pasaron
==================================================
```

Todas las 14 pruebas pasaron exitosamente. Cada patron cuenta con 2 casos de prueba que validan su comportamiento principal.
