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
        """
        This method check if a plate number has the right format and if it's correct according to
        the ecuadorian laws.
        :param plate_number: The string plate number to be checked.
        :return: boolean
        """
        valid_standard_plate = re.compile(r'[ABUCHXOEWGILRMVNQSPYJKTZ][A-Z][A-Z]-[0-9][0-9][0-9][0-9]')
        valid_special_plate = re.compile(r'({})-[0-9][0-9][0-9][0-9]'.
                                         format('|'.join(PlateTypes.SERVICIO_DIPLOMATICO.value
                                                         | PlateTypes.INTERNACION_TEMPORAL.value)))
        try:
            return valid_standard_plate.fullmatch(plate_number) is not None or \
                   (PlateNumber.has_2_letters(plate_number) and valid_special_plate.fullmatch(plate_number) is not None)
        except IndexError:
            return False

    def get_type(self):
        """
        This method return the license type.
        :return: The plate type as a PlateTypes enum type.
        """
        if PlateNumber.has_2_letters(self.plate_number):
            if PlateNumber.get_letters_from_plate(self.plate_number) in PlateTypes.SERVICIO_DIPLOMATICO.value:
                return PlateTypes.SERVICIO_DIPLOMATICO
            if PlateNumber.get_letters_from_plate(self.plate_number) in PlateTypes.INTERNACION_TEMPORAL.value:
                return PlateTypes.INTERNACION_TEMPORAL
        else:
            for type_ in list(PlateTypes):
                if self.get_second_letter() in type_.value:
                    return type_

    @staticmethod
    def has_2_letters(plate_number):
        """
        This function determine is a plate number has 2 or 3 letters.
        :param plate_number: The plate number as string.
        :return: boolean
        """
        return len(PlateNumber.get_letters_from_plate(plate_number)) == 2

    @staticmethod
    def get_letters_from_plate(plate_number):
        """
        This function returns all the letters before the hiphen.
        :param plate_number: The plate number as a string.
        :return: The letters of a plate number.
        """
        return plate_number.split('-')[0]

    def get_second_letter(self):
        """
        This method returns the second letter of a plate number.
        :return: The second letter of a plate number as string.
        """
        return PlateNumber.get_letters_from_plate(self.plate_number)[1]

    def get_last_digit(self):
        """
        This method get the last digit of a plate to check if a particular/private car
        can move around the city.
        :return: The last digit of a plate as an integer.
        """
        return int(self.plate_number[-1])
