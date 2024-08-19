from manim import *


class ParabolaIntro(Scene):
    def construct(self):
        a_tracker = ValueTracker(1)
        b_tracker = ValueTracker(0)
        c_tracker = ValueTracker(0)
        formula_with_parameters = always_redraw(lambda: MathTex(r"f(x) &= {{a}}x^2 + {{b}}x + {{c}} \ (a \neq 0)\\ " +
                                                                r"a &= " + f'{a_tracker.get_value():.2f} \\\\' +
                                                                r"b &= " + f'{b_tracker.get_value():.2f} \\\\' +
                                                                r"c &= " + f'{c_tracker.get_value():.2f} \\\\')
                                                .shift(LEFT * 4))
        graph_x_range = [-4, 4]
        number_plain = NumberPlane(x_range=graph_x_range).shift(RIGHT * 3)
        number_plain.add_coordinates()
        graph = always_redraw(lambda: number_plain.plot(
            lambda x: a_tracker.get_value() * x * x + b_tracker.get_value() * x + c_tracker.get_value()))
        self.play(Write(formula_with_parameters))
        self.play(DrawBorderThenFill(number_plain))
        self.play(Write(graph))
        self.play(a_tracker.animate.set_value(-2), b_tracker.animate.set_value(-8), c_tracker.animate.set_value(-6),
                  run_time=3)
        self.pause(1)
        self.play(a_tracker.animate.set_value(3), b_tracker.animate.set_value(6), c_tracker.animate.set_value(1),
                  run_time=3)
        self.pause(1)
        self.play(a_tracker.animate.set_value(2), b_tracker.animate.set_value(-8), c_tracker.animate.set_value(5),
                  run_time=3)
        self.pause(1)
        self.play(a_tracker.animate.set_value(1), b_tracker.animate.set_value(0), c_tracker.animate.set_value(0),
                  run_time=3)
        self.pause(1)
        dot_point = always_redraw(lambda: Dot((-b_tracker.get_value() / (2 * a_tracker.get_value()),
                                               -(b_tracker.get_value() * b_tracker.get_value() -
                                                 4 * a_tracker.get_value() * c_tracker.get_value()) / (
                                                       4 * a_tracker.get_value()),
                                               0)).set_color(YELLOW).shift(RIGHT * 3))
        dot_label = always_redraw(lambda: MathTex("A").set_color(YELLOW).next_to(dot_point))
        dot = VGroup(dot_point, dot_label)
        self.play(Write(dot))
        formula_with_question = always_redraw(lambda: MathTex(r"A (?, ?)")
                                              .shift(LEFT * 4))
        formula_with_parameters.clear_updaters()
        self.play(FadeTransform(formula_with_parameters, formula_with_question))
        self.pause(1)
        self.play(FadeOut(formula_with_question, graph, dot, number_plain))


class FormulaTransform(Scene):
    def construct(self):
        formula1 = MathTex(r"{{f(x)}} = {{a}}{{x^2}} + {{b}}{{x}} + {{c}}")

        formula1_copy = formula1.copy()
        self.play(Write(formula1))
        self.play(Circumscribe(formula1[5]))
        formula2 = MathTex(r"{{f(x)}} = {{a}}{{x^2}} + {{\frac{a \cdot  b}{a}}}{{x}} + {{c}}")
        self.play(TransformMatchingTex(formula1, formula2))
        self.pause(1)
        self.play(Indicate(formula2[2]), Indicate(formula2[5][0]))
        self.pause(1)
        formula3 = MathTex(r"{{f(x)}} = {{a}}\left({{x^2}} + {{\frac{b}{a}}}{{x}}\right) + {{c}}")
        self.play(TransformMatchingTex(formula2, formula3))
        self.pause(1)
        self.pause(1)
        formula4 = MathTex(r"{{f(x)}} = {{a}}\left({{x^2}} + 2 \cdot {{\frac{b}{2a}}}{{x}}\right) + {{c}}")
        self.play(Circumscribe(formula3[6]))
        self.play(TransformMatchingTex(formula3, formula4))
        self.pause(1)
        self.play(Circumscribe(formula4[6]))
        self.pause(1)
        formula5 = MathTex(r"{{f(x)}} = {{a}}\left({{x^2}} + 2 \cdot {{\frac{b}{2a}}}{{x}} + "
                           r"{{\left(\frac{b}{2a}\right)^2}} - {{\left(\frac{b}{2a}\right)^2}} \right) + {{c}}")
        self.play(TransformMatchingTex(formula4, formula5))
        self.pause(1)
        self.play(Circumscribe(formula5[12]))
        formula6 = MathTex(r"{{f(x)}} = {{a}}\left({{x^2}} + 2 \cdot {{\frac{b}{2a}}}{{x}} + "
                           r"{{\left(\frac{b}{2a}\right)^2}} - {{\frac{b^2}{4a^2}}} \right) + {{c}}")
        self.play(TransformMatchingTex(formula5, formula6))
        formula7 = MathTex(r"{{f(x)}} = {{a}}\left({{x^2}} + 2 \cdot {{\frac{b}{2a}}}{{x}} + "
                           r"{{\left(\frac{b}{2a}\right)^2}} \right) - {{\frac{b^2}{4a}}} + {{c}}")
        self.play(TransformMatchingTex(formula6, formula7))
        self.pause(1)
        hint_f7 = MathTex(r"a^2 + 2ab + b^2 = (a+b)^2").scale(0.5)
        hint_f7.move_to(formula7.get_top()).shift(UP * 0.3)
        self.play(FadeIn(hint_f7))
        self.pause(1)
        formula8 = MathTex(
            r"{{f(x)}} = {{a}}\left({{x}} + {{\frac{b}{2a}}}\right)^2 - {{\frac{b^2}{4a^2}}} + {{c}}")
        self.play(TransformMatchingTex(formula7, formula8), FadeOut(hint_f7))
        self.pause(1)
        self.play(Circumscribe(formula8[9]))
        formula9 = MathTex(r"{{f(x)}} = {{a}}\left({{x}} + {{\frac{b}{2a}}}\right)^2 - {{\frac{b^2 - 4ac}{4a}}}")
        self.play(TransformMatchingTex(formula8, formula9))
        self.pause(1)
        self.play(Circumscribe(formula9[8]))
        final_formula = MathTex(r"{{f(x)}} = {{a}}\left({{x}} + {{\frac{b}{2a}}}\right)^2 {{- \frac{D}{4a}}}")
        self.play(TransformMatchingTex(formula9, final_formula))
        self.pause(1)
        self.play(final_formula.animate.shift(UP))
        x_cord = MathTex().add(final_formula[6].copy())
        y_cord = MathTex().add(final_formula[8].copy())
        self.add(x_cord, y_cord)
        x_0 = MathTex(r"x_{0} = - {{\frac{b}{2a}}}")
        y_0 = MathTex(r"y_{0} = {{- \frac{D}{4a}}}").shift(DOWN * 1.5)
        self.play(TransformMatchingTex(x_cord, x_0), TransformMatchingTex(y_cord, y_0))
        self.pause(1)
