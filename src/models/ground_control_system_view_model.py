import flet as ft
from enum import StrEnum
from random import randint,uniform
from time import sleep
from datetime import datetime
from components.body_panel import BodyPanel
from components.console_panel import ConsolePanel
from components.header_panel import HeaderPanel
from components.side_panel import SidePanel


class State(StrEnum):
    ASCENT = "Ascent"
    SIMULATION = "Simulation"


class GroundControlSystemViewModel:
    def __init__(self, page: ft.Page):
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
        self.page = page
        # Components
        self.body_panel = BodyPanel(
            data=self.data_points_example,
            gps_altitude=self.gps_altitude,
            gps_latitude=self.gps_latitude,
            gps_longitude=self.gps_longitude,
            page=self.page,
        )
        self.side_panel = SidePanel(
            team_id=self.team_id,
            mission_time=self.mission_time,
            telemetry=self.telemetry,
            heat_shield=self.hs_deployed,
            simulation_mode=self.state == State.SIMULATION,
            page=self.page,
        )
        self.header_panel = HeaderPanel(
            state=self.state,
            packet_count=self.packet_count,
            temperature=self.temperature,
            pressure=self.pressure,
            voltage=self.voltage,
            page=self.page,
        )
        self.console_panel = ConsolePanel(
        command=self.command,
        received_data=self.received_data,
    )

    def serial(self):
        packet = 0
        while True:
            # llega la trama
            new_plot = [
                '2030',
                str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")),
                str(packet),
                str(True),
                State.SIMULATION.value,
                str(uniform(1.0,900.0)), # altitude
                str(uniform(1.0,200.0)), # air speed
                str(randint(0,1)),
                str(randint(0,1)),
                str(uniform(1.0,100.0)), # temperature
                str(uniform(1,5)), # voltage
                str(uniform(1.0,100.0)),
                str(datetime.now().strftime("%H:%M:%S")),
                str(uniform(1.0,200.0)),
                str(uniform(1.0,200.0)),
                str(uniform(1.0,200.0)),
                str(uniform(1.0,200.0)),
                str(uniform(1.0,200.0)),
                str(uniform(1.0,200.0)),
                str(uniform(1.0,200.0)),
                'comando'
            ]
            print(new_plot)
            self.header_panel.set_packet(int(new_plot[2]))
            packet += 1
            sleep(1)
