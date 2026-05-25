class Estudiante:
    def __init__(self):
        self.nombre = self.codigo = self.carrera = self.semestre = self.email = self.promedio = None
    def __str__(self):
        return f"Estudiante[{self.nombre} | {self.carrera} | Sem {self.semestre}]"

class EstudianteBuilder:
    def __init__(self): self._e = Estudiante()
    def nombre(self, v):   self._e.nombre   = v; return self
    def codigo(self, v):   self._e.codigo   = v; return self
    def carrera(self, v):  self._e.carrera  = v; return self
    def semestre(self, v): self._e.semestre = v; return self
    def email(self, v):    self._e.email    = v; return self
    def promedio(self, v): self._e.promedio = v; return self
    def build(self):
        if not self._e.nombre: raise ValueError("Nombre obligatorio")
        return self._e

class DirectorMatricula:
    @staticmethod
    def construir_nuevo_ingreso(builder, nombre, codigo, carrera):
        return builder.nombre(nombre).codigo(codigo).carrera(carrera).semestre(1).promedio(0.0).build()
