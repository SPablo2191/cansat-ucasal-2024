import flet as ft
from enum import StrEnum


class State(StrEnum):
    ASCENT = "Ascent"
    SIMULATION = "Simulation"


class GroundControlSystemViewModel:
    def __init__(self):
        self.system_name = "Cookie - Ground Control system (GCS)"
        self.mission_time = "00:00:00"
        self.packet_count = 0
        self.team_id = 2030
        self.state = State.ASCENT
        self.altitude = 0
        self.air_speed = 0
        self.hs_deployed = False  # heatshield state
        self.pc_deployed = False  # parachute state
        self.temperature = 23.0
        self.voltage = 5.0
        self.pressure = 20.0
        self.gps_time = "00:00:00"
        self.gps_altitude = 14.0
        self.gps_latitude = 28.3882648
        self.gps_longitude = -80.6273621
        self.gps_sats = 0
        self.tilt_x = 0.00
        self.tilt_y = 45.00
        self.rot_z = 23.1
        self.cmd_echo = ""
        self.received_data = ""
        self.command = ""
        self.data_points_example = [
            ft.LineChartDataPoint(1, 1),
            ft.LineChartDataPoint(3, 3),
            ft.LineChartDataPoint(5, 4),
            ft.LineChartDataPoint(7, 4),
            ft.LineChartDataPoint(10, 2),
            ft.LineChartDataPoint(12, 2),
            ft.LineChartDataPoint(13, 8),
        ]
        self.telemetry = False
