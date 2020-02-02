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
        valid_standard_plate = re.compile(r'[ABUCHXOEWGILRMVNQSPYJKTZ][A-Z][A-Z]-[0-9][0-9][0-9][0-9]')
        valid_special_plate = re.compile(r'({})-[0-9][0-9][0-9][0-9]'.
                                         format('|'.join(PlateTypes.SERVICIO_DIPLOMATICO.value
                                                         | PlateTypes.INTERNACION_TEMPORAL.value)))
        try:
            print(valid_special_plate)
            print(valid_special_plate.match(plate_number))
            return valid_standard_plate.match(plate_number) is not None or \
                   (PlateNumber.has_2_letters(plate_number) and valid_special_plate.match(plate_number) is not None)
        except IndexError:
            return False

    def get_type(self):
        if PlateNumber.has_2_letters(self.plate_number):
            if PlateNumber.get_letters_from_plate(self.plate_number) in PlateTypes.SERVICIO_DIPLOMATICO.value:
                return PlateTypes.SERVICIO_DIPLOMATICO
            if PlateNumber.get_letters_from_plate(self.plate_number) in PlateTypes.INTERNACION_TEMPORAL.value:
                return PlateTypes.INTERNACION_TEMPORAL
        else:
            for type_ in list(PlateTypes):
                if self.get_second_letter() in type_:
                    return type_

    @staticmethod
    def has_2_letters(plate_number):
        return len(PlateNumber.get_letters_from_plate(plate_number)) == 2

    @staticmethod
    def get_letters_from_plate(plate_number):
        return plate_number.split('-')[0]

    def get_second_letter(self):
        return PlateNumber.get_letters_from_plate(self.plate_number)[1]


