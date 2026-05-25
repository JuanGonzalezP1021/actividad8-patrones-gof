from abc import ABC, abstractmethod

class Calificacion(ABC):
    @abstractmethod
    def valor(self) -> float: pass
    @abstractmethod
    def descripcion(self) -> str: pass

class CalificacionBase(Calificacion):
    def __init__(self, nota, estudiante, materia):
        self._nota, self._estudiante, self._materia = nota, estudiante, materia
    def valor(self): return self._nota
    def descripcion(self): return f"{self._estudiante} | {self._materia} -> {self._nota:.2f}"

class DecoradorCalificacion(Calificacion, ABC):
    def __init__(self, c): self._c = c
    def valor(self): return self._c.valor()
    def descripcion(self): return self._c.descripcion()

class ConBono(DecoradorCalificacion):
    def __init__(self, c, bono, motivo="participacion"):
        super().__init__(c); self._bono = bono; self._motivo = motivo
    def valor(self): return min(5.0, self._c.valor() + self._bono)
    def descripcion(self): return self._c.descripcion() + f" [+{self._bono} por {self._motivo}]"

class ConPenalidad(DecoradorCalificacion):
    def __init__(self, c, penalidad, motivo="entrega tardia"):
        super().__init__(c); self._penalidad = penalidad; self._motivo = motivo
    def valor(self): return max(0.0, self._c.valor() - self._penalidad)
    def descripcion(self): return self._c.descripcion() + f" [-{self._penalidad} por {self._motivo}]"

class ConRedondeo(DecoradorCalificacion):
    def valor(self): return round(self._c.valor(), 1)
    def descripcion(self): return self._c.descripcion() + " [redondeado]"
