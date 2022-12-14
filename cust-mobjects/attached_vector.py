from manim import *

class ObjectDescription:
    def __init__(
        self, 
        mobject: Mobject, 
        name: str,
        direction: np.ndarray,
        **kwargs
    ):
        self._mobject = mobject
        self._name = name
        self._position = mobject.get_center()
        self._direction = direction
        self._vector = self.create_vector(**kwargs)

    @property
    def direction(self) -> np.ndarray:
        return self._direction

    @direction.setter
    def direction(self, new_direction: np.ndarray):
        self._direction = new_direction

    @property
    def position(self) -> np.ndarray:
        return self._position

    @position.setter
    def position(self, new_position: np.ndarray):
        self._position = new_position

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    ########
    @property
    def vector(self, **kwargs) -> Arrow:
        return self._vector

    @vector.setter
    def vector(self, new_vector):
        self._vector = new_vector
    ########

    def create_vector(self, **kwargs) -> Arrow:
        return Arrow(
            start=self._position,
            end=self._position + self._direction,
            buff=0,
            **kwargs
        )

    def update_instance(self, new_dir, **kwargs):
        self._position = self._mobject.get_center()
        self._direction = new_dir
        self._vector.become(
            self.create_vector(**kwargs)
        )

    def __str__(self) -> str:
        return self.name