import pytest

from PyGeo.Point import Point

@pytest.mark.parametrize("test_input,expected", [
    (Point(3, 3), 4.242640687119285), 
    (Point(3, -3), 4.242640687119285), 
    (Point(-3, 3), 4.242640687119285), 
    (Point(-3, -3), 4.242640687119285), 
    (Point(0, 3), 3), 
    (Point(3, 0), 3), 
    (Point(0, -3), 3), 
    (Point(-3, 0), 3), 
    ])

def test_distance(test_input, expected):
    p0 = Point(0, 0)
    assert p0.distance(test_input) == expected
