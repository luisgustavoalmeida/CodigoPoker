import time

import pyautogui

import Origem_pg

import Mesa

import Limpa


# posicao_cartas_mesa = ({3: (518, 327)}, {4: (585, 327)}, {5: (652, 327)})

def apostar_pagar(x_origem, y_origem):
    jogou_uma_vez = False
    # quando se tem que apostar, testa se tem a barra de ajustar a aposta
    if pyautogui.pixelMatchesColor((x_origem + 513), (y_origem + 647), (180, 202, 224), 5):
        # se tem a barra de ajustar a aposta

        # testar se é a ultima carta
        if pyautogui.pixelMatchesColor((x_origem + 652), (y_origem + 327), (249, 249, 249), 5):
            print('ultima carta')
            # cliaca no final da barra
            pyautogui.click((x_origem + 660), (y_origem + 647))

        else:
            print('NÂO é a ultima carta')
            # clicar no meio da barra de ajuste
            pyautogui.click((x_origem + 595), (y_origem + 647))

        for _ in range(150):
            #  teste se a barra foi deslocada
            if not pyautogui.pixelMatchesColor((x_origem + 652), (y_origem + 327), (184, 212, 237), 5):
                break
            time.sleep(0.01)
        # clica no apostar
        print('tem que aposta')
        pyautogui.click((x_origem + 380), (y_origem + 650))
        jogou_uma_vez = True
        return jogou_uma_vez

    elif pyautogui.pixelMatchesColor((x_origem + 342), (y_origem + 601), (255, 255, 255), 5):
        # branco de interceção de pagar e passar sem o quadrado brando
        print('tem que pagar')
        # se nao tem a barra de ajusta a posta e se tem o pagar
        pyautogui.click((x_origem + 380), (y_origem + 604))
        jogou_uma_vez = True
        return jogou_uma_vez
    return jogou_uma_vez


def passa_passa(x_origem, y_origem):
    if pyautogui.pixelMatchesColor((x_origem + 338), (y_origem + 603), (255, 255, 255), 5):
        # branco de interceção do pagar, passar e do quadrado brando
        pyautogui.click((x_origem + 338), (y_origem + 603))


def mesa_recolher(x_origem, y_origem, numero_jogadas=3):
    print('mesa_recolher')

    global lista_salas_jogar
    valor_aposta1 = 100
    valor_aposta2 = 50
    sentou = False
    continua_jogando = True
    jogou_uma_vez = False
    apostar = False
    cont_jogou = 0

    cont_limpa_jogando = 0

    posicao_barra, posicao_lista = list(blinb_rolagem[blind])[-2:]

    while continua_jogando:  # permanece joghando

        # print('joga mesa')

        if cont_limpa_jogando > 40:
            cont_limpa_jogando = 0
            Limpa.fecha_tarefa(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)
        cont_limpa_jogando += 1

        # print("Sentou :", sentou)

        if jogou_uma_vez:
            if pyautogui.pixelMatchesColor((x_origem + 663), (y_origem + 538), (86, 169, 68), tolerance=20):
                # testa se apareceu as mensagens verdes na parte de baixo
                cont_jogou += 1
                print("Jogou vezes igua a: ", cont_jogou)

                if cont_jogou == numero_jogadas:
                    apostar = True
                jogou_uma_vez = False

                if apostar and cont_jogou > numero_jogadas:
                    apostar == False

                if not cadeiras_celular(x_origem, y_origem):
                    print('Sair da mesa fim da jogada com humanos na mesa')
                    humano = True
        else:
            if pyautogui.pixelMatchesColor((x_origem + 663), (y_origem + 538), (86, 169, 68), tolerance=20):
                for i in range(20):
                    time.sleep(0.3)
                    if not cadeiras_celular(x_origem, y_origem):
                        print('Sair da mesa fim da jogada com humanos na mesa')
                        humano = True
                        break

        if apostar:
            print('\n\n         Hora de apostar         \n\n')
            jogou = apostar_pagar(x_origem, y_origem)
            if jogou:
                jogou_uma_vez = True
        else:
            (jogou, apostar) = passa_corre_joga(x_origem, y_origem, valor_aposta1, valor_aposta2)
            if jogou:
                jogou_uma_vez = True

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    Limpa.limpa_jogando(x_origem, y_origem)
    return


x_origem, y_origem = Origem_pg.x_y()
apostar_pagar(x_origem, y_origem)
