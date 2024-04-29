import flet as ft
from components.side_panel import get_side_panel
from components.header_panel import get_header_panel
from components.console_panel import get_console_panel
from components.body_panel import get_body_panel, get_map, get_charts
from models.ground_control_system_view_model import GroundControlSystemViewModel, State


def main(page: ft.Page):
    # configuration
    groundControlSystemViewModel = GroundControlSystemViewModel()
    page.title = groundControlSystemViewModel.system_name
    page.fonts = {"inria sans": "fonts/inria-sans.ttf"}
    page.theme = ft.Theme(font_family="inria sans")
    page.padding = 20
    page.scroll = ft.ScrollMode.HIDDEN
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.splash = ft.ProgressBar(visible=False)

    # Components
    header_panel = get_header_panel(
        state=groundControlSystemViewModel.state,
        packet_count=groundControlSystemViewModel.packet_count,
        temperature=groundControlSystemViewModel.temperature,
        pressure=groundControlSystemViewModel.pressure,
        voltage=groundControlSystemViewModel.voltage,
    )
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

    def go_to_chart(e):
        body_panel.content.content = chart_panel
        page.update()

    def go_to_map(e):
        body_panel.content.content = map_panel
        page.update()

    side_panel = get_side_panel(
        team_id=groundControlSystemViewModel.team_id,
        mission_time=groundControlSystemViewModel.mission_time,
        telemetry=groundControlSystemViewModel.telemetry,
        heat_shield=groundControlSystemViewModel.hs_deployed,
        simulation_mode=groundControlSystemViewModel.state == State.SIMULATION,
        page=page,
        map_click=go_to_map,
        chart_click=go_to_chart,
    )
    page.add(
        ft.Row(
            controls=[
                side_panel,
                ft.Column(
                    controls=[header_panel, body_panel, console_panel],
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
