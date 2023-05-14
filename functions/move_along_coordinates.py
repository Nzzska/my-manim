from manim import *

def move_along_coordinates(
        coordinates:np.ndarray,
        moving_mobject:Mobject,
        scene:Scene,
        rt:float = 10.
):
    single_rt = rt/len(coordinates)
    for X in coordinates:
        scene.play(
            moving_mobject.animate(
                run_time=single_rt,
                rate_func=linear,
                lag_ratio=0
            ).move_to(X)
        )