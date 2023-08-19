import time
import pyautogui

import Google

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False

import IP
import Seleniun
pyautogui.PAUSE = 0

# Define o nome do arquivo da imagem a ser buscada
origem = r'Imagens\Origem.png'
origemB = r'Imagens\OrigemB.png' # imagem do computador da AMD
origem2 = r'Imagens\OrigemAvisoDoSistema.png'

# Define a região da tela onde a imagem será buscada
regiao_busca = (0, 115, 380, 230)  # (x, y, largura, altura)

def localizar_imagem(imagem, regiao, precisao):
    try:
        posicao = pyautogui.locateOnScreen(imagem, region=regiao, confidence=precisao, grayscale=True)
        return posicao
    except :
        print("Ocorreu um erro ao localizar a imagem")
        time.sleep(2)
        return None


def carregado_origem(id, senha, url, navegador):#navegador
    status_conta = None
    cont_erro = 0

    for i in range(3):

        posicao = None
        # Faz x buscas com um intervalo de x segundos entre cada busca
        #print(" 0 x 0...")

        # JanelaSuperior.encontrar_janela_navegador()
        # pyautogui.click(10, 1020)  # clica bobo para nao hibernar

        print("carregado_orige Procurando coodenada 0 x 0...")
        for i in range(60):

            # Procura a imagem na região definida com 99,5% de tolerância, em escala de cinza e retorna a posição
            #posicao = pyautogui.locateOnScreen(origem, region=regiao_busca, confidence=0.997, grayscale=True) #limite maximo de precisao é 0.997
            #precisao = 0.997
            precisao = 0.935
            posicao = localizar_imagem(origem, regiao_busca, precisao)
            if posicao is not None:# Verifica se a imagem foi encontrada
                x_origem, y_origem = posicao.left, posicao.top
                x_origem = int(x_origem)
                y_origem = int(y_origem)
                if status_conta != 'Tutorial':
                    status_conta = 'Carregada'
                return x_origem, y_origem, status_conta
            posicao = localizar_imagem(origemB, regiao_busca, precisao)
            if posicao is not None:# Verifica se a imagem foi encontrada
                x_origem, y_origem = posicao.left, posicao.top
                x_origem = int(x_origem)
                y_origem = int(y_origem)
                if status_conta != 'Tutorial':
                    status_conta = 'Carregada'
                return x_origem, y_origem, status_conta
            #testa se tem botao para aceitar
            else:
                imagem = r'Imagens\Aceite.png'
                regiao = (380, 400, 250, 350)
                precisao = 0.8
                localizado = localizar_imagem(imagem, regiao, precisao)
                if localizado is not None:
                    centro = pyautogui.center(localizado)
                    pyautogui.doubleClick(centro.x, centro.y, button='left')
                    print("clica no aceite")
                    status_conta = 'Tutorial'
                    time.sleep(2)

                regiao = (250, 400, 300, 300)
                imagem = r'Imagens\Banida.png'
                precisao = 0.8
                localizado = localizar_imagem(imagem, regiao, precisao)
                if localizado is not None:
                    print("comta banida para o poker")
                    status_conta = 'Banida'
                    return 0, 0, status_conta

                # tutorial
                regiao = (440, 480, 330, 270)
                imagem = r'Imagens\Continuar2.png'
                precisao = 0.8
                localizado = localizar_imagem(imagem, regiao, precisao)
                if localizado is not None:
                    centro = pyautogui.center(localizado)
                    pyautogui.doubleClick(centro.x, centro.y, button='left')
                    print("clica no continuar")
                    time.sleep(2)

                regiao = (410, 400, 580, 300)
                imagem = r'Imagens\Atualizar.png'
                precisao = 0.8
                localizado = localizar_imagem(imagem, regiao, precisao)
                if localizado is not None:
                    #centro = pyautogui.center(localizado)
                    #pyautogui.doubleClick(centro.x, centro.y, button='left')
                    print("Erro ao entrar no Lobby, tente atualizar a pagina")
                    status_conta = 'Atualizar'
                    return 0, 0, status_conta

                regiao = (340, 800, 385, 105)
                imagem = r'Imagens\CarosJogadores.png'
                precisao = 0.995
                localizado = localizar_imagem(imagem, regiao, precisao)
                if localizado is not None:
                    # centro = pyautogui.center(localizado)
                    # pyautogui.doubleClick(centro.x, centro.y, button='left')
                    print("\n\nCaros jogadores, para garantir um ambiente de jogo mais estável e melhor, o servidor esta em "
                          "manutenção. Durante esse período, talvez voçê não consiga acessar o jogo. Pedimos desculpas "
                          "por qualquer inconveniente. E obrigado pelo seu apoio e compreensão!\n")

                    Google.escrever_IP_banido()
                    print("time 30s para todos os computadores escreverem o ip banido na planilha")
                    time.sleep(30)
                    print('manda trocar IP')
                    IP.ip_troca_agora()
                    print('origem da um f5 e espera 15 segundos ')
                    pyautogui.press('f5')
                    time.sleep(15)
                    continue


            # Espera x segundos antes da próxima tentativa
            #time.sleep(1)
            IP.f5_quando_internete_ocila(id, senha, url, navegador)
            entrou_corretamente, stataus = Seleniun.teste_logado(id, senha, url, navegador)

        if posicao is None:

            cont_erro += 1
            if cont_erro >= 2:
                # se tiverem algumasa tentativas fracaçadas troca o ip
                cont_erro = 0
                print('troca o IP para ver se entra')
                IP.ip_troca_agora()

            print("Não foi encontado a imagem de referencia para determinar a posição de origem")
            #Seleniun.atualizar_pagina(navegador, url)
            IP.tem_internet()
            print('origem da um f5 ')
            pyautogui.press('f5')
            time.sleep(15)

    return 0, 0, status_conta


def x_y(): # apenas para testes
    # # Define a região da tela onde a imagem será buscada
    # regiao_busca = (0, 115, 380, 230)  # (x, y, largura, altura)
    #
    # # Define o nome do arquivo da imagem a ser buscada
    # origem = r'Imagens\Origem.png'
    # # x_origem = None
    # # y_origem = None
    while True:
        posicao = None
        # Faz x buscas com um intervalo de x segundos entre cada busca
        print("Procurando coodenada 0 x 0...")
        for i in range(50):
            # Procura a imagem na região definida com 99,5% de tolerância, em escala de cinza e retorna a posição
            posicao = pyautogui.locateOnScreen(origem, region=regiao_busca, confidence=0.935, grayscale=True) #limite maximo de precisao é 0.997
            # Verifica se a imagem foi encontrada
            if posicao is not None:
                #print("Imagem encontrada na posição:", posicao)
                # Obtém as coordenadas x e o da imagem encontrada
                x_origem, y_origem = posicao.left, posicao.top
                x_origem = int(x_origem)
                y_origem = int(y_origem)
                # pyautogui.click(x_origem, y_origem ) #clica com mouse na origem so para ajudar a visualizar
                #print(f"Coordenadas origem: x={x_origem}, y={y_origem}")
                return x_origem, y_origem
            # Espera x segundos antes da próxima tentativa
            #time.sleep(1)


def x_y_aviso_sistema():

    print("Procurando aviso do sistema")
    for i in range(3):
        # Procura a imagem na região definida com 99,5% de tolerância, em escala de cinza e retorna a posição
        try:
            posicao = pyautogui.locateOnScreen(origem2, region=regiao_busca, confidence=0.993, grayscale=True) #limite maximo de precisao é 0.997
            # Verifica se a imagem foi encontrada
            if posicao is not None:
                #print("Imagem encontrada na posição:", posicao)
                # Obtém as coordenadas x e o da imagem encontrada
                x_origem, y_origem = posicao.left, posicao.top
                x_origem = int(x_origem)
                y_origem = int(y_origem)
                # pyautogui.click(x_origem, y_origem ) #clica com mouse na origem so para ajudar a visualizar
                #print(f"Coordenadas origem: x={x_origem}, y={y_origem}")
                return x_origem, y_origem
        except:
            print("Ocorreu um erro ao localizar a imagem")
            time.sleep(2)
            continue

    return None, None