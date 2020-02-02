"""
    plate_number.py
    -------------------
    This python module contains all the logic related to a Plate number from Ecuador.
"""
from src.constants import PlateTypes
import re


class PlateNumber:

    def __init__(self, plate_number):
        self.plate_number = plate_number

    @staticmethod
    def is_a_valid_plate_number(plate_number):
        valid = re.compile(r'[ABUCHXOEWGILRMVNQSPYJKTZ][A-Z][A-Z]-[0-9][0-9][0-9][0-9]')
        try:
            return valid.match(plate_number) is not None or \
                   (PlateNumber.has_2_letters(plate_number) and PlateNumber.get_letters_from_plate(plate_number) in
                    PlateTypes.SERVICIO_DIPLOMATICO + PlateTypes.INTERNACION_TEMPORAL)
        except IndexError:
            return False

    def get_type(self):
        if PlateNumber.has_2_letters(self.plate_number):
            if PlateNumber.get_letters_from_plate(self.plate_number) in PlateTypes.SERVICIO_DIPLOMATICO:
                return PlateTypes.SERVICIO_DIPLOMATICO
            if PlateNumber.get_letters_from_plate(self.plate_number) in PlateTypes.INTERNACION_TEMPORAL:
                return PlateTypes.INTERNACION_TEMPORAL
        else:
            for type_ in list(PlateTypes):
                if self.get_second_letter() in type_:
                    return type_

    @staticmethod
    def has_2_letters(plate_number):
        return len(PlateNumber.get_letters_from_plate()) == 2

    @staticmethod
    def get_letters_from_plate(plate_number):
        return plate_number.split('-')[0]

    def get_second_letter(self):
        return PlateNumber.get_letters_from_plate(self.plate_number)[1]


