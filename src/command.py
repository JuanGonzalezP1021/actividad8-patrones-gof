from abc import ABC, abstractmethod

class ListaEstudiantes:
    def __init__(self): self._estudiantes = []
    def agregar(self, n): self._estudiantes.append(n)
    def eliminar(self, n):
        if n in self._estudiantes: self._estudiantes.remove(n)
    def listar(self): return list(self._estudiantes)
    def __len__(self): return len(self._estudiantes)

class Comando(ABC):
    @abstractmethod
    def ejecutar(self): pass
    @abstractmethod
    def deshacer(self): pass
    @abstractmethod
    def descripcion(self): pass

class AgregarEstudiante(Comando):
    def __init__(self, lista, nombre): self._lista = lista; self._nombre = nombre
    def ejecutar(self): self._lista.agregar(self._nombre)
    def deshacer(self): self._lista.eliminar(self._nombre)
    def descripcion(self): return f"Agregar '{self._nombre}'"

class EliminarEstudiante(Comando):
    def __init__(self, lista, nombre): self._lista = lista; self._nombre = nombre; self._existia = False
    def ejecutar(self): self._existia = self._nombre in self._lista.listar(); self._lista.eliminar(self._nombre)
    def deshacer(self):
        if self._existia: self._lista.agregar(self._nombre)
    def descripcion(self): return f"Eliminar '{self._nombre}'"

class GestorComandos:
    def __init__(self): self._historial = []; self._cancelados = []
    def ejecutar(self, cmd): cmd.ejecutar(); self._historial.append(cmd); self._cancelados.clear()
    def deshacer(self):
        if self._historial: cmd = self._historial.pop(); cmd.deshacer(); self._cancelados.append(cmd)
    def rehacer(self):
        if self._cancelados: cmd = self._cancelados.pop(); cmd.ejecutar(); self._historial.append(cmd)
    def historial(self): return [c.descripcion() for c in self._historial]
