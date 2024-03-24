from flet import (
    Container,
    Column,
    CrossAxisAlignment,
    alignment,
    BoxShadow,
    colors,
    Offset,
    ShadowBlurStyle,
    Text,
    Row,
    Image,
    ImageFit,
    FontWeight,
    MainAxisAlignment,
    TextAlign,
    padding,
    ElevatedButton,
    icons,
    ButtonStyle,
    Switch,
    IconButton,
    Page,
)
from .horizontal_line import get_horizontal_line
from .change_theme_button import get_change_theme_button


def get_side_panel(
    team_id: int,
    mission_time: str,
    telemetry: bool,
    heat_shield: bool,
    simulation_mode: bool,
    page: Page,
) -> Container:
    button_width = 180
    background_color = "#6B9CC9"

    def open_repo(e):
        page.launch_url("https://github.com/SPablo2191/cansat-ucasal-2024")

    return Container(
        content=Column(
            controls=[
                get_main_title(team_id=team_id),
                get_mission_time(mission_time=mission_time),
                get_horizontal_line(),
                ElevatedButton(
                    "Graph",
                    icon=icons.AUTO_GRAPH_ROUNDED,
                    style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
                    width=button_width,
                ),
                ElevatedButton(
                    "Map",
                    icon=icons.MAP_ROUNDED,
                    style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
                    width=button_width,
                ),
                get_horizontal_line(),
                Column(
                    controls=[
                        Switch(value=telemetry, label="Telemetry"),
                        Switch(value=heat_shield, label="Heat Shield"),
                        Switch(value=simulation_mode, label="Simulation Mode"),
                    ],
                    horizontal_alignment=CrossAxisAlignment.START,
                ),
                get_horizontal_line(),
                ElevatedButton(
                    "Sim. Enable",
                    icon=icons.BROADCAST_ON_PERSONAL_SHARP,
                    style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
                    width=button_width,
                ),
                ElevatedButton(
                    "Sim. Activate",
                    icon=icons.BROADCAST_ON_HOME_OUTLINED,
                    style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
                    width=button_width,
                ),
                ElevatedButton(
                    "Parachute",
                    icon=icons.PARAGLIDING,
                    style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
                    width=button_width,
                ),
                ElevatedButton(
                    "Export",
                    icon=icons.IMPORT_EXPORT_ROUNDED,
                    style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
                    width=button_width,
                ),
                Row(
                    controls=[
                        IconButton(
                            icon=icons.LOGO_DEV,
                            icon_color=background_color,
                            icon_size=30,
                            tooltip="Github Repository",
                            on_click=open_repo,
                        ),
                        get_change_theme_button(page=page, bgcolor=background_color),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.START
        ),
        padding=padding.symmetric(10, 30),
        alignment=alignment.center,
        border_radius=10,
        shadow=BoxShadow(
            spread_radius=1,
            blur_radius=5,
            color=colors.BLUE_GREY_300,
            offset=Offset(0, 0),
            blur_style=ShadowBlurStyle.OUTER,
        ),
        height=1150
    )


def get_main_title(team_id: int):
    text_size = 20
    return Row(
        controls=[
            Text(value="TEAM", weight=FontWeight.BOLD, size=text_size),
            Text(
                value=f"#{team_id}",
                size=text_size,
                weight=FontWeight.BOLD,
                color="#6B9CC9",
            ),
            Image(
                "images/argentina_flag.png",
                fit=ImageFit.CONTAIN,
                width=21,
                height=14,
            ),
        ],
        alignment=MainAxisAlignment.CENTER,
    )


def get_mission_time(mission_time: str):
    return Column(
        controls=[
            Text(value=mission_time, weight=FontWeight.BOLD, size=30),
            Text(
                "Mission Time",
                weight=FontWeight.BOLD,
                text_align=TextAlign.CENTER,
                size=12,
            ),
        ],
        spacing=3,
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )
