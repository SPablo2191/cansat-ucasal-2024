import flet as ft
from components.measurer_card import get_measurer_card
from components.sub_title import get_sub_title
from components.altitude_chart import get_plot_altitude_chart


def main(page: ft.Page):
    page.title = "Cookie - Ground Control system (GCS)"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    page.scroll = ft.ScrollMode.HIDDEN
    mission_time = "00:00:00"
    packet_count = 0
    team_code = 1022
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

    page.add(
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
                            margin=10,
                        ),
                        get_plot_altitude_chart(data_points_example),
                    ]
                ),
            ]
        ),
    )


if __name__ == "__main__":
    ft.app(main)
