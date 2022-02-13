class Actividad:
    def __init__(self, id_actividad, oportunidad, fecha_inicio, fecha_fin, resumen, descripcion):
        self.id_actividad = id_actividad
        self.oportunidad = oportunidad
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.resumen = resumen
        self.descripcion = descripcion

    def getId_actividad(self):
        return self

    def getOportunidad(self):
        return self

    def getFecha_inicio(self):
        return self

    def getFecha_fin(self):
        return self

    def getResumen(self):
        return self

    def getDescripcion(self):
        return self

        # setters

    def setId(self, id_actividad):
        self.id_actividad = id_actividad

    def setOportunidad(self, oportunidad):
        self.oportunidad = oportunidad

    def setFecha_inicio(self, fecha_inicio):
        self.fecha_inicio = fecha_inicio

    def setFecha_fin(self, fecha_fin):
        self.fecha_fin = fecha_fin

    def setResumen(self, resumen):
        self.resumen = resumen

    def setDescripcion(self, descripcion):
        self.resumen = descripcion
