import Limpa
import Origem_pg
import pyautogui
import time
import Limpa
x_origem, y_origem = Origem_pg.x_y()


def cofre_abrir(x_origem, y_origem):
    cofre_fechado = True
    #Limpa.limpa_total(x_origem, y_origem)
    while cofre_fechado:
        pyautogui.doubleClick(x_origem + 214, y_origem + 25)  # clica no no icone do cofre para abrir a janela
        Limpa.limpa_pequeno(x_origem, y_origem)
        if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 170), (111, 79, 51), tolerance=10):  # testa se esta visivel o cofre
            print("Janela do cobre visivel")

            if pyautogui.pixelMatchesColor((x_origem + 420), (y_origem + 340), (76, 56, 39), tolerance=10):  # testa se esta diponivel para digitar senha
                pyautogui.doubleClick(x_origem + 450, y_origem + 340)  # clica no campo para digirta senha
                time.sleep(0.5)
                pyautogui.typewrite("020996Pa") #  coloca a senha no canpo destinado
                time.sleep(0.5)
                pyautogui.press('enter') # Pressione a tecla "Enter"
                time.sleep(0.5)

            if pyautogui.pixelMatchesColor((x_origem + 148), (y_origem + 237), (120, 35, 23), tolerance=10):  # testa se esta diponivel para digitar senha
                print('Cofre aberto')
                cofre_fechado = False
                return True

def cofre_depositar(x_origem, y_origem):
    if cofre_abrir(x_origem, y_origem):
        pyautogui.doubleClick(x_origem + 330, y_origem + 140)  # clica para abrir a tela de depositar
        time.sleep(0.5)
        pyautogui.doubleClick(x_origem + 490, y_origem + 280)  # clica na area para escrever o valor da fichas
        time.sleep(0.5)
        pyautogui.typewrite("40000")  # escreve o valor a ser depositado
        time.sleep(0.5)
        pyautogui.click(x_origem + 490, y_origem + 500)  # clica no botao depositar
        for i in range(30):
            if (pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 475), (14, 134, 7),tolerance=10)
                    or pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 475), (17, 146, 9),tolerance=10)):  # testa se esta diponivel para digitar senha
                pyautogui.doubleClick(x_origem + 490, y_origem + 470)  # clica no botao OK de confirmação de deposito
                print('Valor depositado corretamente')
                return True
            time.sleep(0.2)
        return False

    else:
        print('Cofre não foi aberto')
        return False


def cofre_sacar(x_origem, y_origem):
    if cofre_abrir(x_origem, y_origem):
        pyautogui.doubleClick(x_origem + 660, y_origem + 140)  # clica para abrir a tela de sacara
        time.sleep(0.5)
        pyautogui.doubleClick(x_origem + 490, y_origem + 280)  # clica na area para escrever o valor da fichas
        time.sleep(0.5)
        pyautogui.typewrite("999999999")  # escreve o valor para sacar tudo
        time.sleep(0.5)
        pyautogui.click(x_origem + 490, y_origem + 500)  # clica no botao depositar
        for i in range(30):
            if (pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 475), (14, 134, 7),tolerance=10)
                    or pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 475), (17, 146, 9),tolerance=10)):  # testa se esta diponivel para digitar senha
                pyautogui.doubleClick(x_origem + 490, y_origem + 470)  # clica no botao OK de confirmação de deposito
                print('Valor sacado corretamente')
                return True
            time.sleep(0.2)
        print('Cofre ja estava vazio')
        return True

    else:
        print('Cofre não foi aberto')
        return False


#cofre_sacar(x_origem, y_origem)