from __future__ import annotations
import math


class Point(object):

    """Class to represent a carthesian point"""

    def __init__(self, x: int, y: int):
        """Initialize Point class

        :x: x coordinate
        :y: y coordinate

        """
        self.x = x
        self.y = y

    def distance(self, p2: Point) -> float:
        """Calculates the distance to the second point p2

        :p2: Point to calculate distance to
        :returns: distance
        """
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)
