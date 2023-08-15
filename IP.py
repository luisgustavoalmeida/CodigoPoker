
import Google
import os
import socket
import time
import pywinauto
import pyautogui
# Desabilitar o fail-safe
pyautogui.FAILSAFE = False
import requests
import datetime
#import subprocess
import psutil
import random
import Seleniun
import pygetwindow as gw
import subprocess

LIMITE_IP = 5

# chave nome do computador : tupla( valor 1 celula , valor 2 tipo de conexão)
# "F3" de 3 em 3       #"modem" ou "vero"
# cria um dicionario de tuplas par agurdar os valores das celulas e o tipo de conexao com a internete que cada computador usa
dicionari_PC_IP = {'PC-I5-8600K':   ("F3",  "modem"),
                   'PC-I5-9400A':   ("F6",  "modem"),
                   'PC-I5-9400B':   ("F9",  "modem"),
                   'PC-I5-9400C':   ("F12", "modem"),
                   'PC-R5-7600A':   ("F15", "modem"),
                   'PC-I5-13400A':  ("F18", "modem"),
                   'PC-i3-8145U':   ("F21", "modem"),
                   'PC-I7-9700KF':  ("F24", "vero"),
                   'PC-I7-11850H':  ("F27", "vero")}

# Obter o nome de usuário
nome_usuario = os.getlogin()
#print("Nome de usuário:", nome_usuario)

# Obter o nome do computador
nome_computador = socket.gethostname()
#print("Nome do computador:", nome_computador)

# usa o nome do computador para buscar os valores do dicionario
valor_dicionario = dicionari_PC_IP[nome_computador]
celula = valor_dicionario[0]  # pega o primeiro item da tupla
tipo_conexao = valor_dicionario[1]  # pega o segundo item da tuplas

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

def testa_trocar_IP():
    if (nome_usuario == "PokerIP") and (nome_computador != "PC-I7-9700KF"):  # teste se o usuario do computador é o que troca IP se nao for fica esperando esta livre
        ip()
        return
    elif (nome_usuario == "lgagu") and (nome_computador == "PC-I7-9700KF"):
        ip()
        return
    else:
        return

def f5_quando_internete_ocila(id, senha, url, navegador):
    print('f5_quando_internete_ocila')
    conectado = True
    while True:
        try:
            response = requests.get('http://www.google.com', timeout=1)
            #if response.status_code == 200:
            if response.status_code == 200 or response.status_code == 429:
                print("Conexão com a internet ativa. ")
                if not conectado:
                    try:
                        print("------------------F5-----------------")
                        pyautogui.press('f5')
                        time.sleep(15)
                    except Exception as e:
                        print('erro autogui: ', e)

                    entrou_corretamente, stataus = Seleniun.teste_logado(id, senha, url, navegador)
                return True
        except Exception as e:
            print("Sem conexão com a internet...")
            print(e)
            time.sleep(5)
            conectado = False


def tem_internet():
    cont_erro2 = 0
    cont_erro = 0
    #print('tem_internet')

    sites = [
        'http://www.google.com',
        'http://www.facebook.com',
        'http://www.twitter.com',
        'http://www.youtube.com',
        'http://www.instagram.com',
        'http://www.linkedin.com',
        'http://www.github.com',
        'http://www.reddit.com',
        'http://www.amazon.com',
        'http://www.netflix.com'
    ]

    com_internete = True
    while com_internete:
        print('testa a internete')
        cont_erro2 += 1
        site_aleatorio = random.choice(sites)
        #print(site_aleatorio)
        try:
            response = requests.get(site_aleatorio, timeout=10)
            if response.status_code == 200 or response.status_code == 429:
                print("Conexão com a internet ativa.")
                cont_erro = 0
                cont_erro2 = 0
                com_internete = False
                return True

        except Exception as e:
            print("Sem conexão com a internet. Encerrando os testes...")
            print(e)
            time.sleep(3)
            cont_erro += 1
            print('contagem de erro 1: ', cont_erro)
            if cont_erro >= 5:
                cont_erro = 0
                cont_erro2 = 0
                if nome_usuario == "PokerIP":  # teste se o usuario do computador é o que troca IP se nao for fica esperando esta livre
                    print("Vai par a função de trocar ip")
                    conexao()  # chama a função que troca ip
                elif (nome_usuario == "lgagu") and (nome_computador == "PC-I7-9700KF"):
                    print("Vai par a função de trocar ip")
                    conexao()  # chama a função que troca ip
            continue

        if cont_erro2 >= 20:
            cont_erro = 0
            cont_erro2 = 0
            if nome_usuario == "PokerIP":  # teste se o usuario do computador é o que troca IP se nao for fica esperando esta livre
                print("Vai par a função de trocar ip")
                conexao()  # chama a função que troca ip
            elif (nome_usuario == "lgagu") and (nome_computador == "PC-I7-9700KF"):
                print("Vai par a função de trocar ip")
                conexao()  # chama a função que troca ip
            continue
        print('contagem de erro 1: ', cont_erro)
        print('contagem de erro 2: ', cont_erro2)

    return True
def meu_ip():
    urls = [
        'https://api.ipify.org',
        'http://checkip.amazonaws.com',
        'http://ipinfo.io/ip',
        'http://whatismyip.akamai.com',
        'http://ipecho.net/plain',
        'http://myexternalip.com/raw',
        'http://ip.42.pl/raw',
        'http://ipecho.net/plain',
        'http://eth0.me',
        'http://myip.dnsomatic.com',
        'http://ifconfig.me/ip',
        'https://ipv4.icanhazip.com/',
        'http://ipv4.ident.me/',
        'https://ipv4.icanhazip.com/',
        'http://whatismyipv4.net'
    ]
    random.shuffle(urls)  # Embaralha a lista de URLs
    while True:
        for url in urls:
            #print(url)
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    texto = response.text
                    texto = texto.strip() # remove os espaços em branco (espaços, tabulações e quebras de linha) no início e no final da string
                    print(texto)
                    return texto, True
                else:
                    print("Não houve resposta da API de IP:", url)
            except Exception as e:
                print("Tempo limite excedido ao procurar o elemento.")
                hora_atual = datetime.datetime.now().strftime('%H:%M:%S')
                print("Sem conexão com a internet, hora:", hora_atual, "nova tentativa e outro servidor")
                print(e)
                time.sleep(5)

def nao_tem_internet():
    for i in range(20):
        try:
            response = requests.get('http://www.google.com', timeout=1)
            if response.status_code == 200:
                print("Conexão com a internet ativa.")
                time.sleep(0.5)  # Espera por 5 segundos antes de fazer o próximo teste
        except Exception as e:
            print("Sem conexão com a internet. Encerrando os testes...")
            print(e)
            time.sleep(5)
            break

def ip_troca_agora():
    while True:
        # com_internete = tem_internet()
        # if com_internete:
        if nome_usuario == "PokerIP":  # teste se o usuario do computador é o que troca IP se nao for fica esperando esta livre
            print("Vai par a função de trocar ip")
            conexao()  # chama a função que troca ip
            print('espera a internete estar estavel')
            tem_internet()  # testa ate que internete esteja estavel
            print("Vai para a função que zera a contagem")
            Google.zera_cont_IP(celula)  # Zera a contegem de ip na planilha
            return
        elif (nome_usuario == "lgagu") and (nome_computador == "PC-I7-9700KF"):
            print("Vai par a função de trocar ip")
            conexao()  # chama a função que troca ip
            print('espera a internete estar estavel')
            tem_internet()  # testa ate que internete esteja estavel
            print("Vai para a função que zera a contagem")
            Google.zera_cont_IP(celula)  # Zera a contegem de ip na planilha
            return
        else:
            return


def ip():

    LIMITE_IP = 5

    while True:

        com_internete = tem_internet()
        #tem_internet() # testa se tem internete ativa
        cont_IP = int(Google.pega_valor('IP', celula))  # pega o valor de contas que ja rodaram no IP atual

        if com_internete:

            if cont_IP >= LIMITE_IP or cont_IP < 0:  #testa se esta maior que o lilite ou se esta negativo

                if nome_usuario == "PokerIP":  #teste se o usuario do computador é o que troca IP se nao for fica esperando esta livre
                    print("Vai par a função de trocar ip")
                    conexao() # chama a função que troca ip
                    print('espera a internete estar estavel')
                    tem_internet() # testa ate que internete esteja estavel
                    print("Vai para a função que zera a contagem")
                    Google.zera_cont_IP(celula) # Zera a contegem de ip na planilha
                    return

                elif (nome_usuario == "lgagu") and (nome_computador == "PC-I7-9700KF"):
                    print("Vai par a função de trocar ip")
                    conexao()  # chama a função que troca ip
                    print('espera a internete estar estavel')
                    tem_internet()  # testa ate que internete esteja estavel
                    print("Vai para a função que zera a contagem")
                    Google.zera_cont_IP(celula) # Zera a contegem de ip na planilha
                    return

                else:
                    print("Espera liberar IP")
                    nao_tem_internet()
                    continue

            else:
                print("Continua não tem que trocar IP")
                return


def conexao():

    if tipo_conexao == "vero" or tipo_conexao == "modem":

        # Título e nome da classe da janela que você deseja verificar
        window_title = 'Configurações'
        window_class = 'ApplicationFrameWindow'

        print("manda a jenela de conexao abrir")
        if tipo_conexao == "vero":
            os.system("start ms-settings:network-dialup")  # abre a conexão discada
        elif tipo_conexao == "modem":
            os.system("start ms-settings:network-airplanemode")  # modo aviao

        while True:
            try:
                app = pywinauto.Application().connect(title=window_title, class_name=window_class)
                # A janela já está aberta, ative-a
                app_top_window = app.top_window()
                app_top_window.restore()
                app_top_window.move_window(x=930, y=710, width=500, height=330)
                conexao_x = app_top_window.rectangle().left
                conexao_y = app_top_window.rectangle().top
                app_top_window.set_focus()
                break
            except:
                # A janela não está aberta, abra-a
                print("conexao abrir")
                if tipo_conexao == "vero":
                    os.system("start ms-settings:network-dialup")  # abre a conexão discada
                elif tipo_conexao == "modem":
                    os.system("start ms-settings:network-airplanemode")  # modo aviao
                # Aguarde a janela abrir
                time.sleep(1)
                continue
        time.sleep(0.5)

    elif tipo_conexao == "vpn":
        # Caminho para o executável da VPN

        caminho_executavel_vpn = "C:/Program Files (x86)/ExpressVPN/expressvpn-ui/ExpressVPN.exe"
        conexao_vpn_x = 930
        conexao_vpn_y = 440
        while True:

            print('abre a vpn')
            try:
                vpn_window = gw.getWindowsWithTitle('ExpressVPN')[0]
                print(vpn_window)
                # vpn_window.activate()
                # Verificar se a janela está visível antes de movê-la
                if vpn_window.left == 930 and vpn_window.top == 440:
                    conexao_vpn_vpn_x = vpn_window.left
                    conexao_vpn_vpn_y = vpn_window.top
                    print("A posição da janela é (930, 440).")
                    break
                if vpn_window.left < 0 and vpn_window.top < 0:
                    print('esta minizada')
                    subprocess.Popen(caminho_executavel_vpn)
                else:
                    vpn_window.activate()
                    # Mover a janela da VPN para a posição desejada (x, y) da tela
                    conexao_vpn_vpn_x = 930
                    conexao_vpn_vpn_y = 440

                    vpn_window.moveTo(conexao_vpn_vpn_x, conexao_vpn_vpn_y)
            except Exception as e:
                print("Erro ao abrir a VPN:", e)
                subprocess.Popen(caminho_executavel_vpn)
                time.sleep(5)
                continue
            time.sleep(0.5)


    if tipo_conexao == "vero":
        precisao = 0.9
        print("conexão vero")

        telefone = r"Imagens\Conexao\telefone.png"
        regiao_telefone = (conexao_x + 22, conexao_y + 109, 59, 56)
        desconectar = r"Imagens\Conexao\desconectar.png"
        regiao_desconectar = (conexao_x + 361, conexao_y + 185, 109, 36)
        conectar = r"Imagens\Conexao\conectar.png"
        regiao_conectar = (conexao_x + 124, conexao_y + 185, 92, 34)
        conectado = r"Imagens\Conexao\conectado.png"
        regiao_conectado = (conexao_x + 70, conexao_y + 133, 92, 34)
        fechar = r"Imagens\Conexao\fechar.png"
        regiao_fechar = (conexao_x + 380, conexao_y + 236, 91, 80)
        cancelar = r"Imagens\Conexao\cancelar.png"
        regiao_cancelar = (conexao_x + 358, conexao_y + 204, 111, 36)
        cont_erro = 0

        while True:

            #posicao_telefone = pyautogui.locateOnScreen(telefone, region=regiao_telefone, confidence=0.9, grayscale=True)
            posicao_telefone = localizar_imagem(telefone, regiao_telefone, precisao)
            if posicao_telefone is not None:
                centro_discada = pyautogui.center(posicao_telefone)# Obtém o centro da posição da imagem encontrada
                pyautogui.click(centro_discada)# Clica no centro da posição encontrada
                print("clica no telefoen")

                #posicao_desconectar = pyautogui.locateOnScreen(desconectar, region=regiao_desconectar, confidence=0.9, grayscale=True)
                posicao_desconectar = localizar_imagem(desconectar, regiao_desconectar, precisao)
                if posicao_desconectar is not None:
                    centro_desconectar = pyautogui.center(posicao_desconectar)# Obtém o centro da posição da imagem encontrada
                    pyautogui.click(centro_desconectar)# Clica no centro da posição encontrada
                    time.sleep(1)
                    print("clica no desconectar")

                #posicao_fechar = pyautogui.locateOnScreen(fechar, region=regiao_fechar, confidence=0.9, grayscale=True)
                posicao_fechar = localizar_imagem(fechar, regiao_fechar, precisao)
                if posicao_fechar is not None:
                    cont_erro = 0
                    centro_fechar = pyautogui.center(posicao_fechar)  # Obtém o centro da posição da imagem encontrada
                    pyautogui.click(centro_fechar)  # Clica no centro da posição encontrada
                    print("clica no fechar 1")
                    time.sleep(2)

                #posicao_conectar = pyautogui.locateOnScreen(conectar, region=regiao_conectar, confidence=0.9, grayscale=True)
                posicao_conectar = localizar_imagem(conectar, regiao_conectar, precisao)
                if posicao_conectar is not None:
                    centro_conectar = pyautogui.center(posicao_conectar)# Obtém o centro da posição da imagem encontrada
                    pyautogui.click(centro_conectar)# Clica no centro da posição encontrada
                    time.sleep(1)
                    print("clica no conectar")
                    break


        while True:
            cont_erro += 1

            #posicao_conectado = pyautogui.locateOnScreen(conectado, region=regiao_conectado, confidence=0.9, grayscale=True)
            posicao_conectado = localizar_imagem(conectado, regiao_conectado, precisao)
            if posicao_conectado is not None:
                print("esta conectado")
                app_top_window.minimize()  # minimiza a janela
                return None
                #break

            #posicao_conectar = pyautogui.locateOnScreen(conectar, region=regiao_conectar, confidence=0.9, grayscale=True)
            posicao_conectar = localizar_imagem(conectar, regiao_conectar, precisao)
            if posicao_conectar is not None:
                centro_conectar = pyautogui.center(posicao_conectar)# Obtém o centro da posição da imagem encontrada
                pyautogui.click(centro_conectar)# Clica no centro da posição encontrada
                print("clica no conectar 2")
                time.sleep(1)

            # se deu algum erro e nao conectou aparece um mensagem de erro e opção de fechar
            #posicao_fechar = pyautogui.locateOnScreen(fechar, region=regiao_fechar, confidence=0.9, grayscale=True)
            posicao_fechar = localizar_imagem(fechar, regiao_fechar, precisao)
            if posicao_fechar is not None:
                cont_erro = 0
                centro_fechar = pyautogui.center(posicao_fechar)# Obtém o centro da posição da imagem encontrada
                pyautogui.click(centro_fechar)# Clica no centro da posição encontrada
                print("clica no fechar 2")
                time.sleep(2)

            # se esta demorando muito para conectar clia em cancelar e tenta novamente
            if cont_erro >= 60:
                #posicao_cancelar = pyautogui.locateOnScreen(cancelar, region=regiao_cancelar, confidence=0.9, grayscale=True)
                posicao_cancelar = localizar_imagem(cancelar, regiao_cancelar, precisao)
                if posicao_cancelar is not None:
                    cont_erro = 0
                    centro_cancelar = pyautogui.center(posicao_cancelar)# Obtém o centro da posição da imagem encontrada
                    pyautogui.click(centro_cancelar)# Clica no centro da posição encontrada
                    time.sleep(2)
            time.sleep(0.5)

        # app_top_window.minimize()  # minimiza a janela
        # return None


    elif tipo_conexao == "modem":
        print('modem')
        celular = r"Imagens\Conexao\celular.png"
        regiao_celular = (conexao_x + 19, conexao_y + 261, 55, 22)
        ativado = r"Imagens\Conexao\ativado.png"
        desativado = r"Imagens\Conexao\desativado.png"
        regiao_ativado_desativado = (conexao_x + 75, conexao_y + 292, 73, 22)
        precisao = 0.9

        while True:
            app_top_window.set_focus()
            posicao_celular = localizar_imagem(celular, regiao_celular, precisao)
            if posicao_celular is not None:
                centro_celular = pyautogui.center(posicao_celular)  # Obtém o centro da posição da imagem encontrada
                posicao_botao = pyautogui.Point(centro_celular.x, centro_celular.y + 30)

                posicao_ativado = localizar_imagem(ativado, regiao_ativado_desativado, precisao)
                if posicao_ativado is not None:
                    time.sleep(0.3)
                    pyautogui.click(posicao_botao)  # Clica para desativar a coneção
                    print("foi desativado")
                    time.sleep(0.3)
                    for i in range(50):
                        status = obter_status_conexao("Celular")
                        print('esperando desconectar')
                        if status == "Desconectado":
                            print(status)
                            break
                        time.sleep(0.5)
                    app_top_window.set_focus()

                posicao_desativado = localizar_imagem(desativado, regiao_ativado_desativado, precisao)
                if posicao_desativado is not None:
                    pyautogui.click(posicao_botao)  # Clica para ativar a coneção
                    print("foi ativado")
                    for i in range(100):
                        status = obter_status_conexao("Celular")
                        print('esperando conectar')
                        if status == "Conectado":
                            print(status)
                            app_top_window.minimize()  # minimiza a janela
                            return None
                        time.sleep(0.5)
                    app_top_window.set_focus()

    elif tipo_conexao == "vpn":
        conexao_vpn_x = 930
        conexao_vpn_y = 440
        while True:
            print('refazendo conexao')
            # testa se esta verde e ligado
            if pyautogui.pixelMatchesColor((conexao_vpn_vpn_x + 189), (conexao_vpn_vpn_y + 186), (15, 134, 108), tolerance=10) \
                    or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (77, 182, 172), tolerance=10):
                pyautogui.click(conexao_vpn_x + 189, conexao_vpn_y + 186)
                print('desligou')
                for i in range(100):
                    # testa se esta vermelho e desligado
                    if pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (126, 15, 83), tolerance=10) \
                            or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (164, 17, 94), tolerance=10):
                        time.sleep(0.5)
                        print('VPN Desconectado')
                        break
                    time.sleep(0.5)

            # testa se esta vermelho e desligado
            elif pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (126, 15, 83), tolerance=10) \
                    or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (164, 17, 94), tolerance=10):
                pyautogui.click(conexao_vpn_x + 189, conexao_vpn_y + 186)
                print('ligou')
                for i in range(100):
                    # testa se esta vermelho e desligado
                    if pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (15, 134, 108), tolerance=10) \
                            or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (77, 182, 172), tolerance=10):
                        print('VPN Conectado')
                        # Minimizar a janela
                        vpn_window.minimize()
                        return None
                    time.sleep(0.5)


def localizar_imagem(imagem, regiao, precisao):
    try:
        posicao = pyautogui.locateOnScreen(imagem, region=regiao, confidence=precisao, grayscale=True)
        return posicao
    except:
        print("Ocorreu um erro ao localizar a imagem")
        time.sleep(2)
        return None


def obter_status_conexao(nome_conexao):
    conexoes = psutil.net_if_stats()
    if nome_conexao in conexoes:
        status = conexoes[nome_conexao].isup
        if status:
            return "Conectado"
        else:
            return "Desconectado"
    else:
        time.sleep(0.5)
        return "Conexão não encontrada"


def obter_nomes_conexoes():
    conexoes = psutil.net_if_stats()
    nomes = conexoes.keys()
    print(nomes)
    return nomes

# # Exemplo de uso
# nomes_conexoes = obter_nomes_conexoes()
# for nome in nomes_conexoes:
#     print(nome)

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


# #ip()
# #tem_internet()
#
# tipo_conexao = "modem"
# # # print("chma conexao")
# conexao(tipo_conexao)

# conexao()
