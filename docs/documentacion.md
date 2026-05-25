# Documentacion Tecnica - Patrones GoF Aplicados

## 1. Builder - Constructor de Estudiantes
Separa la construccion de un objeto complejo de su representacion.
Permite construir Estudiante con campos opcionales sin multiples constructores.
**Ejemplo:** EstudianteBuilder().nombre("Ana").carrera("Sistemas").semestre(4).build()

## 2. Factory Method - Generador de Reportes
Delega la creacion del objeto a subclases especializadas.
El cliente usa FabricaPDF o FabricaExcel sin conocer la clase concreta.
**Ejemplo:** FabricaPDF().publicar({"nombre": "Ana", "nota": 4.5})

## 3. Singleton - Configuracion Global
Garantiza una unica instancia de ConfiguracionApp en toda la aplicacion.
Todos los modulos comparten el mismo objeto de configuracion.
**Ejemplo:** ConfiguracionApp().nota_minima_aprobacion = 3.5

## 4. Decorator - Modificacion de Calificaciones
Anade responsabilidades a un objeto dinamicamente sin alterar su clase.
ConBono y ConPenalidad envuelven CalificacionBase y modifican su valor.
**Ejemplo:** ConBono(CalificacionBase(3.8, "Carlos", "Prog II"), 0.3).valor()

## 5. Facade - Sistema Academico Unificado
Provee una interfaz simplificada sobre ModuloNotas, ModuloAsistencia y ModuloCertificados.
El cliente solo llama a SistemaAcademico sin conocer los subsistemas internos.
**Ejemplo:** SistemaAcademico().procesar_fin_semestre("001", "Ana Torres")

## 6. Command - Gestion con Undo/Redo
Encapsula operaciones como objetos para soportar deshacer y rehacer.
GestorComandos mantiene el historial de AgregarEstudiante y EliminarEstudiante.
**Ejemplo:** gestor.deshacer() restaura el estado anterior de la lista.
