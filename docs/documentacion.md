# Documentacion Tecnica - Patrones GoF

## Tabla de los 23 Patrones GoF

### Patrones Creacionales

| Patron | Categoria | Problema que resuelve | Diagrama de clases | Casos de uso | Ventajas | Desventajas | Patrones relacionados |
|--------|-----------|----------------------|-------------------|-------------|----------|-------------|----------------------|
| **Abstract Factory** | Creacional | Crear familias de objetos relacionados sin especificar sus clases concretas | Interfaz AbstractFactory con metodos create, ConcreteFactory implementa, AbstractProduct y ConcreteProduct | Interfaces graficas multiplataforma, conexiones a distintas BD, temas de UI | Aislamiento de clases concretas, facilita intercambio de familias | Dificil agregar nuevos productos, complejidad alta | Factory Method, Singleton, Prototype |
| **Builder** | Creacional | Separar la construccion de un objeto complejo de su representacion para crear distintas representaciones | Director invoca Builder; ConcreteBuilder implementa los pasos; produce Product | Construccion de documentos complejos, generacion de consultas SQL, objetos con muchos parametros opcionales | Permite variaciones del producto, aisla codigo de construccion y representacion | Requiere crear un ConcreteBuilder por cada variante | Abstract Factory, Composite |
| **Factory Method** | Creacional | Delegar la instanciacion a subclases cuando una clase no puede anticipar la clase de objetos que debe crear | Creator declara factoryMethod; ConcreteCreator lo sobreescribe y devuelve ConcreteProduct | Frameworks que instancian objetos definidos por el usuario, generacion de reportes en multiples formatos | Elimina acoplamiento con clases concretas, sigue principio abierto/cerrado | Una subclase por cada producto concreto | Abstract Factory, Template Method, Prototype |
| **Prototype** | Creacional | Crear objetos clonando una instancia existente en lugar de construirla desde cero | Prototype declara clone(); ConcretePrototype lo implementa; Client llama clone() | Objetos costosos de crear, editores graficos con copiar/pegar, configuraciones predefinidas | Reduce subclases, permite agregar/eliminar productos en tiempo de ejecucion | Clonar objetos con referencias circulares es complejo | Abstract Factory, Composite, Decorator |
| **Singleton** | Creacional | Garantizar que una clase tenga una unica instancia con un punto de acceso global | Clase con atributo estatico _instance y metodo getInstance() | Configuracion global, pool de conexiones, logger, cache | Control estricto de acceso, evita variables globales | Dificulta pruebas unitarias, puede ocultar dependencias, problemas en multithreading | Abstract Factory, Builder, Prototype |

### Patrones Estructurales

| Patron | Categoria | Problema que resuelve | Diagrama de clases | Casos de uso | Ventajas | Desventajas | Patrones relacionados |
|--------|-----------|----------------------|-------------------|-------------|----------|-------------|----------------------|
| **Adapter** | Estructural | Convertir la interfaz de una clase en otra que el cliente espera, permitiendo colaboracion entre clases incompatibles | Target define la interfaz; Adapter hereda/compone Adaptee y traduce llamadas | Integracion de librerias externas, migracion entre APIs, adaptacion de datos legacy | Reutilizacion de clases existentes, separa interfaz de implementacion | Anade una capa de indirection, a veces mas simple reescribir | Bridge, Decorator, Proxy |
| **Bridge** | Estructural | Desacoplar una abstraccion de su implementacion para que ambas puedan variar independientemente | Abstraction tiene referencia a Implementor; RefinedAbstraction y ConcreteImplementor | Soporte multiplataforma, drivers de dispositivos, figuras con distintos motores de renderizado | Extensibilidad independiente, oculta detalles de implementacion al cliente | Aumenta complejidad inicial | Abstract Factory, Adapter |
| **Composite** | Estructural | Componer objetos en estructuras de arbol para representar jerarquias parte-todo y tratarlos uniformemente | Component (interfaz); Leaf y Composite (contiene hijos Component) | Sistemas de archivos, menus/submenus, organigramas, expresiones aritmeticas | Facilita agregar nuevos componentes, simplifica el codigo cliente | Puede hacer el diseno demasiado general, dificil restringir tipos de hijos | Chain of Responsibility, Decorator, Flyweight, Iterator, Visitor |
| **Decorator** | Estructural | Anadir responsabilidades a un objeto dinamicamente sin modificar su clase, alternativa flexible a la herencia | Component (interfaz); ConcreteComponent; Decorator envuelve Component; ConcreteDecorator anade comportamiento | Streams de I/O, middleware HTTP, modificacion de calificaciones, extension de UI | Mas flexible que herencia estatica, responsabilidades combinables | Muchos objetos pequenos, dificil depurar cadenas largas | Adapter, Composite, Strategy |
| **Facade** | Estructural | Proveer una interfaz simplificada a un subsistema complejo, reduciendo el acoplamiento | Facade conoce las clases del subsistema; Client solo usa Facade | Librerias complejas, modulos academicos, APIs unificadas, servicios de compilacion | Aislamiento del subsistema, simplifica uso para el cliente | Puede convertirse en god object si se abusa, no impide acceso directo al subsistema | Abstract Factory, Mediator, Singleton |
| **Flyweight** | Estructural | Compartir estado para soportar gran cantidad de objetos de grano fino eficientemente | FlyweightFactory gestiona un pool; Flyweight almacena estado intrinseco; Client provee estado extrinseco | Editores de texto (caracteres), juegos (particulas, arboles), mapas con iconos repetidos | Ahorro significativo de memoria | Aumenta complejidad, intercambio CPU/memoria | Composite, State, Strategy |
| **Proxy** | Estructural | Proporcionar un sustituto o representante de otro objeto para controlar el acceso a el | Subject (interfaz); RealSubject; Proxy controla acceso a RealSubject | Lazy loading de imagenes, control de acceso, cache, logging transparente, objetos remotos | Control de acceso, carga diferida, transparente para el cliente | Puede anadir latencia, complejidad adicional | Adapter, Decorator |

### Patrones de Comportamiento

| Patron | Categoria | Problema que resuelve | Diagrama de clases | Casos de uso | Ventajas | Desventajas | Patrones relacionados |
|--------|-----------|----------------------|-------------------|-------------|----------|-------------|----------------------|
| **Chain of Responsibility** | Comportamiento | Evitar acoplar emisor y receptor permitiendo que mas de un objeto maneje la peticion en una cadena | Handler (interfaz con successor); ConcreteHandler decide si procesa o pasa al siguiente | Middleware de servidores web, validacion de formularios, sistemas de aprobacion, filtros de logging | Reduce acoplamiento, permite agregar/quitar responsables dinamicamente | No hay garantia de que la peticion sea manejada | Composite, Command |
| **Command** | Comportamiento | Encapsular una solicitud como objeto para parametrizar clientes, encolar operaciones y soportar undo/redo | Command (interfaz); ConcreteCommand encapsula accion y receptor; Invoker ejecuta; Receiver realiza la accion | Undo/redo en editores, colas de tareas, transacciones, macros, gestion de estudiantes | Desacopla invocador y ejecutor, soporta deshacer, composicion de comandos | Aumento de clases, complejidad adicional por cada operacion | Composite, Memento, Prototype |
| **Interpreter** | Comportamiento | Definir una representacion de la gramatica de un lenguaje y un interprete que la evalua | AbstractExpression; TerminalExpression; NonterminalExpression; Context | Lenguajes de consulta simples, expresiones regulares, reglas de negocio, calculadoras | Facil de extender la gramatica, cada regla es una clase | Ineficiente para gramaticas complejas, dificil de mantener | Composite, Flyweight, Iterator, Visitor |
| **Iterator** | Comportamiento | Acceder secuencialmente a los elementos de una coleccion sin exponer su representacion interna | Iterator (interfaz con next, hasNext); ConcreteIterator; Aggregate crea Iterator | Recorrido de colecciones (listas, arboles, grafos), cursors de BD, paginacion | Simplifica la interfaz de la coleccion, soporta multiples recorridos simultaneos | Puede ser excesivo para colecciones simples | Composite, Factory Method, Memento |
| **Mediator** | Comportamiento | Reducir dependencias directas entre objetos definiendo un objeto que encapsula su interaccion | Mediator (interfaz); ConcreteMediator coordina; Colleague comunica via Mediator | Chat rooms, torres de control aereo, formularios con campos dependientes | Reduce acoplamiento entre componentes, centraliza el control | El mediador puede volverse un god object complejo | Facade, Observer, Command |
| **Memento** | Comportamiento | Capturar y externalizar el estado interno de un objeto para poder restaurarlo despues sin violar encapsulamiento | Originator crea Memento; Memento almacena estado; Caretaker guarda Mementos | Undo en editores de texto, checkpoints en juegos, historial de transacciones | Preserva encapsulamiento, simplifica el originador | Puede consumir mucha memoria si los estados son grandes | Command, Iterator |
| **Observer** | Comportamiento | Definir una dependencia uno-a-muchos para que cuando un objeto cambie, todos sus dependientes sean notificados | Subject mantiene lista de Observer; ConcreteSubject notifica; ConcreteObserver se actualiza | Sistemas de eventos, suscripciones de UI, notificaciones push, model-view | Acoplamiento minimo entre sujeto y observadores, soporte broadcast | Actualizaciones inesperadas en cascada, memory leaks si no se desregistra | Mediator, Singleton |
| **State** | Comportamiento | Permitir que un objeto altere su comportamiento cuando su estado interno cambia, como si cambiara de clase | Context delega a State; ConcreteState implementa comportamiento para cada estado | Maquinas de estados finitos, flujos de pedido, semaforos, protocolos de red | Elimina condicionales complejos, hace explicitas las transiciones | Aumenta numero de clases, puede ser excesivo para pocos estados | Flyweight, Singleton, Strategy |
| **Strategy** | Comportamiento | Definir una familia de algoritmos intercambiables para que el cliente pueda elegir cual usar en tiempo de ejecucion | Strategy (interfaz); ConcreteStrategy implementa algoritmo; Context usa Strategy | Algoritmos de evaluacion academica, ordenamiento, compresion, calculo de impuestos, validacion | Elimina condicionales, facilita agregar nuevas estrategias, reutilizacion | El cliente debe conocer las estrategias disponibles, overhead si hay pocas variantes | Flyweight, State, Template Method |
| **Template Method** | Comportamiento | Definir el esqueleto de un algoritmo en una operacion, delegando algunos pasos a subclases | AbstractClass define templateMethod con pasos abstractos; ConcreteClass implementa pasos | Frameworks de procesamiento, parsers, generacion de reportes con formato fijo | Reutiliza codigo comun, control de la estructura del algoritmo | Puede violar Liskov si las subclases alteran el flujo esperado, limitado a herencia | Factory Method, Strategy |
| **Visitor** | Comportamiento | Separar un algoritmo de la estructura de objetos sobre la que opera, permitiendo agregar operaciones sin modificar las clases | Visitor (interfaz con visit por tipo); ConcreteVisitor; Element acepta Visitor | Compiladores (AST traversal), exportacion en multiples formatos, calculos sobre estructura de objetos | Agrega operaciones facilmente, acumula estado durante el recorrido | Dificil agregar nuevos tipos de Element, rompe encapsulamiento | Composite, Interpreter, Iterator |

---

## Patrones Implementados en el Proyecto

### 1. Builder - Constructor de Estudiantes

**Problema:** Construir objetos `Estudiante` con multiples campos opcionales sin necesidad de multiples constructores.

**Solucion:** `EstudianteBuilder` permite encadenar metodos para asignar solo los campos deseados, y `DirectorMatricula` ofrece una receta predefinida para estudiantes de nuevo ingreso.

**Clases:**
- `Estudiante` — producto final con atributos nombre, codigo, carrera, semestre, email, promedio.
- `EstudianteBuilder` — builder con metodos encadenables y `build()` que valida nombre obligatorio.
- `DirectorMatricula` — director con metodo estatico `construir_nuevo_ingreso()`.

**Ejemplo:**
```python
e = EstudianteBuilder().nombre("Ana").carrera("Sistemas").semestre(4).build()
```

---

### 2. Factory Method - Generador de Reportes

**Problema:** El cliente necesita generar reportes en distintos formatos (PDF, Excel, HTML) sin conocer las clases concretas.

**Solucion:** `FabricaReporte` define el metodo `crear_reporte()` que cada fabrica concreta sobreescribe para devolver el tipo de reporte correcto.

**Clases:**
- `Reporte` (ABC) — interfaz con `generar()` y `extension()`.
- `ReportePDF`, `ReporteExcel`, `ReporteHTML` — productos concretos.
- `FabricaReporte` (ABC) — creator con `crear_reporte()` y `publicar()`.
- `FabricaPDF`, `FabricaExcel`, `FabricaHTML` — fabricas concretas.

**Ejemplo:**
```python
resultado = FabricaPDF().publicar({"nombre": "Ana", "nota": 4.5})
```

---

### 3. Singleton - Configuracion Global

**Problema:** Multiples modulos necesitan compartir la misma configuracion sin crear instancias duplicadas.

**Solucion:** `ConfiguracionApp` usa `__new__` para garantizar una unica instancia que mantiene idioma, limites y parametros institucionales.

**Clases:**
- `ConfiguracionApp` — singleton con atributos de configuracion y metodo `actualizar()`.

**Ejemplo:**
```python
config = ConfiguracionApp()
config.actualizar("idioma", "en")
assert ConfiguracionApp().idioma == "en"  # misma instancia
```

---

### 4. Decorator - Modificacion de Calificaciones

**Problema:** Modificar calificaciones (bonos, penalidades, redondeo) sin alterar la clase base ni crear subclases para cada combinacion.

**Solucion:** Decoradores envuelven `CalificacionBase` y modifican `valor()` y `descripcion()` de forma apilable.

**Clases:**
- `Calificacion` (ABC) — interfaz con `valor()` y `descripcion()`.
- `CalificacionBase` — componente concreto con nota, estudiante, materia.
- `DecoradorCalificacion` (ABC) — decorador base que delega al componente envuelto.
- `ConBono`, `ConPenalidad`, `ConRedondeo` — decoradores concretos.

**Ejemplo:**
```python
nota = ConBono(CalificacionBase(3.8, "Carlos", "Prog II"), 0.3)
print(nota.valor())       # 4.1
print(nota.descripcion())  # Carlos | Prog II -> 3.80 [+0.3 por participacion]
```

---

### 5. Strategy - Evaluacion Academica

**Problema:** Se necesitan diferentes algoritmos para calcular la nota final de un estudiante (promedio, ponderado, mejores N) y poder cambiar entre ellos en tiempo de ejecucion.

**Solucion:** `ContextoEvaluacion` recibe una `EstrategiaEvaluacion` intercambiable que define como calcular la nota final.

**Clases:**
- `EstrategiaEvaluacion` (ABC) — interfaz con `calcular_nota_final()` y `nombre()`.
- `EvaluacionPromedio` — promedio simple de todas las notas.
- `EvaluacionPonderada` — da mas peso a las ultimas evaluaciones.
- `EvaluacionMejorN` — usa solo las mejores N calificaciones.
- `ContextoEvaluacion` — contexto con `evaluar()` y `cambiar_estrategia()`.

**Ejemplo:**
```python
ctx = ContextoEvaluacion(EvaluacionPromedio())
print(ctx.evaluar("Ana", [4.0, 3.0, 5.0]))
ctx.cambiar_estrategia(EvaluacionMejorN(2))
print(ctx.evaluar("Ana", [4.0, 3.0, 5.0]))
```

---

### 6. Facade - Sistema Academico Unificado

**Problema:** El cliente necesita interactuar con multiples subsistemas (notas, asistencia, certificados) de forma sencilla.

**Solucion:** `SistemaAcademico` ofrece metodos unificados que coordinan los tres modulos internamente.

**Clases:**
- `ModuloNotas` — registro y consulta de calificaciones.
- `ModuloAsistencia` — calculo de porcentajes de asistencia.
- `ModuloCertificados` — emision de certificados y paz y salvo.
- `SistemaAcademico` — fachada que orquesta los tres modulos.

**Ejemplo:**
```python
sistema = SistemaAcademico()
sistema.procesar_fin_semestre("001", "Ana Torres")
```

---

### 7. Command - Gestion con Undo/Redo

**Problema:** Se necesita ejecutar operaciones sobre la lista de estudiantes con la posibilidad de deshacerlas y rehacerlas.

**Solucion:** Cada operacion se encapsula como un objeto `Comando` que sabe como ejecutarse y deshacerse. `GestorComandos` mantiene el historial.

**Clases:**
- `ListaEstudiantes` — receptor con `agregar()`, `eliminar()`, `listar()`.
- `Comando` (ABC) — interfaz con `ejecutar()`, `deshacer()`, `descripcion()`.
- `AgregarEstudiante`, `EliminarEstudiante` — comandos concretos.
- `GestorComandos` — invocador con historial, `deshacer()` y `rehacer()`.

**Ejemplo:**
```python
lista = ListaEstudiantes()
gestor = GestorComandos()
gestor.ejecutar(AgregarEstudiante(lista, "Sofia"))
gestor.deshacer()  # Sofia se elimina
gestor.rehacer()   # Sofia se vuelve a agregar
```
