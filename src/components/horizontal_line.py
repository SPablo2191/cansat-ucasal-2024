from flet import (
    Container,
    colors
)

def get_horizontal_line():
    return Container(
        width = 200,
        height = 5,
        bgcolor=colors.GREY_700,
        border_radius=10,
    )