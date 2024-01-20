import flet as ft


class GroundSystemViewModel:
    system_name = "Cookie - Ground Control system (GCS)"
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
    gps_altitude = 19
    gps_latitude = -24.78913
    gps_longitude = -65.41037
    parachute_status = True
    heat_shield_status = False
    switch_value1 = False
    switch_value2 = False
    switch_value3 = False
    switch_value4 = False
    received_data = ""
    command = ""
