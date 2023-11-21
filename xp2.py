import time

import pyautogui

import Limpa


def pega_2xp(x_origem, y_origem):
    tem_2xp = True
    while tem_2xp:
        pyautogui.doubleClick(x_origem + 260, y_origem + 25)  # clica no no icone dos meus objetos
        Limpa.limpa_pequeno(x_origem, y_origem)
        if pyautogui.pixelMatchesColor((x_origem + 241), (y_origem + 146), (250, 112, 1), tolerance=10):
            # testa se esta meus objetos
            print("Janela dos meus objetos visivel")
            time.sleep(1)
            pyautogui.doubleClick(x_origem + 260, y_origem + 25)  # clica no no icone dos meus objetos
            if pyautogui.pixelMatchesColor((x_origem + 230), (y_origem + 222), (152, 48, 220), tolerance=10):
                # testa se tem a guia de 2xp
                print("Tem a guia de 2xp")
                pyautogui.doubleClick(x_origem + 260, y_origem + 25)  # clica no no icone dos meus objetos
                pyautogui.doubleClick(x_origem + 230, y_origem + 222)  # clica na guia do 2xp
                if (pyautogui.pixelMatchesColor((x_origem + 690), (y_origem + 270), (120, 202, 12), tolerance=10)
                        or pyautogui.pixelMatchesColor((x_origem + 690), (y_origem + 270), (154, 217, 15), tolerance=10)):
                    # testa se tem o cartão de 2XP sem usar
                    print("Tem 2xp")
                    pyautogui.doubleClick(x_origem + 260, y_origem + 25)  # clica no no icone dos meus objetos
                    pyautogui.mouseDown(x_origem + 720, y_origem + 280)  # clica na guia do 2xp
                    time.sleep(1)
                    pyautogui.mouseUp(x_origem + 720, y_origem + 280)  # clica na guia do 2xp
                    time.sleep(1)
                    pyautogui.click(x_origem + 772, y_origem + 160)  # clica no fechar meus objetos
                    return "2XP acionado"
            else:
                print('Não tem a guia de 2xp')
                pyautogui.doubleClick(x_origem + 260, y_origem + 25)  # clica no no icone dos meus objetos
                pyautogui.click(x_origem + 772, y_origem + 160)  # clica no fechar meus objetos
                return "Não tem a guia de 2xp"
        else:
            print('Meus Objetos ainda nao foi aberto')
