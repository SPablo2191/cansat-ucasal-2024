import flet as ft
from components.measurer_card import get_measurer_card


def main(page: ft.Page):
    page.title = "Cookie - Ground Control system (GCS)"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    mission_time = "00:00:00"
    packet_count = 0
    team_code = 1022
    stage_status = "Ascent"
    temperature = 23
    pressure = 20
    voltage = 5

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
                            content=ft.Text(
                                value=f"Payload Temperature, Pressure and Voltage",
                                size=15,
                                weight=ft.FontWeight.BOLD,
                            ),
                            alignment=ft.alignment.center,
                            width=550,
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
                    ]
                ),
            ]
        ),
    )


if __name__ == "__main__":
    ft.app(main)
