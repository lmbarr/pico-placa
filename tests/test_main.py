import pytest
from datetime import time, datetime
from src.main import can_be_on_the_road, is_time_inside_a_forbidden_range, is_allowed_to_circulate
from src.plate_number import PlateNumber


@pytest.mark.parametrize('date_,time_,plate_number,expected', [('2020-02-13', '16:05', 'CD-1010', 'si'),
                                                               ('2020-02-03', '09:29', 'ABC-1011', 'no'),
                                                               ('2020-02-02', '09:59', 'ABC-1010', 'si'),
                                                               ('2020-02-03', '09:29', 'PBI-1742', 'no'),
                                                               ('2020-02-03', '09:31', 'PBI-1742', 'si'),
                                                               ('2020-02-07', '09:29', 'PBI-1749', 'no')])
def test_can_be_on_the_road(date_, time_, plate_number, expected):
    assert expected in can_be_on_the_road(date_, time_, plate_number)


@pytest.mark.parametrize('time_,expected', [(time(7, 0), True), (time(6, 59), False), (time(9, 30), True),
                                            (time(9, 31), False), (time(19, 31), False)])
def test_is_time_inside_a_forbidden_range(time_, expected):
    assert is_time_inside_a_forbidden_range(time_) == expected


@pytest.mark.parametrize('plate_number, date_, time_,expected', [(PlateNumber('CD-1010'), datetime(2020, 2, 13), time(16, 5), True),
                                            (PlateNumber('ABC-1011'), datetime(2020, 2, 3), time(9, 29), False)])
def test_is_allowed_to_circulate(plate_number, date_, time_, expected):
    assert is_allowed_to_circulate(plate_number, date_, time_) == expected


@pytest.mark.parametrize('date_,time_,plate_number', [('2020-02-13', '16:05', 'CD-1010-AVC'),
                                                      ('2020-02-03', '09:29', 'vzx-1011'),
                                                      ('2020-02-02', '09:59', 'Aasdf10'),
                                                      ('2020-02-03', '09:29', '1441-1742'),
                                                      ('2020-02-03', '09:31', 'asdf-Abc'),
                                                      ('2020-02-07', '09:29', 'PBI-1749-AS')])
def test_invalid_plate_number(date_, time_, plate_number):
    assert "invalida" in can_be_on_the_road(date_, time_, plate_number)
