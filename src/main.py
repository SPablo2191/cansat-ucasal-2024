import flet as ft
from components.side_panel import get_side_panel
from models.ground_control_system_view_model import GroundControlSystemViewModel,State
import math

def main(page: ft.Page):
    groundControlSystemViewModel = GroundControlSystemViewModel()
    page.title = groundControlSystemViewModel.system_name
    page.fonts = {
        "inria sans" : "fonts/inria-sans.ttf"
    }
    page.theme = ft.Theme(font_family="inria sans")
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.HIDDEN
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # def animate(e):
    #     gauge.value = user_entry.value
    #     if len(gauge.value) > 0:
    #         current_value = int(gauge.value)
    #         curr_degree = int(current_value * 3) + 210 % 360
    #         if current_value <= 50:
    #             gauge.pointer.rotate.angle = math.radians(curr_degree - 360)
    #         else:
    #             gauge.pointer.rotate.angle = math.radians(abs(curr_degree - 360))
    #     else:
    #         gauge.pointer.rotate.angle = gauge.math.radians(curr_degree - 360)
    #     page.update()

    page.add(
        ft.Row(
            controls=[
                get_side_panel(
                    team_id= groundControlSystemViewModel.team_id,
                    mission_time = groundControlSystemViewModel.mission_time,
                    telemetry= groundControlSystemViewModel.telemetry,
                    heat_shield= groundControlSystemViewModel.hs_deployed,
                    simulation_mode= groundControlSystemViewModel.state == State.SIMULATION,
                    page = page
                )
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
