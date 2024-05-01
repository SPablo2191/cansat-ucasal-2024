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
from time import sleep
from .horizontal_line import get_horizontal_line
from .change_theme_button import get_change_theme_button

class SidePanel:
    def __init__(
        self,
        team_id: int,
        mission_time: str,
        telemetry: bool,
        heat_shield: bool,
        simulation_mode: bool,
        page: Page,
    ) -> None:
        button_width = 180
        background_color = "#6B9CC9"
        self.main_title = self.get_main_title(team_id)
        self.mission_time = self.get_mission_time(mission_time)

        self.charts_button = ElevatedButton(
            "Charts",
            icon=icons.AUTO_GRAPH_ROUNDED,
            style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
            width=button_width,
        )

        self.map_button = ElevatedButton(
            "Map",
            icon=icons.MAP_ROUNDED,
            style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
            width=button_width,
        )

        self.telemety_switch = Switch(value=telemetry, label="Telemetry")

        self.heat_shield_switch = Switch(value=heat_shield, label="Heat Shield")

        self.simulation_mode_switch = Switch(
            value=simulation_mode, label="Simulation Mode"
        )

        self.sim_enable_button = ElevatedButton(
            "Sim. Enable",
            icon=icons.BROADCAST_ON_PERSONAL_SHARP,
            style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
            width=button_width,
        )

        self.sim_activate_button = ElevatedButton(
            "Sim. Activate",
            icon=icons.BROADCAST_ON_HOME_OUTLINED,
            style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
            width=button_width,
        )

        self.parachute_button = ElevatedButton(
            "Parachute",
            icon=icons.PARAGLIDING,
            style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
            width=button_width,
        )

        self.export_button = ElevatedButton(
            "Export",
            icon=icons.IMPORT_EXPORT_ROUNDED,
            style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
            width=button_width,
        )

        self.content = Container(
            content=Column(
                controls=[
                    self.main_title,
                    self.mission_time,
                    get_horizontal_line(),
                    self.charts_button,
                    self.map_button,
                    get_horizontal_line(),
                    Column(
                        controls=[
                            self.telemety_switch,
                            self.heat_shield_switch,
                            self.simulation_mode_switch,
                        ],
                        horizontal_alignment=CrossAxisAlignment.START,
                    ),
                    get_horizontal_line(),
                    self.sim_enable_button,
                    self.sim_activate_button,
                    self.parachute_button,
                    self.export_button,
                    Row(
                        controls=[
                            self.get_repo_button(page=page, bgcolor=background_color),
                            get_change_theme_button(
                                page=page, bgcolor=background_color
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
                alignment=MainAxisAlignment.START,
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
            height=1150,
        )

    def get_main_title(self, team_id: int):
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

    def get_mission_time(self, mission_time: str):
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

    def get_repo_button(self,page: Page, bgcolor: str):
        def open_repo(e):
            page.launch_url("https://github.com/SPablo2191/cansat-ucasal-2024")
        return IconButton(
            icon=icons.LOGO_DEV,
            icon_color=bgcolor,
            on_click=open_repo,
            icon_size=30,
            tooltip="Github Repository",
        )
    def stop_watch(self):
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
            self.mission_time.controls[0].value = (
                f"{hours:02}:{minutes:02}:{seconds:02}"
            )
            sleep(1)
            self.mission_time.controls[0].update()
    


