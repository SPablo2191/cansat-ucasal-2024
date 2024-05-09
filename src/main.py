import flet as ft
import threading
from models.ground_control_system_view_model import GroundControlSystemViewModel


def main(page: ft.Page):
    # configuration
    groundControlSystemViewModel = GroundControlSystemViewModel(page=page)
    page.title = groundControlSystemViewModel.system_name
    page.fonts = {"inria sans": "fonts/inria-sans.ttf"}
    page.theme = ft.Theme(font_family="inria sans")
    page.theme_mode = "light"
    page.padding = 20
    page.scroll = ft.ScrollMode.HIDDEN
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.splash = ft.ProgressBar(visible=False)

    # Functions (Events)
    def connect(e):
        if not groundControlSystemViewModel.telemetry:
            groundControlSystemViewModel.telemetry = True
            groundControlSystemViewModel.side_panel.set_telemetry_switch(e)
            groundControlSystemViewModel.side_panel.set_simulation_switch(e)
            groundControlSystemViewModel.side_panel.mission_in_progress = True
            groundControlSystemViewModel.header_panel.change_telemetry_button(e)
            counter_thread = threading.Thread(
            target=groundControlSystemViewModel.side_panel.stop_watch
            )
            serial_thread = threading.Thread(
                target= groundControlSystemViewModel.serial
            )
            counter_thread.setDaemon(True)
            serial_thread.setDaemon(True)
            counter_thread.start()
            serial_thread.start()
        else:
            groundControlSystemViewModel.telemetry = False
            groundControlSystemViewModel.side_panel.mission_in_progress = False
            groundControlSystemViewModel.header_panel.change_telemetry_button(e)
            groundControlSystemViewModel.side_panel.set_telemetry_switch(e)
            groundControlSystemViewModel.side_panel.set_simulation_switch(e)

    # Components (Events)

    groundControlSystemViewModel.side_panel.charts_button.on_click = groundControlSystemViewModel.body_panel.set_charts
    groundControlSystemViewModel.side_panel.map_button.on_click = groundControlSystemViewModel.body_panel.set_maps
    groundControlSystemViewModel.header_panel.telemetry_button.on_click = connect

    # Page structure
    page.add(
        ft.Row(
            controls=[
                groundControlSystemViewModel.side_panel.content,
                ft.Column(
                    controls=[
                        groundControlSystemViewModel.header_panel.content,
                        groundControlSystemViewModel.body_panel.content,
                        groundControlSystemViewModel.console_panel.content,
                    ],
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
