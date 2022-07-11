from __future__ import annotations

import math

# Module imports
from PyGeo.Geometry import Geometry
from PyGeo.Point import Point


class Circle(Geometry):

    """!
    @author Felix Steinmetz

    @brief Class representing a Circle

    @details This class represents an arbitrary Circle in a 2 dimensional space. It is defined by its center point @p
        and its radius @r.
    """

    def __init__(self, p: Point, r: float):
        """!
        @brief The concstructor of the Circle class.

        @details Initialize new Circle defined by the center point p and its radius r

        @param[in] p Center point of the Circle.
        @param[in] r Radius of the Circle.

        @return Instance of the Circle class.

        """
        self.p = p
        self.r = r

    def area(self) -> float:
        """!
        @brief Calculates the area of the Circle

        @return Calculated area of the Circle.

        """

        area = math.pi * self.r**2

        return area


def perimeter(self) -> float:
    """!
    @brief Calculates the perimeter of the Circle

    @return Calculated perimeter of the Circle.

    """

    perimeter = 2 * math.pi * self.r

    return perimeter
