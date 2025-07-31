import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.device_info import get_screen_size, ajustar_tela_para_dispositivo

def test_get_screen_size_and_ajustar():
    tamanho_antes = get_screen_size()
    ajustar_tela_para_dispositivo()
    tamanho_depois = get_screen_size()
    assert isinstance(tamanho_antes, (list, tuple))
    assert isinstance(tamanho_depois, (list, tuple))
    assert len(tamanho_antes) == 2
    assert len(tamanho_depois) == 2
