import Limpa
import Origem_pg
import pyautogui
import Limpa
x_origem, y_origem = Origem_pg.x_y()


def cofre_entrar(x_origem, y_origem):
    cofre_fechado = True
    while cofre_fechado:
        pyautogui.doubleClick(x_origem + 214, y_origem + 25)  # clica no no icone do cofre para abrir a janela
        Limpa.limpa_pequeno(x_origem, y_origem)
        if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 170), (111, 79, 51), tolerance=10):  # testa se esta visivel o cofre
            print("Janela do cobre visivel")
            Limpa.limpa_pequeno(x_origem, y_origem)
            cofre_fechado = False
            break




cofre_entrar(x_origem, y_origem)