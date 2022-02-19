import enum


class Etapa(enum.Enum):
    nuevo = "nuevo"
    calificado = "Calificado"
    propuesta = "propuesta"
    ganada = "ganada"
    perdida = "perdida"