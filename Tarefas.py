

import pyautogui
# Desabilitar o fail-safe
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0
import os
import time
import OCR_tela
import datetime
import Limpa
import Origem_pg
# from fuzzywuzzy import fuzz #pip install fuzzywuzzy
# import Levenshtein #pip install python-Levenshtein


tarefas_fazer = (#caça-níquel da mesa
                'Jogar o caca-niquel da mesa 150 vezes',
                'Jogar o caca-niquel da mesa 70 vezes',
                'Jogar o caca-niquel da mesa 10 vezes',
                'Ganhar 100.000 fichas no caca niquel da mesa',
                'Ganhar 30.000 fichas no caca niquel da mesa',
                'Ganhar 10.000 fichas no caca niquel da mesa',
                # Casino Genius
                'Jogar no Casino Genius Pro 100 vezes',
                'Jogar no Casino Genius Pro 50 vezes',
                'Jogar no Casino Genius Pro 10 vezes',
                'Ganhar 100.000 fichas no Casino Genius Pro',
                'Ganhar 30.000 fichas no Casino Genius Pro',
                'Ganhar 4.000 fichas no Casino Genius Pro',
                #Cartas Premiadas
                'Jogar 100 vezes nas Cartas Premiadas',
                'Jogar 50 vezes nas Cartas Premiadas',
                'Jogar 10 vezes nas Cartas Premiadas',
                'Ganhar 100.000 fichas nas Cartas Premiadas',
                'Ganhar 30.000 fichas nas Cartas Premiadas',
                'Ganhar 4.000 fichas nas Cartas Premiadas',
                #Poker Slot
                'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 150 vezes',
                'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 70 vezes',
                'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 10 vezes',
                'Ganhar 100.000 fichas no caca niquel slot poker',
                'Ganhar 30.000 fichas no caca niquel slot poker',
                'Ganhar 10.000 fichas no caca niquel slot poker')

dicionario_tarefas_fazer = {#caça-níquel da mesa
                            'Jogar o caca-niquel da mesa 150 vezes': 30,
                            'Jogar o caca-niquel da mesa 70 vezes': 20,
                            'Jogar o caca-niquel da mesa 10 vezes': 10,
                            # Casino Genius
                            'Jogar no Casino Genius Pro 100 vezes': 30,
                            'Jogar no Casino Genius Pro 50 vezes': 20,
                            'Jogar no Casino Genius Pro 10 vezes': 10,
                            'Ganhar 100.000 fichas no Casino Genius Pro': 30,
                            'Ganhar 30.000 fichas no Casino Genius Pro': 20,
                            'Ganhar 4.000 fichas no Casino Genius Pro': 10,
                            #Cartas Premiadas
                            'Jogar 100 vezes nas Cartas Premiadas': 30,
                            'Jogar 50 vezes nas Cartas Premiadas': 20,
                            'Jogar 10 vezes nas Cartas Premiadas': 10,
                            'Ganhar 100.000 fichas nas Cartas Premiadas': 30,
                            'Ganhar 30.000 fichas nas Cartas Premiadas': 20,
                            'Ganhar 4.000 fichas nas Cartas Premiadas': 10,
                            #Poker Slot
                            'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 150 vezes': 30,
                            'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 70 vezes': 20,
                            'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 10 vezes': 10,
                            }

dicionario_tarefas_fazer_sabado = {#caça-níquel da mesa
                            'Jogar o caca-niquel da mesa 150 vezes': 30,
                            'Jogar o caca-niquel da mesa 70 vezes': 20,
                            'Jogar o caca-niquel da mesa 10 vezes': 10,
                            'Ganhar 100.000 fichas no caca niquel da mesa': 30,
                            'Ganhar 30.000 fichas no caca niquel da mesa': 20,
                            'Ganhar 10.000 fichas no caca niquel da mesa': 10,
                            # Casino Genius
                            'Jogar no Casino Genius Pro 100 vezes': 30,
                            'Jogar no Casino Genius Pro 50 vezes': 20,
                            'Jogar no Casino Genius Pro 10 vezes': 10,
                            'Ganhar 100.000 fichas no Casino Genius Pro': 30,
                            'Ganhar 30.000 fichas no Casino Genius Pro': 20,
                            'Ganhar 4.000 fichas no Casino Genius Pro': 10,
                            #Cartas Premiadas
                            'Jogar 100 vezes nas Cartas Premiadas': 30,
                            'Jogar 50 vezes nas Cartas Premiadas': 20,
                            'Jogar 10 vezes nas Cartas Premiadas': 10,
                            'Ganhar 100.000 fichas nas Cartas Premiadas': 30,
                            'Ganhar 30.000 fichas nas Cartas Premiadas': 20,
                            'Ganhar 4.000 fichas nas Cartas Premiadas': 10,
                            #Poker Slot
                            'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 150 vezes': 30,
                            'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 70 vezes': 20,
                            'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 10 vezes': 10,
                            'Ganhar 100.000 fichas no caca niquel slot poker': 30,
                            'Ganhar 30.000 fichas no caca niquel slot poker': 20,
                            'Ganhar 10.000 fichas no caca niquel slot poker': 10}


def localizar_imagem(imagem, regiao, precisao): # ainda tem que implementar
    try:
        posicao = pyautogui.locateOnScreen(imagem, region=regiao, confidence=precisao, grayscale=True)
        return posicao
    except :
        print("Ocorreu um erro ao localizar a imagem")
        time.sleep(2)
        return None

def comparar_listas(x_origem, y_origem, dia_da_semana):

    lista = OCR_tela.tarefas_diaris(x_origem, y_origem)
    lista_do_dia = []

    pontos_disponiveis = 0
    if dia_da_semana == 5:
        for chave in dicionario_tarefas_fazer_sabado:
            if chave in lista:
                pontos_disponiveis += dicionario_tarefas_fazer_sabado[chave]
                lista_do_dia.append(chave)
    else:
        for chave in dicionario_tarefas_fazer:
            if chave in lista:
                pontos_disponiveis += dicionario_tarefas_fazer[chave]
                lista_do_dia.append(chave)

    print(lista_do_dia)
    print("Pontos disponiveis para serem feritos: ", pontos_disponiveis)

    return lista_do_dia, pontos_disponiveis



# def comparar_listas(x_origem, y_origem):
#     lista_comum = []
#     lista_tarefas_disponivel = OCR_tela.tarefas_diaris(x_origem, y_origem)
#     print('lista lida pelo OCR: \n', lista_tarefas_disponivel)
#
#     lista_comum = list(set(tarefas_fazer).intersection(lista_tarefas_disponivel))
#
#     print('\n---------------------------------------\n')
#
#     print("Tarefas para serem feitas: \n",lista_comum)
#
#     print('\n---------------------------------------\n')
#
#     return lista_comum

def comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem):
    lista_comum = []
    continua_jogando = False
    lista_tarefas_disponivel = OCR_tela.tarefas_diaris_posicao1(x_origem, y_origem)

    for item in tarefas_fazer:
        if item in lista_tarefas_disponivel:
            print('comparar_listas_fazendo_tarefa', item)
            continua_jogando = True
            return continua_jogando, item

    lista_tarefas_disponivel = OCR_tela.tarefas_diaris_posicao2(x_origem, y_origem)

    for item in tarefas_fazer:
        if item in lista_tarefas_disponivel:
            print('comparar_listas_fazendo_tarefa', item)
            continua_jogando = True
            return continua_jogando, item

    return continua_jogando, None



    # if lista_tarefas_disponivel is not None:
    #     lista_comum = list(set(tarefas_fazer).intersection(lista_tarefas_disponivel))
    #
    #     print("Tarefas para serem feitas: \n")
    #     for item in lista_comum:
    #         print(item)
    #         print('continua jogando')
    #         continua_jogando = True
    #         return continua_jogando
    #     print('para de jogar')
    #     return continua_jogando



def comparar_imagens(tarefas_fazer, x_origem, y_origem):

    lista_comum = []
    regiao_tarefas = (x_origem + 270, y_origem + 260, 325, 290)
    #print(regiao_tarefas)
    caminho_tarefas = "Imagens\\TarefasFazer\\"
    for i in range(2):
        for nome_tarefa in tarefas_fazer:
            caminho_tarefa = os.path.join(caminho_tarefas + nome_tarefa + ".png")
            #print(caminho_tarefa)

            tarefa_encontrada = pyautogui.locateOnScreen(caminho_tarefa, region=regiao_tarefas, confidence=0.985, grayscale=True)
            if tarefa_encontrada is not None:
                lista_comum.append(nome_tarefa)
        pyautogui.click(708 + x_origem, 419 + y_origem, button='left')
        time.sleep(0.2)

    return lista_comum


def comparar_imagens_tarefa(tarefas_fazer, x_origem, y_origem):# procura as tares, faz baseado na imagems que sao passada na lista

    lista_comum = []
    regiao_tarefas = (x_origem + 270, y_origem + 260, 342, 290)
    precisao =0.94
    #print(regiao_tarefas)
    caminho_tarefas = "Imagens\\TarefasFazer\\"
# assim que encontra a plimeira tarefa da lista ele retona como True
    for nome_tarefa in tarefas_fazer:
        caminho_tarefa = os.path.join(caminho_tarefas + nome_tarefa + ".png")
        #print(caminho_tarefa)
        tarefa_encontrada = localizar_imagem(caminho_tarefa, regiao_tarefas, precisao)
        if tarefa_encontrada is not None:
            return True, nome_tarefa
    pyautogui.click(708 + x_origem, 419 + y_origem, button='left') # rola para ver se a tarefa esta na segunda parte
    time.sleep(0.2)
    for nome_tarefa in tarefas_fazer:
        caminho_tarefa = os.path.join(caminho_tarefas + nome_tarefa + ".png")
        #print(caminho_tarefa)
        tarefa_encontrada = localizar_imagem(caminho_tarefa, regiao_tarefas, precisao)
        if tarefa_encontrada is not None:
            return True, nome_tarefa
    return False, None



def recolher_tarefa(x_origem, y_origem):
    posicao_recolher_tarefa_y = (542, 463, 384, 305)
    clique_recolher = []

    if pyautogui.pixelMatchesColor((x_origem + 670), (y_origem + 305), (59, 188, 21), tolerance=30):  # testa se tem que recolher "verde" apartir da primeira linha
        print("Tem missão para recolher")
        for recolher_y in posicao_recolher_tarefa_y:
            #print(recolher_y)
            if pyautogui.pixelMatchesColor((x_origem + 670), (y_origem + recolher_y), (59, 188, 21), tolerance=30):  # testa se tem que recolher "verde"
                clique_recolher.append(recolher_y)  # adiciona as coordenada de y que deve ser clicadas


    elif pyautogui.pixelMatchesColor((x_origem + 590), (y_origem + 280), (171, 13, 143), tolerance=30):  # testa se tem que recolher tendo missão extra
        print('missão extra')
        if pyautogui.pixelMatchesColor((x_origem + 670), (y_origem + 384), (59, 188, 21), tolerance=30):  # testa se tem que recolher "verde" apartir da segunda linha
            print("Tem missão para recolher")
            for recolher_y in posicao_recolher_tarefa_y:
                #print(recolher_y)
                if pyautogui.pixelMatchesColor((x_origem + 670), (y_origem + recolher_y), (59, 188, 21), tolerance=30):#testa se tem que recolher "verde"
                    clique_recolher.append(recolher_y) # adiciona as coordenada de y que deve ser clicadas

    if clique_recolher:
        for recolhe in clique_recolher:
            pyautogui.doubleClick(x_origem + 670, y_origem + recolhe)  # clica no recolher
        time.sleep(1)

    return


def meta_tarefas(x_origem, y_origem):
    pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
    # chma a funçao para ver a pontuação acumilada nas tarefas
    pontuacao_tarefas = int(OCR_tela.pontuacao_tarefas(x_origem, y_origem))

    # Obter a data atual
    data_atual = datetime.date.today()
    # Obter o dia da semana (0 segunda, 1 terça, 2 quarta, 3 quinta, 4 sexta, 5 sabado, 6 domingo)
    dia_da_semana = data_atual.weekday()

    # dicionarios com os dias da semana e com os valores de meta de cada dia
    metas = {0: 150, 1: 160, 2: 170, 3: 180, 4: 190, 5: 200, 6: 140}
    # busca os objetivos basenado no dia da semana
    meta_dia = metas[dia_da_semana]
    # compara a pontuação atual com o objetivo do dia para saber se foi batido ou nao
    print("meta do dia:", meta_dia, ",pontos atigidos:", pontuacao_tarefas)
    # dicionarios com os dias da semana e com os valores de meta de cada dia
    if pontuacao_tarefas >= meta_dia:
        print("Meta atingida")
        return True, pontuacao_tarefas
    else:
        print('Meta não atingida')
        return False, pontuacao_tarefas

def tem_tarefa_para_recolher(x_origem, y_origem, id, senha, url, navegador):
    if pyautogui.pixelMatchesColor((x_origem + 627), (y_origem + 35), (228, 194, 31), tolerance=30):  # testa se tem que recolher icone das tarefas amarelo
        Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)
        recolher_tarefa(x_origem, y_origem)
        Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)
        meta, pontos = meta_tarefas(x_origem, y_origem)
        return meta, pontos

    else:
        return None, None

#
# #
# x_origem, y_origem = Origem_pg.x_y()
#
# comparar_listas(x_origem, y_origem)

# tarefas_fazer_vezes2 = ('Jogar 100 vezes nas Cartas Premiadas',
#                            'Jogar 50 vezes nas Cartas Premiadas',
#                            'Jogar 10 vezes nas Cartas Premiadas')
# # tarefas_fazer2 = ('Jogar o caca-niquel da mesa 150 vezes', 'Jogar o caca-niquel da mesa 70 vezes', 'Jogar o caca-niquel da mesa 10 vezes')
# continua_jogando, tarefa = comparar_imagens_tarefa(tarefas_fazer_vezes2, x_origem, y_origem)
# print(tarefa)
# # # # #meta_tarefas(x_origem, y_origem)
# # # #
# # # #
# # # #
# # # # # recolher_tarefa(x_origem, y_origem)
# # # meta_tarefas(x_origem, y_origem)
# # # # x_origem, y_origem = Origem_pg.x_y()
# # # # # # # # Comparar as listas e obter os itens em comum
#comparar_listas(x_origem, y_origem)


# # # # # #
# # # itens_comuns= comparar_imagens(tarefas_fazer, x_origem, y_origem)
# # # print("Itens em comum:")
# # # print(itens_comuns)
# # for item in itens_comuns:
# #     print(item)