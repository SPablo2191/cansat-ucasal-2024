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
    MainAxisAlignment
)


def get_side_panel(team_id: int) -> Container:
    return Container(
        content=Column(
            controls=[get_main_title(team_id=team_id)],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        ),
        margin=10,
        padding=10,
        alignment=alignment.center,
        width=150,
        height=125,
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
    return Row(
        controls=[
            Text(
                value="TEAM",
                weight=FontWeight.BOLD,
            ),
            Text(
                value=f"#{team_id}",
                weight=FontWeight.BOLD,
                color= "#6B9CC9"
            ),
            Image(
                "images/argentina_flag.png",
                fit=ImageFit.CONTAIN,
                width=21,
                height=14,
            ),
        ],
        alignment= MainAxisAlignment.CENTER
    )
