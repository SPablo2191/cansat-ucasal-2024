import flet as ft
from components.text_field import get_text_field
from components.gauge import Gauge
from models.ground_control_system_view_model import GroundControlSystemViewModel
import math

def main(page: ft.Page):
    page.title = "Cookie - Ground Control system (GCS)"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    page.scroll = ft.ScrollMode.HIDDEN
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    groundControlSystemViewModel = GroundControlSystemViewModel()
    gauge = Gauge()
    user_entry = get_text_field(value="0")

    def animate(e):
        gauge.value = user_entry.value
        if len(gauge.value) > 0:
            current_value = int(gauge.value)
            curr_degree = int(current_value * 3) + 210 % 360
            if current_value <= 50:
                gauge.pointer.rotate.angle = math.radians(curr_degree - 360)
            else:
                gauge.pointer.rotate.angle = math.radians(abs(curr_degree - 360))
        else:
            gauge.pointer.rotate.angle = gauge.math.radians(curr_degree - 360)
        page.update()

    page.add(
        ft.Row(
            controls=[

            ]
        )
    )


if __name__ == "__main__":
    DESKTOP = True
    try:
        WEB_PORT = 8000

        if DESKTOP:
            ft.app(target=main, assets_dir="assets")
        else:
            ft.app(target=main, assets_dir="assets", port=WEB_PORT, view=ft.WEB_BROWSER)

    except Exception as app_error:
        print(app_error)
