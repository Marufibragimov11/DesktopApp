import flet as ft


def main(page: ft.Page):
    page.title = "My App"
    page.theme_mode = 'dark'  # Initial theme mode
    page.window_width = 720
    page.window_height = 510
    page.window_resizable = False

    text_map = {
        'dark': "dark",
        'light': "light",
    }

    def change_theme(e):
        if page.theme_mode == 'dark':
            page.theme_mode = 'light'
            text_value = text_map['light']
        else:
            page.theme_mode = 'dark'
            text_value = text_map['dark']

        text.value = text_value
        page.update()

    def navigate(e):
        pass

    text = ft.Text(value=text_map[page.theme_mode])

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Settings"),
            ft.NavigationDestination(icon=ft.icons.CLEAR, label="ChatGPT"),
            ft.NavigationDestination(icon=ft.icons.SETTINGS, label="Settings"),
        ],
        on_change=navigate
    )

    page.add(
        ft.Row(
            [
                text,
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
            ],
            alignment=ft.MainAxisAlignment.END
        ),
    )


ft.app(target=main)
