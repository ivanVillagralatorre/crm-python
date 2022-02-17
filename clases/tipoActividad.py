import enum


class TipoActividad(enum.Enum):
    nuevo = "nuevo"
    calificado = "Calificado"
    propuesta = "propuesta"
    ganada = "ganada"
    perdida = "perdida"
