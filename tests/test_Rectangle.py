import pytest

from PyGeo.Point import Point
from PyGeo.Rectangle import Rectangle


@pytest.mark.parametrize("test_input,expected", [
    ((Point(0, 0), Point(1, 1)), 1),
    ((Point(0, 0), Point(3, 3)), 9),
    ((Point(0, 0), Point(3, -3)), 9),
    ((Point(0, 0), Point(-3, 3)), 9),
    ((Point(0, 0), Point(-3, -3)), 9),
])
def test_area(test_input, expected):
    R = Rectangle(test_input[0], test_input[1])
    assert R.area() == expected
