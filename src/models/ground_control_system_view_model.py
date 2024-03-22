import flet as ft


class GroundControlSystemViewModel:
    def __init__(self):
        self.system_name = "Cookie - Ground Control system (GCS)"
        self.mission_time = "00:00:00"
        self.packet_count = 0
        self.team_id = 2030
        self.state = "Ascent"
        self.altitude = 0
        self.air_speed = 0
        self.hs_deployed = False # heatshield state
        self.pc_deployed = False # parachute state
        self.temperature = 23
        self.voltage = 5
        self.pressure = 20
        self.gps_time = "00:00:00"
        self.gps_altitude = 14
        self.gps_latitude = 28.3882648
        self.gps_longitude = -80.6273621
        self.gps_sats = 0
        self.tilt_x = 0.00
        self.tilt_y = 45.00
        self.rot_z = 23.1
        self.cmd_echo = ""
        self.received_data = ""
        self.command = ""
        self.data_points_example = []
