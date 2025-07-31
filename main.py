from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import Screen 
import os
from kivy.lang import Builder
from kivy.core.window import Window
# from utils.device_info import ajustar_tela_para_dispositivo
from utils.hotreload import HotReloader


# Ajusta a tela para o dispositivo
# ajustar_tela_para_dispositivo()
Window.size = [400, 700]


# Define o gerenciador de telas do aplicativo
class UI(MDScreenManager):
    def __init__(self, **kwargs):
        """
        Inicializa o gerenciador de telas do aplicativo.
        Adicione todas as telas necessárias aqui.
        """
        super(UI, self).__init__(**kwargs)
        # As telas são definidas no arquivo KV (appshop.kv)
        # Adicione outras telas via Python apenas se necessário


# Classe principal do aplicativo
class AppShop(MDApp):
    DEBUG=True
    KV_DIRS=[
        os.path.join(os.getcwd(),"kv")
    ]

    # Inicializa a aplicação principal do AppShop.
    # Define o gerenciador de telas e outras configurações iniciais.
    def __init__(self, **kwargs):
        """
        Inicializa a aplicação principal do AppShop.
        """
        super(AppShop, self).__init__(**kwargs)
        self.manager_screens = None


    # Método build do KivyMD para construir a interface principal.
    # Retorna o gerenciador de telas.
    def build(self):
        """
        Método padrão do KivyMD para construir a interface principal.
        Retorna o gerenciador de telas.
        """
        Builder.load_file(os.path.join("kv", "appshop.kv"))
        return UI()


# Executa a aplicação principal do AppShop.
if __name__ == '__main__':
    app = AppShop()
    hot = HotReloader(app)
    hot.start()
    app.run()