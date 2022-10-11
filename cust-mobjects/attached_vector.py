from turtle import position
from unicodedata import name
from manim import *

class ObjectDescription:
    def __init__(
        self, 
        mobject: Mobject, 
        name: str,
        direction: np.ndarray
    ):
        self._mobject = mobject
        self._name = name
        self._position = mobject.get_center()
        self._direction = direction

    @property
    def direction(self) -> Arrow:
        pass

    @property
    def position(self) -> np.ndarray:
        pass

    @property
    def name(self) -> str:
        pass

    def create_vector(self) -> Arrow:
        pass

    def __str__(self) -> str:
        return self.name