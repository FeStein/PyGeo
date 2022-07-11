import pytest

from PyGeo.Point import Point
from PyGeo.Triangle import Triangle


@pytest.mark.parametrize("test_input,expected", [
    ((Point(-1, 0), Point(1, 0), Point(0, 2)), 2),
    ((Point(1, 0), Point(-1, 0), Point(0, 2)), 2),
    ((Point(0, 2), Point(-1, 0), Point(1, 0)), 2),
])
def test_area(test_input, expected):
    T = Triangle(test_input[0], test_input[1], test_input[2])
    assert T.area() == expected
