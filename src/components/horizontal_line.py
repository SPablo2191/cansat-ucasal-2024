from flet import (
    Container,
    colors
)

def get_horizontal_line():
    return Container(
        width = 150,
        height = 5,
        bgcolor=colors.GREY_800,
        border_radius=10,
    )