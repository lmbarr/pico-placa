"""
    constants.py
    -------------
    This python module contains all the specifics about the pico y placa logic.
"""
from enum import Enum, auto
from datetime import time
from string import ascii_uppercase

Days = {'MONDAY': (1, 2),
        'Tuesday': (3, 4),
        'Wednesday': (5, 6),
        'Thursday': (7, 8),
        'Friday': (9, 10)}


class ForbiddenTimeRanges(Enum):
    FIRST_RANGE = (time(7, 0), time(9, 30))
    SECOND_RANGE = (time(16, 0), time(19, 30))


class PlateTypes(Enum):
    COMERCIAL = {'A', 'U', 'Z'}
    GUBERNAMENTAL = {'E'}
    DE_USO_OFICIAL = {'X'}
    GOBIERNO_AUTONOMO = {'M'}
    PARTICULAR = set(ascii_uppercase) - (COMERCIAL + GUBERNAMENTAL + DE_USO_OFICIAL + GOBIERNO_AUTONOMO)
    SERVICIO_DIPLOMATICO = {'CC', 'CD', 'OI', 'AT'}
    INTERNACION_TEMPORAL = {'IT'}
