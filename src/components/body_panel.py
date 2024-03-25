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
    MainAxisAlignment,
    AnimatedSwitcher,
    AnimatedSwitcherTransition,
    AnimationCurve,
    CrossAxisAlignment,
    Image,
)
from .chart import get_plot_chart
from .map import FletMap


def get_body_panel(data) -> Container:
    animatedSwitcher = AnimatedSwitcher(
        get_charts(data=data),
        transition=AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=AnimationCurve.BOUNCE_OUT,
        switch_out_curve=AnimationCurve.BOUNCE_IN,
    )
    return Container(
        content=animatedSwitcher,
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
                alignment=MainAxisAlignment.CENTER,
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


def get_map(gps_altitude, gps_latitude, gps_longitude):
    print(
        f"http://a.tile.openstreetmap.org/{gps_altitude}/{gps_latitude}/{gps_longitude}.png"
    )
    return Column(
        controls=[
            Row(
                controls=[
                    Text(
                        "Map",
                        size=30,
                        weight=FontWeight.BOLD,
                        text_align=TextAlign.CENTER,
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                controls=[
                    Column(
                        controls=[
                            Row(
                                controls=[
                                    Text(
                                        "Longitude",
                                        weight=FontWeight.BOLD,
                                        size=20,
                                    ),
                                    Text(
                                        "0",
                                        weight=FontWeight.BOLD,
                                        size=25,
                                    ),
                                ]
                            ),
                            Row(
                                controls=[
                                    Text(
                                        "Longitude",
                                        weight=FontWeight.BOLD,
                                        size=20,
                                    ),
                                    Text(
                                        "0",
                                        weight=FontWeight.BOLD,
                                        size=25,
                                    ),
                                ]
                            ),
                            Row(
                                controls=[
                                    Text(
                                        "Longitude",
                                        weight=FontWeight.BOLD,
                                        size=20,
                                    ),
                                    Text(
                                        "0",
                                        weight=FontWeight.BOLD,
                                        size=25,
                                    ),
                                ]
                            ),
                            Row(
                                controls=[
                                    Text(
                                        "Longitude",
                                        weight=FontWeight.BOLD,
                                        size=20,
                                    ),
                                    Text(
                                        "0",
                                        weight=FontWeight.BOLD,
                                        size=25,
                                    ),
                                ]
                            ),
                        ]
                    ),
                    Image(src="https://tile.openstreetmap.org/7/63/42.png"),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
        ],
        alignment=MainAxisAlignment.START,
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )
