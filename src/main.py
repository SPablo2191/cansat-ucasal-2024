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
    # Components (Events)

    groundControlSystemViewModel.side_panel.charts_button.on_click = groundControlSystemViewModel.body_panel.set_charts
    groundControlSystemViewModel.side_panel.map_button.on_click = groundControlSystemViewModel.body_panel.set_maps

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
