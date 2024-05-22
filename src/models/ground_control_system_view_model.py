import flet as ft
from random import randint, uniform
from time import sleep
from datetime import datetime
import threading

from components.body_panel import BodyPanel
from components.console_panel import ConsolePanel
from components.header_panel import HeaderPanel
from components.side_panel import SidePanel
from models.state import State

from utils.communication_helper import CommunicationHelper
from utils.csv_helper import write_in_csv


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
        self.communication_helper = CommunicationHelper()
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
            simulation_mode=self.state == False,
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
        command = 'CMD,2030,SIM,ENABLE'
        try:
            self.communication_helper.send(command)
        except Exception as e:
            print(e)
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Command '{command}' sent succesfully")
        )
        self.page.snack_bar.open = True
        self.page.update()

    def send_beacon_command(self, e):
        command = 'CMD,2030,BCN,ON'
        try:
            self.communication_helper.send(command)
        except Exception as e:
            print(e)
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Command '{command}' sent succesfully")
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

        # enable buttons
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

        # Connect with the xbee
        self.communication_helper.set_listener(option.text)
        self.communication_helper.set_sender(option.text)
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

    def parachute_deployed(self, value: str):
        return value.upper() == "C"

    def heat_shield_deployed(self, value: str):
        return value.upper() == "P"

    def telemetry_start(self, e):
        if not self.telemetry:
            self.set_telemetry()
            self.side_panel.set_telemetry_switch()
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
            self.side_panel.set_telemetry_switch()
            # enable command buttons
            self.side_panel.set_beacon(e)
            self.side_panel.set_heat_shield(e)
            self.side_panel.set_parachute(e)

    def serial(self):
        time = 0
        while self.telemetry:
            # llega la trama
            telemetry_data = self.communication_helper.listen()
            if len(telemetry_data) == 0:
                continue
            # csv
            write_in_csv(telemetry_data)
            # header
            self.header_panel.set_state(telemetry_data[4])
            self.header_panel.set_packet(int(telemetry_data[2]))
            self.header_panel.set_temperature(float(telemetry_data[9]))
            self.header_panel.set_voltage(float(telemetry_data[10]))
            self.header_panel.set_pressure(float(telemetry_data[11]))

            # side panel
            if self.heat_shield_deployed(telemetry_data[7]):
                self.side_panel.set_heat_shield_switch()
            if self.parachute_deployed(telemetry_data[8]):
                self.side_panel.set_parachute_switch()
            # console
            self.console_panel.set_received(" ; ".join(telemetry_data))

            # body
            # Charts
            self.altitude_data_points.append(
                ft.LineChartDataPoint(time, telemetry_data[5])
            )
            self.body_panel.update_altitude_chart(self.altitude_data_points)

            self.temperature_data_points.append(
                ft.LineChartDataPoint(time, telemetry_data[9])
            )
            self.body_panel.update_temperature_chart(self.temperature_data_points)

            self.voltage_data_points.append(
                ft.LineChartDataPoint(time, telemetry_data[10])
            )
            self.body_panel.update_voltage_chart(self.voltage_data_points)

            self.air_speed_data_points.append(
                ft.LineChartDataPoint(time, telemetry_data[11])
            )
            self.body_panel.update_air_speed_chart(self.air_speed_data_points)

            # maps
            self.body_panel.altitude.value = f"{round(float(telemetry_data[13]),2)}"
            self.body_panel.latitude.value = f"{round(float(telemetry_data[14]),7)}"
            self.body_panel.longitude.value = f"{round(float(telemetry_data[15]),7)}"
            self.body_panel.gps_sat.value = f"{round(float(telemetry_data[16]),2)}"
            self.body_panel.tilt_x_tilt_y.value = f"{round(float(telemetry_data[17]),2)},{round(float(telemetry_data[18]),2)}"
            self.body_panel.rot_z.value = f"{telemetry_data[19]:02}"

            self.body_panel.altitude.update()
            self.body_panel.latitude.update()
            self.body_panel.longitude.update()
            self.body_panel.gps_sat.update()
            self.body_panel.tilt_x_tilt_y.update()
            self.body_panel.rot_z.update()

            # map 
            try:
                self.body_panel.map.latitude = float(telemetry_data[14])
                self.body_panel.map.longitude =float(telemetry_data[14])
                self.body_panel.map.zoom = float(telemetry_data[15])
                self.body_panel.map.update()
            except Exception as e:
                print(e)
