from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

class AppShop(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"

        return MDScreen(
            MDLabel(
                text="Hello, World!",
                halign="center",
                theme_text_color="Custom",
                text_color=(0.4, 0.2, 0.6, 1),  # Roxo suave
                font_style="H4"
            )
        )

if __name__ == '__main__':
    AppShop().run()