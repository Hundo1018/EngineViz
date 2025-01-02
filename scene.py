from manim import *


class AABBScene(Scene):
    def construct(self):
        circle = Circle(2)  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square(2)  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        
        line = Line()
        line.set_fill(GREEN,opacity=0.5)

        axes = Axes([1, 20, 1], [1, 20, 1], axis_config={"include_numbers": True})

        self.add(axes)
        self.play(Create(circle), Create(square),Create(line))  # show the shapes on screen
