from __future__ import annotations

import math

# Module imports
from Geometry import Geometry
from Point import Point


class Circle(Geometry):

    """Circle Class"""

    def __init__(self, p: Point, r: float):
        """Initialize new Circle defined by the center point p and its radius r

        :p: center point
        :r: radius

        """
        self.p = p
        self.r = r

    def area(self) -> float:
        """Calculates area of the circle
        :returns: area

        """

        area = 2 * math.pi * self.r**2

        return area
