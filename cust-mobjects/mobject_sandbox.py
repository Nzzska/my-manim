from manim import *
from .Users.Oskaras.Desktop.Mymanim.custmobjects import MechanicsVector, ObjectDescription

class Test(Scene):
    def construct(self):
        sq = Square(2)
        self.add(sq)