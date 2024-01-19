import flet as ft
from components.measurer_card import get_measurer_card
from components.sub_title import get_sub_title
from components.altitude_chart import get_plot_altitude_chart
from components.map import FletMap
from components.element_status import get_element_status
from components.text_field import get_text_field


def main(page: ft.Page):
    page.title = "Cookie - Ground Control system (GCS)"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    page.scroll = ft.ScrollMode.HIDDEN
    mission_time = "00:00:00"
    packet_count = 0
    team_code = 2030
    stage_status = "Ascent"
    temperature = 23
    pressure = 20
    voltage = 5
    data_points_example = [
        ft.LineChartDataPoint(1, 1),
        ft.LineChartDataPoint(3, 3),
        ft.LineChartDataPoint(5, 4),
        ft.LineChartDataPoint(7, 4),
        ft.LineChartDataPoint(10, 2),
        ft.LineChartDataPoint(12, 2),
        ft.LineChartDataPoint(13, 8),
    ]
    latitude = -24.78913
    longitude = -65.41037
    parachute_status = True
    heat_shield_status = False
    switch_value1 = False
    switch_value2 = False
    switch_value3 = False
    switch_value4 = False
    received_data = ""
    command = ""

    page.add(
        # Header
        ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.ACCESS_TIME),
                                ft.Text(value=f"Mission Time: {mission_time}"),
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.MOVE_TO_INBOX_ROUNDED),
                                ft.Text(value=f"Packet count: {packet_count}"),
                            ]
                        ),
                    ],
                ),
                ft.Text(f"TEAM {team_code}", size=30, weight=ft.FontWeight.BOLD),
                ft.Text(f"Stage: {stage_status}"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=100,
        ),


        # Body
        ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=get_sub_title(
                                value="Payload Temperature, Pressure and Voltage"
                            ),
                            alignment=ft.alignment.center,
                            width=450,
                            margin=30,
                        ),
                        ft.Row(
                            controls=[
                                get_measurer_card(
                                    value=f"{temperature}°C", title="Temperature"
                                ),
                                get_measurer_card(
                                    value=f"{pressure} kPa", title="Pressure"
                                ),
                                get_measurer_card(
                                    value=f"{voltage} V", title="Voltage"
                                ),
                            ]
                        ),
                        ft.Container(
                            content=get_sub_title(value="Payload Altitude"),
                            alignment=ft.alignment.center,
                            width=550,

                        ),
                        get_plot_altitude_chart(data_points_example),
                    ]
                ),
                ft.Column(
                    controls=[
                        ft.Container(
                            content=get_sub_title(value="GPS Latitude and Longitude"),
                            alignment=ft.alignment.center,
                            width=450,
                            margin=20,
                        ),
                        ft.Container(
                            
                            content=FletMap(
                                zoom=19,
                                latitude=latitude,
                                longtitude=longitude,
                                screenView=(2, 2),
                            ),
                            alignment=ft.alignment.center,
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=10,
                                color=ft.colors.BLUE_GREY_300,
                                offset=ft.Offset(0, 0),
                                blur_style=ft.ShadowBlurStyle.OUTER,
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Column(
                    controls=[
                        get_element_status(
                            value="Parachute",
                            icon=ft.icons.PARAGLIDING,
                            status=parachute_status,
                        ),
                        get_element_status(
                            value="Heat Shield",
                            icon=ft.icons.SHIELD,
                            status=heat_shield_status,
                        ),
                        ft.Switch(value=switch_value1, label="Btn 1"),
                        ft.Switch(value=switch_value2, label="Btn 2"),
                        ft.Switch(value=switch_value3, label="Btn 3"),
                        ft.Switch(value=switch_value4, label="Btn 4"),
                    ]
                ),
            ]
        ),
        ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        get_sub_title(value="Telemetry"),
                        get_text_field(value=received_data, placeholder="Received", width= 1000),
                        ft.Row(controls=[
                            get_text_field(value=command , placeholder="Command", width= 800),
                            ft.FilledButton(
                                text="Send",
                                icon=ft.icons.SEND,
                                width=180,
                                height= 50,
                                style= ft.ButtonStyle(
                                    shape= ft.RoundedRectangleBorder(radius=10)
                                )
                            ),
                        ])
                    ]
                ),
            ]
        ),
    )


if __name__ == "__main__":
    ft.app(main)
