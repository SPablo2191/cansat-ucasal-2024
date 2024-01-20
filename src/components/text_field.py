from flet import TextField


def get_text_field(value, placeholder=None, width=100):
    return TextField(value=value, hint_text=placeholder, width=width)
