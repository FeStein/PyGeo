from __future__ import annotations

import math


class Point(object):

    """!
    @author Felix Steinmetz

    @brief Class representing a Point

    @details This class represents an arbitrary Point in a 2 dimensional space.

    """

    def __init__(self, x: int, y: int):
        """!
        @brief The constructor of the Point class

        @details Initialize new Point defined by the coordinates @p x and @p y.

        @param[in] x,y Coordinates of the Point.

        @return Instance of the Point class.

        """

        self.x = x
        self.y = y

    def distance(self, p2: Point) -> float:
        """!
        @brief distance between point and @p p2

        @details Calculates the distance between the Point and @p p2.

        @param[in] p2 Point to calculate the distance to.

        @return distance between the Point and @p p2.

        """

        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)
