from manim import *

class MechanicsVector(Arrow):
    """ A vector specialized for use in animations of motion.

    Parameters
    ----------
    #Todo
    """
    def __init__(
        self,
        center_mob: Mobject,
        name: str = 'v',
        buff: float = 0.,
        direction: np.ndarray = RIGHT, 
        **kwargs
    ):
        self._buff = buff
        self._name = name
        self._center_mob = center_mob
        self._direction = direction
        if len(direction) == 2:
            direction = np.hstack([direction, 0])
        super().__init__(
            start=center_mob.get_center(), 
            end=direction+center_mob.get_center(), 
            buff=buff, 
            **kwargs
        )
    
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, new_direction: np.ndarray):
        if len(new_direction) == 2:
            new_direction = np.hstack([new_direction, 0])
        self._direction = new_direction

    @direction.getter
    def direction(self) -> np.ndarray:
        return self._direction
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @name.getter
    def name(self) -> str:
        return self._name


    def get_tex_name(self, **kwargs) -> Tex:
        return Tex(
            tex_strings=f"$\\vec{{self.name}}$", 
            **kwargs
        ).next_to(self.get_center())

    def update_vector(self, new_dir):
        self._direction = new_dir
        self.put_start_and_end_on(
            start=self._center_mob.get_center(),
            end=self._center_mob.get_center() + self._direction
        )

    def __str__(self):
        return self.name

