from __future__ import annotations

from PyGeo.Geometry import Geometry
# Module imports
from PyGeo.Point import Point


class Rectangle(Geometry):

    """!
    @author Felix Steinmetz

    @brief Class representing a Rectangle

    @details This class represents an arbitrary Rectangle in a 2 dimensional
        space. It is defined by its two corner points.
    """

    def __init__(self, p1: Point, p2: Point):
        """!
        @brief The constructor of the Rectangle class.

        @details Initialize new Rectangle defined by the two corner points p1 and p2.

        @param[in] p1,p2 Corner points of the Rectangle.

        @return Instance of the Rectangle class.

        """

        self.p1 = p1
        self.p2 = p2

    def area(self) -> float:
        """!
        @brief Calculates the area of the Rectangle

        @return Calculated area of the Rectangle.

        """
        x_dis = abs(self.p1.x - self.p2.x)
        y_dis = abs(self.p1.y - self.p2.y)

        area = x_dis * y_dis

        return area


def perimeter(self) -> float:
    """!
    @brief Calculates the perimeter of the Rectangle

    @return Calculated perimeter of the Rectangle.

    """
    x_dis = abs(self.p1.x - self.p2.x)
    y_dis = abs(self.p1.y - self.p2.y)

    perimeter = 2 * (x_dis + y_dis)

    return perimeter
