
class Oportunidad:

    def __init__(self, id_oportunidad, etapa, prioridad, riesgo, correo):
        self.id_oportunidad = id_oportunidad
        self.etapa = etapa
        self.prioridad = prioridad
        self.riesgo = riesgo
        self.correo = correo
        self.listaClientes = {}
        self.listaActividades = {}
