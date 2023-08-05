import datetime
import time
import IP
import pyautogui

hora_roleta = 4  # defina o tempo disponivel para a roleta em horas
minutos_roleta = 59 # defina o tempo disponivel para a roleta em minutos

tempo_total = 18000 # 5 horas em segudos

tempo_tarefa = tempo_total - (hora_roleta * 3600) - (minutos_roleta * 60) # tempo tarefa em segundos # tempo total menos tempo não usado nas roletas
janela_tarefa = 900  # janela de 15 minutos para ir para as roletas quando esta no tarefas

faixa_tempo = 120
guias = ["R1", "R2", "R3", "R4", "R5"]
def mudar_guia(id, guia):
    hora_atual = datetime.datetime.now().time()
    # print(hora_atual)
    tempo_atual = (hora_atual.hour * 3600) + (hora_atual.minute * 60) + hora_atual.second

    # print("tempo_tarefa", tempo_tarefa)
    # print('guia: ', guia)
    # print('id: ', id)
    while tempo_atual > 86280: # se maior que 23:58:00
        print('espera virar 0h')
        time.sleep(10)
        hora_atual = datetime.datetime.now().time()
        tempo_atual = (hora_atual.hour * 3600) + (hora_atual.minute * 60) + hora_atual.second

    if (guia == "R1") or (guia == "R2") or (guia == "R3") or (guia == "R4") or (guia == "R5"):
        if id == "": # se a cabou o R vai para tarefa
            if tempo_tarefa > 0: # se tem algim tempo destinado as tarefas
                print('Fim do R, vai para as tarefas')
                # T1
                guia_atual = "T1"
                print('vai para a guia', guia_atual)
                return guia_atual
            elif tempo_tarefa <= 0:
                #print('hora teste 3')
                IP.ip_troca_agora()
                while True:
                    hora_atual = datetime.datetime.now().time()
                    tempo_atual = (hora_atual.hour * 3600) + (hora_atual.minute * 60) + hora_atual.second
                    print('Fim da lista, espera horario para iniciar novo R\n Hora: ',hora_atual)
                    time.sleep(30)

                    for j in range(0, 5):

                        inicio_faixa = tempo_total * j
                        fim_faixa = inicio_faixa + faixa_tempo

                        if inicio_faixa <= tempo_atual <= fim_faixa:
                            print("tempo atigido, inicia novo R")
                            for i, guia_atual in enumerate(guias):

                                print("gia atual:", guia_atual)
                                if (i * tempo_total) <= tempo_atual <= ((i + 1) * tempo_total - tempo_tarefa):
                                    print('vai para a guia',guia_atual)
                                    return guia_atual

        else:
            for i, guia_atual in enumerate(guias):
                # print("gia atual:", guia_atual)
                if (i * tempo_total) <= tempo_atual <= ((i + 1) * tempo_total - tempo_tarefa):
                    print('vai para a guia', guia_atual)
                    return guia_atual
            # T1
            guia_atual = "T1"
            print('vai para a guia', guia_atual)
            return guia_atual

    elif guia == "T1":
        if id == "":
            print('Fim do tarefas, espera a hora para começar os Rs')
            IP.ip_troca_agora()
            while True:
                hora_atual = datetime.datetime.now().time()
                tempo_atual = (hora_atual.hour * 3600) + (hora_atual.minute * 60) + hora_atual.second
                print('Fim da lista, espera pelo horario para iniciar novo R. \n Hora: ', hora_atual)
                time.sleep(30)
                for j in range(0, 5):
                    inicio_faixa = tempo_total * j
                    fim_faixa = inicio_faixa + faixa_tempo
                    if inicio_faixa <= tempo_atual <= fim_faixa:
                        print("tempo atigido, inicia novo R")
                        for i, guia_atual in enumerate(guias):
                            print("gia atual:", guia_atual)
                            if (i * tempo_total) <= tempo_atual <= ((i + 1) * tempo_total - tempo_tarefa):
                                print('vai para a guia', guia_atual)
                                return guia_atual
        else:
            for j in range(0, 5):
                inicio_faixa = tempo_total * j
                fim_faixa = inicio_faixa + faixa_tempo
                if inicio_faixa <= tempo_atual <= fim_faixa:
                    print("tempo atigido, inicia novo R")
                    for i, guia_atual in enumerate(guias):
                        if (i * tempo_total) <= tempo_atual <= ((i + 1) * tempo_total - tempo_tarefa):
                            print('vai para a guia', guia_atual)
                            return guia_atual
                # T1
            guia_atual = "T1"
            print('vai para a guia', guia_atual)
            return guia_atual

    else:
        for i, guia_atual in enumerate(guias):
            # print("gia atual:", guia_atual)
            if (i * tempo_total) <= tempo_atual <= ((i + 1) * tempo_total - tempo_tarefa):
                print('vai para a guia', guia_atual)
                return guia_atual
        # T1
        guia_atual = "T1"
        print('vai para a guia', guia_atual)
        return guia_atual

def fim_tempo_tarefa():
    hora_atual = datetime.datetime.now().time()
    tempo_atual = (hora_atual.hour * 3600) + (hora_atual.minute * 60) + hora_atual.second
    if tempo_atual > 86280:
        print('interrompe a tarefa e vai pra o R1, proximo das 0h')
        return True

    for i in range(0, 5):
        inicio_faixa = tempo_total * i
        fim_faixa = inicio_faixa + faixa_tempo
        if inicio_faixa <= tempo_atual <= fim_faixa:
            print('interrompe a tarefa e vai pra o R')
            return True
    return False

# guia = "R1"
# id = ""
# #
# guia = mudar_guia(id, guia)
# print(guia)

