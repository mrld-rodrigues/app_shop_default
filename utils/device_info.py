from kivy.core.window import Window

def get_screen_size():
    """
    Retorna o tamanho atual da tela do dispositivo (largura, altura).
    """
    return Window.size

def ajustar_tela_para_dispositivo():
    """
    Ajusta o tamanho da janela do app para o tamanho da tela do dispositivo.
    """
    largura, altura = get_screen_size()
    Window.size = (largura, altura)

# Exemplo de uso:
if __name__ == "__main__":
    print(f"Tamanho da tela: {get_screen_size()}")
    ajustar_tela_para_dispositivo()
