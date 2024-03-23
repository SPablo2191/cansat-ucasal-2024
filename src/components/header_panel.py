from flet import (
    Container,
    Row,
    padding,
    alignment,
    BoxShadow,
    colors,
    Offset,
    ShadowBlurStyle,
    Column,
    Text,
    CrossAxisAlignment,
    FontWeight,
    Dropdown,
    dropdown,
    ElevatedButton,
    icons,
    ButtonStyle,
)


def get_header_panel(
    state: str, packet_count: int, temperature: float, pressure: float, voltage: float
) -> Container:
    return Container(
        content=Row(
            controls=[
                get_state(),
                get_data(label="Packet Count", value=str(packet_count)),
                get_data(label="Temperature", value=f"{temperature} °C"),
                get_data(label="Pressure", value=f"{pressure} kPa"),
                get_data(label="Voltage", value=f"{voltage}V"),
                get_serial_port_options(),
                get_connection_buttons()
            ],
            spacing=40,
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


def get_state():
    return Column(
        controls=[
            Text("State"),
        ],
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )


def get_data(label: str, value: str):
    return Column(
        controls=[
            Text(label, weight=FontWeight.BOLD),
            Text(value, weight=FontWeight.BOLD, size=20),
        ],
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )


def get_serial_port_options():
    return Column(
        controls=[
            Text("Serial Port", weight=FontWeight.BOLD),
            Dropdown(
                hint_text="Choose a port...",
                width=200,
                options=[
                    dropdown.Option("Red"),
                    dropdown.Option("Green"),
                    dropdown.Option("Blue"),
                ],
            ),
        ],
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )


def get_connection_buttons():
    button_width = 180
    background_color = "#6B9CC9"
    return Column(
        controls=[
            ElevatedButton(
                "DISCONNECT",
                disabled=True,
                icon=icons.LOGOUT_ROUNDED,
                style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
                width=button_width,
            ),
            ElevatedButton(
                "CONNECT",
                disabled=False,
                icon=icons.LOGIN_ROUNDED,
                style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
                width=button_width,
            ),
        ],
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )
