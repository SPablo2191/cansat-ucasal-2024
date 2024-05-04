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
    Page,
    LineChartDataPoint,
    LineChartData
)
from .chart import get_plot_chart
from .map import FletMap


class BodyPanel:
    def __init__(self, data, gps_altitude, gps_latitude, gps_longitude, page : Page) -> None:
        self.page = page
        self.altitude_chart = get_plot_chart(data, "Altitude (m)", "Time (s)")
        self.voltage_chart = get_plot_chart(data, "Voltage (V)", "Time (s)")
        self.temperature_chart = get_plot_chart(data, "Temperature (C°)", "Time (s)")
        self.air_speed_chart = get_plot_chart(data, "Air Speed (kPa)", "Time (s)")
        self.chart_container = self.get_charts()
        self.animated_switcher = AnimatedSwitcher(
            self.chart_container,
            transition=AnimatedSwitcherTransition.SCALE,
            duration=500,
            reverse_duration=100,
            switch_in_curve=AnimationCurve.BOUNCE_OUT,
            switch_out_curve=AnimationCurve.BOUNCE_IN,
        )
        self.map = FletMap(
            expand=True,
            latitude=gps_latitude,
            longtitude=gps_longitude,
            zoom=int(gps_altitude),
            screenView=[3, 2],
        )
        self.longitude = Text(
            f"{gps_longitude}",
            weight=FontWeight.BOLD,
            size=25,
        )
        self.latitude = Text(
            f"{gps_latitude}",
            weight=FontWeight.BOLD,
            size=25,
        )
        self.altitude = Text(
            f"{gps_altitude} m",
            weight=FontWeight.BOLD,
            size=25,
        )
        self.tilt_x_tilt_y = Text(
            f"{0.00},{45.00}",
            weight=FontWeight.BOLD,
            size=25,
        )
        self.rot_z = Text(
            f"{23.1} dgs",
            weight=FontWeight.BOLD,
            size=25,
        )
        self.gps_sat = Text(
            f"{6}",
            weight=FontWeight.BOLD,
            size=25,
        )
        self.map_container = self.get_map()
        self.content = Container(
            content=self.animated_switcher,
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
    def set_charts(self):
        self.animated_switcher.content = self.chart_container
        self.page.update()
    def set_maps(self):
        self.animated_switcher.content = self.map_container
        self.page.update()
    
    def get_charts(self):
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
                        self.altitude_chart,
                        self.voltage_chart,
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    controls=[
                        self.temperature_chart,
                        self.air_speed_chart,
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
            ],
        )
    def update_chart(self,data: list[LineChartDataPoint]):
        chart_data = [
        LineChartData(
            data_points=data,
            color= colors.CYAN,
            stroke_width=5,
            curved=True,
            stroke_cap_round=True,
        )
    ]
        self.altitude_chart.data_series = chart_data
        self.altitude_chart.max_y = max(point.y for point in data)
        self.altitude_chart.max_x = max(point.x for point in data)
        self.altitude_chart.update()
        self.page.update()

    def get_map(self):
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
                                        self.longitude,
                                    ]
                                ),
                                Row(
                                    controls=[
                                        Text(
                                            "Latitude",
                                            weight=FontWeight.BOLD,
                                            size=20,
                                        ),
                                        self.latitude,
                                    ]
                                ),
                                Row(
                                    controls=[
                                        Text(
                                            "Altitude",
                                            weight=FontWeight.BOLD,
                                            size=20,
                                        ),
                                        self.altitude,
                                    ]
                                ),
                                Row(
                                    controls=[
                                        Text(
                                            "Tilt X, Tilt Y",
                                            weight=FontWeight.BOLD,
                                            size=20,
                                        ),
                                        self.tilt_x_tilt_y,
                                    ]
                                ),
                                Row(
                                    controls=[
                                        Text(
                                            "Rot Z",
                                            weight=FontWeight.BOLD,
                                            size=20,
                                        ),
                                        self.rot_z,
                                    ]
                                ),
                                Row(
                                    controls=[
                                        Text(
                                            "GPS Sats",
                                            weight=FontWeight.BOLD,
                                            size=20,
                                        ),
                                        self.gps_sat,
                                    ]
                                ),
                            ]
                        ),
                        self.map,
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=60,
                ),
            ],
            alignment=MainAxisAlignment.START,
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )
