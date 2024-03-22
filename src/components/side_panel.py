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
    padding
)
from .horizontal_line import get_horizontal_line

def get_side_panel(team_id: int, mission_time: str) -> Container:
    return Container(
        content=Column(
            controls=[
                get_main_title(team_id=team_id),
                get_mission_time(mission_time=mission_time),
                get_horizontal_line(),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        ),
        padding=padding.symmetric(20,30),
        alignment=alignment.center,
        border_radius=10,
        shadow=BoxShadow(
            spread_radius=1,
            blur_radius=5,
            color=colors.BLUE_GREY_300,
            offset=Offset(0, 0),
            blur_style=ShadowBlurStyle.OUTER,
        ),
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
