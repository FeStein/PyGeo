import pytest
from PyGeo.Circle import Circle
from PyGeo.Point import Point


@pytest.mark.parametrize("test_input,expected", [
    ((Point(0, 0), 0.5), 0.25 * 3.141592653589793),
    ((Point(0, 0), 1), 1*3.141592653589793),
    ((Point(0, 0), 5), 25*3.141592653589793),
])
def test_area(test_input, expected):
    C = Circle(test_input[0], test_input[1])
    assert C.area() == expected
