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
    ElevatedButton,
    icons,
    ButtonStyle,
    RoundedRectangleBorder,
    Row,
    MainAxisAlignment
)
from .text_field import get_text_field

class ConsolePanel:
    def __init__(self, command: str, received_data: str) -> None:
        self.txt_received = get_text_field(
                            value=received_data,
                            label="Received",
                            read_only=True,
                            width=600,
                        )
        self.txt_command = get_text_field(
                            value=command,
                            label="Command",
                            placeholder="Enter a command...",
                            width=600,
                        )
        self.send_button = ElevatedButton(
                    text="Send",
                    icon=icons.SEND,
                    width=190,
                    height=50,
                    style=ButtonStyle(
                        shape=RoundedRectangleBorder(radius=10),
                        bgcolor="#6B9CC9",
                        color=colors.WHITE,
                    ),
                )
        self.content = Container(
        content=Row(
            controls=[
                Column(
                    controls=[
                        self.txt_received,
                        self.txt_command,
                    ]
                ),
               self.send_button,
            ],
        alignment=MainAxisAlignment.CENTER,
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
        

