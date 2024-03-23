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
                Container(
                    width=60
                )
            ],
            spacing= 40
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
            Text(label),
            Text(value, weight=FontWeight.BOLD, size=20),
        ],
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )
