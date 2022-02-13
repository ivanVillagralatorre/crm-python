# coding=utf-8
class Cliente:
    oport = {}

    def __init__(self, id_clie, nombre, apellido, telefono, email):
        self.id_clie = id_clie
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    def setOportunidad(self, oportunidad):
        self.oport[oportunidad.id_oportunidad] = oportunidad
