import plate_number
from datetime import datetime, time
import time
from .constants import PlateTypes, ForbiddenTimeRanges, Days


def can_be_on_the_road(date_, time_, plate_number):

    if plate_number.PlateNumber.is_a_valid_plate_number(plate_number):
        plate_number = plate_number.PlateNumber(plate_number)
        date_ = datetime(*date_.split('-'))
        time_ = time(*time_.split(':'))

        if is_allowed_to_circulate(plate_number, date_, time_):
            return f"Vehiculo con placas {plate_number} en la fecha {date_} y hora {time_} puede circular"
        else:
            return f"Vehiculo con placas {plate_number} en la fecha {date_} y hora {time_} no puede circular"
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
