class Oportunidad:
    clientes = {}
    actividades = {}

    def __init__(self, id_oportunidad, etapa, prioridad, riesgo, correo):
        self.id_oportunidad = id_oportunidad
        self.etapa = etapa
        self.prioridad = prioridad
        self.riesgo = riesgo
        self.correo = correo

    # getters

    def setCliente(self, cliente):
        self.clientes[cliente.id_clie] = cliente

    def setActividad(self, actividad):
        self.actividades[actividad.id_actividad] = actividad
