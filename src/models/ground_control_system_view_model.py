import flet as ft
from enum import StrEnum
from random import randint, uniform
from time import sleep
from datetime import datetime
import threading

from components.body_panel import BodyPanel
from components.console_panel import ConsolePanel
from components.header_panel import HeaderPanel
from components.side_panel import SidePanel


class State(StrEnum):
    PRE_LAUNCH = "Pre Launch"
    ASCENT = "Ascent"
    DESCENT = "Descent"
    SEPARATION = "Separation"
    SIMULATION = "Simulation"
    LANDED = "Landed"


class GroundControlSystemViewModel:
    def __init__(self, page: ft.Page):
        self.system_name = "Cookie - Ground Control system (GCS)"
        self.mission_time = "00:00:00"
        self.packet_count = 0
        self.team_id = 2030
        self.state = State.PRE_LAUNCH
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
        self.altitude_data_points = [ft.LineChartDataPoint(0, 0)]
        self.voltage_data_points = [ft.LineChartDataPoint(0, 0)]
        self.temperature_data_points = [ft.LineChartDataPoint(0, 0)]
        self.air_speed_data_points = [ft.LineChartDataPoint(0, 0)]
        self.telemetry = False
        self.page = page
        # Components
        self.body_panel = BodyPanel(
            data=self.altitude_data_points,
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
        self.side_panel.sim_enable_button.on_click = self.set_simulation_mode
        self.side_panel.sim_activate_button.on_click = self.send_sim_enable_command
        self.side_panel.beacon_button.on_click = self.send_beacon_command
        self.side_panel.parachute_button.on_click = self.send_parachute_command
        self.side_panel.heat_shield_button.on_click = self.send_heatshield_command

        self.header_panel = HeaderPanel(
            state=self.state,
            packet_count=self.packet_count,
            temperature=self.temperature,
            pressure=self.pressure,
            voltage=self.voltage,
            page=self.page,
        )
        self.header_panel.telemetry_button.on_click = self.telemetry_start
        self.header_panel.connect_button.on_click = self.connect
        self.header_panel.disconnect_button.on_click = self.disconnect
        self.console_panel = ConsolePanel(
            command=self.command,
            received_data=self.received_data,
        )

    def set_telemetry(self):
        self.telemetry = not self.telemetry

    def set_simulation_mode(self, e):
        self.side_panel.set_sim_enable(e)

    def send_parachute_command(self, e):
        #
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Command '' sent succesfully")
        )
        self.page.snack_bar.open = True
        self.page.update()

    def send_heatshield_command(self, e):
        #
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Command '' sent succesfully")
        )
        self.page.snack_bar.open = True
        self.page.update()

    def send_sim_enable_command(self, e):
        #
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Command 'CMD,2030,SIM,ENABLE' sent succesfully")
        )
        self.page.snack_bar.open = True
        self.page.update()

    def send_beacon_command(self, e):
        #
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Command 'CMD,2030,BCN,ON' sent succesfully")
        )
        self.page.snack_bar.open = True
        self.page.update()

    def connect(self, e):
        option = self.find_option(self.header_panel.serials.controls[1].value)
        if option is None:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Choose a port to connect")
            )
            self.page.snack_bar.open = True
            self.page.update()
            return
        self.header_panel.disconnect_button.disabled = (
            not self.header_panel.disconnect_button.disabled
        )
        self.header_panel.telemetry_button.disabled = (
            not self.header_panel.telemetry_button.disabled
        )
        self.side_panel.sim_enable_button.disabled = (
            not self.side_panel.sim_enable_button.disabled
        )
        self.header_panel.connect_button.disabled = (
            not self.header_panel.connect_button.disabled
        )
        self.header_panel.serials.controls[1].disabled = (
            not self.header_panel.serials.controls[1].disabled
        )
        self.header_panel.serials.controls[1].update()
        self.header_panel.connect_button.update()
        self.header_panel.disconnect_button.update()
        self.header_panel.telemetry_button.update()
        self.side_panel.sim_enable_button.update()
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Port {option.text}: Connected")
        )
        self.page.snack_bar.open = True
        self.page.update()

    def disconnect(self, e):
        option = self.find_option(self.header_panel.serials.controls[1].value)
        if option is None:
            return
        self.header_panel.disconnect_button.disabled = (
            not self.header_panel.disconnect_button.disabled
        )
        self.header_panel.telemetry_button.disabled = (
            not self.header_panel.telemetry_button.disabled
        )
        self.header_panel.connect_button.disabled = (
            not self.header_panel.connect_button.disabled
        )
        self.side_panel.sim_enable_button.disabled = (
            not self.side_panel.sim_enable_button.disabled
        )
        # enable dropdown
        self.header_panel.serials.controls[1].disabled = (
            not self.header_panel.serials.controls[1].disabled
        )
        self.header_panel.serials.controls[1].update()

        self.header_panel.connect_button.update()
        self.header_panel.disconnect_button.update()
        self.header_panel.telemetry_button.update()
        self.side_panel.sim_enable_button.update()
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Port {option.text}: Disconnected")
        )
        self.page.snack_bar.open = True
        self.page.update()

    def find_option(self, option_name):
        for option in self.header_panel.serials.controls[1].options:
            if option_name == option.key:
                return option
        return None

    def telemetry_start(self, e):
        if not self.telemetry:
            self.set_telemetry()
            self.side_panel.set_telemetry_switch(e)
            self.side_panel.set_mission_progress()
            # enable command buttons
            self.side_panel.set_beacon(e)
            self.side_panel.set_heat_shield(e)
            self.side_panel.set_parachute(e)

            self.header_panel.change_telemetry_button(e)
            counter_thread = threading.Thread(target=self.side_panel.stop_watch)
            serial_thread = threading.Thread(target=self.serial)
            counter_thread.setDaemon(True)
            serial_thread.setDaemon(True)
            counter_thread.start()
            serial_thread.start()
        else:
            self.set_telemetry()
            self.side_panel.set_mission_progress()
            self.header_panel.change_telemetry_button(e)
            self.side_panel.set_telemetry_switch(e)
            # enable command buttons
            self.side_panel.set_beacon(e)
            self.side_panel.set_heat_shield(e)
            self.side_panel.set_parachute(e)


    def serial(self):
        packet = 0
        altitude = 1.0
        time = 1
        while self.telemetry:
            print("escuchando...")
            # llega la trama
            # new_plot = [
            #     "2030",  # team_Id 0
            #     str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")),  # mission time 1
            #     str(packet),  # packet 2
            #     str(True),  # MODE 3
            #     State.SIMULATION.value,  # State 4
            #     str(altitude),  # altitude 5
            #     str(uniform(1.0, 200.0)),  # air speed 6
            #     str(randint(0, 1)),  # heat shield 7
            #     str(randint(0, 1)),  # parachute 8
            #     str(uniform(1.0, 100.0)),  # temperature 9
            #     str(uniform(1, 5)),  # voltage 10
            #     str(uniform(1.0, 100.0)),  # pressure 11
            #     str(datetime.now().strftime("%H:%M:%S")),  # gps time 12
            #     str(uniform(1.0, 200.0)),  # gps altitude 13
            #     str(uniform(1.0, 200.0)),  # latitude 14
            #     str(uniform(1.0, 200.0)),  # longitude 15
            #     str(uniform(1.0, 200.0)),  # sats 16
            #     str(uniform(1.0, 200.0)),  # tilt X 17
            #     str(uniform(1.0, 200.0)),  # tilt y 18
            #     str(uniform(1.0, 200.0)),  # rot z 19
            #     "comando",  # cmd echo 20
            # ]
            # print(new_plot)

            # # header
            # self.header_panel.set_state(new_plot[4])
            # self.header_panel.set_packet(int(new_plot[2]))
            # self.header_panel.set_temperature(float(new_plot[9]))
            # self.header_panel.set_voltage(float(new_plot[10]))
            # self.header_panel.set_pressure(float(new_plot[11]))
            # # console
            # self.console_panel.set_received(" ; ".join(new_plot))
            # # body
            # # Charts
            # self.altitude_data_points.append(ft.LineChartDataPoint(time, new_plot[5]))
            # self.body_panel.update_altitude_chart(self.altitude_data_points)

            # self.temperature_data_points.append(
            #     ft.LineChartDataPoint(time, new_plot[9])
            # )
            # self.body_panel.update_temperature_chart(self.temperature_data_points)

            # self.voltage_data_points.append(ft.LineChartDataPoint(time, new_plot[10]))
            # self.body_panel.update_voltage_chart(self.voltage_data_points)

            # self.air_speed_data_points.append(ft.LineChartDataPoint(time, new_plot[11]))
            # self.body_panel.update_air_speed_chart(self.air_speed_data_points)

            # # maps
            # self.body_panel.altitude.value = f"{round(float(new_plot[13]),2)}"
            # self.body_panel.latitude.value = f"{round(float(new_plot[14]),7)}"
            # self.body_panel.longitude.value = f"{round(float(new_plot[15]),7)}"
            # self.body_panel.gps_sat.value = f"{round(float(new_plot[16]),2)}"
            # self.body_panel.tilt_x_tilt_y.value = (
            #     f"{round(float(new_plot[17]),2)},{round(float(new_plot[18]),2)}"
            # )
            # self.body_panel.rot_z.value = f"{new_plot[19]:02}"

            # self.body_panel.altitude.update()
            # self.body_panel.latitude.update()
            # self.body_panel.longitude.update()
            # self.body_panel.gps_sat.update()
            # self.body_panel.tilt_x_tilt_y.update()
            # self.body_panel.rot_z.update()

            # # self.body_panel.map.latitude = float(new_plot[14])
            # # self.body_panel.map.longitude =float(new_plot[14])
            # # self.body_panel.map.zoom = float(new_plot[15])
            # # self.body_panel.map.update()

            # packet += 1
            # altitude += 0.5
            # time += 1
            sleep(1)
