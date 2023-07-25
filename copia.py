
import Google
import os
import socket
import time
import pywinauto
import pyautogui
import requests
import datetime
#import subprocess
import psutil

# Obter o nome do computador
nome_computador = socket.gethostname()
#print("Nome do computador:", nome_computador)

# Obter o nome de usuário
nome_usuario = os.getlogin()
#print("Nome de usuário:", nome_usuario)

# chave nome do computador : tupla( valor 1 celula , valor 2 tipo de conexão)
# "F3" de 3 em 3       #"modem" ou "vero"
# cria um dicionario de tuplas par agurdar os valores das celulas e o tipo de conexao com a internete que cada computador usa
dicionari_PC_IP = {'PC-I5-8600K': ("F3", "modem"),
                   'PC-I5-9400A': ("F6", "modem"),
                   'PC-I5-9400B': ("F9", "modem"),
                   'PC-I5-9400C': ("F12", "modem"),
                   'PC-I7-9700KF': ("F15", "vero"),
                   'PC-I7-11850H': ("F18", "vero"),
                   'PC-i3-8145U': ("F21", "vero"), }

def usuario_IP_nao():
    #nome_usuario = os.getlogin()
    if nome_usuario != "PokerIP":
        ip()
        return
def usuario_IP_sim():
    #nome_usuario = os.getlogin()
    if nome_usuario == "PokerIP":
        ip()
        return


def tem_internet():
    while True:
        try:
            #socket.create_connection(("www.google.com", 80), timeout=0)
            #print("Internet ativa")
            response = requests.get('https://api.ipify.org')
            if response.status_code == 200:
                print(response.text)
                return response.text
            else:
                return None
        except OSError:
            hora_atual = datetime.datetime.now().strftime('%H:%M:%S')
            print("Sem conexão com a internet, hora: ", hora_atual, "nova tentativa em 5 segundos")
            time.sleep(5)


def ip():

    LIMITE_IP = 5

    # usa o nome do computador para buscar os valores do dicionario
    valor_dicionario = dicionari_PC_IP[nome_computador]
    celula = valor_dicionario[0] # pega o primeiro item da tupla
    tipo_conexao = valor_dicionario[1] # pega o segundo item da tuplas
    #print(celula)
    #print(tipo_conexao)

    while True:
        #tem_internet() # testa se tem internete ativa
        cont_IP = Google.testa_valor('IP', celula) # pega o valor de contas que ja rodaram no IP atual
        cont_IP = int(cont_IP) # converte par int
        #print(cont_IP)
        if cont_IP >= LIMITE_IP or cont_IP < 0: #testa se esta maior que o lilite ou se esta negativo
            if (nome_usuario == "PokerIP" ) and (nome_computador != "PC-I7-9700KF"): # teste se o usuario do computador é o que troca IP se nao for fica esperando esta livre
                print("Vai par a função de trocar ip")
                conexao(tipo_conexao) # chama a função que troca ip
                print("Vai para a função que zera a contagem")
                Google.zera_cont_IP(celula) # Zera a contegem de ip na planilha
                break
            elif (nome_usuario == "lgagu") and (nome_computador == "PC-I7-9700KF") :
                print("Vai par a função de trocar ip")
                conexao(tipo_conexao) # chama a função que troca ip
                print("Vai para a função que zera a contagem")
                Google.zera_cont_IP(celula) # Zera a contegem de ip na planilha
            else:
                print("Espera 3s para testar se livre")
                time.sleep(3)
        else:
            print("Continua não tem que trocar IP")
            break


def conexao(tipo_conexao):

    # Título e nome da classe da janela que você deseja verificar
    window_title = 'Configurações'
    window_class = 'ApplicationFrameWindow'

    try:
        app = pywinauto.Application().connect(title=window_title, class_name=window_class)
        # A janela já está aberta, ative-a
        app_top_window = app.top_window()
        app_top_window.restore()
        app_top_window.move_window(x=1420, y=0, width=300, height=50)
        app_top_window.set_focus()
    except:
        # A janela não está aberta, abra-a
        if tipo_conexao == "vero":
            os.system("start ms-settings:network-dialup")  # abre a conexão discada
        elif tipo_conexao == "modem":
            os.system("start ms-settings:network-airplanemode")  # modo aviao
        # Aguarde a janela abrir
        while True:
            try:
                app = pywinauto.Application().connect(title=window_title, class_name=window_class)
                app_top_window = app.top_window()
                break
            except pywinauto.application.ProcessNotFoundError:
                time.sleep(1)

                if tipo_conexao == "vero":
                    os.system("start ms-settings:network-dialup")  # abre a conexão discada
                elif tipo_conexao == "modem":
                    os.system("start ms-settings:network-airplanemode")  # modo aviao
                time.sleep(1)
                app = pywinauto.Application().connect(title=window_title, class_name=window_class)
                app_top_window = app.top_window()
                app_top_window.restore()
                app_top_window.move_window(x=1420, y=0, width=300, height=50)
                app_top_window.set_focus()
                continue
    time.sleep(0.5)
    # app_top_window.minimize() # minimiza a janela

    if tipo_conexao == "vero":

        telefone = r"Imagens\Conexao\telefone.png"
        regiao_telefone = (1434, 109, 1493, 165)
        desconectar = r"Imagens\Conexao\desconectar.png"
        regiao_desconectar = (1773, 185, 1882, 221)
        conectar = r"Imagens\Conexao\conectar.png"
        regiao_conectar = (1536, 185, 1628, 219)
        conectado = r"Imagens\Conexao\conectado.png"
        regiao_conectado = (1482, 133, 1565, 161)
        fechar = r"Imagens\Conexao\fechar.png"
        regiao_fechar = (1792, 236, 1883, 269)
        cancelar = r"Imagens\Conexao\cancelar.png"
        regiao_cancelar = (1770, 204, 1882, 240)
        cont_erro = 0

        while True:

            posicao_telefone = pyautogui.locateOnScreen(telefone, region=regiao_telefone, confidence=0.9, grayscale=True)
            if posicao_telefone is not None:
                centro_discada = pyautogui.center(posicao_telefone)# Obtém o centro da posição da imagem encontrada
                pyautogui.click(centro_discada)# Clica no centro da posição encontrada

                posicao_desconectar = pyautogui.locateOnScreen(desconectar, region=regiao_desconectar, confidence=0.9, grayscale=True)
                if posicao_desconectar is not None:
                    centro_desconectar = pyautogui.center(posicao_desconectar)# Obtém o centro da posição da imagem encontrada
                    pyautogui.click(centro_desconectar)# Clica no centro da posição encontrada
                    time.sleep(1)

                posicao_conectar = pyautogui.locateOnScreen(conectar, region=regiao_conectar, confidence=0.9, grayscale=True)
                if posicao_conectar is not None:
                    centro_conectar = pyautogui.center(posicao_conectar)# Obtém o centro da posição da imagem encontrada
                    pyautogui.click(centro_conectar)# Clica no centro da posição encontrada
                    break

        while True:
            cont_erro += 1

            posicao_conectado = pyautogui.locateOnScreen(conectado, region=regiao_conectado, confidence=0.9, grayscale=True)
            if posicao_conectado is not None:
                break

            posicao_conectar = pyautogui.locateOnScreen(conectar, region=regiao_conectar, confidence=0.9, grayscale=True)
            if posicao_conectar is not None:
                centro_conectar = pyautogui.center(posicao_conectar)# Obtém o centro da posição da imagem encontrada
                pyautogui.click(centro_conectar)# Clica no centro da posição encontrada

            # se deu algum erro e nao conectou aparece um mensagem de erro e opção de fechar
            posicao_fechar = pyautogui.locateOnScreen(fechar, region=regiao_fechar, confidence=0.9, grayscale=True)
            if posicao_fechar is not None:
                cont_erro = 0
                centro_fechar = pyautogui.center(posicao_fechar)# Obtém o centro da posição da imagem encontrada
                pyautogui.click(centro_fechar)# Clica no centro da posição encontrada
                time.sleep(2)

            # se esta demorando muito para conectar clia em cancelar e tenta novamente
            if cont_erro >= 500:
                posicao_cancelar = pyautogui.locateOnScreen(cancelar, region=regiao_cancelar, confidence=0.9, grayscale=True)
                if posicao_cancelar is not None:
                    cont_erro = 0
                    centro_cancelar = pyautogui.center(posicao_cancelar)# Obtém o centro da posição da imagem encontrada
                    pyautogui.click(centro_cancelar)# Clica no centro da posição encontrada
                    time.sleep(2)

        app_top_window.minimize()  # minimiza a janela

    elif tipo_conexao == "modem":
        celular = r"Imagens\Conexao\celular.png"
        regiao_celular = (1440, 261, 1495, 283)
        ativado = r"Imagens\Conexao\ativado.png"
        desativado = r"Imagens\Conexao\desativado.png"
        regiao_ativado_desativado = (1498, 292, 1571, 309)

        while True:
            posicao_celular = pyautogui.locateOnScreen(celular, region=regiao_celular, confidence=0.9, grayscale=True)
            if posicao_celular is not None:
                centro_celular = pyautogui.center(posicao_celular)  # Obtém o centro da posição da imagem encontrada
                posicao_botao = pyautogui.Point(centro_celular.x, centro_celular.y + 30)
                # pyautogui.click(posicao_botao)  # Clica no centro da posição encontrada o Y ta delocado para clicar no botao
                posicao_ativado = pyautogui.locateOnScreen(ativado, region=regiao_ativado_desativado, confidence=0.9, grayscale=True)

                if posicao_ativado is not None:
                    pyautogui.click(posicao_botao)  # Clica para desativar a coneção
                    print("foi desativado")
                    #time.sleep(0.8)
                    while True:
                        status = obter_status_conexao("Celular")
                        if status == "Desconectado":
                            print(status)
                            break


                posicao_desativado = pyautogui.locateOnScreen(desativado, region=regiao_ativado_desativado, confidence=0.9, grayscale=True)
                if posicao_desativado is not None:
                    pyautogui.click(posicao_botao)  # Clica para ativar a coneção
                    print("foi ativado")
                    #time.sleep(0.25)
                    while True:
                        status = obter_status_conexao("Celular")
                        if status == "Conectado":
                            print(status)
                            app_top_window.minimize()  # minimiza a janela
                            break

                    break
    return

def obter_status_conexao(nome_conexao):
    conexoes = psutil.net_if_stats()
    if nome_conexao in conexoes:
        status = conexoes[nome_conexao].isup
        if status:
            return "Conectado"
        else:
            time.sleep(0.5)
            return "Desconectado"
    else:
        time.sleep(0.5)
        return "Conexão não encontrada"

# def ativar_destivar_conexao(nome_conexao, status):
#     try:
#         comando = f'netsh interface set interface "{nome_conexao}" admin="{status}"'
#         #subprocess.run(comando, shell=True, check=True)
#         subprocess.run(comando, shell=True, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
#         print(f"A conexão {nome_conexao} foi ativada com sucesso.")
#     except subprocess.CalledProcessError as e:
#         if e.returncode == 1:
#             ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", __file__, None, 1)
#         else:
#             print(f"Erro ao ativar a conexão {nome_conexao}: {e}")


# ip()
#tem_internet()