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

import threading

from Variaveis_Globais import aviso_sistema_global, alterar_global_aviso_sistema



id = "x"
senha = ""
linha = ""
cont_IP = 10
guia = ""
guia_recebida = ""
LIMITE_IP = 5
ja_fez_tutorial = True

# Variáveis globais para as variáveis e controle da tarefa independente
id_novo = ""
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

        # Verificar se a tarefa deve continuar executando ou parar
        if continuar_tarefa:
            print("Executando tarefa independente...")

            # Atualizar as variáveis
            id_novo, senha_novo, linha_novo, cont_IP_novo = Google.credenciais(guia)  # pega id e senha para o proximo login
            continuar_tarefa = False

            # Indicar que a tarefa terminou e está pronta para aguardar novo comando
            tarefa_concluida.release()
        else:
            print("Tarefa independente parada.")
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

    print("guia:", guia)
    id, senha, linha, cont_IP = Google.credenciais(guia)
    if id == "":
        Seleniun.sair_face(url, navegador)
        guia = HoraT.mudar_guia(id, guia)
        id, senha, linha, cont_IP = Google.credenciais(guia)

    url = str(Google.pega_valor('Dados', 'F1'))
    dia_da_semana = datetime.datetime.now().weekday() # busca o dia da semana 0 segunda 1 terça ... 6 domeingo
    #login
    while True:
        #parte deo codigo que faz loguin
        ip, com_internet = IP.meu_ip()  # obtem meu endereço de IP
        valor_fichas = ""
        pontuacao_tarefas = ""
        hora_atual = ""
        status_conta = None

        if cont_IP >= LIMITE_IP or cont_IP < 0:  # se a contagem de ip ta fora da faixa vai para a função
            IP.ip()  # testa se o numero de contas esta dentro do limite antes de trocar ip

        entrou_corretamente, stataus = Seleniun.fazer_login(id, senha, url, navegador)
        if entrou_corretamente is False:  # se nao entrou no face
            print("conta nao entou no Facebook")
            Google.marca_caida(stataus, guia, linha)
            break

        while True:

            if entrou_corretamente is True:
                x_origem, y_origem, status_conta = Origem_pg.carregado_origem(id, senha, url, navegador)
                print(status_conta)
                if status_conta is not None:
                    break

            entrou_corretamente, stataus = Seleniun.teste_logado(id, senha, url, navegador)
            if entrou_corretamente is False:  # se nao entrou no face
                print("conta nao entou no Facebook")
                Google.marca_caida(stataus, guia, linha)
                break

        if entrou_corretamente is False:  # se nao entrou no face
            Google.marca_caida(stataus, guia, linha)
            break
        ja_fez_tutorial = True
        if status_conta != 'Carregada':  # testa status da conta
            if status_conta == 'Banida':  # se aconta esta banida
                print("conta banida tem que marcar na plinilha")
                Google.marca_banida("Banida", guia, linha)
                break
            elif status_conta == 'Tutorial':
                ja_fez_tutorial = False
                print('vai fazer tutorial')
                entrou_corretamente, stataus = Seleniun.teste_logado(id, senha, url, navegador)
                if entrou_corretamente == False:  # se nao entrou no face
                    Google.marca_caida(stataus, guia, linha)
                    break
                time.sleep(2)
                if Limpa.limpa_pequeno(x_origem, y_origem):
                    break
                Limpa.faz_tutorial(x_origem, y_origem)
                if Limpa.limpa_total(x_origem, y_origem):
                    break

            elif status_conta == 'Atualizar':
                break

        entrou_corretamente, stataus = Seleniun.teste_logado(id, senha, url, navegador)
        if entrou_corretamente is False:  # se nao entrou no face
            Google.marca_caida(stataus, guia, linha)
            break

        if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
            break

        # Comando para iniciar a tarefa independente
        continuar_tarefa = True
        iniciar_tarefa.release()

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

                    conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador) #retorna se a conta ta upada ou nao
                    if conta_upada:
                        IP.f5_quando_internete_ocila(id, senha, url, navegador)
                        entrou_corretamente, stataus = Seleniun.teste_logado(id, senha, url, navegador)
                        if not entrou_corretamente:  # se nao entrou no face
                            Google.marca_caida(stataus, guia, linha)
                            break
                        pontuacao_tarefas = OCR_tela.pontuacao_tarefas(x_origem, y_origem)
                        Limpa.fecha_tarefa(x_origem, y_origem)

                elif roleta == 'roleta_2':

                    print("dia da semana", dia_da_semana)

                    if dia_da_semana == 6 or dia_da_semana == 0 or dia_da_semana == 5: # testa se é sabado ou domingo
                        if pyautogui.pixelMatchesColor((x_origem + 750), (y_origem + 38), (245, 218, 96), tolerance=10) \
                                or pyautogui.pixelMatchesColor((x_origem + 802), (y_origem + 38), (245, 218, 96), tolerance=10):
                            print('conta sem upar')

                            for i in range(20):
                                time_sair = time.perf_counter()
                                tempo_total = time_sair - time_rodou
                                print('tempo que ja clicou no rodou', tempo_total)
                                if tempo_total > 18:
                                    print('ja pode sair do r2')
                                    break
                                time.sleep(1)
                                pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone roleta, ja roda sozinho

                            if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                                break
                            print('conta nao esta upada abre os iniciantes')

                            Mesa.joga_uma_vez(x_origem, y_origem)
                            time.sleep(2)
                            Limpa.iniciantes(x_origem, y_origem)
                            Limpa.limpa_total(x_origem, y_origem)

                        elif 100000 < valor_fichas < 400000:
                            for i in range(20):
                                time_sair = time.perf_counter()
                                tempo_total = time_sair - time_rodou
                                print('tempo que ja clicou no rodou', tempo_total)
                                if tempo_total > 18:
                                    print('ja pode sair do r2')
                                    break
                                time.sleep(1)
                                pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone roleta, ja roda sozinho

                            if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                                break
                            print('conta nao esta upada abre os iniciantes')

                            Mesa.joga_uma_vez(x_origem, y_origem)
                            time.sleep(2)
                            Limpa.iniciantes(x_origem, y_origem)
                            Limpa.limpa_total(x_origem, y_origem)

            # if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
            #     break

            entrou_corretamente, stataus = Seleniun.teste_logado(id, senha, url, navegador)
            if entrou_corretamente is False:  # se nao entrou no face
                Google.marca_caida(stataus, guia, linha)
                break

            if hora_que_rodou is None:
                hora_que_rodou = datetime.datetime.now().strftime('%H:%M:%S')

            valores = [valor_fichas, pontuacao_tarefas, hora_que_rodou, ip]
            Google.escrever_valores_lote(valores, guia, linha) # escreve as informaçoes na planilha apartir da coluna E

            # id, senha, linha, cont_IP = Google.credenciais(guia) # pega id e senha par o proximo login

            # if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
            #     break

            if roleta == 'roleta_1': # saber se roleta R1 ja terminou de rodar para sair da conta
                for i in range(50):
                    time_sair = time.perf_counter()
                    tempo_total = time_sair - time_rodou
                    print('tempo que ja clicou no rodou: ', tempo_total)
                    if tempo_total > 13:
                        print('ja pode sair do r1')
                        break

                    time.sleep(0.3)
                    pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone da roleta para abir
                    if pyautogui.pixelMatchesColor((x_origem + 495), (y_origem + 315), (227, 120, 14), tolerance=20):  # testa de roleta 1 ta aberta
                        pyautogui.doubleClick(x_origem + 492, y_origem + 383)  # clica no meio da roleta para rodar
                #Limpa.premio_r1(x_origem, y_origem)

            elif roleta == 'roleta_2':
                for i in range(20):
                    time_sair = time.perf_counter()
                    tempo_total = time_sair - time_rodou
                    print('tempo que ja clicou no rodou',tempo_total)
                    if tempo_total > 2:
                        print('ja pode sair do r2')
                        break
                    time.sleep(0.3)
                    pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone roleta, ja roda sozinho
                #Limpa.premio_r2(x_origem, y_origem)

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
                    lista_tarefas_fazer = Tarefas.comparar_listas(x_origem, y_origem)
                    print('numero de tarefas para serem feitos: ', len(lista_tarefas_fazer))
                    print('lista de tarefas para se fazer: ', lista_tarefas_fazer)
                    if lista_tarefas_fazer:
                        print("\n\n Foi encontrado ao menos uma tarefa\n\n")
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
                    lista_tarefas_fazer = Tarefas.comparar_listas(x_origem, y_origem)

                if HoraT.fim_tempo_tarefa():
                    Limpa.limpa_total(x_origem, y_origem)
                    break
                if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                    break
                if (len(lista_tarefas_fazer) <= 0) or meta_atingida or (valor_fichas < 40000):
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
                    lista_tarefas_fazer = Tarefas.comparar_listas(x_origem, y_origem)

                if HoraT.fim_tempo_tarefa():
                    Limpa.limpa_total(x_origem, y_origem)
                    break
                if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                    break
                if (len(lista_tarefas_fazer) <= 0) or meta_atingida or (valor_fichas < 40000):
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
                    lista_tarefas_fazer = Tarefas.comparar_listas(x_origem, y_origem)

                if HoraT.fim_tempo_tarefa():
                    Limpa.limpa_total(x_origem, y_origem)
                    break
                if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                    break
                if (len(lista_tarefas_fazer) <= 0) or meta_atingida or (valor_fichas < 40000):
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
                    lista_tarefas_fazer = Tarefas.comparar_listas(x_origem, y_origem)

                if HoraT.fim_tempo_tarefa():
                    Limpa.limpa_total(x_origem, y_origem)
                    break
                if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                    break
                if (len(lista_tarefas_fazer) <= 0) or meta_atingida or (valor_fichas < 40000):
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
                    lista_tarefas_fazer = Tarefas.comparar_listas(x_origem, y_origem)

                if HoraT.fim_tempo_tarefa():
                    Limpa.limpa_total(x_origem, y_origem)
                    break
                if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                    break
                if (len(lista_tarefas_fazer) <= 0) or meta_atingida or (conta_upada is False) or (valor_fichas < 40000):
                    break
                elif 'Apostar 20 fichas ou mais em 9 linhas do caca' in lista_tarefas_fazer\
                        or 'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 150 vezes' in lista_tarefas_fazer\
                        or 'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 70 vezes' in lista_tarefas_fazer\
                        or 'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 10 vezes' in lista_tarefas_fazer:

                    print('jogar caça niquel poker slote')

                    print("\n\n Faz Slote... \n\n")
                    Slot.solot_joga_vezes(x_origem, y_origem, id, senha, url, navegador)
            Aneis.recolhe_aneis(x_origem, y_origem)
            if Limpa.ja_esta_logado(x_origem, y_origem) == "sair da conta":
                print('ja esta logado sai')
            else:
                if HoraT.fim_tempo_tarefa():
                    valores = [""]
                    tarefa_concluida.acquire()
                    Google.apagar_numerodo_pc(valores, guia, linha)  # apaga o nume do pc
                    Google.apagar_numerodo_pc(valores, guia, linha_novo)  # apaga o nume do pc
                else:
                    valor_fichas = OCR_tela.valor_fichas(x_origem, y_origem)
                    hora_que_rodou = datetime.datetime.now().strftime('%H:%M:%S')
                    conta_upada = Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)  # retorna se a conta ta upada ou nao
                    if conta_upada:
                        meta_atingida, pontuacao_tarefas = Tarefas.meta_tarefas(x_origem, y_origem)
                        pontuacao_tarefas = OCR_tela.pontuacao_tarefas(x_origem, y_origem)
                    valores = [valor_fichas, pontuacao_tarefas, hora_que_rodou, ip]
                    Google.escrever_valores_lote(valores, guia, linha)  # escreve as informaçoes na planilha apartir da coluna E
                    #id, senha, linha, cont_IP = Google.credenciais(guia)  # pega id e senha par o proximo login
                    #id, senha, linha, cont_IP = id_novo, senha_novo, linha_novo, cont_IP_novo

        # Aguardar a tarefa terminar
        tarefa_concluida.acquire()

        id, senha, linha, cont_IP = id_novo, senha_novo, linha_novo, cont_IP_novo

        Seleniun.sair_face(url, navegador)
        guia_recebida = HoraT.mudar_guia(id, guia)
        if guia != guia_recebida:
            dia_da_semana = datetime.datetime.now().weekday()  # busca o dia da semana 0 segunda 1 terça ... 6 domeingo
            url = str(Google.pega_valor('Dados', 'F1'))
            guia = guia_recebida
            id, senha, linha, cont_IP = Google.credenciais(guia)  # pega id e senha par o proximo login
        guia = guia_recebida