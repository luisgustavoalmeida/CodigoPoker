import time
import cv2
import os
import re
import numpy
import pyautogui

import Limpa

# Desabilitar o fail-safe
pyautogui.FAILSAFE = False
import pytesseract
import Origem_pg
import IP
import difflib
from Variaveis_Globais import alterar_global_aviso_sistema

from PIL import Image


'''
--psm 0: Modo de segmentação automática com detecção de bloco.
--psm 1: Modo de segmentação automática com detecção de linha.
--psm 2: Modo de segmentação automática com detecção de palavra.
--psm 3: Modo totalmente automático com detecção de bloco.
--psm 4: Modo de segmentação de caractere único.
--psm 5: Modo de segmentação de palavra única.
--psm 6: Modo de segmentação de bloco de texto com detecção automática de linhas.
--psm 7: Modo tratamento de imagem - Linha única, sem OCR.
--psm 8: Modo tratamento de imagem - Palavra única, sem OCR.
--psm 9: Modo tratamento de imagem - Caractere único, sem OCR.
--psm 10: Modo tratamento de imagem - Tratamento de imagem por OSD.
--oem 0: Usar o Tesseract OCR Engine padrão.
--oem 1: Usar o Tesseract OCR Engine LSTM.
--oem 2: Usar o Tesseract OCR Engine com LSTM apenas para treinamento.
--oem 3: Usar o Tesseract OCR Engine com LSTM apenas para inferência.
-c tessedit_char_whitelist=0123456789: Restringir o OCR apenas aos caracteres
-c tessedit_char_blacklist=abcde: Excluir caracteres específicos do OCR. Nesse exemplo, os caracteres 'a', 'b', 'c', 'd' e 'e' serão excluídos da análise.
-l eng: Definir o idioma do OCR. Nesse exemplo, o idioma é definido como inglês. Você pode substituir "eng" pelo código de idioma adequado, como "por" para português.
-psm 11: Modo tratamento de imagem - Sparse text. Usado para texto com layout irregular ou não estruturado.
-psm 12: Modo tratamento de imagem - Sparse text com OSD. Similar ao modo 11, mas com detecção de orientação e script
-e textonly_pdf=1: Gera um arquivo PDF contendo apenas o texto extraído, sem imagens ou formatação.
-c preserve_interword_spaces=1: Preserva os espaços entre as palavras durante a extração do texto.
-c textord_tabfind_show_vlines=1: Exibe linhas verticais encontradas durante o processo de detecção de tabelas.
-c textord_tabfind_find_tables=1: Ativa a detecção automática de tabelas.
-c textord_tabfind_find_tables_recursive=1: Ativa a detecção recursiva de tabelas, útil para tabelas aninhadas.
-c tessedit_create_hocr=1: Gera um arquivo HOCR (HTML OCR) contendo o texto extraído com informações de layout e formatação.
-c hocr_font_info=1: Inclui informações sobre a fonte no arquivo HOCR gerado.
-c hocr_char_boxes=1: Inclui informações sobre os limites de cada caractere no arquivo HOCR gerado.
'''

## caminho do tesseract # C:\Program Files\Tesseract-OCR
## para funcionar corretametne o Tesseract tem que estar instalado a baixo tem links de ajuda
## https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i?newreg=e845d9256ce84548ab80ff4b5f241429
## https://github.com/UB-Mannheim/tesseract/wiki
#https://www.youtube.com/watch?v=Wx3SyNwZtsA&t=751s&ab_channel=HashtagPrograma%C3%A7%C3%A3o
# tem que coloar o arquivo "por.traineddata" de idioma de protugues no caminho C:\Program Files\Tesseract-OCR\tessdata
# Caminho para o executável do Tesseract
caminho_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# verifica se o caminho do executável do Tesseract é válido
if not os.path.isfile(caminho_tesseract):
    raise Exception("Caminho do executável do Tesseract inválido")

#x_origem, y_origem = Origem_pg.carregado_origem()
#print(x_origem, y_origem)


def OCR_regiao (regiao, config, inveter_cor, fator_ampliacao,contraste):

    try:
        # captura a imagem da tela
        imagem = pyautogui.screenshot()

        # recorta a região de interesse da imagem
        imagem_recortada = imagem.crop(regiao)

        if fator_ampliacao != 1:
            imagem_recortada = imagem_recortada.resize((imagem_recortada.width * fator_ampliacao, imagem_recortada.height * fator_ampliacao))

        # exive a imagem
        #imagem_recortada.show()

        # converte a imagem para escala de cinza
        imagem_recortada = cv2.cvtColor(numpy.asarray(imagem_recortada), cv2.COLOR_BGR2GRAY)


        # inverte as cores da imagem
        if inveter_cor:
            imagem_recortada = cv2.bitwise_not(imagem_recortada)

        if contraste != 1:  # Fator de aumento de contraste (pode ser ajustado conforme necessário)
            imagem_recortada = cv2.convertScaleAbs(imagem_recortada, alpha=contraste , beta=0)

        # cv2.imshow("Imagem", imagem_recortada)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # passa o OCR na imagem recortada
        pytesseract.pytesseract.tesseract_cmd = caminho_tesseract
        texto = pytesseract.image_to_string(imagem_recortada, config=config, lang="por")
        #colocar o arquivo de idioma "por.traineddata" no diretorio C:\Program Files\Tesseract-OCR\tessdata

        # Imprime o texto encontrado pelo OCR
        #print("texto encontrado pelo OCR: ",texto)

        # deleta a imagem recortada
        del imagem_recortada
        del imagem

        if len(texto) > 0:
            # Remove os espaços em branco no início e no final do texto
            texto = texto.strip()  # remove os espaços em branco (espaços, tabulações e quebras de linha) no início e no final da string
            # print("___________________\n")
            # print("OCR_tela. Texto encontrado pelo OCR: \n", texto)
            # print("\n___________________")
            return texto
        else:
            print("Nenhum texto foi detectado.")
            return None

    except Exception as e:
        print("Erro ao executar OCR: ", e)
        return None

def valor_fichas(x_origem, y_origem):
    print('Lendo o valor das fichas ...')
    # Define a região de interesse
    inveter_cor = True
    fator_ampliacao = 2
    contraste = 1.7
    #config = '--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789.'

    regiao_ficha = (x_origem + 69, y_origem + 7, x_origem + 135, y_origem + 26) # Ficha
    # Executa o OCR na região de interesse

    config = '--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'
    lido = OCR_regiao(regiao_ficha, config, inveter_cor, fator_ampliacao, contraste)
    #print(lido)

    if lido != None:
        lido = re.sub(r"\D+", "", lido) # remove caracteres nao numericos
        lido = lido.replace(" ", "").replace(".", "")

        try:
            lido = int(lido)
            if 500 < lido < 15000000:
                print("valor das fichas: ",lido)
                return lido
        except ValueError:
            # Lidar com a conversão falhada para um número inteiro
            print("Erro ao converter para inteiro")

    config = '--psm 6 -c tessedit_char_whitelist=0123456789.'
    lido = OCR_regiao(regiao_ficha, config, inveter_cor, fator_ampliacao, contraste)
    # print(lido)

    if lido != None:
        lido = re.sub(r"\D+", "", lido)  # remove caracteres nao numericos
        lido = lido.replace(" ", "").replace(".", "")

        try:
            lido = int(lido)
            if 500 < lido < 15000000:
                print("valor das fichas: ", lido)
                return lido
        except ValueError:
            # Lidar com a conversão falhada para um número inteiro
            print("Erro ao converter para inteiro")
            return 0
    else:
        print('valor fichas nao encontrado')
        return 0

def tempo_roleta(x_origem, y_origem):
    inveter_cor = True
    fator_ampliacao = 1
    contraste = 1
    config = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789:'
    regiao =(x_origem + 662, y_origem + 44, x_origem + 711,y_origem + 56)
    for i in range(4):
        tempo = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste)  # posição onde fica o tempo para a proxima roleta
        #print(tempo)
        if tempo is not None:
            tempo = re.sub(r"\D+", "", tempo)  # remove caracteres nao numericos
            tempo = tempo.replace(" ", "").replace(":", "")

            tempo = int(tempo)  # muda o tipo de variavel de str para int
            try:
                print("tempo: ", tempo)
                return tempo
            except:
                tempo = 0
                # print("tepo: ", tempo)
                return tempo
        time.sleep(2)
    tempo = 0
    # print("tepo: ", tempo)
    return tempo

def pontuacao_tarefas(x_origem, y_origem):
    valores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
    pontuacao = 0

    inveter_cor = True
    fator_ampliacao = 2
    contraste = 1.4
    config = '--psm 6 --oem 1 -c tessedit_char_whitelist=0123456789/'  #
    regiao = (x_origem + 777, y_origem + 516, x_origem + 829, y_origem + 536)

    for i in range(2):
        pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
        time.sleep(0.3)

        pontuacao = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste) #pontuação
        print('pontiuação 1: ', pontuacao)

        if pontuacao is not None:
            if "/200" in pontuacao:
                pontuacao = pontuacao.split("/")[0]
                pontuacao = re.sub(r"\D", "", pontuacao)  # pega apenas os numero
                pontuacao = pontuacao.replace(" ", "")
                try:
                    pontuacao = int(pontuacao)
                    if pontuacao in valores:
                        #print("pontuacao: ", pontuacao)
                        print("pontuacao: ", pontuacao)
                        return pontuacao
                except:
                    continue
        pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
        time.sleep(2)

    pontuacao = 1
    # print("pontuacao: ", pontuacao)
    return pontuacao

def tarefas_diaris_posicao1(x_origem, y_origem):
    lista = []

    # Define a região de interesse
    config = '--psm 6 --oem 1'
    inveter_cor = True
    fator_ampliacao = 1
    contraste = 1

    print('\n\n OCR tarefas diarias \n')
    regiao = (x_origem + 274, y_origem + 267, x_origem + 589, y_origem + 551)
    for i in range(1):
        pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
        time.sleep(0.2)
        # Executa o OCR na região de interesse
        #print("chama o ocr a 1 vez \n")
        texto = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste)
        if texto is not None:
            lista = remover_termos(texto)
            #print(lista)
            return lista
    return lista
def tarefas_diaris_posicao2(x_origem, y_origem):
    lista = []
    if pyautogui.pixelMatchesColor((x_origem + 707), (y_origem + 280), (87, 0, 176), tolerance=5):  # testa se tem barra de rolagem na lista de tarefas
        # print('tem barra para rolar\n')
        pyautogui.doubleClick(708 + x_origem, 419 + y_origem)  # rola para ver se a tarefa esta na segunda parte
        time.sleep(0.2)

        # Define a região de interesse
        config = '--psm 6 --oem 1'
        inveter_cor = True
        fator_ampliacao = 1
        contraste = 1

        print('\n\n OCR tarefas diarias \n')
        regiao = (x_origem + 274, y_origem + 267, x_origem + 589, y_origem + 551)
        for i in range(1):
            # Executa o OCR na região de interesse
            #print("chama o ocr a 1 vez \n")
            texto = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste)
            if texto is not None:
                lista = remover_termos(texto)
                #print(lista)
                return lista
        #print(lista)
        return lista
    return lista

def tarefas_diaris(x_origem, y_origem):
    lista = []
    lista2 = []
    # Define a região de interesse
    config = '--psm 6 --oem 1'
    inveter_cor = True
    fator_ampliacao = 1
    contraste = 1
    #config = None
    print('\n\n OCR tarefas diarias \n')
    regiao = (x_origem + 274, y_origem + 267, x_origem + 589, y_origem + 551)
    for i in range(1):
        pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
        time.sleep(0.2)
        # Executa o OCR na região de interesse
        #print("chama o ocr a 1 vez \n")
        texto = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste)
        if texto is not None:
            lista = remover_termos(texto)
            #print('teste se tem que rolar\n')
            if pyautogui.pixelMatchesColor((x_origem + 707), (y_origem + 280), (87, 0, 176), tolerance=5): # testa se tem barra de rolagem na lista de tarefas
                #print('tem barra para rolar\n')
                for j in range(1):
                    pyautogui.doubleClick(708 + x_origem, 419 + y_origem)  # rola para ver se a tarefa esta na segunda parte
                    time.sleep(0.2)
                    #print('tem coisa na lista 1')
                    #print("chama o ocr a 2 vez\n")
                    texto = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste)
                    if texto is not None:
                        lista2 = remover_termos(texto)
                        if lista2:# testa se esta vazia
                            for item in lista2:
                                if item not in lista:
                                    # inclui na lista o itens nao repitidos
                                    lista.append(item)
                            #print(lista)
                            return lista
            else:
                #print(lista)
                return lista
            time.sleep(2)
    #print(lista)
    return lista

def tarefas_diaris_trocar(x_origem, y_origem):
    for i in range(2):
        pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
        if not pyautogui.pixelMatchesColor((x_origem + 174), (y_origem + 278), (247, 230, 255), tolerance=5):  # testa se tem barra de rolagem na lista de tarefas
            print('ja foi trocada a tarefa')
            return

        para_trocar = ['Participe de um GIRE & GANHE/campeonato de eliminacao 1 vezes',
                       'Participe de um GIRE & GANHE/campeonato de eliminacao 2 vezes',
                       'Participe de um GIRE & GANHE/campeonato de eliminacao 3 vezes',
                       'Ganhar um premio em um GIRE & GANHE/torneio de eliminacao',
                       'Jogue 10 maos nas mesas OMAHA com blinds acima de 200',
                       'Jogue 20 maos nas mesas OMAHA com blinds acima de 200',
                       'Jogue 40 maos nas mesas OMAHA com blinds acima de 200',
                       'Ganhe 5 maos nas mesas OMAHA com blinds acima de 200',
                       'Ganhe 10 maos nas mesas OMAHA com blinds acima de 200',
                       'Ganhe 20 maos nas mesas OMAHA com blinds acima de 200',
                       'Ganhe 10.000 fichas nas mesas OMAHA',
                       'Ganhe 50.000 fichas nas mesas OMAHA',
                       'Ganhe 200.000 fichas nas mesas OMAHA',
                       'Jogue JACKS OR BETTER 10 vezes',
                       'Jogue JACKS OR BETTER 50 vezes',
                       'Jogue JACKS OR BETTER 100 vezes',
                       'Ganhe 10.000 fichas do JACKS OR BETTER',
                       'Ganhe 50.000 fichas do JACKS OR BETTER',
                       'Ganhe 200.000 fichas do JACKS OR BETTER',
                       'Consiga Flush ou qualquer mao superior nas mesas OMAHA',
                       'Ganhar 10 maos em uma mesa com blinds acima de 25',
                       'Jogar 20 mao em uma mesa com blinds acima de 25',
                       'Tirar Sequencia 1 vezes em mesas com blinds maiores que 25',
                       'Tirar trinca 1 vez em mesa com blinds maiores que 25',
                       'Tirar um flush ou quaquer maos superior 1 vez em mesas com blinds laiores que 25',
                       'Ganhar 10 maos em uma mesa com blinds acima de 50',
                       'Ganhar 20 maos em uma mesa com blinds acima de 50',
                       'Ganhar 30.000 fichas em mesas com blinds acima da 50',
                       'Jogar 20 mao em uma mesa com blinds acima de 50',
                       'Jogar 40 mao em uma mesa com blinds acima de 50',
                       'Tirar Flush ou qualquer mao superior 1 vez em mesas com blindes maiores que 25',
                       'Tirar Sequencia 1 vez em mesas com blinds maiores que 50',
                       'Tirar Sequencia 2 vezes em mesas com blinds maiores que 50',
                       'Tirar trinca 1 vez em mesas com blinds maiores que 50',
                       'Ganhar 20 maos em uma mesa com blinds acima de 100',
                       'Ganhar 100.000 fichas em mesas com blinds acima de 50',
                       'Ganhe 200.000 fichas em mesas com blinds acima de 100',
                       'Jogar 20 mao em uma mesa com blinds acima de 100',
                       'Jogar 40 mao em uma mesa com blinds acima de 100',
                       'Tirar Flush ou qualquer mao superior 1 vez em mesas com blindes maiores que 50',
                       'Tirar Flush ou qualquer mao superior 2 vezes em mesas com blinds maiores que 100',
                       'Tirar Sequencia 2 vezes em mesas com blinds maiores que 100',
                       'Tirar Trinca 2 vezes em mesas com blinds maiores que 100']



        # Define a região de interesse
        config = '--psm 6 --oem 1'
        inveter_cor = True
        fator_ampliacao = 1
        contraste = 1
        #config = None
        print('\n\n OCR tarefas diarias  troca\n')
        regiao0 = (x_origem + 274, y_origem + 268, x_origem + 591, y_origem + 310)
        regiao1 = (x_origem + 274, y_origem + 348, x_origem + 591, y_origem + 390)
        regiao2 = (x_origem + 274, y_origem + 428, x_origem + 591, y_origem + 470)
        regiao3 = (x_origem + 274, y_origem + 508, x_origem + 591, y_origem + 550)

        regioes = [regiao0, regiao1, regiao2, regiao3, regiao1, regiao2, regiao3]

        lista_trocar_tarefa = texto_lista = []

        for i, regiao in enumerate(regioes):

            print(i)

            if i == 4:
                pyautogui.doubleClick(708 + x_origem, 418 + y_origem)  # rola para ver se a tarefa esta na segunda parte
                time.sleep(0.2)

            texto = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste)
            if texto is not None:
                # Mapear caracteres especiais
                texto = texto.replace('ç', 'c').replace('í', 'i').replace('ê', 'e').replace('-', ' ').replace('ã', 'a')
                texto = texto.replace('\n', ' ').rstrip('.')
                print(texto)
                lista_trocar_tarefa.append(texto)

        print(lista_trocar_tarefa)

        for item in para_trocar:
            matches = difflib.get_close_matches(item, lista_trocar_tarefa, n=1, cutoff=0.985)
            if matches:
                posicao = lista_trocar_tarefa.index(matches[0])
                print(f'O item "{item}" da lista "para_trocar" é semelhante a "{matches[0]}" na posição {posicao} da lista "lista_trocar_tarefa".')

                if posicao <= 3:
                    pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
                    time.sleep(0.2)
                elif posicao > 3 :
                    pyautogui.doubleClick(708 + x_origem, 418 + y_origem)  # rola para ver se a tarefa esta na segunda parte
                    time.sleep(0.2)
                if posicao == 0:
                    pyautogui.click(x_origem + 171, y_origem + 283)  # clica na setinha
                elif posicao == 1 or posicao == 4:
                    pyautogui.click(x_origem + 171, y_origem + 363)  # clica na setinha
                elif posicao == 2 or posicao == 5:
                    pyautogui.click(x_origem + 171, y_origem + 443)  # clica na setinha
                elif posicao == 3 or posicao == 6:
                    pyautogui.click(x_origem + 171, y_origem + 523) # clica na setinha

                time.sleep(0.3)
                pyautogui.doubleClick(x_origem + 635, y_origem + 25)  # clica no tarefas diarias
                time.sleep(0.3)
                pyautogui.click(x_origem + 545, y_origem + 401)  # clica no ok
                print("tarefa tocada")
                time.sleep(1)
                break
    print('nao tem tarefa na lista de troca')

# def remover_termos(texto):
#     if texto is None:
#         return []
#
#     termos = ['rico tab bien odio ia Lana nina iodo iii ua ind ias de 50', 'ua a nn ao Cidia ias ini fundir insira E en,',
#               'unas boina ia iara ia caia so uniiitn tias', 'iu da age dai ain adiantado iria daria',
#               'ia a nao tis io dial us iria vãs,', 'TA AAm e mA a Eg NE eRr aaA', 'ESET EN) TN RI E e RR E',
#               '& 1000 PN ke. São', 'S +500 BP +11)', "em es = ou CO'", '1000 A)1000 A', '6 +2000 P+30', 'C200  BPD0 |',
#               '* +500 B 10', 'l; *1000 [A', '6 2000 B 30', 'B 500 B 10', 'C200  BPD0', '& 500 B 10', '3 +500 A/)',
#               'E 27 a/) =', '6 500 B 10', 'B 500 A/)', '& 1000 A)', 'Sum CEPE.', 'pc ai fa', '6 500 R/', 'º +500 /',
#               'E 27 a =', 'pacos ra', '4 500 Po', 'pç ai fa', 'paços ra', '& 500 [A', '& 1000 P', '1000 UA)', 'B +s00 A',
#               '& 1000 A', '1000 [A', 'pião SO', 'poça fo', '2000 B0', '1000 A)', '200 BP0', 'poça fa', 'B 500 /',
#               '2000 BP', '500 Bi)', '2000 PD', 'POA fo', '100 Pn', '200 PD', '500 Bi', '200 BP', '0 BA /', ') [A;/',
#               'poo P0', 'SM Pt', 'os“ 3', '500 A', '|||.', ') R/', ') ”', '/ -', '/ ”', 'P0', '[A', 'B0', ')', '/']
#
#     # Remover termos do texto
#     for termo in termos:
#         texto = texto.replace(termo, '')
#
#     # Remover linhas vazias entre textos
#     linhas = texto.split('\n')
#     texto_formatado = []
#     linha_vazia = False
#
#     for linha in linhas:
#         if linha.strip() == '':
#             if linha_vazia:
#                 texto_formatado.append(linha)
#                 linha_vazia = False
#             else:
#                 linha_vazia = True
#         else:
#             texto_formatado.append(linha)
#             linha_vazia = False
#
#     texto_formatado = '\n'.join(texto_formatado)
#
#     # Extrair itens de texto formatado
#     itens = texto_formatado.split('\n\n')
#
#     # Remover caracteres indesejados e formar a lista final
#     lista = [item.replace('\n', ' ').strip().rstrip('.').replace("í", "i").replace("ç", "c") for item in itens if len(item) > 34]
#
#     #print(lista)
#
#     return lista


def remover_termos(texto):
    if texto is None:
        return []

    # Substituir caracteres especiais
    texto = texto + '\n'
    texto = re.sub(r'ç', 'c', texto)
    texto = re.sub(r'í', 'i', texto)
    texto = re.sub(r'\.\n', '\n', texto)
    texto = re.sub(r'caca\n\nniquel', 'caca niquel', texto)
    texto = re.sub(r'caca\nniquel', 'caca niquel', texto)

    # print('Texto sem Ç, sem Í, sem .')
    # print(texto)

    termos =['Jogar o caca-niquel da mesa 150 vezes',
             'Jogar o caca-niquel da mesa 70 vezes',
             'Jogar o caca-niquel da mesa 10 vezes',
             'Jogar no Casino Genius Pro 100 vezes',
             'Jogar no Casino Genius Pro 50 vezes',
             'Jogar no Casino Genius Pro 10 vezes',
             'Ganhar 100.000 fichas no Casino Genius Pro',
             'Ganhar 30.000 fichas no Casino Genius Pro',
             'Ganhar 4.000 fichas no Casino Genius Pro',
             'Jogar 100 vezes nas Cartas Premiadas',
             'Jogar 50 vezes nas Cartas Premiadas',
             'Jogar 10 vezes nas Cartas Premiadas',
             'Ganhar 100.000 fichas nas Cartas Premiadas',
             'Ganhar 30.000 fichas nas Cartas Premiadas',
             'Ganhar 4.000 fichas nas Cartas Premiadas',
             'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 150 vezes',
             'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 70 vezes',
             'Apostar 20 fichas ou mais em 9 linhas do caca niquel Poker Slot 10 vezes','Consiga Flush ou qualquer mao superior nas mesas OMAHA',
                ]

    linhas = texto.split('\n')
    texto_formatado = '\n'.join([linha for linha in linhas if linha.strip() in termos or linha.strip() == ''])


    # print('Texto')
    # print(texto_formatado)

    # Extrair itens de texto formatado
    itens = texto_formatado.split('\n')

    # Remover caracteres indesejados e formar a lista final
    #lista = [item.replace('\n', ' ').strip() for item in itens if len(item) > 34]
    lista = [re.sub(r'\s+', ' ', item.replace('\n', ' ').strip()) for item in itens if len(item) > 34]

    # print('lista')
    # print(lista)
    return lista


def blind_sala(x_origem, y_origem):
    inveter_cor = True
    fator_ampliacao = 1
    contraste = 1
    config = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789KM' #
    regiao = (x_origem + 52, y_origem + 99, x_origem + 125, y_origem + 115)
    pontuacao = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste) #pontuação
    if pontuacao is not None:
        pontuacao = pontuacao.replace(" ", "")
        pontuacao = pontuacao.replace("/", "")
        # pontuacao = pontuacao.split('/')
        # pontuacao = pontuacao[0]
        # pontuacao = re.sub(r"\D", "", pontuacao)  # pega apenas os numero
        # #pontuacao = re.sub(r" ", "", pontuacao)  # remove espoços
        # pontuacao = int(pontuacao)
        # #print("pontuacao: ", pontuacao)
        return pontuacao
    else:
        pontuacao = 0

        return pontuacao

def valor_apostar(x_origem, y_origem):
    inveter_cor = False
    fator_ampliacao = 1
    contraste = 1
    config = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789' #
    regiao = (x_origem + 420, y_origem + 644, x_origem + 474, y_origem + 658)
    valor = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste) #pontuação
    if valor is not None:
        print("pontuacao: ", valor)
        valor = int(valor)
        return valor
    else:
        valor = 0
        print("pontuacao: ", valor)
        return valor

def aviso_do_sistema():
    '''Retona True se caso tivert aviso do sistema :
    Aviso do sistema
    Jocê já está logado no jogo em outra página, esta
    Sessão foi cancelada!'''

    x_origem, y_origem = Origem_pg.x_y_aviso_sistema() # tenta encontar a origem quando tem aviso do sistema
    if x_origem is not None: # se tem aviso do sistema
        inveter_cor = False
        fator_ampliacao = 1
        contraste = 1
        config = '--psm 3'
        regiao = (x_origem + 321, y_origem + 268, x_origem + 658, y_origem + 433)
        valor = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste)
        if valor is not None:
            if 'Aviso do sistema' in valor:
                print('foi encontrado um: Aviso do sistema')
                if 'cancelada' in valor:
                    print("Mesagem: ", valor)
                    alterar_global_aviso_sistema(True)
                    return True
        else:
            return False
    else:
        return False

def aviso_sistema(x_origem, y_origem):
    print('aviso_sistema')
    # testa sem tem o azul do atualizar a pagina do aviso do sistema
    resposta = "ok"
    if pyautogui.pixelMatchesColor((x_origem + 491), (y_origem + 417), (25, 117, 186), tolerance=19):
        inveter_cor = False
        fator_ampliacao = 1
        contraste = 1
        config = '--psm 3'
        regiao = (x_origem + 321, y_origem + 268, x_origem + 658, y_origem + 433)
        valor = OCR_regiao(regiao, config, inveter_cor, fator_ampliacao, contraste)
        if valor is not None:
            if 'Aviso do sistema' in valor:
                print('foi encontrado um: Aviso do sistema')
                if 'cancelada' in valor:
                    print("Mesagem: ", valor)
                    resposta = "sair da conta"
                    return True, resposta
                elif 'atualizar' in valor:
                    print("Mesagem: ", valor)
                    resposta = "erro de comunicação"
                    IP.tem_internet()
                    print('Erro de comunicação, favor atualizar a página para continuar com o processo')
                    pyautogui.press('f5')
                    print('espera 25 segundos')
                    time.sleep(25)
                    print('continua')
                    return True, resposta
                else:
                    return False, resposta
        else:
            return False, resposta
    else:
        return False, resposta

# #
# # # #         #aviso_do_sistema()
#
#x_origem, y_origem = Origem_pg.x_y()# # # # # # # # print(x_origem)
# tarefas_diaris_trocar(x_origem, y_origem)

# tarefas_diaris(x_origem, y_origem)
# # # # # # # # # print(y_origem)
# # # # # # # # # # # valor_apostar(x_origem, y_origem)
# # # # # # # # # #
# # # # # # # # # # # # valor = blind_sala(x_origem, y_origem)
# # # # # # # # # # # # print(valor)
# lista_tarefas_disponivel = tarefas_diaris(x_origem, y_origem)
# print(lista_tarefas_disponivel)
# # # # # # # # # #
# # # # tempo_roleta(x_origem, y_origem)
# # # # # # # # #
# lido = valor_fichas(x_origem, y_origem)
# print(lido)
# # # # # # # # #
#pontuacao_tarefas(x_origem, y_origem)
# # # # # #
# # # # # # #def rola_tarefa_0():
# # # # # # #pyautogui.click(708 + x_origem, 426 + y_origem, button='left')