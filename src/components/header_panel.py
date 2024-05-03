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
    MainAxisAlignment,
    Page
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
        page : Page
    ) -> None:
        button_width = 180
        background_color = "#6B9CC9"
        self.page = page
        self.state = self.get_state()
        self.packet_count = self.get_data(label="Packet Count", value=str(packet_count))
        self.temperature = self.get_data(label="Temperature", value=f"{temperature} °C")
        self.pressure = self.get_data(label="Pressure", value=f"{pressure} kPa")
        self.voltage = self.get_data(label="Voltage", value=f"{voltage}V")
        self.serials = self.get_serial_port_options()
        self.disconnect_button = ElevatedButton(
                    "DISCONNECT",
                    disabled=True,
                    icon=icons.LOGOUT_ROUNDED,
                    style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
                    width=button_width,
                )
        self.connect_button = ElevatedButton(
                    "CONNECT",
                    disabled=False,
                    icon=icons.LOGIN_ROUNDED,
                    style=ButtonStyle(color=colors.WHITE, bgcolor=background_color),
                    width=button_width,
                )
        self.button_wrapper = Column(
            controls=[
                self.connect_button,
                self.disconnect_button,
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
            ],
            spacing=40,
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
    # packet 
    def set_packet(self,value : int):
        self.packet_count.controls[1].value = value
        self.packet_count.controls[1].update()

    def get_state(self):
        return Column(
            controls=[
                Text("State"),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )

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
                        dropdown.Option("Red"),
                        dropdown.Option("Green"),
                        dropdown.Option("Blue"),
                    ],
                ),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
    )
    def packet_increase(self):
        while True:
            print("hola")
            sleep(1)

    


