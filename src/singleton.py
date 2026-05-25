class ConfiguracionApp:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.idioma = "es"
            cls._instancia.max_estudiantes_por_grupo = 30
            cls._instancia.nota_minima_aprobacion = 3.0
            cls._instancia.nombre_institucion = "Universidad Nacional"
        return cls._instancia

    def actualizar(self, clave, valor):
        setattr(self, clave, valor)
        return self
