import flet as ft
import math
from components.side_panel import get_side_panel
from components.header_panel import get_header_panel
from components.console_panel import get_console_panel
from components.body_panel import get_body_panel
from models.ground_control_system_view_model import GroundControlSystemViewModel, State


def main(page: ft.Page):
    groundControlSystemViewModel = GroundControlSystemViewModel()
    page.title = groundControlSystemViewModel.system_name
    page.fonts = {"inria sans": "fonts/inria-sans.ttf"}
    page.theme = ft.Theme(font_family="inria sans")
    page.padding = 20
    page.scroll = ft.ScrollMode.HIDDEN
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.splash = ft.ProgressBar(visible=False)

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
                    team_id=groundControlSystemViewModel.team_id,
                    mission_time=groundControlSystemViewModel.mission_time,
                    telemetry=groundControlSystemViewModel.telemetry,
                    heat_shield=groundControlSystemViewModel.hs_deployed,
                    simulation_mode=groundControlSystemViewModel.state
                    == State.SIMULATION,
                    page=page,
                ),
                ft.Column(
                    controls=[
                        get_header_panel(
                            state=groundControlSystemViewModel.state,
                            packet_count=groundControlSystemViewModel.packet_count,
                            temperature=groundControlSystemViewModel.temperature,
                            pressure=groundControlSystemViewModel.pressure,
                            voltage=groundControlSystemViewModel.voltage,
                        ),
                        get_body_panel(),
                        get_console_panel(
                            command=groundControlSystemViewModel.command,
                            received_data=groundControlSystemViewModel.received_data,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    expand= True
                ),
            ],
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
