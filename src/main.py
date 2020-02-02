"""
    main.py
    --------------
    This python module is the first layer of all the logic and at a high level
    determine if a vehicule can circulate or not.
"""
from src.plate_number import PlateNumber
from datetime import datetime, time
from src.constants import PlateTypes, ForbiddenTimeRanges, Days


def can_be_on_the_road(date_, time_, plate_number):
    """
    This function determined at a high level if a vehicle can or can not be on the roads of Quito.
    :param date_: The string date that we get from the templates/template.html page
    :param time_: The string time that we get from the templates/template.html page
    :param plate_number: The string license plate number that we get from the templates/template.html page
    :return: The string message to be rendered in the templates/response.html
    """

    if PlateNumber.is_a_valid_plate_number(plate_number):
        plate_number = PlateNumber(plate_number)
        date_ = datetime(*[int(num) for num in date_.split('-')])
        time_ = time(*[int(num) for num in time_.split(':')])

        if is_allowed_to_circulate(plate_number, date_, time_):
            return f"Vehiculo con placas {plate_number.plate_number} en la fecha {date_.strftime('%m/%d/%Y')} y hora {time_} puede circular"
        else:
            return f"Vehiculo con placas {plate_number.plate_number} en la fecha {date_.strftime('%m/%d/%Y')} y hora {time_} no puede circular"
    else:
        return "Placa invalida"


def is_allowed_to_circulate(plate_number, date_, time_):
    if plate_number.get_type() is not PlateTypes.PARTICULAR:
        return True
    else:
        day = date_.strftime('%A')
        return plate_number.get_last_digit() not in Days.get(day, []) and not is_time_inside_a_forbidden_range(time_)


def is_time_inside_a_forbidden_range(time_):
    return any(range_[0] <= time_ <= range[1] for range_ in ForbiddenTimeRanges)
