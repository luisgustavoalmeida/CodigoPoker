import os
import socket
import time
import IP
import Google
import datetime

from selenium import webdriver
from bs4 import BeautifulSoup

import selenium.common.exceptions as sel_exceptions
import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
# Desabilitar o fail-safe
pyautogui.FAILSAFE = False

#def criar_drive():
servico = Service(ChromeDriverManager().install())  # criar um objeto Service com o caminho do webdriver
nome_computador = socket.gethostname()
nome_usuario = os.getlogin()
pasta_cookies = os.path.join(os.getcwd(), fr'C:\Cookie\{nome_usuario}')

options = Options()  # Criar um objeto 'Options' para definir as opções do Chrome
# options.add_argument("user-data-dir=C:\\Users\\lgagu\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1") # Você pode encontrar o caminho digitando "chrome://version/" na barra de endereço do Google Chrome e procurando o valo
options.add_argument('--disable-blink-features=AutomationControlled')  # desabilitam a detecção de automação no Chrome
options.add_argument("--disable-save-password-bubble")  #desabilitará a caixa de diálogo para salvar senhas do navegador
#options.add_argument("--disable-extensions")  # Desabilitar as extensões do Chrome
options.add_argument("--disable-infobars")  # Desabilitar a barra de informações do Chrome
options.add_argument("--disable-notifications")  # Desabilitar as notificações do Chrome
options.add_argument("--disable-save-password-bubble")  # Desabilitar a caixa de diálogo para salvar senhas
options.add_argument("--disable-password-generation")  # desabilita a geração automática de senhas pelo navegado
# options.add_argument('--disable-cookies')  # desabilita o envio de cookies durante a navegação.
# options.add_argument('--disable-first-party-cookies')  # Desativa o uso de cookies de primeira parte.
# options.add_argument('--disable-third-party-cookies') # Desativa o uso de cookies de terceiros.
# options.add_argument('--block-new-cookie-requests') # Bloqueia solicitações de criação de novos cookies.
#options.add_argument("--enable-cookies") # abilita o envio de cookies durante a navegação.
options.add_argument(f"--user-data-dir={pasta_cookies}")
#options.add_argument("--user-data-dir=/path/to/empty/folder") # Especifica um diretório vazio para a coleta de cookies. Isso permite que você utilize cookies pré-existentes ou salve os cookies gerados durante a execução do script.
options.add_argument("--disable-autofill")  # desabilitará o recurso de preenchimento automático de formulários do navegador.
options.add_argument("--disable-geolocation")  # desativar a funcionalidade de localização do navegador durante a execução do script Selenium
options.add_argument("--window-size=1380,1050")# Definir o tamanho da janela # largura altura options.add_argument("--window-size=1440,1045")
options.add_argument("--window-position=-8,-5")# Mover a janela para a posição (0,0) da tela
options.add_argument("--mute-audio") # desativar o áudio
#options.add_argument("--disable-gpu") # Desabilita o uso da GPU pelo navegador.
#options.add_argument("--disable-translate") # Desabilita a tradução automática de páginas pelo navegador

#options.add_argument("--disable-local-storage") # Desabilita o uso de armazenamento local pelo navegador. Isso inclui o armazenamento de dados em cache e outros recursos relacionados a cookies.
#options.add_argument("--disable-session-storage") # Desabilita o uso de armazenamento de sessão pelo navegador. Isso inclui o armazenamento temporário de dados relacionados a sessões de navegação.

options.add_experimental_option("detach", True) # para manter o navegador aberto

#options.add_argument("--headless")# faz com que o browser não abra durante o processo
# options.add_argument("--disable-popup-blocking")                            #desabilitar o bloqueio de pop-ups no Chrome. Quando o Selenium abre o navegador, por padrão, o bloqueio de pop-ups é habilitado
#options.add_experimental_option("excludeSwitches", ["enable-automation"])   # Adicionar uma opção experimental para desabilitar a mensagem "O Chrome está sendo controlado por um software de teste automatizado."
# options.add_experimental_option('useAutomationExtension', False)            # Adicionar uma opção experimental para desabilitar a extensão do WebDriver

#navegador = webdriver.Chrome(service=servico, options=options)  # Inicializar o driver do navegador
# print(navegador)


def cria_nevegador():
    print('Criando o navegador')
    navegador = webdriver.Chrome(service=servico, options=options)  # Inicializar o driver do navegador
    # Redefina o tempo limite para 10 segundos para a segunda parte do código
    navegador.set_page_load_timeout(60)
    return navegador
    # while True:
    #     try:
    #         navegador = webdriver.Chrome(service=servico, options=options)  # Inicializar o driver do navegador
    #         return navegador
    #     except Exception as e:
    #         print("Ocorreu um erro ao criar o navegador:")
    #         print(e)
    #         time.sleep(5)


def abrir_navegador(url, navegador):
    while True:
        print("abrir navegador")
        IP.tem_internet()
        try:
            navegador.get(url)
            return
        except Exception as e:
            print(f"Erro ao abrir o navegador: {e}")
            navegador.quit()
            time.sleep(10)
            continue


def se_esta_lagado(navegador):
    if navegador.get_cookie("c_user"):
        print("Está logado no Facebook.")
        return True
    else:
        print("Não está logado no Facebook.")
        return False


def pega_url(navegador, url):
    while True:
        IP.tem_internet()
        try:
            url_atual = navegador.current_url
            return url_atual
        except Exception as e:
            print("Erro ao obter o URL do navegador, erro: ", e)
            IP.tem_internet()
            print(" clica no atualizar a pagina, atualizar")
            # pyautogui.press('f5')
            # navegador.get(url)
            pyautogui.click(85, 60)
            time.sleep(15)


def teste_logado(id, senha, url, navegador):
    url_atual = pega_url(navegador, url)
    if ("/pokerbrasil?" in url_atual) or ("/rallyacespoker" in url_atual):
        # print("teste_logado ok")
        entrou = True
        status = 'Carregada'
        return entrou, status

    elif ("/pokerbrasil?" not in url_atual) or ("/rallyacespoker" in url_atual):  # se nao esta logado
        print("teste_logado deslogado")
        IP.tem_internet()
        entrou, status = fazer_login(id, senha, url, navegador)
        return entrou, status


def fazer_login(id, senha, url, navegador):
    while True:
        if se_esta_lagado(navegador) is True:
            sair_face(url, navegador)

        print("faz login")
        IP.tem_internet()
        print('continua login')
        url_atual = pega_url(navegador, url)

        if "/login/" in url_atual:

            try:
                email_field = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
                email_field.clear()
                email_field.send_keys(id)
                password_field = navegador.find_element(By.NAME, 'pass')
                password_field.clear()
                password_field.send_keys(senha)
                # fazer login clicando no botão de login
                login_button = navegador.find_element(By.NAME, 'login')
                login_button.click()
                for i in range(20):
                    time.sleep(1)
                    url_atual = pega_url(navegador, url)
                    #  print(url_atual)
                    if "/login/" not in url_atual:
                        if ("/pokerbrasil?" in url_atual) or ("/rallyacespoker" in url_atual):
                            # https://apps.facebook.com/pokerbrasil?vtype&amfmethod=appLinkFanPageAward&SignedParams=JrLALkSch1wuQxrULK6SWLAcpjTOb9Pmi5QvavvikU0.eyJhY3QiOiJmcCIsImZwX2FpZCI6IjU5ODUifQ&fbclid=IwAR252AFFL560939epg6Ki4tzNtLvgQJiZISVIZXFPjjBpBp5TNLBNX6TFXk
                            print("A conta está certa.")
                            entrou = True
                            status = 'Carregada'
                            return entrou, status

                        elif "/checkpoint/" in url_atual:
                            # https://www.facebook.com/checkpoint/1501092823525282/?next=https%3A%2F%2Fwww.facebook.com%2F%3Fsk%3Dwelcome

                            entrou = False
                            status = "Anomalia Fecebook"
                            print("A conta está suspensa.")
                            time.sleep(6)
                            lista_face_caidas = ['você recorreu da decisão',
                                                 'confirmar que é você',
                                                 'confirmar que és tu',
                                                 'Insira o número de celular',
                                                 'Insere o número de telemóvel',
                                                 'Carregue uma foto sua',
                                                 'Sua conta foi desativada',
                                                 'Sua conta foi suspensa',
                                                 'sua conta foi bloqueada',
                                                 'Suspendemos a tua conta',
                                                 'Desabilitamos sua conta',
                                                 'você apresentou um recurso',
                                                 'Confirme seu número de celular',
                                                 'precisamos confirmar que esta conta pertence a você']

                            for item in lista_face_caidas:
                                # percorre os textos que tem quando tem conta caida para o face
                                try:
                                    elemento = navegador.find_element(By.XPATH, f"//span[contains(text(), '{item}')]")
                                    print(item)
                                    status = item
                                    return entrou, status
                                except NoSuchElementException:
                                    continue
                            # se nao for algum item da lista retorna uma mensagem generica

                            elementos_para_clicar = ["Começar", "Avançar", "Avançar", "Avançar",
                                                     "Voltar para o Facebook"]
                            encontrou = False
                            for i in range(2):
                                for elemento in elementos_para_clicar:
                                    elemento_seletor = f'div[aria-label="{elemento}"]'
                                    print("procura: ", elemento)
                                    try:
                                        elemento_clicavel = WebDriverWait(navegador, 3).until(
                                            EC.element_to_be_clickable((By.CSS_SELECTOR, elemento_seletor)))
                                        elemento_clicavel.click()
                                        print("Clicou em: ", elemento)
                                        time.sleep(5)
                                        encontrou = True
                                    except Exception as e:  # Corrigido o erro aqui, "as e" ao invés de "e Exception:"
                                        print("Elememto para clicar não encontrado: ", elemento)
                                        continue
                            if encontrou:
                                time.sleep(3)
                                navegador.get(url)
                                time.sleep(5)
                            else:
                                return entrou, status

                        elif "/user_cookie_choice/" in url_atual:
                            # https://www.facebook.com/privacy/consent/user_cookie_choice/?source=pft_user_cookie_choice
                            print('responder cookies')

                            elemento_recusar = navegador.find_element(By.XPATH, f"//span[contains(text(), 'Recusar cookies opcionais')]")
                            if elemento_recusar:
                                elemento_recusar.click()
                                print('clicou')
                                time.sleep(5)
                                navegador.get(url)
                                time.sleep(5)
                            else:
                                status = "cookie"
                                entrou = False
                                return entrou, status

                        elif "/privacy/consent/pipa/" in url_atual:
                            # https://www.facebook.com/privacy/consent/pipa/?params%5Bpft_surface%5D=facebook_comet&params%5Bis_new_user_blocking_flow%5D=true&params%5Bpft_session_key%5D=afa5f865-6574-4376-9cb2-3349c7a3aed0&source=pipa_blocking_flow
                            print("Concorde com os itens")
                            entrou = False
                            status = "Concorde com os itens"
                            return entrou, status

                        elif "/privacy/" in url_atual:
                            #  https://www.facebook.com/privacy/consent/lgpd_migrated/?source=lgpd_blocking_flow
                            print("A conta termos de privacidade")
                            time.sleep(5)
                            lista_face = ['bloqueado temporariamente', 'concorde', 'temporariamente']
                            for item in lista_face: # percorre os textos que tem quando tem conta caida para o face
                                try:
                                    elemento = navegador.find_element(By.XPATH, f"//span[contains(text(), '{item}')]")
                                    print(item)
                                    status = item
                                    entrou = False
                                    return entrou, status
                                except NoSuchElementException:
                                    continue

                            # lista de elemento clicaveis
                            elementos_para_clicar = ["Começar", "Gerenciar configurações", "Salvar", "Continuar",
                                                     "Voltar para o Facebook", "Usar essa atividade",
                                                     "Usar essa atividade", "Fechar"]

                            for i in range(2):
                                for elemento in elementos_para_clicar:
                                    elemento_seletor = f'div[aria-label="{elemento}"]'
                                    print("procura: ", elemento)
                                    try:
                                        elemento_clicavel = WebDriverWait(navegador, 3).until(
                                            EC.element_to_be_clickable((By.CSS_SELECTOR, elemento_seletor)))
                                        elemento_clicavel.click()
                                    except Exception as e:  # Corrigido o erro aqui, "as e" ao invés de "e Exception:"
                                        print("Elememto para clicar não encontrado: ", elemento)
                                        print(e)
                                        continue

                            time.sleep(3)
                            navegador.get(url)
                            time.sleep(5)

                    elif ("/login/?privacy" in url_atual) or ("/device-based/regular/login/?" in url_atual):
                        print("senha incorreta")
                        print('manda sair')
                        sair_face(url, navegador)

                        entrou = False
                        status = "Senha incorreta"
                        return entrou, status

                    else:
                        lista_face = ['Você não pode usar este recurso no momento', 'Limitamos a frequência',
                                      'senha inserida está incorreta', 'Esqueceu a conta?', 'Tentar outra forma']
                        for item in lista_face:  # percorre os textos que tem quando tem conta caida para o face
                            try:
                                elemento = navegador.find_element(By.XPATH, f"//span[contains(text(), '{item}')]")
                                print(item)
                                status = item
                                entrou = False
                                return entrou, status
                            except NoSuchElementException:
                                continue

                print("Não carregou o poker")
                entrou = False
                status = "Não ok, outro"
                return entrou, status

            except Exception as e:

                print("Tempo limite excedido ao procurar o elemento faz_login.")
                print(e)
                sair_face(url, navegador)
                continue

        abrir_navegador(url, navegador)


def fechar_navegador(navegador):
    navegador.quit()


def sair_face(url, navegador):
    for i in range(10):

        print("sair do facebook")
        IP.tem_internet()
        script = """javascript:void(function(){ function deleteAllCookiesFromCurrentDomain() { var cookies = document.cookie.split("; "); for (var c = 0; c < cookies.length; c++) { var d = window.location.hostname.split("."); while (d.length > 0) { var cookieBase = encodeURIComponent(cookies[c].split(";")[0].split("=")[0]) + '=; expires=Thu, 01-Jan-1970 00:00:01 GMT; domain=' + d.join('.') + ' ;path='; var p = location.pathname.split('/'); document.cookie = cookieBase + '/'; while (p.length > 0) { document.cookie = cookieBase + p.join('/'); p.pop(); }; d.shift(); } } } deleteAllCookiesFromCurrentDomain(); location.href = '""" + url + """'; })();"""

        try:

            navegador.execute_script(script)
            WebDriverWait(navegador, 5).until(EC.presence_of_element_located((By.NAME, 'email')))
            return

        except Exception as e:

            print("ERRO ao executar o script sair ")
            print(e)
            # time.sleep(3)
            IP.tem_internet()
            print("Da um F5 e espera 3 segundos")
            # pyautogui.press('f5')
            navegador.get(url)
            # navegador.execute_script(script)
            time.sleep(3)
            # continue
            print("testa se tem nao é vc")

            try:

                # Esperar até que o elemento "Não é você?" seja clicável
                # elemento_nao_e_voce = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Não é você?"]')))
                elemento_nao_e_voce = WebDriverWait(navegador, 5).until(EC.element_to_be_clickable((By.ID, 'not_me_link')))

                # Clicar no elemento
                print('Clicar no elemento')
                elemento_nao_e_voce.click()
                print('espera 2s')
                time.sleep(2)

            except Exception as e:

                print("Elemento não encontrado na página.", e)


def atualizar_pagina(navegador, url):
    while True:
        IP.tem_internet()# testa se tem internete enste de atualizar a pagina
        try:
            navegador.get(url)
            return
        except Exception as e:
            print("Erro de conexão com a internet. Tentando novamente em 5 segundos...")
            print(e)
            time.sleep(10)
            continue


def busca_link(navegador):
    print('busca_link')

    if (nome_usuario == "PokerIP"): #and (nome_computador == "PC-I5-8600K"):
        id = "stefaniaalmeida.jf"
        senha = "$TE20091992te"
        # id = "Luis.gustavo.almeida88"
        # senha = "020996Pa"
        endereco_falha = 'F2'

    elif (nome_usuario == "lgagu"): #and (nome_computador == "PC-I7-9700KF"):
        id = "stefaniaalmeida.jf"
        senha = "$TE20091992te"
        endereco_falha = 'F3'

    elif (nome_usuario == "PokerIP"): #and (nome_computador == "PC-i3-8145U"):
        id = "carolina.fedoci"
        senha = "Lg1405lG"
        endereco_falha = 'F4'

    url = "https://pt-br.facebook.com/"

    navegador.get(url)

    time.sleep(3)

    if se_esta_lagado(navegador) is True:
        sair_face(url, navegador)

    print('faz login')
    email_field = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
    email_field.clear()
    email_field.send_keys(id)
    password_field = navegador.find_element(By.NAME, 'pass')
    password_field.clear()
    password_field.send_keys(senha)
    # fazer login clicando no botão de login
    login_button = navegador.find_element(By.NAME, 'login')
    login_button.click()

    print('fez login agurda 7 segundo para a paguna carregar')
    time.sleep(7)
    print('digita o endereço da fanpage')
    # Abrir a página do Facebook da qual você deseja obter a última postagem
    pagina_do_facebook = "https://www.facebook.com/people/Poker-Brasil/100064546038812/"
    navegador.get(pagina_do_facebook)
    print('agurade 7 segundas para a pagina carregar')
    time.sleep(7)

    print('rola')
    # Esperar um pouco para a rolagem ser concluída
    navegador.implicitly_wait(5)  # Aguarde por 5 segundos (ou o tempo que for necessário)

    try:
        # Encontrar todos os elementos de imagem na página
        elementos_imagem = navegador.find_elements(By.TAG_NAME, 'img')

    except TimeoutException:
        # Se ocorrer um TimeoutException, informe que a imagem não foi encontrada e escreva o erro no arquivo de dados
        print("Imagem não encontrada na página")
        Google.escrever_celula("Imagem não encontrada na página", 'Dados', endereco_falha)
        return

    # Procurar o primeiro link que começa com o padrão especificado
    teste_url = False
    try:
        # Iterar sobre os elementos de imagem e verificar se a URL começa com o padrão desejado
        for elemento in elementos_imagem:
            url_imagem = elemento.get_attribute('src')
            # print(url_imagem)
            # Verificar se a URL começa com o padrão especificado
            if url_imagem.startswith("https://external.fjdf2-2.fna.fbcdn.net/emg1"):
                print("\n\n URL válida: \n\n", url_imagem)
                # Se encontrar a URL válida, clicar no elemento e sair do loop
                elemento.click()
                print("\n\n Clicou na imagem correspondente \n\n ")
                teste_url = True
                break

    except Exception as e:
        # Se ocorrer uma exceção ao encontrar a URL, informar o erro e escrever no arquivo de dados
        print('Erro ao encontrar a URL:', str(e))
        Google.escrever_celula("Erro ao encontrar a URL", 'Dados', endereco_falha)
        return

    if not teste_url:
        print('url fora do padrao ou nao encontrada')
        #Google.escrever_celula('url fora do padrao ou nao encontrada', 'Dados', endereco_falha)
        pyautogui.click(670, 730)
        print('clique burro para tentar achar a imagem')
        #return

    time.sleep(5)

    # Obtém todos os identificadores de guias abertas
    guias_abertas = navegador.window_handles

    # Verifica o número de guias abertas
    if len(guias_abertas) == 2:

        print("Existem duas guias abertas, continua.")
        # Faça algo com as duas guias, se necessário
    else:
        print("Não existem duas guias abertas.")
        Google.escrever_celula('url fora do padrao ou nao encontrada a imagem com clique burro ', 'Dados', endereco_falha)

        guias_abertas = navegador.window_handles

        # Verifica se há mais de uma guia aberta
        if len(guias_abertas) > 1:
            # Fecha todas as guias adicionais, exceto a primeira
            for guia_id in guias_abertas[1:]:
                navegador.switch_to.window(guia_id)  # Alterna para a guia que será fechada
                navegador.close()  # Fecha a guia ativa

            # Após fechar as guias adicionais, volta para a primeira guia
            navegador.switch_to.window(guias_abertas[0])

            print("Apenas uma guia foi mantida aberta.")
        else:
            print("Apenas uma guia já está aberta.")
        return

    # Alterne o foco para a nova guia (segunda guia)
    navegador.switch_to.window(navegador.window_handles[1])
    time.sleep(5)
    # Pegar o link da barra de endereço do navegador
    link_da_barra_de_endereco = navegador.current_url
    # Feche a segunda guia
    navegador.close()
    # Volte para a primeira guia, se necessário
    navegador.switch_to.window(navegador.window_handles[0])
    # Verificar se a URL começa com o padrão desejado
    padrao_desejado = "https://apps.facebook.com/pokerbrasil?vtype=&amfmethod=appLinkFanPageAward&SignedParams="
    if link_da_barra_de_endereco.startswith(padrao_desejado):
        print("A URL começa com o padrão desejado.")
        print(link_da_barra_de_endereco)
        print('escreve o link')
        Google.escrever_celula(link_da_barra_de_endereco, 'Dados', 'F1')

        # Obtenha a data e hora atual
        data_hora_atual = str(datetime.datetime.now())
        print('escreve a data da atialização: ', data_hora_atual)
        if (nome_usuario == "PokerIP") and (nome_computador == "PC-I5-8600K"):
            Google.escrever_celula(data_hora_atual, 'Dados', endereco_falha)
        elif (nome_usuario == "lgagu") and (nome_computador == "PC-I7-9700KF"):
            Google.escrever_celula(data_hora_atual, 'Dados', endereco_falha)

        print('Link copiado com sucesso')
        time.sleep(5)
        return
    else:
        Google.escrever_celula("link fanpag fora do padrão", 'Dados', endereco_falha)
        print("link fanpag fora do padrão")


######################################################################################################################
# # para abrir o navegador e deixar abero. Descomentar as duas linhas abaixo
# navegador = cria_nevegador()
# busca_link(navegador)
#time.sleep(10000)


