from flet import Page, IconButton, ButtonStyle, colors
import time


def get_change_theme_button(page: Page, bgcolor : str) -> IconButton:
    def changetheme(e):
        page.splash.visible = True
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()
        time.sleep(0.5)
        toggledarklight.selected = not toggledarklight.selected
        page.splash.visible = False
        page.update()

    toggledarklight = IconButton(
        on_click=changetheme,
        icon="dark_mode",
        selected_icon="light_mode",
        bgcolor= bgcolor,
        style=ButtonStyle(color=colors.WHITE),
    )
    return toggledarklight
