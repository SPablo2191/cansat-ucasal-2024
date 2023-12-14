import flet as ft
from components.text_field import get_text_field
from utils.operations import increase_value,decrease_value

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = get_text_field(value="0")

    def minus_click(e):
        txt_number.value = decrease_value(value=int(txt_number.value))
        page.update()

    def plus_click(e):
        txt_number.value = increase_value(value=int(txt_number.value))
        page.update()

    page.add(
        ft.Text("Cansat"),
        ft.Row(
            [  
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

if __name__ == "__main__":
    ft.app(main)