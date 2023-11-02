
import Firebase
import pyautogui
import time
import Tarefas
import Slot
import Cartas
import Genius
import Limpa
import OCR_tela
import Mesa


def solot_joga_vezes_upando(x_origem, y_origem):
    Firebase.confirmacao_comando_resposta('Iniciando Slote')
    joga_vezes = True
    cont_jogadas = 0
    continua_jogando = True

    Limpa.limpa_total(x_origem, y_origem)

    while continua_jogando: # permanece joghando cartas premiadas ate nao ter mais a mição jogar x vezes

        slot_aberto = Slot.abre_slot(x_origem, y_origem, joga_vezes)

        if slot_aberto:
            print('espera girar na cor certa')
            for i in range(20):
                #espera poder clicar no girar
                if pyautogui.pixelMatchesColor((x_origem + 922), (y_origem + 609), (216, 17, 2), tolerance=5):
                    pyautogui.doubleClick(x_origem + 922, y_origem + 609)  # clica em girar
                    print("clicar no girar")
                    cont_jogadas += 1
                    status_upando = 'Jogando Slote ' + str(cont_jogadas)
                    Firebase.confirmacao_comando_resposta(status_upando)
                    break
                time.sleep(0.3)

        status_tarefa = Tarefas.recolher_tarefa_upando(x_origem, y_origem)
        print(status_tarefa)
        if status_tarefa == "Não tem missão":
            continua_jogando = True
        elif status_tarefa == "Recolhido":
            continua_jogando = False
        else:
            continua_jogando = False

        if not continua_jogando:
            print("FIM")
            Limpa.limpa_total(x_origem, y_origem)
            Firebase.confirmacao_comando_resposta('Terminou Slote')
            return 'Terminou Slote'
    return


def genius_joga_vezes_upando(x_origem, y_origem):
    Firebase.confirmacao_comando_resposta('Iniciando Genius')
    cont_jogadas = 0
    continua_jogando = True
    regiao = (473 + x_origem, 101 + y_origem, 20, 32)  # (x, y, largura, altura)
    imagem1 = r'Imagens\Genius\tempo6.png'
    precisao = 0.9

    Limpa.limpa_total(x_origem, y_origem)

    while continua_jogando: # permanece joghando cartas premiadas ate nao ter mais a mição jogar x vezes

        genius_aberto = Genius.abre_genius(x_origem, y_origem)

        if genius_aberto:
            print('espera espera pelo valor de tempo certo')

            for i in range(80):
                #espera o time
                posicao = Genius.localizar_imagem(imagem1, regiao, precisao)
                if posicao is not None:  # Verifica se a imagem foi encontrada
                    print("faz a aposta")
                    if pyautogui.pixelMatchesColor((x_origem + 449), (y_origem + 655), (193, 119, 70), tolerance=5):
                        # Testa se tem uma setinha para cima
                        pyautogui.click(x_origem + 603, y_origem + 223)  # clica em Staci ganha
                        cont_jogadas += 1
                        status_upando = 'Jogando Slote ' + str(cont_jogadas)
                        Firebase.confirmacao_comando_resposta(status_upando)
                        print('espera o tempo passar ate sair o premio')

                    else:
                        for i in range(5):
                            pyautogui.click(x_origem + 603, y_origem + 223)  # clica em Staci ganha
                            time.sleep(0.1)
                        Firebase.confirmacao_comando_resposta('Jogou a quantia gatis')

                    time.sleep(10)
                    break

                time.sleep(0.3)

            status_tarefa = Tarefas.recolher_tarefa_upando(x_origem, y_origem)
            print(status_tarefa)
            if status_tarefa == "Não tem missão":
                continua_jogando = True
            elif status_tarefa == "Recolhido":
                continua_jogando = False
            else:
                continua_jogando = False

            if not continua_jogando:
                print("FIM")
                Limpa.limpa_total(x_origem, y_origem)
                Firebase.confirmacao_comando_resposta('Terminou Genius')
                return 'Terminou Genius'
    return


def cartas_premidas_joga_vezes_upando(x_origem, y_origem):
    Firebase.confirmacao_comando_resposta('Iniciando Cartas')
    cont_jogadas = 0
    continua_jogando = True

    Limpa.limpa_total(x_origem, y_origem)

    while continua_jogando: # permanece joghando cartas premiadas ate nao ter mais a mição jogar x vezes
        cartas_aberto = Cartas.abre_cartas_premidas(x_origem, y_origem)  # abre o cartas premidas
        confirmar = False
        if cartas_aberto:

            print("tem cartas vezes")
            for i in range(100):
                print('espera as cartas virado para baixo')
                #espera ter as cartas virado para baixo lado marrom para cima
                if pyautogui.pixelMatchesColor((x_origem + 490), (y_origem + 239), (111, 26, 37), tolerance=10):
                    print("ta com as cartas viradas para baixo")
                    if pyautogui.pixelMatchesColor((x_origem + 394), (y_origem + 483), (239, 231, 212), tolerance=10): # Teste se tem 1000 fichas gratis
                        for i in range(10):
                            pyautogui.click(x_origem + 658, y_origem + 341)  # clica nas cartas vermelhas
                            time.sleep(0.1)
                        Firebase.confirmacao_comando_resposta('Jogou a quantia gatis')

                    pyautogui.click(x_origem + 658, y_origem + 341) # clica nas cartas vermelhas
                    for i in range(100):
                        #testa se tem a ficha de 200 verde na posição correta
                        if pyautogui.pixelMatchesColor((x_origem + 641), (y_origem + 344), (193, 46, 47), tolerance=5):
                            print('200 fichas no lugar')
                            pyautogui.doubleClick(x_origem + 711, y_origem + 422)  #clica em comfirmar
                            cont_jogadas += 1
                            status_upando = 'Jogando Cartas ' + str(cont_jogadas)
                            Firebase.confirmacao_comando_resposta(status_upando)
                            confirmar = True
                            break

                if confirmar:
                    break

                time.sleep(0.3)

        # espera ate as cartas virartem para cima, ficar brancas
        for i in range(20):
            if pyautogui.pixelMatchesColor((x_origem + 440), (y_origem + 200), (252, 253, 253), tolerance=5):
                break
            time.sleep(0.3)
        # se nao virou as cartas da um limpa todal para desagarrar possivel falhar na hora de trocar ip
        if not(pyautogui.pixelMatchesColor((x_origem + 440), (y_origem + 200), (252, 253, 253), tolerance=5)):
            if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                return "sair da conta"

        status_tarefa = Tarefas.recolher_tarefa_upando(x_origem, y_origem)
        print(status_tarefa)
        if status_tarefa == "Não tem missão":
            continua_jogando = True
        elif status_tarefa == "Recolhido":
            continua_jogando = False
        else:
            continua_jogando = False

        if not continua_jogando:
            print("FIM")
            Limpa.limpa_total(x_origem, y_origem)
            Firebase.confirmacao_comando_resposta('Terminou Cartas')
            return 'Terminou Cartas'

    return


def levantar_mesa(x_origem, y_origem):
    sentado = "manda levantar"
    for i in range(50):
        if pyautogui.pixelMatchesColor((x_origem + 619), (y_origem + 631), (67, 89, 136), tolerance=1):  # testa se esta dentro da mesa
            print('Não esta sentado')
            sentado = "levantou da mesa"
            Firebase.confirmacao_comando_resposta(sentado)
            break

        if (pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (27, 92, 155),  tolerance=19)
                or pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (19, 64, 109),  tolerance=19)):  # testa se esta dentro da mesa

            pyautogui.click(947 + x_origem, 78 + y_origem)#setinha
            time.sleep(0.3)
            pyautogui.click(925 + x_origem, 204 + y_origem)#Levantar

            if pyautogui.pixelMatchesColor((x_origem + 455), (y_origem + 417), (25, 116, 184), tolerance=19):  # aviso do sistema "tem certesa de que quer sair da mesa?"
                pyautogui.click(641 + x_origem, 278 + y_origem)  # clica no x do aviso do sistema "tem certesa de que quer sair da mesa?"
                print("aviso do sistema")
                time.sleep(0.3)
                pyautogui.click(947 + x_origem, 78 + y_origem)  # setinha
                time.sleep(0.3)
                pyautogui.click(925 + x_origem, 204 + y_origem)  # Levantar

    return sentado


def passa_ate_lv7(x_origem, y_origem): # para se fazer tarefas
    #Firebase.confirmacao_comando_resposta("Jogando mesa")
    level_conta = 0
    status_comando = "Jogando mesa"
    so_tem_gire = "continua"

    while True:
        comando = Firebase.comando_escravo
        if comando == "Levanta":
            status_comando = levantar_mesa(x_origem, y_origem)
            return

        Firebase.confirmacao_comando_resposta(status_comando)

        Limpa.limpa_jogando(x_origem, y_origem)

        status_tarefas = Tarefas.recolher_tarefa_upando(x_origem, y_origem)

        if status_tarefas == "Recolhido":
            lista, so_tem_gire = OCR_tela.tarefas_diaris_upando(x_origem, y_origem)

        if pyautogui.pixelMatchesColor((x_origem + 480), (y_origem + 650), (43, 16, 9), tolerance=3):
            pyautogui.click((x_origem + 640), (y_origem + 72)) # clica para passar animação de recolher

        if pyautogui.pixelMatchesColor((x_origem + 619), (y_origem + 631), (67, 89, 136), tolerance=1):  # testa se esta sentado
            print("Levantou")
            print("Emvia um comando para levantar os outros escravos")
            Firebase.comando_coleetivo_escravo_escravo("Levanta")
            return

        else:

            if level_conta < 7:
                # se nao esta com v azul dentro do quadrado branco e se esta com quadrado branco
                if ((not pyautogui.pixelMatchesColor((x_origem + 333), (y_origem + 610), (59, 171, 228), tolerance=1))
                        and (pyautogui.pixelMatchesColor((x_origem + 333), (y_origem + 610), (255, 255, 255), tolerance=1))):
                    pyautogui.click((x_origem + 337), (y_origem + 605))
                    # time.sleep(0.3)
                    print("Passou")
                    level_conta = OCR_tela.level_conta(x_origem, y_origem)
                    status_comando = "Passou" + " " + so_tem_gire

                elif pyautogui.pixelMatchesColor((x_origem + 480), (y_origem + 650), (255, 255, 255), tolerance=1): # testa se tem area branca
                    pyautogui.click((x_origem + 337), (y_origem + 605))
                    print("Pagou")
                    level_conta = OCR_tela.level_conta(x_origem, y_origem)
                    status_comando = "Pagou" + " " + so_tem_gire

            else:
                if pyautogui.pixelMatchesColor((x_origem + 480), (y_origem + 650), (255, 255, 255), tolerance=1): # testa se tem area branca
                    pyautogui.click((x_origem + 528), (y_origem + 605))  # clica no correr
                    print("Correu")
                    status_comando = "Correu" + " " + so_tem_gire


def solot_genius_cartas_upando(x_origem, y_origem, blind):
    solot_joga_vezes_upando(x_origem, y_origem)
    genius_joga_vezes_upando(x_origem, y_origem)
    cartas_premidas_joga_vezes_upando(x_origem, y_origem)
    Mesa.escolher_blind(x_origem, y_origem, blind)

def genius_cartas_upando(x_origem, y_origem, blind):
    genius_joga_vezes_upando(x_origem, y_origem)
    cartas_premidas_joga_vezes_upando(x_origem, y_origem)
    Mesa.escolher_blind(x_origem, y_origem, blind)

def cartas_upando(x_origem, y_origem, blind):
    cartas_premidas_joga_vezes_upando(x_origem, y_origem)
    Mesa.escolher_blind(x_origem, y_origem, blind)