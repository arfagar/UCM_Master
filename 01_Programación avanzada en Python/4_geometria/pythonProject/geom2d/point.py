from geom2d import Vector
from typing import Self


class Point:
    def __init__(self, x: float, y: float):
        # _x e _y son atributos privados.
        self._x: float = x
        self._y: float = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @x.setter
    def x(self, x) -> None:
        self._x = x

    @y.setter
    def y(self, y) -> None:
        self._y = y

    def __str__(self) -> str:
        return f"({self.x:.4f}, {self.y:.4f})"

    def __repr__(self) -> str:
        return f"V({self.x}, {self.y})"

    @staticmethod
    def label_class():
        return 1

    def __hash__(self):
        return hash((self.label_class, self.x, self.y))

    def __sub__(self, other: Self) -> Vector:
        x_new = self.x-other.x
        y_new = self.y-other.y
        return Vector(x_new, y_new)

    def distance(self, other: Self) -> float:
        return (self-other).mod
