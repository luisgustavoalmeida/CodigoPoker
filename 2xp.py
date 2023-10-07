import Origem_pg
import pyautogui
import time
import Limpa
x_origem, y_origem = Origem_pg.x_y()

def pega_2xp(x_origem, y_origem):
    tem_2xp = True
    while tem_2xp:
        pyautogui.doubleClick(x_origem + 260, y_origem + 25)  # clica no no icone dos meus objetos
        Limpa.limpa_pequeno(x_origem, y_origem)
        if pyautogui.pixelMatchesColor((x_origem + 441), (y_origem + 146), (250, 112, 1), tolerance=10):  # testa se esta meus objetos
            print("Janela dos meus objetos visivel")
            if pyautogui.pixelMatchesColor((x_origem + 230), (y_origem + 222), (152, 48, 220), tolerance=10):  # testa se tem a guia de 2xp
                print("Tem a guia de 2xp")
                pyautogui.doubleClick(x_origem + 230, y_origem + 222)  # clica na guia do 2xp

                lista_posi = (270, 350, 430, 510)
                for posi in lista_posi:
                    if (pyautogui.pixelMatchesColor((x_origem + 690), (y_origem + posi), (120, 202, 12), tolerance=10)
                            or pyautogui.pixelMatchesColor((x_origem + 690), (y_origem + posi), (154, 217, 15), tolerance=10)):  # testa se tem o cartão de 2XP sem usar
                        print("Tem 2xp")
                        pyautogui.mouseDown(x_origem + 720, y_origem + 280)  # clica na guia do 2xp
                        time.sleep(1)
                        pyautogui.mouseUp(x_origem + 720, y_origem + 280)  # clica na guia do 2xp
                        time.sleep(1)
                        if pyautogui.pixelMatchesColor((x_origem + 690), (y_origem + posi), (156, 184, 207), tolerance=10):  # testa se tem o cartão de 2XP USADO
                            print("2XP ja foi acionado")
                            return
                        break
                    else:
                        if pyautogui.pixelMatchesColor((x_origem + 690), (y_origem + posi), (156, 184, 207), tolerance=10):  # testa se tem o cartão de 2XP USADO
                            print("2XP ja foi acionado")
                            return

            else:
                print('Não tem a guia de 2xp')

        else:
            print('Meus Objetos ainda nao foi aberto')