from flet import (
    Container,
    Column,
    Text,
    CrossAxisAlignment,
    alignment,
    BoxShadow,
    colors,
    Offset,
    ShadowBlurStyle,
)


def get_measurer_card(value: str, title: str) -> Container:
    return Container(
        content=Column(
            controls=[
                Text(value, size=30),
                Text(title),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        ),
        margin=10,
        padding=10,
        alignment=alignment.center,
        width=150,
        height=150,
        border_radius=10,
        shadow=BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=colors.BLUE_GREY_300,
            offset=Offset(0, 0),
            blur_style=ShadowBlurStyle.OUTER,
        ),
    )
