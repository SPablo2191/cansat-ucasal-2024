import flet as ft



class Gauge:
    def __init__(self):
        self.value = "0"
        self.pointer = ft.Image(
            src="images/gauge_pointer.png",
            fit=ft.ImageFit.CONTAIN,
            rotate=ft.transform.Rotate(
                -2.6179938779914944, alignment=ft.alignment.center
            ),
            animate_rotation=ft.animation.Animation(800, ft.AnimationCurve.DECELERATE),
        )
        self.gauge_background = ft.Image(
            src="images/gauge.png",
            fit=ft.ImageFit.CONTAIN,
        )
        self.gauge_cap = ft.Image(
            src="images/gauge_cap.png",
            fit=ft.ImageFit.CONTAIN,
        )

    def get_component(self):
        return ft.Stack(
            [self.gauge_background, self.pointer, self.gauge_cap],
            width=350,
            height=350,
        )


