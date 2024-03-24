from flet import (
    Container,
    Column,
    alignment,
    BoxShadow,
    colors,
    Offset,
    ShadowBlurStyle,
    padding,
    Row,
    Text,
    FontWeight,
    TextAlign,
    MainAxisAlignment
)
from .chart import get_plot_chart


def get_body_panel(data) -> Container:
    return Container(
        content=Column(controls=[get_charts(data=data)]),
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


def get_charts(data):
    return Column(
        controls=[
            Row(
                controls=[
                    Text(
                        "Charts",
                        size=30,
                        weight=FontWeight.BOLD,
                        text_align=TextAlign.CENTER,
                    ),
                ],
                alignment= MainAxisAlignment.CENTER
            ),
            Row(
                controls=[
                    get_plot_chart(data, "Altitude (m)", "Time (s)"),
                    get_plot_chart(data, "Voltage (V)", "Time (s)"),
                ]
            ),
            Row(
                controls=[
                    get_plot_chart(data, "Temperature (C°)", "Time (s)"),
                    get_plot_chart(data, "Air Speed (kPa)", "Time (s)"),
                ]
            ),
        ]
    )
