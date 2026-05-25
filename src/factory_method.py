from abc import ABC, abstractmethod

class Reporte(ABC):
    @abstractmethod
    def generar(self, datos: dict) -> str: pass
    @abstractmethod
    def extension(self) -> str: pass

class ReportePDF(Reporte):
    def generar(self, datos): return f"[PDF] Reporte: {datos.get('nombre')} | {datos.get('materia')} | {datos.get('nota')}"
    def extension(self): return "pdf"

class ReporteExcel(Reporte):
    def generar(self, datos): return f"[EXCEL] Reporte: {datos.get('nombre')} | {datos.get('materia')} | {datos.get('nota')}"
    def extension(self): return "xlsx"

class ReporteHTML(Reporte):
    def generar(self, datos): return f"<html><body><p>{datos.get('nombre')} - {datos.get('nota')}</p></body></html>"
    def extension(self): return "html"

class FabricaReporte(ABC):
    @abstractmethod
    def crear_reporte(self) -> Reporte: pass
    def publicar(self, datos): return self.crear_reporte().generar(datos)

class FabricaPDF(FabricaReporte):
    def crear_reporte(self): return ReportePDF()

class FabricaExcel(FabricaReporte):
    def crear_reporte(self): return ReporteExcel()

class FabricaHTML(FabricaReporte):
    def crear_reporte(self): return ReporteHTML()
