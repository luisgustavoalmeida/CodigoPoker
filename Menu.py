import Aneis
import Google
import Seleniun
import Origem_pg
import OCR_tela
import Roletas
import Limpa
import IP
import HoraT
import Tarefas
import datetime
import time
import Mesa
import Cartas
import Slot
import Genius
import pyautogui
import datetime
import os
import socket

import threading

from Variaveis_Globais import aviso_sistema_global, alterar_global_aviso_sistema

global aviso_sistema_global


# Obter o nome de usuário
nome_usuario = os.getlogin()
# Obter o nome do computador
nome_computador = socket.gethostname()
LIMITE_IP = 5
if nome_usuario == "PokerIP":  # teste se o usuario do computador é o que troca IP se nao for fica esperando esta livre
    LIMITE_IP = 5
elif (nome_usuario == "lgagu") and (nome_computador == "PC-I7-9700KF"):
    LIMITE_IP = 5
else:
    LIMITE_IP = 4

print("limite de troca de IP: ", LIMITE_IP)

id = "x"
senha = ""
linha = ""
cont_IP = 10
guia = ""
guia_recebida = ""

ja_fez_tutorial = True

# Variáveis globais para as variáveis e controle da tarefa independente
id_novo = "x"
senha_novo = ""
linha_novo = ""
cont_IP_novo = ""
continuar_tarefa = False

# Semaphore para iniciar a tarefa independente
iniciar_tarefa = threading.Semaphore(0)
# Semaphore para a tarefa independente indicar que terminou e aguardar novo comando
tarefa_concluida = threading.Semaphore(0)

# Função que será executada na tarefa independente
def tarefa_independente():
    global continuar_tarefa
    global guia
    global id_novo
    global senha_novo
    global linha_novo
    global cont_IP_novo

    while True:
        # Aguardar o comando para iniciar a execução
        iniciar_tarefa.acquire()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        # Verificar se a tarefa deve continuar executando ou parar
        if continuar_tarefa:
            print("Executando tarefa independente...")

            # Atualizar as variáveis
            id_novo, senha_novo, linha_novo, cont_IP_novo = Google.credenciais(guia)  # pega id e senha para o proximo login
            continuar_tarefa = False

            # Indicar que a tarefa terminou e está pronta para aguardar novo comando
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            tarefa_concluida.release()
        else:
            print("&&&&&&&&     &&&&&&&&     Tarefa independente parada.     &&&&&&&&     &&&&&&&&")
            # Indicar que a tarefa terminou de executar
            tarefa_concluida.release()

# Iniciar a execução da tarefa independente
tarefa = threading.Thread(target=tarefa_independente)
tarefa.start()

url = str(Google.pega_valor('Dados', 'F1'))

navegador = Seleniun.cria_nevegador()
Seleniun.abrir_navegador(url, navegador)
while True:
    alterar_global_aviso_sistema(False)

    guia = HoraT.mudar_guia(id, guia)

    url = str(Google.pega_valor('Dados', 'F1'))

    print("guia:", guia)
    if id == id_novo or id == "":
        id, senha, linha, cont_IP = Google.credenciais(guia)

        if id == "":
            Seleniun.sair_face(url, navegador)
            guia = HoraT.mudar_guia(id, guia)
            id, senha, linha, cont_IP = Google.credenciais(guia)

    else:
        id, senha, linha, cont_IP = id_novo, senha_novo, linha_novo, cont_IP_novo


    dia_da_semana = int(datetime.datetime.now().weekday()) # busca o dia da semana 0 segunda 1 terça ... 6 domeingo

    #login
    while True:
        #parte deo codigo que faz loguin
        ip, com_internet = IP.meu_ip()  # obtem meu endereço de IP
        valor_fichas = ""
        pontuacao_tarefas = ""
        hora_atual = ""
        status_poker = None
        valores = [""]
        roda = True
        entrou_corretamente = True
        stataus_facebook = 'Carregada'
        hora_fim_tarefa = False

        while roda:

            if cont_IP >= LIMITE_IP or cont_IP < 0:  # se a contagem de ip ta fora da faixa vai para a função
                IP.ip(LIMITE_IP)  # testa se o numero de contas esta dentro do limite antes de trocar ip
            print('____________________ manda iniciar a tarefa independete_________________')
            # Comando para iniciar a tarefa independente
            continuar_tarefa = True
            iniciar_tarefa.release()

            entrou_corretamente, stataus_facebook = Seleniun.fazer_login(id, senha, url, navegador)
            if entrou_corretamente is False:  # se nao entrou no face
                print("conta nao entou no Facebook")
                #Google.marca_caida(stataus_facebook, guia, linha)
                break

            while True:

                if entrou_corretamente is True:
                    x_origem, y_origem, status_poker = Origem_pg.carregado_origem(id, senha, url, navegador)
                    print(status_poker)
                    if status_poker is not None:
                        break

                entrou_corretamente, stataus_facebook = Seleniun.teste_logado(id, senha, url, navegador)
                if entrou_corretamente is False:  # se nao entrou no face
                    print("conta nao entou no Facebook")
                    #Google.marca_caida(stataus_facebook, guia, linha)
                    break

            if entrou_corretamente is False:  # se nao entrou no face
                #Google.marca_caida(stataus_facebook, guia, linha)
                break

            ja_fez_tutorial = True

            if status_poker != 'Carregada':  # testa status da conta
                if status_poker == 'Banida':  # se aconta esta banida
                    print("conta banida tem que marcar na plinilha")
                    #Google.marca_banida("Banida", guia, linha)
                    break

                elif status_poker == 'Tutorial':
                    ja_fez_tutorial = False
                    print('vai fazer tutorial')
                    entrou_corretamente, stataus_facebook = Seleniun.teste_logado(id, senha, url, navegador)
                    if entrou_corretamente is False:  # se nao entrou no face
                        #Google.marca_caida(stataus_facebook, guia, linha)
                        break
                    time.sleep(2)
                    if Limpa.limpa_pequeno(x_origem, y_origem) == "sair da conta":
                        break
                    Limpa.faz_tutorial(x_origem, y_origem)
                    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                        break

                elif status_poker == 'Atualizar':
                    break

            entrou_corretamente, stataus_facebook = Seleniun.teste_logado(id, senha, url, navegador)
            if entrou_corretamente is False:  # se nao entrou no face
                #Google.marca_caida(stataus_facebook, guia, linha)
                break

            if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                break

            ###########Roletas
            if guia != "T1":

                if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                    break

                valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem)

                roleta, hora_que_rodou, time_rodou = Roletas.roletas(x_origem, y_origem, id, senha, url, navegador)
                print("roleta: ", roleta)

                if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                    break

                if ja_fez_tutorial: # so entra se a conta ja é velha
                    ## para pegar os pontos das tarefas
                    if roleta == 'roleta_1': # saber se roleta R1

                        print("dia da semana", dia_da_semana)

                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador) #retorna se a conta ta upada ou nao
                        if conta_upada:
                            IP.f5_quando_internete_ocila(id, senha, url, navegador)
                            entrou_corretamente, stataus_facebook = Seleniun.teste_logado(id, senha, url, navegador)
                            if not entrou_corretamente:  # se nao entrou no face
                                #Google.marca_caida(stataus_facebook, guia, linha)
                                break
                            pontuacao_tarefas = OCR_tela.pontuacao_tarefas(x_origem, y_origem)
                            Limpa.fecha_tarefa(x_origem, y_origem)

                entrou_corretamente, stataus_facebook = Seleniun.teste_logado(id, senha, url, navegador)
                if entrou_corretamente is False:  # se nao entrou no face
                    #Google.marca_caida(stataus_facebook, guia, linha)
                    break

                if hora_que_rodou is None:
                    hora_que_rodou = datetime.datetime.now().strftime('%H:%M:%S')

                if roleta == 'roleta_1': # saber se roleta R1 ja terminou de rodar para sair da conta
                    for i in range(50):
                        time_sair = time.perf_counter()
                        tempo_total = time_sair - time_rodou
                        print('tempo que ja clicou no rodou: ', tempo_total)
                        if tempo_total >= 12:
                            print('ja pode sair do r1')
                            break

                        time.sleep(0.3)
                        pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone da roleta para abir
                        if pyautogui.pixelMatchesColor((x_origem + 495), (y_origem + 315), (227, 120, 14), tolerance=20):  # testa de roleta 1 ta aberta
                            pyautogui.doubleClick(x_origem + 492, y_origem + 383)  # clica no meio da roleta para rodar
                    Mesa.dia_de_jogar_mesa(x_origem, y_origem, dia_da_semana, valor_fichas, time_rodou, roleta)

                elif roleta == 'roleta_2':
                    for i in range(20):
                        pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone roleta, ja roda sozinho
                        time_sair = time.perf_counter()
                        tempo_total = time_sair - time_rodou
                        print('tempo que ja clicou no rodou',tempo_total)
                        if tempo_total >= 0.5:
                            print('ja pode sair do r2')
                            break
                        time.sleep(0.3)
                        #pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone roleta, ja roda sozinho
                    #Mesa.dia_de_jogar_mesa(x_origem, y_origem, dia_da_semana, valor_fichas, time_rodou, roleta)

                valores = [valor_fichas, pontuacao_tarefas, hora_que_rodou, ip]
                roda = False
                break

            #######################Tarefas
            elif guia == "T1":
                lista_tarefas_fazer = []
                for i in range(2):
                    print('\n TAREFAS \n')

                    if HoraT.fim_tempo_tarefa():
                        break
                    if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                        break
                    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                        break


                    for i in range(2):

                        if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                            break

                        Aneis.recolhe_aneis(x_origem, y_origem)

                        print('\n\n procurando tarefas...\n\n')
                        valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem)
                        print("Valor da fichas: ", valor_fichas)
                        if valor_fichas < 40000: # se a conta tem menos de 110K vai para a proxima
                            print('quantidade de fichas insuficiente para jogar')
                            break

                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)  # retorna se a conta ta upada ou nao
                        print("Conta upada: ", conta_upada)
                        if conta_upada is False: # se a conta nao esta upada passa par a proxima
                            break

                        Tarefas.recolher_tarefa(x_origem, y_origem)  # recolhe se tiver alguma tarefa batida
                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)
                        meta_atingida, pontuacao_tarefas = Tarefas.meta_tarefas(x_origem, y_origem)
                        print("Meta atigida :", meta_atingida)
                        if meta_atingida or (conta_upada is False) or (valor_fichas < 40000): # se a meta ja foi atingida vai para a proxima
                            break

                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)  # retorna se a conta ta upada ou nao
                        OCR_tela.tarefas_diaris_trocar(x_origem, y_origem)
                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)  # retorna se a conta ta upada ou nao
                        meta_atingida, pontuacao_tarefas = Tarefas.meta_tarefas(x_origem, y_origem)
                        lista_tarefas_fazer, pontos_disponiveis = Tarefas.comparar_listas(x_origem, y_origem, dia_da_semana)
                        print('numero de tarefas para serem feitos: ', len(lista_tarefas_fazer))
                        print('lista de tarefas para se fazer: ', lista_tarefas_fazer)
                        if lista_tarefas_fazer:
                            print("\n\n Não há tarefas para serem feitas\n\n")
                            break

                        if dia_da_semana == 5: # testa se é sabado ultimo dia das tarefas
                            if ((pontuacao_tarefas + pontos_disponiveis) < 150) and (pontuacao_tarefas < 150):
                                print('\n\nA soma dos pontos disponiveis e os pontos feitos não atigem 200, o máximo que pode atingir é:', pontuacao_tarefas + pontos_disponiveis)
                                break
                            if ((pontuacao_tarefas + pontos_disponiveis) < 200) and (pontuacao_tarefas >= 150):
                                print('\n\nA soma dos pontos disponiveis e os pontos feitos não atigem 200, o máximo que pode atingir é:', pontuacao_tarefas + pontos_disponiveis)
                                break

                        if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                            break
                        time.sleep(2)
                        if Limpa.limpa_total(x_origem, y_origem):
                            break

                    if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                        break

                    if HoraT.fim_tempo_tarefa():
                        Limpa.limpa_total(x_origem, y_origem)
                        break

                    if (len(lista_tarefas_fazer) <= 0) or meta_atingida or (valor_fichas < 40000):
                        break

                    ##### se tem alguma tarefa para ser feita vai começar deste ponto
                    elif 'Jogar o caca-niquel da mesa 150 vezes' in lista_tarefas_fazer\
                            or 'Jogar o caca-niquel da mesa 70 vezes' in lista_tarefas_fazer\
                            or 'Jogar o caca-niquel da mesa 10 vezes' in lista_tarefas_fazer:

                        print('jogar mesa')
                        time.sleep(1)
                        print("\n\n Faz as tarefas... \n\n")
                        Mesa.joga(x_origem, y_origem, id, senha, url, navegador)
                        time.sleep(1)

                        if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                            break
                        Aneis.recolhe_aneis(x_origem, y_origem)
                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)  # retorna se a conta ta upada ou nao
                        Tarefas.recolher_tarefa(x_origem, y_origem)  # recolhe se tiver alguma tarefa batida
                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)
                        meta_atingida, pontuacao_tarefas = Tarefas.meta_tarefas(x_origem, y_origem)
                        lista_tarefas_fazer, pontos_disponiveis = Tarefas.comparar_listas(x_origem, y_origem, dia_da_semana)

                    if HoraT.fim_tempo_tarefa():
                        Limpa.limpa_total(x_origem, y_origem)
                        break
                    if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                        break
                    if (len(lista_tarefas_fazer) <= 0) or meta_atingida or (valor_fichas < 40000):
                        break
                    if dia_da_semana == 5:  # testa se é sabado ultimo dia das tarefas
                        if ((pontuacao_tarefas + pontos_disponiveis) < 150) and (pontuacao_tarefas < 150):
                            print(
                                '\n\nA soma dos pontos disponiveis e os pontos feitos não atigem 200, o máximo que pode atingir é:',
                                pontuacao_tarefas + pontos_disponiveis)
                            break
                        if ((pontuacao_tarefas + pontos_disponiveis) < 200) and (pontuacao_tarefas >= 150):
                            print(
                                '\n\nA soma dos pontos disponiveis e os pontos feitos não atigem 200, o máximo que pode atingir é:',
                                pontuacao_tarefas + pontos_disponiveis)
                            break
                    elif 'Jogar 100 vezes nas Cartas Premiadas' in lista_tarefas_fazer\
                            or 'Jogar 50 vezes nas Cartas Premiadas' in lista_tarefas_fazer\
                            or 'Jogar 10 vezes nas Cartas Premiadas' in lista_tarefas_fazer:
                        print('jogar cartas premidas vezes')

                        print("\n\n Faz Cartas premiadas vezes... \n\n")
                        Cartas.cartas_premidas_joga_vezes(x_origem, y_origem, id, senha, url, navegador)

                        if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                            break
                        Aneis.recolhe_aneis(x_origem, y_origem)
                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)  # retorna se a conta ta upada ou nao
                        Tarefas.recolher_tarefa(x_origem, y_origem)  # recolhe se tiver alguma tarefa batida
                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)
                        meta_atingida, pontuacao_tarefas = Tarefas.meta_tarefas(x_origem, y_origem)
                        lista_tarefas_fazer, pontos_disponiveis = Tarefas.comparar_listas(x_origem, y_origem, dia_da_semana)

                    if HoraT.fim_tempo_tarefa():
                        Limpa.limpa_total(x_origem, y_origem)
                        break
                    if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                        break
                    if (len(lista_tarefas_fazer) <= 0) or meta_atingida or (valor_fichas < 40000):
                        break
                    if dia_da_semana == 5:  # testa se é sabado ultimo dia das tarefas
                        if ((pontuacao_tarefas + pontos_disponiveis) < 150) and (pontuacao_tarefas < 150):
                            print(
                                '\n\nA soma dos pontos disponiveis e os pontos feitos não atigem 200, o máximo que pode atingir é:',
                                pontuacao_tarefas + pontos_disponiveis)
                            break
                        if ((pontuacao_tarefas + pontos_disponiveis) < 200) and (pontuacao_tarefas >= 150):
                            print(
                                '\n\nA soma dos pontos disponiveis e os pontos feitos não atigem 200, o máximo que pode atingir é:',
                                pontuacao_tarefas + pontos_disponiveis)
                            break
                    elif 'Ganhar 100.000 fichas nas Cartas Premiadas' in lista_tarefas_fazer \
                            or 'Ganhar 30.000 fichas nas Cartas Premiadas' in lista_tarefas_fazer \
                            or 'Ganhar 4.000 fichas nas Cartas Premiadas' in lista_tarefas_fazer:
                        print('jogar cartas preimiadas valor')

                        print("\n\n Faz Cartas premiadas valor... \n\n")
                        Cartas.cartas_premidas_joga_valor(x_origem, y_origem, id, senha, url, navegador, lista_tarefas_fazer, valor_fichas)

                        if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                            break
                        Aneis.recolhe_aneis(x_origem, y_origem)
                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)  # retorna se a conta ta upada ou nao
                        Tarefas.recolher_tarefa(x_origem, y_origem)  # recolhe se tiver alguma tarefa batida
                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)
                        meta_atingida, pontuacao_tarefas = Tarefas.meta_tarefas(x_origem, y_origem)
                        lista_tarefas_fazer, pontos_disponiveis = Tarefas.comparar_listas(x_origem, y_origem, dia_da_semana)

                    if HoraT.fim_tempo_tarefa():
                        Limpa.limpa_total(x_origem, y_origem)
                        break
                    if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                        break
                    if (len(lista_tarefas_fazer) <= 0) or meta_atingida or (valor_fichas < 40000):
                        break
                    if dia_da_semana == 5:  # testa se é sabado ultimo dia das tarefas
                        if ((pontuacao_tarefas + pontos_disponiveis) < 150) and (pontuacao_tarefas < 150):
                            print(
                                '\n\nA soma dos pontos disponiveis e os pontos feitos não atigem 200, o máximo que pode atingir é:',
                                pontuacao_tarefas + pontos_disponiveis)
                            break
                        if ((pontuacao_tarefas + pontos_disponiveis) < 200) and (pontuacao_tarefas >= 150):
                            print(
                                '\n\nA soma dos pontos disponiveis e os pontos feitos não atigem 200, o máximo que pode atingir é:',
                                pontuacao_tarefas + pontos_disponiveis)
                            break
                    elif 'Jogar no Casino Genius Pro 100 vezes' in lista_tarefas_fazer\
                            or 'Jogar no Casino Genius Pro 50 vezes' in lista_tarefas_fazer\
                            or 'Jogar no Casino Genius Pro 10 vezes' in lista_tarefas_fazer:
                        print('Jogar Casino genius vezes')

                        print("\n\n Faz as Genius vezes... \n\n")
                        Genius.genius_joga_vezes(x_origem, y_origem, id, senha, url, navegador)

                        if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                            break
                        Aneis.recolhe_aneis(x_origem, y_origem)
                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)  # retorna se a conta ta upada ou nao
                        Tarefas.recolher_tarefa(x_origem, y_origem)  # recolhe se tiver alguma tarefa batida
                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)
                        meta_atingida, pontuacao_tarefas = Tarefas.meta_tarefas(x_origem, y_origem)
                        lista_tarefas_fazer, pontos_disponiveis = Tarefas.comparar_listas(x_origem, y_origem, dia_da_semana)

                    if HoraT.fim_tempo_tarefa():
                        Limpa.limpa_total(x_origem, y_origem)
                        break
                    if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                        break
                    if (len(lista_tarefas_fazer) <= 0) or meta_atingida or (valor_fichas < 40000):
                        break
                    if dia_da_semana == 5:  # testa se é sabado ultimo dia das tarefas
                        if ((pontuacao_tarefas + pontos_disponiveis) < 150) and (pontuacao_tarefas < 150):
                            print(
                                '\n\nA soma dos pontos disponiveis e os pontos feitos não atigem 200, o máximo que pode atingir é:',
                                pontuacao_tarefas + pontos_disponiveis)
                            break
                        if ((pontuacao_tarefas + pontos_disponiveis) < 200) and (pontuacao_tarefas >= 150):
                            print(
                                '\n\nA soma dos pontos disponiveis e os pontos feitos não atigem 200, o máximo que pode atingir é:',
                                pontuacao_tarefas + pontos_disponiveis)
                            break
                    elif 'Ganhar 100.000 fichas no Casino Genius Pro' in lista_tarefas_fazer \
                            or 'Ganhar 30.000 fichas no Casino Genius Pro' in lista_tarefas_fazer \
                            or 'Ganhar 4.000 fichas no Casino Genius Pro' in lista_tarefas_fazer:
                        print('Jogar Casino genius valor')

                        print("\n\n Faz Genius valor... \n\n")
                        Genius.genius_joga_valor(x_origem, y_origem, id, senha, url, navegador, lista_tarefas_fazer)

                        if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                            break
                        Aneis.recolhe_aneis(x_origem, y_origem)
                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)  # retorna se a conta ta upada ou nao
                        Tarefas.recolher_tarefa(x_origem, y_origem)  # recolhe se tiver alguma tarefa batida
                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)
                        meta_atingida, pontuacao_tarefas = Tarefas.meta_tarefas(x_origem, y_origem)
                        lista_tarefas_fazer, pontos_disponiveis = Tarefas.comparar_listas(x_origem, y_origem, dia_da_semana)

                    if HoraT.fim_tempo_tarefa():
                        Limpa.limpa_total(x_origem, y_origem)
                        break
                    if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                        break
                    if (len(lista_tarefas_fazer) <= 0) or meta_atingida or (conta_upada is False) or (valor_fichas < 40000):
                        break
                    if dia_da_semana == 5:  # testa se é sabado ultimo dia das tarefas
                        if ((pontuacao_tarefas + pontos_disponiveis) < 150) and (pontuacao_tarefas < 150):
                            print(
                                '\n\nA soma dos pontos disponiveis e os pontos feitos não atigem 200, o máximo que pode atingir é:',
                                pontuacao_tarefas + pontos_disponiveis)
                            break
                        if ((pontuacao_tarefas + pontos_disponiveis) < 200) and (pontuacao_tarefas >= 150):
                            print(
                                '\n\nA soma dos pontos disponiveis e os pontos feitos não atigem 200, o máximo que pode atingir é:',
                                pontuacao_tarefas + pontos_disponiveis)
                            break
                    elif 'Apostar 20 fichas ou mais em 9 linhas do caca' in lista_tarefas_fazer\
                            or 'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 150 vezes' in lista_tarefas_fazer\
                            or 'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 70 vezes' in lista_tarefas_fazer\
                            or 'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 10 vezes' in lista_tarefas_fazer:

                        print('jogar caça niquel poker slote')

                        print("\n\n Faz Slote... \n\n")
                        Slot.solot_joga_vezes(x_origem, y_origem, id, senha, url, navegador)

                if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                    print('ja esta logado sai')
                else:
                    Aneis.recolhe_aneis(x_origem, y_origem)

                    if HoraT.fim_tempo_tarefa():
                        hora_fim_tarefa = True
                    else:
                        hora_fim_tarefa = False
                        valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem)
                        hora_que_rodou = datetime.datetime.now().strftime('%H:%M:%S')
                        conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)  # retorna se a conta ta upada ou nao
                        if conta_upada:
                            meta_atingida, pontuacao_tarefas = Tarefas.meta_tarefas(x_origem, y_origem)
                            pontuacao_tarefas = OCR_tela.pontuacao_tarefas(x_origem, y_origem)
                        valores = [valor_fichas, pontuacao_tarefas, hora_que_rodou, ip]
                roda = False
                break

        Seleniun.sair_face(url, navegador)

        print('-----------------espera terminar tarefa independente----------------')
        # Aguardar a tarefa terminar
        tarefa_concluida.acquire()

        print('tarefa independente liberada')

        while True:
            if not continuar_tarefa:
                break
            time.sleep(0.3)

        print('tarefa independente terminada')

        if entrou_corretamente is False:  # se nao entrou no face

            print("Conta não entou, o Statos é: ", stataus_facebook)
            Google.marca_caida(stataus_facebook, guia, linha)
            id, senha, linha, cont_IP = id_novo, senha_novo, linha_novo, cont_IP_novo

        elif status_poker == 'Banida':
            print("Conta não entou, o Statos é: ", status_poker)
            Google.marca_caida(status_poker, guia, linha)
            id, senha, linha, cont_IP = id_novo, senha_novo, linha_novo, cont_IP_novo

        elif status_poker == 'Atualizar':
            print("Conta não entou, o Statos é: ", status_poker)
            id, senha, linha, cont_IP = id_novo, senha_novo, linha_novo, cont_IP_novo

        elif entrou_corretamente is True:  # se nao entrou no face

            if hora_fim_tarefa is True:
                #  apaga os valore quando da a hoara de sair do tarefas
                Google.apagar_numerodo_pc(valores, guia, linha)  # apaga o nume do pc
                Google.apagar_numerodo_pc(valores, guia, linha_novo)  # apaga o nume do pc
            else:
                # escre os valores na planilha
                Google.escrever_valores_lote(valores, guia, linha)  # escreve as informaçoes na planilha apartir da coluna E
                id, senha, linha, cont_IP = id_novo, senha_novo, linha_novo, cont_IP_novo

        guia_recebida = HoraT.mudar_guia(id, guia)
        if guia != guia_recebida:
            dia_da_semana = datetime.datetime.now().weekday()  # busca o dia da semana 0 segunda 1 terça ... 6 domeingo
            url = str(Google.pega_valor('Dados', 'F1'))
            guia = guia_recebida
            id, senha, linha, cont_IP = Google.credenciais(guia)  # pega id e senha par o proximo login
        guia = guia_recebida

