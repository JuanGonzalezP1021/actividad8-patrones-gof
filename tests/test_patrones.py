import sys, os, io, contextlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from singleton import ConfiguracionApp
from factory_method import FabricaPDF, FabricaExcel
from builder import EstudianteBuilder, DirectorMatricula
from decorator import CalificacionBase, ConBono, ConPenalidad
from facade import SistemaAcademico
from command import ListaEstudiantes, AgregarEstudiante, GestorComandos
from strategy import (EvaluacionPromedio, EvaluacionPonderada,
                      EvaluacionMejorN, ContextoEvaluacion)

# ── Singleton ──────────────────────────────────────────────

def test_singleton_misma_instancia():
    assert ConfiguracionApp() is ConfiguracionApp()

def test_singleton_estado_compartido():
    ConfiguracionApp().actualizar("idioma", "fr")
    assert ConfiguracionApp().idioma == "fr"
    ConfiguracionApp().actualizar("idioma", "es")

# ── Factory Method ─────────────────────────────────────────

def test_factory_pdf():
    assert "PDF" in FabricaPDF().publicar({"nombre": "Ana", "materia": "Prog II", "nota": 4.5})

def test_factory_excel():
    assert "EXCEL" in FabricaExcel().publicar({"nombre": "Luis", "materia": "Calculo", "nota": 3.8})

# ── Builder ────────────────────────────────────────────────

def test_builder_campos():
    e = EstudianteBuilder().nombre("Maria").carrera("Sistemas").semestre(4).build()
    assert e.nombre == "Maria" and e.carrera == "Sistemas"

def test_builder_director():
    e = DirectorMatricula.construir_nuevo_ingreso(EstudianteBuilder(), "Pedro", "001", "Matematicas")
    assert e.semestre == 1

# ── Decorator ──────────────────────────────────────────────

def test_decorator_bono():
    assert ConBono(CalificacionBase(3.5, "Carlos", "Prog II"), 0.5).valor() == 4.0

def test_decorator_penalidad():
    assert abs(ConPenalidad(CalificacionBase(4.0, "Laura", "Algebra"), 0.3).valor() - 3.7) < 0.001

# ── Facade ─────────────────────────────────────────────────

def test_facade_instancia():
    s = SistemaAcademico()
    assert s._notas is not None and s._asistencia is not None

def test_facade_registrar():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        SistemaAcademico().registrar_calificacion("001", "Ana", "Prog II", 4.5)
    assert "NOTAS" in buf.getvalue()

# ── Command ────────────────────────────────────────────────

def test_command_agregar():
    lista = ListaEstudiantes(); g = GestorComandos()
    g.ejecutar(AgregarEstudiante(lista, "Sofia"))
    assert "Sofia" in lista.listar()

def test_command_deshacer():
    lista = ListaEstudiantes(); g = GestorComandos()
    g.ejecutar(AgregarEstudiante(lista, "Miguel"))
    g.deshacer()
    assert "Miguel" not in lista.listar()

# ── Strategy ───────────────────────────────────────────────

def test_strategy_promedio():
    ctx = ContextoEvaluacion(EvaluacionPromedio())
    resultado = ctx.evaluar("Ana", [4.0, 3.0, 5.0])
    assert "4.00" in resultado and "APROBADO" in resultado

def test_strategy_cambio_dinamico():
    ctx = ContextoEvaluacion(EvaluacionPromedio())
    ctx.cambiar_estrategia(EvaluacionMejorN(2))
    resultado = ctx.evaluar("Luis", [2.0, 4.5, 3.5])
    # Mejores 2: (4.5 + 3.5) / 2 = 4.0
    assert "4.00" in resultado and "Mejores 2" in resultado


# ── Runner ─────────────────────────────────────────────────

if __name__ == "__main__":
    tests = [
        ("Singleton - misma instancia",     test_singleton_misma_instancia),
        ("Singleton - estado compartido",    test_singleton_estado_compartido),
        ("Factory Method - PDF",             test_factory_pdf),
        ("Factory Method - Excel",           test_factory_excel),
        ("Builder - campos",                 test_builder_campos),
        ("Builder - director",               test_builder_director),
        ("Decorator - bono",                 test_decorator_bono),
        ("Decorator - penalidad",            test_decorator_penalidad),
        ("Facade - instancia",              test_facade_instancia),
        ("Facade - registrar",              test_facade_registrar),
        ("Command - agregar",               test_command_agregar),
        ("Command - deshacer",              test_command_deshacer),
        ("Strategy - promedio",             test_strategy_promedio),
        ("Strategy - cambio dinamico",      test_strategy_cambio_dinamico),
    ]
    print("\n" + "="*50)
    print("  PRUEBAS - Actividad 8: Patrones GoF")
    print("="*50)
    ok = 0
    for nombre, t in tests:
        try:
            t(); print(f"  OK   {nombre}"); ok += 1
        except Exception as e:
            print(f"  FAIL {nombre}: {e}")
    print("="*50)
    print(f"  {ok}/{len(tests)} pruebas pasaron")
    print("="*50 + "\n")
