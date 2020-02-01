from .predicates import has_right_pattern, get_letters_from_plate


def validate_plate_number(plate_number: string):
    if has_right_pattern(plate_number):
        first_letter, second_letter, third_letter = get_letters_from_plate(plate_number)


    else:
        print("Wrong input")
