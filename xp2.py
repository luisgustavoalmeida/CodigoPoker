import time

import pyautogui

import Limpa


def pega_2xp(x_origem, y_origem):

    for _ in range(60):
        if pyautogui.pixelMatchesColor((x_origem + 241), (y_origem + 146), (249, 108, 1), tolerance=5):
            # testa se esta meus objetos esta visivel
            print("Janela dos meus objetos visivel")
            pyautogui.doubleClick(x_origem + 260, y_origem + 25)  # clica no no icone dos meus objetos
            time.sleep(1)
            pyautogui.doubleClick(x_origem + 260, y_origem + 25)  # clica no no icone dos meus objetos
            if (pyautogui.pixelMatchesColor((x_origem + 230), (y_origem + 222), (154, 49, 221), tolerance=10)
                    and pyautogui.pixelMatchesColor((x_origem + 241), (y_origem + 146), (249, 108, 1), tolerance=10)):
                # testa se tem a guia de 2xp # testa se esta meus objetos esta visivel
                print("Tem a guia de 2xp")
                pyautogui.doubleClick(x_origem + 260, y_origem + 25)  # clica no no icone dos meus objetos
                pyautogui.doubleClick(x_origem + 230, y_origem + 222)  # clica na guia do 2xp
                if (pyautogui.pixelMatchesColor((x_origem + 690), (y_origem + 290), (107, 185, 12), tolerance=10)
                        or pyautogui.pixelMatchesColor((x_origem + 690), (y_origem + 290), (130, 200, 14), tolerance=10)):
                    # testa se tem o cartão de 2XP sem usar ( muda cor com o mouse em cima)
                    print("Tem 2xp")
                    pyautogui.doubleClick(x_origem + 260, y_origem + 25)  # clica no no icone dos meus objetos
                    pyautogui.mouseDown(x_origem + 720, y_origem + 280)  # clica usar 2XP
                    time.sleep(0.7)
                    pyautogui.mouseUp(x_origem + 720, y_origem + 280)  # clica usar 2XP
                    time.sleep(1)
                    # pyautogui.click(x_origem + 772, y_origem + 160)  # clica no fechar meus objetos
                    print('2XP Acionado')
                    time.sleep(1)
                    # return "2XP acionado"
            elif ((not pyautogui.pixelMatchesColor((x_origem + 230), (y_origem + 222), (154, 49, 221), tolerance=10))
                  and pyautogui.pixelMatchesColor((x_origem + 241), (y_origem + 146), (249, 108, 1), tolerance=5)):
                # testa se não tem a guia de 2xp # testa se esta meus objetos esta visivel
                print('Não tem a guia de 2xp')
                pyautogui.doubleClick(x_origem + 260, y_origem + 25)  # clica no no icone dos meus objetos
                pyautogui.click(x_origem + 772, y_origem + 160)  # clica no fechar meus objetos
                return "Não tem a guia de 2xp"
        else:
            print('Meus Objetos ainda nao foi aberto')
            pyautogui.doubleClick(x_origem + 260, y_origem + 25)  # clica no no icone dos meus objetos
            print('clica nos meus objetos')
            Limpa.limpa_pequeno(x_origem, y_origem)

    print('Não tem a guia de 2xp')
    pyautogui.doubleClick(x_origem + 260, y_origem + 25)  # clica no no icone dos meus objetos
    pyautogui.click(x_origem + 772, y_origem + 160)  # clica no fechar meus objetos
    return "Não tem a guia de 2xp"

# import Origem_pg
#
# (x_origem, y_origem) = Origem_pg.x_y()
# pega_2xp(x_origem, y_origem)
