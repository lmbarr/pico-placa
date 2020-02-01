import re


class PlateNumber:

    def __init__(self, plate_number):
        self.plate_number = plate_number

    @staticmethod
    def is_a_valid_plate_number():
        pass

    @classmethod
    def constructor(cls, plate_number):
        if cls.is_a_valid_plate_number():
            return cls(plate_number)


    def has_right_pattern(plate_number):
        valid = re.compile(r'[A-Z][A-Z][A-Z]-[0-9][0-9][0-9][0-9]')
        return valid.match(plate_number) is not None


    def get_letters_from_plate(plate_number):
        return plate_number.split('-')[0]