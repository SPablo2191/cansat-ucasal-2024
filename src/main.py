import flet as ft
import threading
from models.ground_control_system_view_model import GroundControlSystemViewModel, State


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

    def go_to_chart(e):
        groundControlSystemViewModel.body_panel.set_charts()

    def go_to_map(e):
        groundControlSystemViewModel.body_panel.set_maps()

    def connect(e):
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

    # Components (Events)

    groundControlSystemViewModel.side_panel.charts_button.on_click = go_to_chart
    groundControlSystemViewModel.side_panel.map_button.on_click = go_to_map
    groundControlSystemViewModel.header_panel.connect_button.on_click = connect

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
