"""
    constants.py
    -------------
    This python module contains all the specifics about the pico y placa logic.
"""
from enum import Enum, auto
from datetime import time


Days = {'MONDAY': (1, 2),
        'Tuesday': (3, 4),
        'Wednesday': (5, 6),
        'Thursday': (7, 8),
        'Friday': (9, 10)}


class ForbiddenTimeRanges(Enum):
    FIRST_RANGE = (time(7, 0), time(9, 30))
    SECOND_RANGE = (time(16, 0), time(19, 30))


class PlateTypes(Enum):
    COMERCIAL = auto()
    GUBERNAMENTAL = auto()
    DE_USO_OFICIAL = auto()
    GOBIERNO_AUTONOMO = auto()
    PARTICULAR = auto()
    SERVICIO_DIPLOMATICO = auto()
    INTERNACION_TEMPORAL = auto()

