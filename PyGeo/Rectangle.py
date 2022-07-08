from __future__ import annotations

import math

# Module imports
from Point import Point
from Geometry import Geometry

class Rectangle(object):

    """Rectangle Class"""

    def __init__(self, p1: Point, p2: Point):
        """Initialize new Rectangle defined by the corner points p1 and p2

        :p1: First corner point
        :p2: First corner point

        """
        self.p1 = p1
        self.p2 = p2

    def area(self) -> float:
        """Calculates area of the rectangle
        :returns: area

        """
        x_dis = abs(self.p1.x - self.p2.x)
        y_dis = abs(self.p1.y - self.p2.y)

        area = x_dis * y_dis

        return area
