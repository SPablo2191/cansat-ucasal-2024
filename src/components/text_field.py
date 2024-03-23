from flet import TextField


def get_text_field(value, placeholder=None, label=None, width=100, read_only=None):
    return TextField(
        value=value,
        label=label,
        hint_text=placeholder,
        width=width,
        read_only=read_only,
    )
