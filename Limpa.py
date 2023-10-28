import time
import pyautogui
# Desabilitar o fail-safe
pyautogui.FAILSAFE = False
import Origem_pg
pyautogui.PAUSE = 0
import OCR_tela
import IP
import Seleniun
import Slot


def teste_limpo(x_origem, y_origem):
    pyautogui.click(490 + x_origem, 70 + y_origem) # clique bobo para passar alguma naimação
    #barra azul do looby
    if pyautogui.pixelMatchesColor((x_origem + 685), (y_origem + 360), (215, 234, 244), tolerance=5):
        print("teste_limpo: Esta no Lobby, ta limpo")
        return True
    else:
        print('teste_limpo: não esta limpo')
        return False


def ja_esta_logado(x_origem, y_origem):

    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 370), (224, 227, 229), tolerance=5):
        print('ja_esta_logado')
        aviso_sistema, resposta = OCR_tela.aviso_sistema(x_origem, y_origem)
        print(resposta)
        if aviso_sistema:
            if resposta == "sair da conta":
                print("sair da conta")
                return "sair da conta"
    else:
        return False


def limpa_jogando(x_origem, y_origem):
    print('limpa_jogando')

    pyautogui.click(x_origem + 43, y_origem + 388) # clica no anel

    if (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 117), (72, 71, 76), tolerance=5) or
            pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 117), (22, 21, 23), tolerance=5)):
        pyautogui.click(821 + x_origem, 138 + y_origem)  # clica no fechar tarefa
        print('fecha lista tarefas')

    #voce ganhou 2500
    elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 179), (71,0,148), tolerance=6):
        pyautogui.click(x_origem + 490, y_origem + 480, button='left')
        print("Voce ganhou 2500")

    # Subiu de nivel
    elif pyautogui.pixelMatchesColor((x_origem + 492), (y_origem + 443), (25, 118, 188), tolerance=6) \
            or pyautogui.pixelMatchesColor((x_origem + 492), (y_origem + 443), (29, 139, 200), tolerance=6):
        pyautogui.click(x_origem + 492, y_origem + 443, button='left')
        print("Subiu de nivel")

    # Quebou seu recorde
    elif pyautogui.pixelMatchesColor((x_origem + 772), (y_origem + 170), (242, 246, 0), tolerance=6) :
        pyautogui.click(x_origem + 703, y_origem + 170, button='left')
        print("Quebou seu recorde")

    # nivel 2
    elif pyautogui.pixelMatchesColor((x_origem + 492), (y_origem + 390), (237, 105, 0), tolerance=10):
        pyautogui.click(x_origem + 492, y_origem + 390, button='left')
        print("nivel 2")

    # Presentinho de dentro da mesa
    elif pyautogui.pixelMatchesColor((x_origem + 38), (y_origem + 526), (187, 153, 111), tolerance=19):
        pyautogui.click(x_origem + 38, y_origem + 526, button='left')
        print("Presentinho de dentro da mesa")

    # aviso do sistema dentro da mesa
    elif pyautogui.pixelMatchesColor((x_origem + 455), (y_origem + 417), (25, 116, 184), tolerance=19):
        pyautogui.click(641 + x_origem, 278 + y_origem)  # clica no x do aviso do sistema "tem certesa de que quer sair da mesa?"
        print("aviso do sistema dentro da mesa")

    # Laranja
    elif (pyautogui.pixelMatchesColor((x_origem + 237), (y_origem + 165), (224, 9, 5), tolerance=20)) or \
            (pyautogui.pixelMatchesColor((x_origem + 240), (y_origem + 167), (228, 22, 5), tolerance=20)):
        pyautogui.click(771 + x_origem, 156 + y_origem, button='left')
        print("promoçao laranja")

    # Fecha promoçoes
    elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 118), (72, 71, 76), tolerance=20):
        pyautogui.click(821 + x_origem, 138 + y_origem, button='left')
        print("Promoção padrão")

    # clica no Normal
    elif pyautogui.pixelMatchesColor((x_origem + 162), (y_origem + 160), (12, 72, 108), tolerance=5):
        pyautogui.click(x_origem + 164, y_origem + 161)
        print("Clica no Normal")


def limpa_pequeno(x_origem, y_origem):
    print('limpa_pequeno')
    if ja_esta_logado(x_origem, y_origem) == "sair da conta" :
        return "sair da conta"

    pyautogui.click(490 + x_origem, 70 + y_origem, button='left')  # clique bobo para passar alguma naimação
    # voce ja recebeu seu premio, deixe um pouco para os outros
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 435), (175, 23, 18), tolerance=15):
        pyautogui.click(x_origem + 490, y_origem + 435)
        print("voce ja recebeu seu premio, deixe um pouco para os outros")

    # voce ganhou 2500
    elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 179), (71, 0, 148), tolerance=15):
        pyautogui.click(x_origem + 490, y_origem + 480, button='left')
        print("Voce ganhou 2500")

    # Subiu de nivel
    elif (pyautogui.pixelMatchesColor((x_origem + 492), (y_origem + 443), (25, 118, 188), tolerance=15)
          or pyautogui.pixelMatchesColor((x_origem + 492), (y_origem + 443), (29, 139, 200), tolerance=15)):
        pyautogui.click(x_origem + 492, y_origem + 443, button='left')
        print("Subiu de nivel")

    # Resutado da temporada - Bronse 1
    elif pyautogui.pixelMatchesColor((x_origem + 705), (y_origem + 216), (150, 104, 177), tolerance=10):
        pyautogui.click(x_origem + 721, y_origem + 218)
        print("Subiu de nivel")

    # nivel 2
    elif pyautogui.pixelMatchesColor((x_origem + 492), (y_origem + 390), (237, 105, 0), tolerance=10):
        pyautogui.click(x_origem + 492, y_origem + 390, button='left')
        print("nivel 2")

    # Quebou seu recorde
    elif pyautogui.pixelMatchesColor((x_origem + 772), (y_origem + 170), (242, 246, 0), tolerance=15):
        pyautogui.click(x_origem + 703, y_origem + 170, button='left')
        print("Quebou seu recorde")

    # aviso do sistema "tem certesa de que quer sair da mesa?" "vc so pode jogar depois de estar sentado""
    elif pyautogui.pixelMatchesColor((x_origem + 455), (y_origem + 417), (25, 116, 184), tolerance=19):  # aviso do sistema "tem certesa de que quer sair da mesa?"
        pyautogui.click(641 + x_origem, 278 + y_origem)  # clica no x do aviso do sistema "tem certesa de que quer sair da mesa?"
        print("aviso do sistema: limpa_pequeno")
        if pyautogui.pixelMatchesColor((x_origem + 491), (y_origem + 417), (25, 118, 188), tolerance=20):
            print('tem mensagem com atuializar')
            aviso_sistema, resposta = OCR_tela.aviso_sistema(x_origem, y_origem)
            if resposta == "sair da conta":
                print("sair da conta")
                return "sair da conta"

    # clica no Normal
    elif pyautogui.pixelMatchesColor((x_origem + 162), (y_origem + 160), (12, 72, 108), tolerance=15):
        pyautogui.click(x_origem + 164, y_origem + 161)
        print("Clica no Normal")

    # dispo nivel em acesso antecipado para jogadores VIP
    elif pyautogui.pixelMatchesColor((x_origem + 702), (y_origem + 104), (27, 53, 167), tolerance=10):
        pyautogui.click(x_origem + 896, y_origem + 22)
        print("dispo nivel em acesso antecipado para jogadores VIP")

    ## Genius Muito tempo desde a sua unlima aposta
    elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 612), (80, 73, 76), tolerance=15):
        if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 415), (25, 118, 188), tolerance=15) \
                or pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 415), (29, 139, 200), tolerance=15):## Genius Muito tempo desde a sua unlima aposta
            pyautogui.mouseDown(x_origem + 490, y_origem + 415, button='left')
            print("Genius Muito tempo desde a sua unlima apostar")
            time.sleep(1)
            pyautogui.mouseUp()

    # testa se o torneino semanal esta no loob
    elif pyautogui.pixelMatchesColor((x_origem + 154), (y_origem + 105), (70, 70, 71), tolerance=15):
        # Slot Classico testa se esta no slot com ele limpo ou com alguma mensagem, quando tem alguma messagem fica um pouco escuro
        if not (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (46, 22, 9), tolerance=15)
                or pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (18, 9, 4), tolerance=5)):
            print('print("Torneio semanal de forma errada no loby")')
            limpo = teste_limpo(x_origem, y_origem)
            if limpo:
                pyautogui.click(x_origem + 920, y_origem + 150)
                print('clica para abrir o slot 777')
                time.sleep(3)
                for i in range(40):
                    # Slot Classico
                    if (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (46, 22, 9), tolerance=15)
                            or pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (18, 9, 4), tolerance=15)):
                        time.sleep(10)
                        pyautogui.click(910 + x_origem, 80 + y_origem)
                        print("Slot Classico, fecha")
                        limpa_tarefas(x_origem, y_origem)
                        limpo = teste_limpo(x_origem, y_origem)
                        if limpo:
                            break
                    time.sleep(0.5)
                limpa_tarefas(x_origem, y_origem)
                # testa se o torneino semanal esta no loob
                if pyautogui.pixelMatchesColor((x_origem + 154), (y_origem + 105), (70, 70, 71), tolerance=15):
                    # Slot Classico testa se esta no slot com ele limpo ou com alguma mensagem, quando tem alguma messagem fica um pouco escuro
                    if not (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (46, 22, 9), tolerance=15)
                            or pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (18, 9, 4), tolerance=5)):
                        print('print("Torneio semanal de forma errada no loby")')
                        limpo = teste_limpo(x_origem, y_origem)
                        if limpo:
                            IP.tem_internet()
                            print("erro no torneio semanal, Da um F5")
                            pyautogui.press('f5')
                            # Seleniun.atualizar_pagina(navegador, url)
                            time.sleep(25)

    # um martelo gratis par adestruir os goblins e receber recompensa ( tema de halowin)
    elif pyautogui.pixelMatchesColor((x_origem + 500), (y_origem + 190), (0, 27, 38), tolerance=15):
        pyautogui.click(495 + x_origem, 520 + y_origem)

    elif pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 370), (224, 227, 229), tolerance=15):
        aviso_sistema, resposta = OCR_tela.aviso_sistema(x_origem, y_origem)
        if aviso_sistema:
            if resposta == "sair da conta":
                print("sair da conta")
                return "sair da conta"

    # o novo banco esta aberto"
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 155), (114, 62, 25), tolerance=20):
        pyautogui.click(495 + x_origem, 400 + y_origem)
        print("o novo banco esta aberto")

    #if not(teste_limpo(x_origem, y_origem)):  # se ta limpo nem entra

    try:
        if (pyautogui.pixelMatchesColor(215, 1000, (36, 37, 38), tolerance=5)  # mensagem do canto inferior esquedo " Você esta offiline no momento."
                or pyautogui.pixelMatchesColor(700, 650, (32, 33, 36), tolerance=5)  # fundo cinza com o dinoçauro
                or pyautogui.pixelMatchesColor(700, 650, (255, 255, 255), tolerance=2)  # retangulo branco no meio da tela quando esta sem internete
                or pyautogui.pixelMatchesColor(700, 650, (221, 221, 221), tolerance=7)  # tela cinza clara com cara triste
                or pyautogui.pixelMatchesColor(700, 650, (238, 238, 238), tolerance=7)):  # tela cinza clara com cara triste
            print("aguarda 5 segundos e faz um novo teste se a pagina nao carregou")
            time.sleep(5)
            try:
                if (pyautogui.pixelMatchesColor(215, 1000, (36, 37, 38), tolerance=5)  # mensagem do canto inferior esquedo " Você esta offiline no momento."
                        or pyautogui.pixelMatchesColor(700, 650, (32, 33, 36), tolerance=5)  # fundo cinza com o dinoçauro
                        or pyautogui.pixelMatchesColor(700, 650, (255, 255, 255), tolerance=2)  # retangulo branco no meio da tela quando esta sem internete
                        or pyautogui.pixelMatchesColor(700, 650, (221, 221, 221), tolerance=7)  # tela cinza clara com cara triste
                        or pyautogui.pixelMatchesColor(700, 650, (238, 238, 238), tolerance=7)):  # tela cinza clara com cara triste
                    print("Falha na pagina e a tela esta branca, da um F5")
                    IP.tem_internet()
                    #navegador.get(url)
                    pyautogui.press('f5')
                    time.sleep(15)
            except Exception as e:
                # Lide com o erro aqui, por exemplo, exiba uma mensagem de erro ou registre-o em um arquivo de log
                print(f'Erro: {e}')
    except Exception as e:
        # Lide com o erro aqui, por exemplo, exiba uma mensagem de erro ou registre-o em um arquivo de log
        print(f'Erro: {e}')


def limpa_tarefas(x_origem, y_origem): # fecha todas as tarefas que sao feitas
    print('limpa_tarefas')
    pyautogui.click(490 + x_origem, 70 + y_origem, button='left')  # clique bobo para passar alguma naimação
    limpa_pequeno(x_origem, y_origem)
    if teste_limpo(x_origem, y_origem): # se ta limpo nem entra
        return

    #Cartas premiadas
    elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 213), (18,42,91), tolerance=19):
        pyautogui.click(763 + x_origem, 193 + y_origem, button='left')
        print("Cartas premiadas")

    #Mesa
    elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (27, 92, 155),  tolerance=19) \
            or pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (19, 64, 109),  tolerance=19) :  # testa se esta dentro da mesa

        pyautogui.click(947 + x_origem, 78 + y_origem)#setinha
        time.sleep(0.3)
        pyautogui.click(925 + x_origem, 204 + y_origem)#Levantar
        time.sleep(0.2)
        pyautogui.click(947 + x_origem, 78 + y_origem)#setinha
        time.sleep(0.2)
        pyautogui.click(925 + x_origem, 111 + y_origem)#Lobby
        if pyautogui.pixelMatchesColor((x_origem + 455), (y_origem + 417), (25, 116, 184), tolerance=19):  # aviso do sistema "tem certesa de que quer sair da mesa?"
            pyautogui.click(641 + x_origem, 278 + y_origem)  # clica no x do aviso do sistema "tem certesa de que quer sair da mesa?"
            print("aviso do sistema")
            time.sleep(0.3)
            pyautogui.click(947 + x_origem, 78 + y_origem)  # setinha
            time.sleep(0.3)
            pyautogui.click(925 + x_origem, 204 + y_origem)  # Levantar
            time.sleep(0.2)
            pyautogui.click(947 + x_origem, 78 + y_origem)  # setinha
            time.sleep(0.2)
            pyautogui.click(925 + x_origem, 111 + y_origem)  # Lobby

        print("Sai da Mesa")

    #Casino Genius
    elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 612), (111, 100, 105), tolerance=19):
        pyautogui.click(910 + x_origem, 80 + y_origem)
        print("Casino Genius")

    #Slot Classico
    elif pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (46, 22, 9), tolerance=5) \
            or pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 668), (18, 9, 4), tolerance=5):
        pyautogui.click(910 + x_origem, 80 + y_origem)
        print("Slot Classico")

    fecha_tarefa(x_origem, y_origem)


def fecha_tarefa(x_origem, y_origem): #fecha a lista de tarefas diarias
    print('fecha_tarefa')
    #pyautogui.click(490 + x_origem, 70 + y_origem, button='left')  # clique bobo para passar alguma naimação
    #Tarefas diarias
    for i in range(20):
        if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 133), (47, 0, 90), tolerance=2):
            pyautogui.click(821 + x_origem, 138 + y_origem)
            time.sleep(0.5)
            print("fecha Tarefas diarias")
        else:
            return

        # o novo banco esta aberto"
        if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 155), (114, 62, 25), tolerance=20):
            pyautogui.click(495 + x_origem, 400 + y_origem, button='left')
            print("o novo banco esta aberto")

        time.sleep(0.3)
    limpa_total(x_origem, y_origem)


def limpa_promocao(x_origem, y_origem):
    '''Limpa as promoções exceto as tarefas que são feitas'''
    print('limpa_promocao')
    pyautogui.click(490 + x_origem, 70 + y_origem, button='left')  # clique bobo para passar alguma naimação
    limpa_pequeno(x_origem, y_origem)
    if ja_esta_logado(x_origem, y_origem) == "sair da conta" :
        return "sair da conta"

    if teste_limpo(x_origem, y_origem): # se ta limpo nem entra
        return None

    # amigos on line e opiçoes
    if pyautogui.pixelMatchesColor((x_origem + 879), (y_origem + 190), (235,237,239), tolerance=19):
        pyautogui.click(909 + x_origem, 84 + y_origem, button='left')
        print("amigos on line e opiçoes")

    # o novo banco esta aberto"
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 155), (114, 62, 25), tolerance=20):
        pyautogui.click(495 + x_origem, 400 + y_origem, button='left')
        print("o novo banco esta aberto")

    # Fique milionario jogando
    if pyautogui.pixelMatchesColor((x_origem + 545), (y_origem + 105), (167, 100, 48), tolerance=10):
        pyautogui.click(812 + x_origem, 240 + y_origem)
        print("Fique milionario jogando")

    # Valete ou mais
    if pyautogui.pixelMatchesColor((x_origem + 400), (y_origem + 70), (12, 6, 42), tolerance=10):
        pyautogui.mouseDown(895 + x_origem, 82 + y_origem) # aperta e segura
        time.sleep(0.4)
        pyautogui.mouseUp(895 + x_origem, 82 + y_origem)  # aperta e segura
        print("Valete ou mais")

    #Vip
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 100), (46, 29, 21), tolerance=5):
        pyautogui.click(921 + x_origem, 89 + y_origem, button='left')
        print("vip")

    # Desafios do Rallyaces
    if pyautogui.pixelMatchesColor((x_origem + 920), (y_origem + 105), (150, 138, 220), tolerance=10):
        pyautogui.click(920 + x_origem, 105 + y_origem)
        print("Desafios do Rallyaces")

    # Mega Giro e roleta2
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 107), (38, 24, 77), tolerance=10):
        pyautogui.click(884 + x_origem, 135 + y_origem, button='left')
        print("Mega Giro e roleta2")

    # Gostosuras de Halloween
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (18, 17, 19), tolerance=10):
        pyautogui.click(495 + x_origem, 315 + y_origem)
        print("Gostosuras de Halloween")
        time.sleep(1)

    # Fecha promoçoes exceto tarefas
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (73, 71, 76), tolerance=20):
        print("Promoção padrão")
        if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 133), (48, 0, 96), tolerance=10):
            print("Tarefas diarias, se fecha no limpa")
        else:
            pyautogui.click(821 + x_origem, 138 + y_origem)
            print("Promoção padrão clica no fechar")

    # Oferta de primeira recarga
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 176), (252, 123, 0), tolerance=20):
        pyautogui.click(826 + x_origem, 176 + y_origem, button='left')
        print("Oferta de primeira recarga")

    # Banco do poker regras aberto
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (46, 38, 26), tolerance=20):
        pyautogui.click(777 + x_origem, 217 + y_origem, button='left')
        time.sleep(0.5)
        pyautogui.click(821 + x_origem, 138 + y_origem, button='left')
        print("Banco do poker")

    # Banco do poker
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (115, 96, 64), tolerance=20):
        pyautogui.click(821 + x_origem, 138 + y_origem, button='left')
        print("Banco do poker")

    # VS pegar a carta
    if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 118), (29,28,30), tolerance=8):
        pyautogui.click(477 + x_origem, 500 + y_origem, button='left')
        print("VS pegar a carta")

    # Roleta 1
    if pyautogui.pixelMatchesColor((x_origem + 495), (y_origem + 315), (211, 110, 12), tolerance=25):
        pyautogui.click(882 + x_origem, 171 + y_origem)
        print("limpa Roleta1")

    # Roleta depois da roleta e Mega giro
    if pyautogui.pixelMatchesColor((x_origem + 472), (y_origem + 120), (218, 106, 4), tolerance=20):
        pyautogui.click(884 + x_origem, 136 + y_origem)
        print("Roleta depois da roleta e Mega giro")

    # Laranja
    if ((pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 165), (224, 9, 5), tolerance=20)) or
            (pyautogui.pixelMatchesColor((x_origem + 240), (y_origem + 167), (228, 22, 5), tolerance=20))):
        pyautogui.click(771 + x_origem, 156 + y_origem, button='left')
        print("promoçao laranja")

    # raliacesses
    if ((pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 167), (255, 204, 125), tolerance=19)) or
            (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 167), (74, 40, 12), tolerance=19))):  # aneis
        pyautogui.click(811 + x_origem, 168 + y_origem, button='left')
        print("aneis")

    # Voce Noa Jogou Nehum Jogo De Poker Essasemana
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 225), (13, 17, 41), tolerance=6):
        pyautogui.click(x_origem + 722, y_origem + 219, button='left')
        print("Voce Noa Jogou Nehum Jogo De Poker Essasemana")


def limpa_total(x_origem, y_origem):

    print('limpa_total')
    cont_erro_limpa = 0
    for i in range(50):
        pyautogui.click(490 + x_origem, 70 + y_origem)  # clique bobo para passar alguma naimação
        limpa_pequeno(x_origem, y_origem)
        cont_erro_limpa += 1
        if cont_erro_limpa >= 30:
            cont_erro_limpa = 0
            print('Erro no limpa, da um F5')
            pyautogui.press('f5')
            print('espera 25 segundos')
            time.sleep(25)
            print('esperou 25 segundos')

        if ja_esta_logado(x_origem, y_origem) == "sair da conta":
            return "sair da conta"
        limpa_pequeno(x_origem, y_origem)
        if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
            return None
        limpa_tarefas(x_origem, y_origem) # fecha as tarefas que sao feitas cartas genius slote mesa ...
        if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
            return None
        fecha_tarefa(x_origem, y_origem) # fecha a lista de tarefas diarias
        if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
            return None
        limpa_promocao(x_origem, y_origem)
        if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
            return None
        limpa_tarefas(x_origem, y_origem)
        if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
            return None
        iniciantes(x_origem, y_origem)
        if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
            return None


def limpa_total_fazendo_tarefa(x_origem, y_origem):
    print('limpa_total_fazendo_tarefa')

    if ja_esta_logado(x_origem, y_origem) == "sair da conta":
        return "sair da conta"
    limpa_pequeno(x_origem, y_origem)
    limpa_promocao(x_origem, y_origem)
    #fecha_tarefa(x_origem, y_origem) # fecha a lista de tarefas diarias


def limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador): #abre o tarefas
    print('limpa_abre_tarefa')
    # testa se a tarefa diaria é de conta sem upar cadeado na cartas premidas
    if (pyautogui.pixelMatchesColor((x_origem + 750), (y_origem + 38), (245, 218, 96), tolerance=10)
            or pyautogui.pixelMatchesColor((x_origem + 802), (y_origem + 38), (245, 218, 96), tolerance=10)):
        print("Tarefas diarias conta sem upar")
        return False

    elif (pyautogui.pixelMatchesColor((x_origem + 750), (y_origem + 38), (10, 54, 112), tolerance=10)
          or pyautogui.pixelMatchesColor((x_origem + 802), (y_origem + 38), (10, 54, 112), tolerance=10)):
        print("Tarefas diarias conta upada")

        cont_limpa_tarefas = 0
        for i in range(600):

            for i in range(20):
                IP.f5_quando_internete_ocila(id, senha, url, navegador)
                pyautogui.doubleClick(x_origem + 635, y_origem + 25) #clica no tarefas diarias
                print("Limpa Tarefas diarias")
                time.sleep(0.5)
                pyautogui.doubleClick(x_origem + 193, y_origem + 172) #clica dentro do tarefas diarias
                limpa_pequeno(x_origem, y_origem)
                #testa se tarefa diariaria esta aberta e limpa
                if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 133), (48, 0, 96), tolerance=20):
                    print("Tarefas diarias pausa")
                    time.sleep(1.5)
                    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 133), (48, 0, 96), tolerance=20):
                        print("Tarefas diarias limpo...")
                        return True
                #testa se a tarefa diaria é de conta sem upar
                if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 133), (1, 50, 254), tolerance=20):
                    pyautogui.click(821 + x_origem, 138 + y_origem, button='left') #clique para fechar
                    print("Tarefas diarias conta sem upar")
                    return False

            limpa_promocao(x_origem, y_origem)

            cont_limpa_tarefas += 1
            if cont_limpa_tarefas >= 60:
                cont_limpa_tarefas = 0
                #da um F5
                IP.tem_internet()
                print("limpa tarefa Da um F5")
                # pyautogui.press('f5')
                navegador.get(url)
                # Seleniun.atualizar_pagina(navegador, url)
                time.sleep(15)
                entrou_corretamente, stataus = Seleniun.teste_logado(id, senha, url, navegador)
                limpa_total(x_origem, y_origem)

            time.sleep(1)
        return False
    return False


def forca_iniciante(x_origem, y_origem):
    print('forca_iniciante')
    limpa_total(x_origem, y_origem)
    # testa se esta visivel o começar ja
    for i in range(30):
        print('procura começar ja')
        if pyautogui.pixelMatchesColor((x_origem + 672), (y_origem + 146), (179, 216, 127), tolerance=5):
            print('clique começar ja ')
            pyautogui.click(672 + x_origem, 146 + y_origem)  # clica no começar ja
            time.sleep(4)
            limpa_tarefas(x_origem, y_origem)
            time.sleep(1)
            iniciantes(x_origem, y_origem)
            limpa_total(x_origem, y_origem)
            return
        time.sleep(1)
    return


def iniciantes(x_origem, y_origem):
    print("iniciantes")
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 173), (34, 0, 109), tolerance=20):
        for i in range(10):
            print("Recompensa de logim para iniciantes")
            if pyautogui.pixelMatchesColor((x_origem + 310), (y_origem + 326), (234, 114, 32), tolerance=20):
                pyautogui.click(310 + x_origem, 326 + y_origem) # pega o 2xp
                print("Primeiro dia, EXPX2")
                time.sleep(2)
                pyautogui.click(777 + x_origem, 173 + y_origem)  # clica no fechar
                time.sleep(1)

            if pyautogui.pixelMatchesColor((x_origem + 424), (y_origem + 326), (234, 114, 32), tolerance=20):
                pyautogui.click(424 + x_origem, 326 + y_origem) # pega o anel
                print("Segundo dia, anel")
                time.sleep(2)
                pyautogui.click(777 + x_origem, 173 + y_origem)  # clica no fechar
                time.sleep(1)
            if pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 326), (234, 114, 32), tolerance=20):
                pyautogui.click(534 + x_origem, 326 + y_origem) # pega o anel
                print("Terceiro  dia, 2.000")
                time.sleep(2)
                pyautogui.click(478 + x_origem, 529 + y_origem)  # clica no pegar
                time.sleep(2)

            if pyautogui.pixelMatchesColor((x_origem + 310), (y_origem + 475), (234, 114, 32), tolerance=20):
                pyautogui.click(310 + x_origem, 475 + y_origem)  # pega o 2xp
                print("Qarto dia, Caixa102")
                time.sleep(2)
                pyautogui.click(777 + x_origem, 173 + y_origem)  # clica no fechar
                time.sleep(1)
            if pyautogui.pixelMatchesColor((x_origem + 424), (y_origem + 475), (234, 114, 32), tolerance=20):
                pyautogui.click(424 + x_origem, 475 + y_origem)  # pega o anel
                print("Quinto dia, 5.000")
                time.sleep(2)
                pyautogui.click(478 + x_origem, 529 + y_origem)  # clica no pegar
                time.sleep(2)
            if pyautogui.pixelMatchesColor((x_origem + 534), (y_origem + 475), (234, 114, 32), tolerance=20):
                pyautogui.click(534 + x_origem, 475 + y_origem)  # pega o anel
                print("Sexto dia, Bilhete")
                time.sleep(2)
                pyautogui.click(777 + x_origem, 173 + y_origem)  # clica no fechar
                time.sleep(1)

            if pyautogui.pixelMatchesColor((x_origem + 716), (y_origem + 470), (172, 70, 2), tolerance=20):
                pyautogui.click(743 + x_origem, 465 + y_origem)  # pega o anel
                print("Setimo dia, 10.000")
                time.sleep(2)
                pyautogui.click(478 + x_origem, 529 + y_origem)  # clica no pegar
                time.sleep(2)
            #time.sleep(1)
        pyautogui.click(777 + x_origem, 173 + y_origem)  # clica no fechar


def faz_tutorial(x_origem,y_origem):
    for i in range(100):
        print('Tutorial...')
        #testa se esta aparecendo o 500 Fichas
        if pyautogui.pixelMatchesColor((x_origem + 545), (y_origem + 378), (251, 213, 3), tolerance=20):
            print("500 fichas, clica no OK")
            pyautogui.click(x_origem + 550, y_origem + 500) # clica no ok
            #time.sleep(1)

        if pyautogui.pixelMatchesColor((x_origem + 484), (y_origem + 325), (255, 254, 104), tolerance=10):
            print('Girar roleta gratis')
            pyautogui.doubleClick(x_origem + 490, y_origem + 380)  # clica no girar gratis da roleta
            time.sleep(15)

        if pyautogui.pixelMatchesColor((x_origem + 475), (y_origem + 475), (38, 1, 61), tolerance=10):
            print('clica no sim jogar agora')
            pyautogui.mouseDown(x_origem + 470, y_origem + 420)  # Sim, jogar agora
            time.sleep(0.3)
            pyautogui.mouseUp(x_origem + 470, y_origem + 420)  # Sim, jogar agora
            time.sleep(1)

        limpa_pequeno(x_origem, y_origem)
        limpa_tarefas(x_origem, y_origem)

        time.sleep(1)

        if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 173), (34, 0, 109), tolerance=20):
            for i in range(40):
                print("Recompensa de logim para iniciantes")
                time.sleep(0.5)
                if pyautogui.pixelMatchesColor((x_origem + 310), (y_origem + 326), (234, 114, 32), tolerance=30):
                    pyautogui.click(310 + x_origem, 326 + y_origem)  # pega o 2xp
                    print("Primeiro dia, EXPX2")
                    time.sleep(2)
                    pyautogui.click(777 + x_origem, 173 + y_origem)  # clica no fechar
                    time.sleep(1)
                    print('fim do tutorial')
                    break

            pyautogui.click(777 + x_origem, 173 + y_origem)  # clica no fechar
            time.sleep(2)
            break


def premio_r1 (x_origem, y_origem):
    print('premio_r1')
    fecha_tarefa(x_origem, y_origem)
    for i in range(100):
        #print('espera...')
        #Roleta 1 aberta esperando bater o premio
        if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 611), (255, 196, 255), tolerance=20):  # testa de roleta 1 ta aberta
            print("terminou de rodar o R1 da um time")
            time.sleep(2)
            print("sai do R1")
            return True
        time.sleep(0.05)
        fecha_tarefa(x_origem, y_origem)
        limpa_pequeno(x_origem, y_origem)
        limpa_promocao(x_origem, y_origem)
        limpa_tarefas(x_origem, y_origem)
        if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
            return True
    print('deu o tempo')
    return True


def premio_r2 (x_origem, y_origem):
    print('premio_r2')
    for i in range(100):
        if pyautogui.pixelMatchesColor((x_origem + 365), (y_origem + 580), (22, 0, 100), tolerance=20):  # espera o premio sair
            print("roleta 2 aberta pegou o pemio pode sair")
            return True
        time.sleep(0.05)
        fecha_tarefa(x_origem, y_origem)
        limpa_pequeno(x_origem, y_origem)
        limpa_promocao(x_origem, y_origem)
        limpa_tarefas(x_origem, y_origem)
        iniciantes(x_origem, y_origem)
        if teste_limpo(x_origem, y_origem):  # se ta limpo nem entra
            return True
    print('deu o tempo')
    return True


def aviso_canto_lobby (x_origem, y_origem):
    '''Fecha propaganda'''
    #fecha mnsagem no canto inferior da tela
    if pyautogui.pixelMatchesColor((x_origem + 281), (y_origem + 561), (255, 255, 255), tolerance=5):
        pyautogui.click(x_origem + 281, y_origem + 561)
        print("fechou aviso canto da tela")


def limpa_abre_tarefa2(x_origem, y_origem): #abre o tarefas
    # pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
    # if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 133), (47, 0, 90), tolerance=20):
    #     print("Tarefas diarias ja esta limpo")
    #     return True

    for i in range(600):

        for i in range(20):
            #IP.f5_quando_internete_ocila(id, senha, url, navegador)
            #time.sleep(2)
            pyautogui.doubleClick(x_origem + 635, y_origem + 25) # clica no tarefas diarias
            print("Limpa Tarefas diarias")
            time.sleep(0.5)
            pyautogui.doubleClick(x_origem + 193, y_origem + 172) # clica dentro do tarefas diarias
            # time.sleep(0.5)

            limpa_pequeno(x_origem, y_origem)
            #testa se tarefa diariaria esta aberta e limpa
            if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 133), (47, 0, 90), tolerance=20):
                print("Tarefas diarias pausa")
                time.sleep(0.5)
                if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 133), (47, 0, 90), tolerance=20):
                    print("Tarefas diarias limpo")
                    return True
            #testa se a tarefa diaria é de conta sem upar
            if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 133), (5,0,97), tolerance=20):
                pyautogui.click(821 + x_origem, 138 + y_origem, button='left') #clique para fechar
                print("Tarefas diarias conta sem upar")
                return False

        limpa_promocao(x_origem, y_origem)

        time.sleep(1)
    return False

# #
# x_origem, y_origem = Origem_pg.x_y()
# limpa_pequeno(x_origem, y_origem)
# # limpa_jogando(x_origem, y_origem)
# limpa_total(x_origem, y_origem)
# # faz_tutorial(x_origem,y_origem)
# # # # # #iniciantes(x_origem, y_origem)
# # # # # # # # # # aviso_canto_lobby(x_origem, y_origem)
# # # limpa_total(x_origem, y_origem)
# # limpa_abre_tarefa2(x_origem, y_origem)
# limpa_promocao(x_origem, y_origem)


