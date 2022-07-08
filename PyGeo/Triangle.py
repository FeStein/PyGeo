from __future__ import annotations

import math

# Module imports
from Point import Point
from Geometry import Geometry


class Triangle(object):

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

        area = self.p1.x * self.p2.y + self.p2.x * self.p3.y + self.p3.x * self.p1.y - \
            self.p1.y * self.p2.x - self.p2.y * self.p3.x - self.p3.y * self.p1.x

        return area / 2
