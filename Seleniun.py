import os
import socket
import time
import IP
from selenium import webdriver
import selenium.common.exceptions as sel_exceptions
import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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
options.add_argument("--window-size=1440,1045")# Definir o tamanho da janela # largura altura
options.add_argument("--window-position=0,0")# Mover a janela para a posição (0,0) da tela
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
    while True:
        try:
            navegador = webdriver.Chrome(service=servico, options=options)  # Inicializar o driver do navegador
            return navegador
        except Exception as e:
            print("Ocorreu um erro ao criar o navegador:")
            print(e)
            time.sleep(5)


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

def teste_logado(id, senha, url, navegador):
    url_atual = navegador.current_url
    if "/pokerbrasil?" in url_atual: # se nao esta logado
        #print("teste_logado ok")
        entrou = True
        status = 'Carregada'
        return entrou, status

    elif "/pokerbrasil?" not in url_atual:  # se nao esta logado
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

        url_atual = navegador.current_url
        if "/login/" in url_atual:
            try:
                email_field = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.NAME, 'email')))
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
                    url_atual = navegador.current_url
                    #print(url_atual)

                    if "/login/" not in url_atual:
                        if "/pokerbrasil?" in url_atual:
                            #https://apps.facebook.com/pokerbrasil?vtype&amfmethod=appLinkFanPageAward&SignedParams=JrLALkSch1wuQxrULK6SWLAcpjTOb9Pmi5QvavvikU0.eyJhY3QiOiJmcCIsImZwX2FpZCI6IjU5ODUifQ&fbclid=IwAR252AFFL560939epg6Ki4tzNtLvgQJiZISVIZXFPjjBpBp5TNLBNX6TFXk
                            print("A conta está certa.")
                            entrou = True
                            status = 'Carregada'
                            return entrou, status

                        elif "/checkpoint/" in url_atual:
                            #https://www.facebook.com/checkpoint/1501092823525282/?next=https%3A%2F%2Fwww.facebook.com%2F%3Fsk%3Dwelcome
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
                                                 'Suspendemos a tua conta',
                                                 'Desabilitamos sua conta']

                            for item in lista_face_caidas: # percorre os textos que tem quando tem conta caida para o face
                                try:
                                    elemento = navegador.find_element(By.XPATH, f"//span[contains(text(), '{item}')]")
                                    print(item)
                                    status = item
                                    return entrou, status
                                except NoSuchElementException:
                                    continue
                            # se nao for algum item da lista retorna uma mensagem generica
                            return entrou, status

                        elif "/user_cookie_choice/" in url_atual:
                            #https://www.facebook.com/privacy/consent/user_cookie_choice/?source=pft_user_cookie_choice
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
                            #https://www.facebook.com/privacy/consent/pipa/?params%5Bpft_surface%5D=facebook_comet&params%5Bis_new_user_blocking_flow%5D=true&params%5Bpft_session_key%5D=afa5f865-6574-4376-9cb2-3349c7a3aed0&source=pipa_blocking_flow
                            print("Concorde com os itens")
                            entrou = False
                            status = "Concorde com os itens"
                            return entrou, status

                        elif "/privacy/" in url_atual:
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
                            #https://www.facebook.com/privacy/consent/lgpd_migrated/?source=lgpd_blocking_flow
                            elemento_comecar = WebDriverWait(navegador, 5).until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Começar"]')))
                            elemento_comecar.click()

                            elemento_gerenciar = WebDriverWait(navegador, 5).until(EC.element_to_be_clickable(
                                (By.CSS_SELECTOR, 'div[aria-label="Gerenciar configurações"]')))
                            elemento_gerenciar.click()

                            elemento_salvar = WebDriverWait(navegador, 5).until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Salvar"]')))
                            elemento_salvar.click()

                            elemento_continuar = WebDriverWait(navegador, 5).until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Continuar"]')))
                            elemento_continuar.click()

                            elemento_fechar = WebDriverWait(navegador, 5).until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Fechar"]')))
                            elemento_fechar.click()
                            time.sleep(3)
                            navegador.get(url)
                            time.sleep(5)

                    elif "/device-based/regular/login/?" in url_atual:
                        print("senha incorreta")
                        entrou = False
                        status = "senha incorreta"
                        return entrou, status

                    else:
                        lista_face = ['Você não pode usar este recurso no momento', 'Limitamos a frequência',
                                      'senha inserida está incorreta', 'Esqueceu a conta?','Tentar outra forma']
                        for item in lista_face:  # percorre os textos que tem quando tem conta caida para o face
                            try:
                                elemento = navegador.find_element(By.XPATH, f"//span[contains(text(), '{item}')]")
                                print(item)
                                status = item
                                entrou = False
                                return entrou, status
                            except NoSuchElementException:
                                continue
                #else:
                print("Não carregou o poker")
                entrou = False
                status = "não ok, outro"
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
            time.sleep(3)
            IP.tem_internet()
            print("Da um F5 e espera 3 segundos")
            pyautogui.press('f5')
            # navegador.execute_script(script)
            time.sleep(3)
            continue
        #print('testa se esta visivel o login senha')
        # try:
        #     WebDriverWait(navegador, 3).until(EC.presence_of_element_located((By.NAME, 'email')))
        #     return
        # except Exception as e:
        #     print("Tempo limite excedido tentar sair novamente ")
        #     print(e)
        #     time.sleep(3)
        #     IP.tem_internet()
        #     continue

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



#navegador = cria_nevegador()
# #
#abrir_navegador(url, navegador)
# usuario = 'lga.gustavo.a@gmail.com'
# senha = '020996Pa'
# fazer_login(usuario, senha, url, navegador)
#time.sleep(10000)
# navegador.quit()

######################################################################################################################
## para abrir o navegador e deixar abero. Descomentar as duas linhas abaixo
#navegador = cria_nevegador()
#time.sleep(10000)


