from flet import (
    Container,
    Row,
    padding,
    alignment,
    BoxShadow,
    colors,
    Offset,
    ShadowBlurStyle,
    Column,
    Text,
    CrossAxisAlignment,
    FontWeight,
    Dropdown,
    dropdown,
    ElevatedButton,
    icons,
    ButtonStyle,
    IconButton,
    MainAxisAlignment,
    Page,
    SnackBar,
)
from time import sleep


class HeaderPanel:
    def __init__(
        self,
        state: str,
        packet_count: int,
        temperature: float,
        pressure: float,
        voltage: float,
        page: Page,
    ) -> None:
        button_width = 180
        background_color = "#6B9CC9"
        self.page = page
        self.state = self.get_data(label="State", value=state)
        self.packet_count = self.get_data(label="Packet Count", value=str(packet_count))
        self.temperature = self.get_data(label="Temperature", value=f"{temperature} °C")
        self.pressure = self.get_data(label="Pressure", value=f"{pressure} kPa")
        self.voltage = self.get_data(label="Voltage", value=f"{voltage}V")
        self.serials = self.get_serial_port_options()
        self.telemetry_button = IconButton(
            icon=icons.PLAY_CIRCLE_FILLED_ROUNDED,
            icon_color=colors.GREEN,
            icon_size=80,
            tooltip="Start Mission",
            disabled=True
        )
        self.disconnect_button = ElevatedButton(
            "DISCONNECT",
            disabled=True,
            icon=icons.LOGOUT_ROUNDED,
            style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
            width=button_width
        )
        self.connect_button = ElevatedButton(
            "CONNECT",
            disabled=False,
            icon=icons.LOGIN_ROUNDED,
            style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
            width=button_width
        )
        self.button_wrapper = Column(
            controls=[
                self.connect_button,
                self.disconnect_button,
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )
        self.telemetry_wrapper = Column(
            controls=[
                # Text("Telemetry", weight=FontWeight.BOLD),
                self.telemetry_button,
                # Text("OFF", weight=FontWeight.BOLD),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )
        self.content = Container(
            content=Row(
                controls=[
                    self.state,
                    self.packet_count,
                    self.temperature,
                    self.pressure,
                    self.voltage,
                    self.serials,
                    self.button_wrapper,
                    self.telemetry_wrapper,
                ],
                spacing=20,
                alignment=MainAxisAlignment.CENTER,
            ),
            padding=padding.symmetric(10, 30),
            alignment=alignment.center,
            border_radius=10,
            shadow=BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color=colors.BLUE_GREY_300,
                offset=Offset(0, 0),
                blur_style=ShadowBlurStyle.OUTER,
            ),
        )

    # telemetry
    def change_telemetry_button(self, e):
        if self.telemetry_button.icon_color == colors.GREEN:
            self.telemetry_button.icon_color = colors.RED
            self.telemetry_button.icon = icons.PAUSE_CIRCLE_FILLED_ROUNDED
            self.telemetry_button.tooltip = 'Finish Mission'
        else:
            self.telemetry_button.icon_color = colors.GREEN
            self.telemetry_button.icon = icons.PLAY_CIRCLE_FILLED_ROUNDED
            self.telemetry_button.tooltip = 'Start Mission'
        self.telemetry_button.update()

    # state
    def set_state(self, value: str):
        self.state.controls[1].value = value
        self.state.controls[1].update()

    # packet
    def set_packet(self, value: int):
        self.packet_count.controls[1].value = value
        self.packet_count.controls[1].update()

    # temperature
    def set_temperature(self, value: float):
        self.temperature.controls[1].value = f"{round(value,2)} °C"
        self.temperature.controls[1].update()

    # pressure
    def set_pressure(self, value: float):
        self.pressure.controls[1].value = f"{round(value,2)} kPa"
        self.pressure.controls[1].update()

    # temperature
    def set_voltage(self, value: float):
        self.voltage.controls[1].value = f"{round(value, 2)}V"
        self.voltage.controls[1].update()

    def get_data(self, label: str, value: str):
        return Column(
            controls=[
                Text(label, weight=FontWeight.BOLD),
                Text(value, weight=FontWeight.BOLD, size=20),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )

    def get_serial_port_options(self):
        return Column(
            controls=[
                Text("Serial Port", weight=FontWeight.BOLD),
                Dropdown(
                    hint_text="Choose a port...",
                    width=200,
                    options=[
                        dropdown.Option(
                            key = "COM1: Communications Port (COM1) [ACPI\PNP0501\1]",
                            text = "COM1"
                        ),
                        dropdown.Option(
                            key = "COM7: MediaTek USB Port (COM7) [USB VID:PID=0E8D:0003 SER=6 LOCATION=1-2.1]",
                            text = "COM7"
                        ),
                    ],
                ),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )
