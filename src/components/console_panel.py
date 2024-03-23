from flet import (
    Container,
    Column,
    CrossAxisAlignment,
    alignment,
    BoxShadow,
    colors,
    Offset,
    ShadowBlurStyle,
    padding,
    FilledButton,
    icons,
    ButtonStyle,
    RoundedRectangleBorder,
    Row,
)
from .text_field import get_text_field


def get_console_panel(command: str, received_data : str) -> Container:
    return Container(
        content=Row(
            controls=[
                Column(
                    controls=[
                        get_text_field(
                            value=received_data,
                            label="Received",
                            read_only=True,
                            width=600,
                        ),
                        get_text_field(
                            value=command,
                            label="Command",
                            placeholder = "Enter a command...",
                            width=600,
                        ),
                    ]
                ),
                FilledButton(
                    text="Send",
                    icon=icons.SEND,
                    width=190,
                    height=50,
                    style=ButtonStyle(shape=RoundedRectangleBorder(radius=10)),
                ),
            ]
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
    )
