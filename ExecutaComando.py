
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
import xp2
import Firebase



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

    guia = 'Up'

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
            if guia == "Up":
                Firebase.confirmacao_comando_resposta('Entrou')

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

                # codigo deve ser escrito aqui dentro ...

                status_comando = 'Aguardando comando'
                blind = ""
                while True:
                    comando = Firebase.comando_escravo
                    #print(comando)
                    Tarefas.recolher_tarefa_upando(x_origem, y_origem)

                    if comando == "Sair":
                        status_comando = "Saindo"
                        break

                    elif comando == "Mesa1":
                        blind = '500/1K'
                        status_comando = Mesa.escolher_blind(x_origem, y_origem, blind)

                    elif comando == "Mesa2":
                        blind = '1K/2K'
                        status_comando = Mesa.escolher_blind(x_origem, y_origem, blind)

                    elif comando == "Senta":
                        sentou = Mesa.sentar_mesa(x_origem, y_origem, False, blind)
                        if sentou:
                            status_comando = "Sentou"
                        else:
                            status_comando = "Não sentou"

                    elif comando == "Recolher":
                        status_comando = Tarefas.recolher_tarefa_upando(x_origem, y_origem)

                    elif comando == "Levanta":
                        status_comando = Mesa.levantar_mesa(x_origem, y_origem)

                    elif comando == "Slot":
                        Firebase.confirmacao_comando_resposta("Fazendo Slot")
                        Slot.solot_joga_vezes_upando(x_origem, y_origem)

                    elif comando == "2xp":
                        status_comando = xp2.pega_2xp(x_origem, y_origem)

                    Firebase.confirmacao_comando_resposta(status_comando)

                Firebase.confirmacao_comando_resposta('Entrendo em uma nova conta')

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


            Google.escrever_valores_lote(valores, guia, linha)  # escreve as informaçoes na planilha apartir da coluna E
            id, senha, linha, cont_IP = id_novo, senha_novo, linha_novo, cont_IP_novo
