
import Firebase
print(Firebase.comando_escravo)


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
LIMITE_IP = 6


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
        #ip, com_internet = IP.meu_ip()  # obtem meu endereço de IP
        ip = ""
        hora_que_rodou = 0
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
            #if cont_IP >= LIMITE_IP or cont_IP < 0:  # se a contagem de ip ta fora da faixa vai para a função
            IP.ip(LIMITE_IP)  # testa se o numero de contas esta dentro do limite antes de trocar ip

            entrou_corretamente, stataus_facebook = Seleniun.fazer_login(id, senha, url, navegador)

            print('____________________ manda iniciar a tarefa independete_________________')
            # Comando para iniciar a tarefa independente
            continuar_tarefa = True
            iniciar_tarefa.release()

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

            #######################Tarefas
            if guia == "T1":

                pontos_disponiveis = 200
                pontuacao_tarefas = 0
                meta_atingida = False
                conta_upad = True
                valor_fichas = 0
                parar_tarefas = False
                lista_tarefas_fazer = []

                if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                    parar_tarefas = True
                    break
                if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                    parar_tarefas = True
                    break

                for j in range(2):
                    print('procura tarefa, tentativa:', j)
                    for i in range(3):
                        print('\n TAREFAS \n')


                        (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas, lista_tarefas_fazer,
                         pontos_disponiveis, hora_fim_tarefa) \
                            = (Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, id, senha, url, navegador,
                                                                      dia_da_semana))
                        time.sleep(2)

                        if parar_tarefas:
                            print('Fim das tarefas')
                            time.sleep(2)
                            break

                        print("--------------parte 1---------------")

                        if ('Jogar o caca-niquel da mesa' in lista_tarefas_fazer
                                or 'Jogar o caca-niquel da mesa 150 vezes' in lista_tarefas_fazer
                                or 'Jogar o caca-niquel da mesa 70 vezes' in lista_tarefas_fazer
                                or 'Jogar o caca-niquel da mesa 10 vezes' in lista_tarefas_fazer):

                            print("\n\n Jogar o caca-niquel da mesa vezes \n\n")

                            Mesa.joga(x_origem, y_origem, id, senha, url, navegador, 200)
                            time.sleep(1)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas,
                             lista_tarefas_fazer, pontos_disponiveis, hora_fim_tarefa) \
                                = Tarefas.testa_continuar_fazendo_tarefa(x_origem,y_origem, id, senha,
                                                                         url, navegador, dia_da_semana)
                        print("--------------parte 2---------------")
                        if parar_tarefas:
                            break

                        if ('vezes nas Cartas Premiadas' in lista_tarefas_fazer
                                or 'Jogar 100 vezes nas Cartas Premiadas' in lista_tarefas_fazer
                                or 'Jogar 50 vezes nas Cartas Premiadas' in lista_tarefas_fazer
                                or 'Jogar 10 vezes nas Cartas Premiadas' in lista_tarefas_fazer):

                            print("\n\n Jogar vezes nas Cartas Premiadas \n\n")
                            Cartas.cartas_premidas_joga_vezes(x_origem, y_origem, id, senha, url, navegador)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas,
                             lista_tarefas_fazer, pontos_disponiveis, hora_fim_tarefa) \
                                = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, id, senha,
                                                                         url, navegador, dia_da_semana)
                        print("--------------parte 3---------------")
                        if parar_tarefas:
                            break

                        if ('fichas nas Cartas Premiadas' in lista_tarefas_fazer
                                or 'Ganhar 100.000 fichas nas Cartas Premiadas' in lista_tarefas_fazer
                                or 'Ganhar 30.000 fichas nas Cartas Premiadas' in lista_tarefas_fazer
                                or 'Ganhar 4.000 fichas nas Cartas Premiadas' in lista_tarefas_fazer):

                            print("\n\n Ganhar fichas nas Cartas Premiadas \n\n")
                            Cartas.cartas_premidas_joga_valor(x_origem, y_origem, id, senha, url, navegador,
                                                              lista_tarefas_fazer, valor_fichas)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas,
                             lista_tarefas_fazer, pontos_disponiveis, hora_fim_tarefa) \
                                = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, id, senha,
                                                                         url, navegador, dia_da_semana)

                        if parar_tarefas:
                            break

                        if ('Jogar no Casino Genius Pro' in lista_tarefas_fazer
                                or 'Jogar no Casino Genius Pro 100 vezes' in lista_tarefas_fazer
                                or 'Jogar no Casino Genius Pro 50 vezes' in lista_tarefas_fazer
                                or 'Jogar no Casino Genius Pro 10 vezes' in lista_tarefas_fazer):

                            print("\n\n Jogar no Casino Genius Pro vezes \n\n")
                            Genius.genius_joga_vezes(x_origem, y_origem, id, senha, url, navegador)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas,
                             lista_tarefas_fazer, pontos_disponiveis, hora_fim_tarefa) \
                                = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, id, senha,
                                                                         url, navegador, dia_da_semana)

                        print("--------------parte 4---------------")
                        if parar_tarefas:
                            break

                        if ('fichas no Casino Genius Pro' in lista_tarefas_fazer
                                or 'Ganhar 100.000 fichas no Casino Genius Pro' in lista_tarefas_fazer
                                or 'Ganhar 30.000 fichas no Casino Genius Pro' in lista_tarefas_fazer
                                or 'Ganhar 4.000 fichas no Casino Genius Pro' in lista_tarefas_fazer):

                            print("\n\n Ganhar fichas no Casino Genius Pro \n\n")
                            Genius.genius_joga_valor(x_origem, y_origem, id, senha, url, navegador, lista_tarefas_fazer)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas,
                             lista_tarefas_fazer, pontos_disponiveis, hora_fim_tarefa) \
                                = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, id, senha,
                                                                         url, navegador, dia_da_semana)

                        print("--------------parte 5---------------")
                        if parar_tarefas:
                            break

                        if ('Apostar 20 fichas ou mais em 9 linhas do caca' in lista_tarefas_fazer
                                or 'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 150 vezes' in lista_tarefas_fazer
                                or 'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 70 vezes' in lista_tarefas_fazer
                                or 'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 10 vezes' in lista_tarefas_fazer):

                            print("\n\n Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot vezes \n\n")

                            Slot.solot_joga_vezes(x_origem, y_origem, id, senha, url, navegador, True)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas,
                             lista_tarefas_fazer, pontos_disponiveis, hora_fim_tarefa) \
                                = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, id, senha,
                                                                         url, navegador, dia_da_semana)

                        print("--------------parte 6---------------")
                        if parar_tarefas:
                            break

                        if ('fichas no caca niquel slot poker' in lista_tarefas_fazer
                                or 'Ganhar 100.000 fichas no caca niquel Slot Poker' in lista_tarefas_fazer
                                or 'Ganhar 30.000 fichas no caca niquel Slot Poker' in lista_tarefas_fazer
                                or 'Ganhar 10.000 fichas no caca niquel Slot Poker' in lista_tarefas_fazer):

                            print("\n\n Ganhar fichas no caca niquel slot poker \n\n")

                            Slot.solot_joga_vezes(x_origem, y_origem, id, senha, url, navegador, False)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas,
                             lista_tarefas_fazer, pontos_disponiveis, hora_fim_tarefa) \
                                = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, id, senha,
                                                                         url, navegador, dia_da_semana)

                        print("--------------parte 7---------------")
                        if parar_tarefas:
                            break

                        if ('fichas no caca niquel da mesa' in lista_tarefas_fazer
                                or 'Ganhar 100.000 fichas no caca niquel da mesa' in lista_tarefas_fazer
                                or 'Ganhar 30.000 fichas no caca niquel da mesa' in lista_tarefas_fazer
                                or 'Ganhar 10.000 fichas no caca niquel da mesa' in lista_tarefas_fazer):

                            print("\n\n Ganhar fichas no caca niquel da mesa \n\n")

                            Mesa.joga(x_origem, y_origem, id, senha, url, navegador, 2000)

                            (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas,
                             lista_tarefas_fazer, pontos_disponiveis, hora_fim_tarefa) \
                                = Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, id, senha,
                                                                         url, navegador, dia_da_semana)

                        print("--------------parte 8---------------")
                        if parar_tarefas:
                            break

                    # (parar_tarefas, valor_fichas, conta_upada, meta_atingida, pontuacao_tarefas, lista_tarefas_fazer,
                    #  pontos_disponiveis, hora_fim_tarefa) = \
                    #     (Tarefas.testa_continuar_fazendo_tarefa(x_origem, y_origem, id, senha, url, navegador, dia_da_semana))

                hora_que_rodou = datetime.datetime.now().strftime('%H:%M:%S')

                print('valor_fichas', valor_fichas)
                print('pontuacao_tarefas', pontuacao_tarefas)
                print('hora_que_rodou', hora_que_rodou)

                roda = False
                break

        ip, com_internet = IP.meu_ip()  # obtem meu endereço de IP
        valores = [valor_fichas, pontuacao_tarefas, hora_que_rodou, ip]
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

        elif entrou_corretamente:  # se nao entrou no face

            if hora_fim_tarefa:
                valores = [""]
                #  apaga os valore quando da a hoara de sair do tarefas
                Google.apagar_numerodo_pc(valores, guia, linha)  # apaga o nume do pc
                Google.apagar_numerodo_pc(valores, guia, linha_novo)  # apaga o nume do pc

            else:
                # escre os valores na planilha
                Google.escrever_valores_lote(valores, guia, linha)  # escreve as informaçoes na planilha apartir da coluna E
                id, senha, linha, cont_IP = id_novo, senha_novo, linha_novo, cont_IP_novo
