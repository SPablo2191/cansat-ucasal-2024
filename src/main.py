import flet as ft

from time import sleep
import threading

from components.side_panel import SidePanel
from components.header_panel import HeaderPanel
from components.console_panel import get_console_panel
from components.body_panel import get_body_panel, get_map, get_charts
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
        body_panel.content.content = chart_panel
        page.update()

    def go_to_map(e):
        body_panel.content.content = map_panel
        page.update()

    def stop_watch(e):
        seconds = minutes = hours = 0
        while True:
            if seconds != 59:
                seconds += 1
            elif minutes != 59:
                minutes += 1
                seconds = 0
            else:
                hours += 1
                minutes = 0
            side_panel.mission_time.controls[0].value = (
                f"{hours:02}:{minutes:02}:{seconds:02}"
            )
            sleep(1)
            side_panel.mission_time.controls[0].update()

    def connect(e):
        # counter_thread = threading.Thread(target=stop_watch(e))
        packet_thread = threading.Thread(target=header_panel.packet_increase)
        # counter_thread.setDaemon(True)
        packet_thread.setDaemon(True)
        # counter_thread.start()
        packet_thread.start()
        

    # Components
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

    body_panel = get_body_panel(data=groundControlSystemViewModel.data_points_example)

    chart_panel = get_charts(data=groundControlSystemViewModel.data_points_example)

    map_panel = get_map(
        gps_altitude=groundControlSystemViewModel.gps_altitude,
        gps_latitude=groundControlSystemViewModel.gps_latitude,
        gps_longitude=groundControlSystemViewModel.gps_longitude,
    )
    console_panel = get_console_panel(
        command=groundControlSystemViewModel.command,
        received_data=groundControlSystemViewModel.received_data,
    )

    page.add(
        ft.Row(
            controls=[
                side_panel.content,
                ft.Column(
                    controls=[header_panel.content, body_panel, console_panel],
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
