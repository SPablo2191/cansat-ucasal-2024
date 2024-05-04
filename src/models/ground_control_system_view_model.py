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
        self.voltage = 0
        self.pressure = 0
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
            ft.LineChartDataPoint(0,0)
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
                '2030', # team_Id 0
                str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")), # mission time 1
                str(packet), # packet 2
                str(True), # MODE 3
                State.SIMULATION.value, # State 4
                str(uniform(1.0,900.0)), # altitude 5
                str(uniform(1.0,200.0)), # air speed 6
                str(randint(0,1)),# heat shield 7
                str(randint(0,1)), # parachute 8
                str(uniform(1.0,100.0)), # temperature 9
                str(uniform(1,5)), # voltage 10 
                str(uniform(1.0,100.0)), # pressure 11
                str(datetime.now().strftime("%H:%M:%S")), # gps time 12
                str(uniform(1.0,200.0)), # gps altitude 13
                str(uniform(1.0,200.0)), # latitude 14
                str(uniform(1.0,200.0)), # longitude 15
                str(uniform(1.0,200.0)), # sats 16
                str(uniform(1.0,200.0)), # tilt X 17
                str(uniform(1.0,200.0)), # tilt y 18
                str(uniform(1.0,200.0)), # rot z 19
                'comando' # cmd echo 20
            ]
            print(new_plot)
            # header 
            self.header_panel.set_state(new_plot[4])
            self.header_panel.set_packet(int(new_plot[2])) 
            self.header_panel.set_temperature(float(new_plot[9]))
            self.header_panel.set_voltage(float(new_plot[10]))
            self.header_panel.set_pressure(float(new_plot[11]))
            # console
            self.console_panel.set_received(' ; '.join(new_plot))
            self.data_points_example.append(ft.LineChartDataPoint(randint(1,100),new_plot[5]))
            self.body_panel.update_chart(self.data_points_example)
            packet += 1
            sleep(1)
