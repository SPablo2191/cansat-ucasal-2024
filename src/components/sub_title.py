from flet import Text, FontWeight


def get_sub_title(value: str):
    return Text(
        value=value,
        size=15,
        weight=FontWeight.BOLD,
    )
