class ModuloNotas:
    def registrar_nota(self, codigo, materia, nota):
        return f"[NOTAS] Nota {nota:.1f} registrada para {codigo} en {materia}."
    def obtener_promedio(self, codigo): return 4.1
    def esta_aprobado(self, codigo, minima=3.0): return self.obtener_promedio(codigo) >= minima

class ModuloAsistencia:
    def calcular_porcentaje(self, codigo): return 88.5
    def cumple_minimo(self, codigo, minimo=75.0): return self.calcular_porcentaje(codigo) >= minimo

class ModuloCertificados:
    def emitir_certificado_notas(self, codigo, nombre): return f"[CERTIFICADOS] Certificado emitido para {nombre} ({codigo})."
    def emitir_paz_salvo(self, codigo): return f"[CERTIFICADOS] Paz y salvo emitido para {codigo}."

class SistemaAcademico:
    def __init__(self):
        self._notas = ModuloNotas()
        self._asistencia = ModuloAsistencia()
        self._certificados = ModuloCertificados()

    def registrar_calificacion(self, codigo, nombre, materia, nota):
        print(self._notas.registrar_nota(codigo, materia, nota))
        estado = "APROBADO" if self._notas.esta_aprobado(codigo) else "REPROBADO"
        print(f"  -> Promedio: {self._notas.obtener_promedio(codigo):.1f} | {estado}")

    def procesar_fin_semestre(self, codigo, nombre):
        print(f"\n{'='*45}\n  Cierre: {nombre} ({codigo})\n{'='*45}")
        print(f"  Asistencia: {self._asistencia.calcular_porcentaje(codigo)}%")
        print(f"  Promedio: {self._notas.obtener_promedio(codigo):.1f}")
        if self._asistencia.cumple_minimo(codigo) and self._notas.esta_aprobado(codigo):
            print(self._certificados.emitir_certificado_notas(codigo, nombre))
            print(self._certificados.emitir_paz_salvo(codigo))
