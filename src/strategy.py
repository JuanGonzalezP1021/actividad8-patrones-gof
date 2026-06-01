from abc import ABC, abstractmethod


class EstrategiaEvaluacion(ABC):
    """Interfaz comun para todas las estrategias de evaluacion."""
    @abstractmethod
    def calcular_nota_final(self, notas: list[float]) -> float:
        pass

    @abstractmethod
    def nombre(self) -> str:
        pass


class EvaluacionPromedio(EstrategiaEvaluacion):
    """Calcula la nota final como promedio simple de todas las notas."""
    def calcular_nota_final(self, notas):
        if not notas:
            return 0.0
        return round(sum(notas) / len(notas), 2)

    def nombre(self):
        return "Promedio Simple"


class EvaluacionPonderada(EstrategiaEvaluacion):
    """Calcula la nota final dando mas peso a las ultimas evaluaciones.

    Los pesos se asignan de forma lineal creciente: la primera nota tiene
    peso 1, la segunda peso 2, etc.
    """
    def calcular_nota_final(self, notas):
        if not notas:
            return 0.0
        pesos = list(range(1, len(notas) + 1))
        total = sum(n * p for n, p in zip(notas, pesos))
        return round(total / sum(pesos), 2)

    def nombre(self):
        return "Ponderada Progresiva"


class EvaluacionMejorN(EstrategiaEvaluacion):
    """Calcula la nota final usando solo las mejores N calificaciones."""
    def __init__(self, n: int = 3):
        self._n = n

    def calcular_nota_final(self, notas):
        if not notas:
            return 0.0
        mejores = sorted(notas, reverse=True)[:self._n]
        return round(sum(mejores) / len(mejores), 2)

    def nombre(self):
        return f"Mejores {self._n}"


class ContextoEvaluacion:
    """Contexto que usa una estrategia de evaluacion intercambiable."""
    def __init__(self, estrategia: EstrategiaEvaluacion):
        self._estrategia = estrategia

    def cambiar_estrategia(self, estrategia: EstrategiaEvaluacion):
        self._estrategia = estrategia

    def evaluar(self, estudiante: str, notas: list[float]) -> str:
        nota_final = self._estrategia.calcular_nota_final(notas)
        estado = "APROBADO" if nota_final >= 3.0 else "REPROBADO"
        return (f"{estudiante} | Estrategia: {self._estrategia.nombre()} | "
                f"Nota final: {nota_final:.2f} | {estado}")

    @property
    def estrategia_actual(self):
        return self._estrategia
