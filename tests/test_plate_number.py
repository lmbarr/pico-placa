import pytest
from src.plate_number import PlateNumber
from src.constants import PlateTypes


@pytest.mark.parametrize('plate_number,expected', [('PBI-1742-1234', False), ('PBI-1742', True), ('fasfd', False),
                                                   ('AxA-1111', False)])
def test_is_a_valid_plate_number(plate_number, expected):
    assert PlateNumber.is_a_valid_plate_number(plate_number) == expected


@pytest.mark.parametrize('plate_number,expected', [(PlateNumber('PBI-1742'), PlateTypes.PARTICULAR),
                                                   (PlateNumber('CD-1742'), PlateTypes.SERVICIO_DIPLOMATICO),
                                                   (PlateNumber('AAB-0123'), PlateTypes.COMERCIAL),
                                                   (PlateNumber('IT-0654'), PlateTypes.INTERNACION_TEMPORAL)])
def test_get_type(plate_number, expected):
    assert plate_number.get_type() == expected


@pytest.mark.parametrize('plate_number,expected', [(PlateNumber('PBI-1742'), False),
                                                   (PlateNumber('CD-1742'), True),
                                                   (PlateNumber('AAB-0123'), False),
                                                   (PlateNumber('IT-0654'), True)])
def test_has_2_letters(plate_number, expected):
    assert PlateNumber.has_2_letters(plate_number.plate_number) == expected


@pytest.mark.parametrize('plate_number,expected', [(PlateNumber('PBI-1742'), 'PBI'),
                                                   (PlateNumber('CD-1742'), 'CD'),
                                                   (PlateNumber('AAB-0123'), 'AAB'),
                                                   (PlateNumber('IT-0654'), 'IT')])
def test_get_letters_from_plate(plate_number, expected):
    assert PlateNumber.get_letters_from_plate(plate_number.plate_number) == expected


@pytest.mark.parametrize('plate_number,expected', [(PlateNumber('PBI-1742'), 2),
                                                   (PlateNumber('CD-1742'), 2),
                                                   (PlateNumber('AAB-0123'), 3),
                                                   (PlateNumber('IT-0654'), 4)])
def test_get_last_digit(plate_number, expected):
    assert plate_number.get_last_digit() == expected
