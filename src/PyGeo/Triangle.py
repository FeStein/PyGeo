from __future__ import annotations

from math import sqrt

# Module imports
from PyGeo.Geometry import Geometry
from PyGeo.Point import Point


class Triangle(Geometry):

    """!
    @author Felix Steinmetz

    @brief Class representing a Triangle

    @details This class represents an arbitrary Triangle in a 2 dimensional space. It is defined by its three corner
        points.
    """

    def __init__(self, p1: Point, p2: Point, p3: Point):
        """!
        @brief The constructor of the Triangle class.

        @details Initialize new Triangle defined by the 3 corner points p1-p3.

        @param[in] p1,p2,p3 Corner points of the Triangle.

        @return Instance of the Triangle class.

        """

        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self) -> float:
        """!
        @brief Calculates the area of the Triangle

        @return Calculated area of the triangle.

        """

        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)

        s = (a + b + c) / 2

        area = sqrt(s * (s - a) * (s - b) * (s - c))

        return area

    def perimeter(self) -> float:
        """!
        @brief Calculates the perimeter of the Triangle

        @return Calculated perimeter of the triangle.

        """

        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)

        perimeter = a + b + c

        return perimeter
