from flet import (
    Image,
    ImageFit,
    transform,
    animation,
    alignment,
    AnimationCurve,
    Stack,
    Page,
)
import math

def get_gauge(referent_value: str, page: Page):
    def animate(e):
        value = referent_value
        if len(value) > 0:
            current_value = int(value)
            curr_degree = int(current_value * 3) + 210 % 360
            if current_value <= 50:
                pointer.rotate.angle = math.radians(curr_degree - 360)
            else:
                pointer.rotate.angle = math.radians(abs(curr_degree - 360))
        else:
            pointer.rotate.angle = math.radians(curr_degree - 360)
        page.update()

    value = "0"
    pointer = Image(
        src="images/gauge_pointer.png",
        fit=ImageFit.CONTAIN,
        rotate=transform.Rotate(-2.6179938779914944, alignment=alignment.center),
        animate_rotation=animation.Animation(800, AnimationCurve.DECELERATE),
    )
    gauge_background = Image(
        src="images/gauge.png",
        fit=ImageFit.CONTAIN,
    )
    gauge_cap = Image(
        src="images/gauge_cap.png",
        fit=ImageFit.CONTAIN,
    )
    return Stack(
        [gauge_background, pointer, gauge_cap],
        width=350,
        height=350,
    )
