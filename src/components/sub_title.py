from flet import Text, FontWeight


def get_sub_title(value: str):
    return Text(
        value=f"Payload Temperature, Pressure and Voltage",
        size=15,
        weight=FontWeight.BOLD,
    )
