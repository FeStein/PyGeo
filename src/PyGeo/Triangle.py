from __future__ import annotations

from math import sqrt

# Module imports
from PyGeo.Geometry import Geometry
from PyGeo.Point import Point


class Triangle(Geometry):

    """Triangle Class"""

    def __init__(self, p1: Point, p2: Point, p3: Point):
        """Initialize new Triangle defined by the 3 corner points p1-p3.

        :p1: first corner point
        :p2: second corner point
        :p3: third corner point

        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self) -> float:
        """Calculates area of the Triangle
        :returns: area

        """

        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)

        s = (a + b + c) / 2

        area = sqrt(s * (s - a) * (s - b) * (s - c))

        return area
