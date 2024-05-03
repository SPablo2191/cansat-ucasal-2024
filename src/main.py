import flet as ft
import threading

from components.side_panel import SidePanel
from components.header_panel import HeaderPanel
from components.console_panel import ConsolePanel
from components.body_panel import BodyPanel
from models.ground_control_system_view_model import GroundControlSystemViewModel, State


def main(page: ft.Page):
    # configuration
    groundControlSystemViewModel = GroundControlSystemViewModel()
    page.title = groundControlSystemViewModel.system_name
    page.fonts = {"inria sans": "fonts/inria-sans.ttf"}
    page.theme = ft.Theme(font_family="inria sans")
    page.theme_mode = "light"
    page.padding = 20
    page.scroll = ft.ScrollMode.HIDDEN
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.splash = ft.ProgressBar(visible=False)

    # Functions

    def go_to_chart(e):
        body_panel.set_charts()

    def go_to_map(e):
        body_panel.set_maps()

    def connect(e):
        counter_thread = threading.Thread(target=side_panel.stop_watch)
        packet_thread = threading.Thread(target=header_panel.packet_increase)
        counter_thread.setDaemon(True)
        packet_thread.setDaemon(True)
        counter_thread.start()
        packet_thread.start()

    # Components
    body_panel = BodyPanel(
        data=groundControlSystemViewModel.data_points_example,
        gps_altitude=groundControlSystemViewModel.gps_altitude,
        gps_latitude=groundControlSystemViewModel.gps_latitude,
        gps_longitude=groundControlSystemViewModel.gps_longitude,
        page=page,
    )
    side_panel = SidePanel(
        team_id=groundControlSystemViewModel.team_id,
        mission_time=groundControlSystemViewModel.mission_time,
        telemetry=groundControlSystemViewModel.telemetry,
        heat_shield=groundControlSystemViewModel.hs_deployed,
        simulation_mode=groundControlSystemViewModel.state == State.SIMULATION,
        page=page,
    )
    side_panel.charts_button.on_click = go_to_chart
    side_panel.map_button.on_click = go_to_map

    header_panel = HeaderPanel(
        state=groundControlSystemViewModel.state,
        packet_count=groundControlSystemViewModel.packet_count,
        temperature=groundControlSystemViewModel.temperature,
        pressure=groundControlSystemViewModel.pressure,
        voltage=groundControlSystemViewModel.voltage,
        page=page,
    )
    header_panel.connect_button.on_click = connect


    console_panel = ConsolePanel(
        command=groundControlSystemViewModel.command,
        received_data=groundControlSystemViewModel.received_data,
    )

    page.add(
        ft.Row(
            controls=[
                side_panel.content,
                ft.Column(
                    controls=[header_panel.content, body_panel.content, console_panel.content],
                    alignment=ft.MainAxisAlignment.START,
                    expand=True,
                    height=1150,
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
