from flet import (
    Container,
    Column,
    Icon,
    alignment,
    MainAxisAlignment,
    CrossAxisAlignment,
    Text,
    FontWeight,
    colors,
)


def get_element_status(icon, value, status):
    return Container(
        content=Column(
            controls=[
                Text(value=value, size=15, weight=FontWeight.BOLD),
                Icon(
                    icon, color=colors.GREEN_400 if status else colors.RED_400, size=50
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
        ),
        width=100,
        alignment= alignment.center,
        margin=20,
    )
