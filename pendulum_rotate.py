from manim import *
from simulations.pendulum_sim import angle_pendulum_sim

class PendulumSim(Scene):
    def construct(self):
        pivot = Dot(color=RED).move_to(np.array([0., 1., 0]))
        weight = Circle(
            radius=0.5,
            color=RED, 
            fill_opacity=1
        ).move_to(np.array([1., -1., 0.]))
        rod = Line(
            color=RED, 
            start=pivot.get_center(), 
            end=weight.get_center(), 
            buff=0
        )

        vec = -1*weight.get_center() + pivot.get_center()
        vec_normed = vec/np.linalg.norm(vec)
        angle = np.arccos(vec_normed[1])

        simulation_result = angle_pendulum_sim(
            angle,
            9.8,
            np.linalg.norm(pivot.get_center()-weight.get_center()),
            np.linspace(0, 5, 101)
        )


        pendulum = VGroup(pivot, weight, rod)
        self.add(pendulum)
        previous_angle = angle
        for theta in simulation_result:
            self.play(
                pendulum.animate(
                    rate_func=linear,
                    run_time=5./len(simulation_result)
                ).rotate(
                    theta - previous_angle,
                    about_point=pivot.get_center()
                )
            )
            previous_angle = theta
        
