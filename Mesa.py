
import socket
import time
import pyautogui
# Desabilitar o fail-safe
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0
import Limpa
import OCR_tela
import IP
import Tarefas
import HoraT

lista_salas_niquel = ('1537',  '1538', '1546', '1542', '1545', '1543', '1541', '1540', '1536', '1535', '1769', '1768',
                      '1767', '1766', '1765',)

def localizar_imagem(imagem, regiao, precisao):
    try:
        posicao = pyautogui.locateOnScreen(imagem, region=regiao, confidence=precisao, grayscale=True)
        return posicao
    except:
        print("Ocorreu um erro ao localizar a imagem")
        time.sleep(2)
        return None

def cadeiras_livres(x_origem, y_origem):
    dicionario_cadeira = {'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)}
    cadeiras_livres = 0
    for chave, valor in dicionario_cadeira.items():
        print("chave: ", chave, "  valor :", valor)
        cadeira_x, cadeira_y = valor
        cor_seta_amarela = (254, 207, 0)
        if pyautogui.pixelMatchesColor((x_origem + cadeira_x), (y_origem + cadeira_y), (cor_seta_amarela), tolerance=10):
            cadeiras_livres += 1
            print(cadeiras_livres)
    print("esta mesa tem: ", cadeiras_livres, " cadeiras livres")

def clica_seta_sentar(x_origem, y_origem):

    dicionari_PC_cadeira = {'PC-I5-8600K': {'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)},
                            'PC-I5-9400A': {'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_3': (847, 366), 'cadeira_2': (828, 211), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131), 'cadeira_1': (659, 127)},
                            'PC-I5-9400B': {'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211)},
                            'PC-I5-9400C': {'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_9': (312, 131), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_8': (134, 194)},
                            'PC-I7-9700KF': {'cadeira_7': (118, 360), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)},
                            'PC-R5-7600A': {'cadeira_7': (118, 360), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)},
                            'PC-I5-13400A': {'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_7': (118, 360), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)},
                            'PC-I7-11850H': {'cadeira_7': (118, 360), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)},
                            'PC-i3-8145U': {'cadeira_7': (118, 360), 'cadeira_3': (847, 366), 'cadeira_4': (690, 451), 'cadeira_5': (495, 452), 'cadeira_6': (276, 451), 'cadeira_1': (659, 127), 'cadeira_2': (828, 211), 'cadeira_8': (134, 194), 'cadeira_9': (312, 131)}}

    nome_computador = socket.gethostname()
    prioridade_cadeira = dicionari_PC_cadeira[nome_computador]
    #print(prioridade_cadeira)
    for chave, valor in prioridade_cadeira.items():
        cadeira_x, cadeira_y = valor
        if pyautogui.pixelMatchesColor((x_origem + cadeira_x), (y_origem + cadeira_y), (254, 207, 0), tolerance=10):
            pyautogui.click((x_origem + cadeira_x), (y_origem + cadeira_y))
            print(chave, "livre" )
            return True
    return False

def sentar_mesa(x_origem, y_origem, senta_com_maximo):
    sentou = False
    # testa se esta aparecendo o botao azul "Jogar agora"

    print('testando dentro se ta dentro da mesa')
    if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (27, 92, 155), tolerance=19):#testa se esta dentro da mesa
        print("esta dentro da mesa")

        blind_sala = OCR_tela.blind_sala(x_origem, y_origem)
        if "2040" == blind_sala:
            print("sentar mesa Esta na sala certa")
        else:
            print("sentar mesa Esta na sala errada")
            sentou = False
            return False

        posicao_jogaragora_x = 495 + x_origem
        posicao_jogaragora_y = 627 + y_origem
        cor_jogaragora = (15, 160, 220)

        if not(pyautogui.pixelMatchesColor(posicao_jogaragora_x, posicao_jogaragora_y, cor_jogaragora, tolerance=10)): # test se tem o botao jogar agoar apara seber se ja ta sentado
            print('ja esta sentado')
            sentou = True
            return sentou
        else:
            print('tenta sentar')
            for i in range(10):
                print("CHAMA A FUNÇÃO SENTAR")
                clica_seta = clica_seta_sentar(x_origem, y_origem)
                #clica_seta = True
                if clica_seta:
                    posicao_comprar_x = 490 + x_origem
                    posicao_comprar_y = 480 + y_origem
                    cor_comprar = (30, 140, 206)

                    posicao_nao_possui_fichas_x = 490 + x_origem
                    posicao_nao_possui_fichas_y = 400 + y_origem
                    cor_nao_possui_fichas = (209, 211, 213)
                    cor_nao_possui_fichas2 = (30, 138, 218)

                    cor_recompra_automatica = (24, 115, 183)

                    compra_ajustada = False

                    for i in range(20):#testa algumas vezes
                        #time.sleep(0.5)
                        # teste se o botão azul do com comprar esta visivel
                        if pyautogui.pixelMatchesColor( posicao_comprar_x, posicao_comprar_y, cor_comprar, tolerance=35):
                            print("tem comprar")

                            #testa o tipo de caixa de comprar ficha, testa se a caixa é mais larga, olha uma mao cinsa segurando um dinheiro
                            if pyautogui.pixelMatchesColor((x_origem + 313), (y_origem + 445), (55,57,62), tolerance=20):
                                print("janela mais alta")
                                # Marca a re-compra automatica
                                pyautogui.click((x_origem + 522), (y_origem + 405))
                                posicao_valor_minimo_x = 324 + x_origem
                                posicao_valor_minimo_y = 354 + y_origem
                                posicao_valor_maximo_x = 659 + x_origem
                                posicao_valor_maximo_y = 354 + y_origem
                                posicao_recompra_automatica_x = 520 + x_origem
                                posicao_recompra_automatica_Y = 407 + y_origem

                            else:
                                #testa o tipo de caixa de comprar ficha, testa se a caixa é mais larga, olha uma mao cinsa segurando um dinheiro
                            #elif pyautogui.pixelMatchesColor((x_origem + 313), (y_origem + 445), (222,225,227), tolerance=20):
                                print("janela mais baixa")
                                # Marca a re-compra automatica
                                pyautogui.click((x_origem + 522), (y_origem + 424))
                                posicao_valor_minimo_x = 324 + x_origem
                                posicao_valor_minimo_y = 372 + y_origem
                                posicao_valor_maximo_x = 659 + x_origem
                                posicao_valor_maximo_y = 372 + y_origem
                                posicao_recompra_automatica_x = 520 + x_origem
                                posicao_recompra_automatica_Y = 427 + y_origem

                            if senta_com_maximo:
                                pyautogui.doubleClick(posicao_valor_maximo_x, posicao_valor_maximo_y)  # clica no ajuste maximo de fichas
                                time.sleep(0.6)
                                for i in range(500):  # testa algumas vezes
                                    if (pyautogui.pixelMatchesColor(posicao_comprar_x, posicao_comprar_y, cor_comprar, tolerance=35)):# testa se o botao ta azul
                                        compra_ajustada = True
                                        break
                                    pyautogui.click((x_origem + 290), (y_origem + 363))# clina no diminuir ate o botao ficar azul

                            else:
                                pyautogui.doubleClick(posicao_valor_minimo_x, posicao_valor_minimo_y)  # clica no ajuste minimo de fichas
                                compra_ajustada = True

                            if compra_ajustada:
                                if not (pyautogui.pixelMatchesColor(posicao_recompra_automatica_x, posicao_recompra_automatica_Y, cor_recompra_automatica, tolerance=10)):  # testa se o botao ta azul
                                    pyautogui.mouseDown(posicao_recompra_automatica_x, posicao_recompra_automatica_Y)  # Clica no recompra automatica
                                    print('marca recompra automatica')
                                    time.sleep(0.3)
                                for i in range(10):
                                    pyautogui.mouseDown(posicao_comprar_x, posicao_comprar_y)  # clica no comprar
                                    print("Clicou no comprar")
                                    time.sleep(0.6)
                                    pyautogui.mouseUp(posicao_comprar_x, posicao_comprar_y)  # clica no comprar
                                    if not (pyautogui.pixelMatchesColor(posicao_comprar_x, posicao_comprar_y, cor_comprar, tolerance=35)):
                                        break
                                time.sleep(0.5)
                                if pyautogui.pixelMatchesColor(posicao_nao_possui_fichas_x, posicao_nao_possui_fichas_y, cor_nao_possui_fichas2, tolerance=20):  # testa se sentou junto
                                    pyautogui.click((x_origem + 641), (y_origem + 278))  # clica no fechar mensagem de nao tem fichas
                                    print("Ja tem alguem sentado ou duas contas ao mesmo tempo")
                                    sentou = False
                                    return sentou
                                else:
                                    print('sentou')
                                    sentou = True
                                    return sentou

                        #se assim que clicar na setinha nao ter fichas suficiente
                        elif (pyautogui.pixelMatchesColor(posicao_nao_possui_fichas_x, posicao_nao_possui_fichas_y, cor_nao_possui_fichas, tolerance=10)) \
                                or (pyautogui.pixelMatchesColor(posicao_nao_possui_fichas_x, posicao_nao_possui_fichas_y, cor_nao_possui_fichas2, tolerance=10)):
                            pyautogui.click((x_origem + 641), (y_origem + 278), button='left') # clica no fechar mensagem de nao tem fichas
                            print("Não possui fichas suficiente")
                            sentou = False
                            return sentou
    print('nao esta dentro da mesa')
    return sentou
def escolher_blind(x_origem, y_origem, blind):
    blinb_rolagem = {'1/2': (534, 478), '2/4': (534, 504), '5/10': (534, 530), '10/20': (534, 556), '20/40': (534, 582),
                     '20/50': (548, 478), '50/100': (548, 504), '100/200': (548, 530), '200/400': (548, 556), '500/1K': (548, 582),
                     '1K/2K': (563, 478), '2K/4K': (563, 504), '5K/10K': (563, 530), '10K/20K': (563, 556), '20K/40K': (563, 582),
                     '50K/100K': (571, 530), '100K/200K': (571, 556), '500K/1M': (571, 582)}

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"
    Limpa.aviso_canto_lobby(x_origem, y_origem)

    for i in range(20):# abrir o menu blind
        #testa se a caixa de escolha do blind esta aberta, olha a barra preta
        if pyautogui.pixelMatchesColor((x_origem + 200), (y_origem + 450), (0, 0, 0), tolerance=1):
            pyautogui.click(268 + x_origem, 571 + y_origem, button='left')  # clica no aptualizar blind
            print("blind aberto")
            break
        else:
            pyautogui.click(71 + x_origem, 619 + y_origem, button='left')  # clica para abrir o blind
            print("clica para abrir o blind")
            time.sleep(0.3)

    for i in range(10):# abrir a barra de rolagem de valores
        #testa se a barra de rolagem esta aberta
        if pyautogui.pixelMatchesColor((x_origem + 200), (y_origem + 475), (0, 0, 0), tolerance=1):
            print("Barra de rolagem aberta")
            break
        else:
            pyautogui.click(293 + x_origem, 450 + y_origem, button='left')  # clica para abrir o blind
            print("clica para abrir a barra de rolagem")
            time.sleep(0.3)

    posicao_barra, posicao_lista = blinb_rolagem[blind]

    pyautogui.doubleClick(300 + x_origem, posicao_barra + y_origem, button='left')  # clica para rolar
    time.sleep(0.2)
    pyautogui.doubleClick(200 + x_origem, posicao_lista + y_origem, button='left')  # clica no valor dentro da lista
    time.sleep(0.2)
    pyautogui.click(71 + x_origem, 619 + y_origem, button='left')  # clica para fechar o blind

    pyautogui.doubleClick(405 + x_origem, 233 + y_origem)  # clica para fechar o blind
    blind_sala = None
    for i in range(20):
        if pyautogui.pixelMatchesColor((x_origem + 358), (y_origem + 264), (26, 29, 33), tolerance=5):# testa se tem sala toda vazia
            pyautogui.doubleClick(490 + x_origem, 263 + y_origem)  # clica para entar na sala vazia
            for i in range(20):
                if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 580), (48, 137, 198), tolerance=19): # testa se esta na mesa
                    blind_sala = OCR_tela.blind_sala(x_origem, y_origem)
                    print(blind_sala)
                    break
            if blind_sala != None:
                break
        else:
            print("Não tem sala vazia")
    blind = blind.replace("/", "")
    if blind == blind_sala:
        print("Esta na sala certa")
        return True
    else:
        print("Esta na sala errada")
        return False



def ajuste_valor_niquel(x_origem, y_origem):
    duzentos, auto10 = False, False
    # Define a região da tela onde a imagem será buscada


    for i in range(20):
        posicao_200 = None
        Limpa.aviso_canto_lobby(x_origem, y_origem)
        # Procura a imagem na região definida com 99,5% de tolerância, em escala de cinza e retorna a posição
        #posicao_200 = pyautogui.locateOnScreen(valor_200, region=regiao_busca_200, confidence=0.99, grayscale=True)  # limite maximo de precisao é 0.997
        imagem = r'Imagens\Niquel\niquel200.png'
        regiao = (77 + x_origem, 652 + y_origem, 49, 15)  # (x, y, largura, altura)
        precisao = 0.9
        posicao_200 = localizar_imagem(imagem, regiao, precisao)
        if posicao_200 is not None:# Verifica se a imagem foi encontrada
            print("foi encontado 200")
            duzentos = True
            break

        elif posicao_200 is None:  # Verifica se a imagem foi encontrada
            print("NÂO foi encontado 200")
            pyautogui.click(x_origem + 161, y_origem + 658)
            time.sleep(0.3)
            pyautogui.click(x_origem + 161, y_origem + 636)
            time.sleep(0.3)

    for i in range(20):
        posicao_10auto = None
        Limpa.aviso_canto_lobby(x_origem, y_origem) # fecha propaganda
        # Procura a imagem na região definida com 99,5% de tolerância, em escala de cinza e retorna a posição
        #posicao_10auto = pyautogui.locateOnScreen(auto_10, region=regiao_busca_AUTO10, confidence=0.99, grayscale=True)  # limite maximo de precisao é 0.997
        regiao = (207 + x_origem, 652 + y_origem, 58, 13)  # (x, y, largura, altura)
        precisao = 0.9
        imagem = r'Imagens\Niquel\10auto.png'
        posicao_10auto = localizar_imagem(imagem, regiao, precisao)
        if posicao_10auto is not None:# Verifica se a imagem foi encontrada
            print("foi encontado 10 AUTO")
            auto10 = True
            break

        elif posicao_10auto is None:  # Verifica se a imagem foi encontrada
            print("NÂO foi encontado 10 AUTO")
            pyautogui.mouseDown(x_origem + 234, y_origem + 659)#aperta e segura 10auto
            time.sleep(0.5)
            pyautogui.mouseUp(x_origem + 234, y_origem + 659)#aperta e segura 10auto
            time.sleep(0.3)
            pyautogui.click(x_origem + 234, y_origem + 615)#escolhe 10auto na lista
            time.sleep(0.3)
            pyautogui.click(x_origem + 641, y_origem + 278)#clica para fechar a mensagem vc so pode jogar depois de estar sentado

    return duzentos, auto10


def sala_minima_niquel(x_origem, y_origem, num_mesa):

    if not pyautogui.pixelMatchesColor((x_origem + 280), (y_origem + 210), (73, 177, 9), tolerance=5):
        pyautogui.click(280 + x_origem, 200 + y_origem)  # clica na lista de aprendizes
        time.sleep(1)
    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"
    Limpa.aviso_canto_lobby(x_origem, y_origem)
    pyautogui.doubleClick(310 + x_origem, 617 + y_origem)  # clica FORA caixa de busca de salas para apagar o valor
    time.sleep(0.3)
    pyautogui.doubleClick(190 + x_origem, 617 + y_origem) #clica na caixa de busca de salas
    time.sleep(0.3)
    pyautogui.write(num_mesa) #escreve o numero da sala na barra de busca
    print('mesa: ', num_mesa)
    time.sleep(0.5)
    cont_erro_entrar_mesa = 0
    blind_sala = None
    for i in range(20):
        if pyautogui.pixelMatchesColor((x_origem + 435), (y_origem + 264), (26, 29, 33), tolerance=5):  # testa se tem sala com pelo menos um lugar vazio, olha se tem preto no fim da barra de ocupação
            pyautogui.doubleClick(490 + x_origem, 263 + y_origem)  # clica para entar na sala vazia

            for i in range(40):
                if pyautogui.pixelMatchesColor((x_origem + 435), (y_origem + 264), (26, 29, 33), tolerance=5):  # testa se tem sala com pelo menos um lugar vazio, olha se tem preto no fim da barra de ocupação
                    pyautogui.doubleClick(490 + x_origem, 263 + y_origem)  # clica para entar na sala vazia
                    cont_erro_entrar_mesa += 1

                Limpa.limpa_jogando(x_origem, y_origem)

                if pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 674), (27, 92, 155), tolerance=19):  # testa se esta dentro da mesa
                    Limpa.limpa_jogando(x_origem, y_origem)
                    blind_sala = OCR_tela.blind_sala(x_origem, y_origem)
                    print(blind_sala)
                    break

                time.sleep(1)

                if cont_erro_entrar_mesa >= 5:
                    Limpa.limpa_total(x_origem, y_origem)
                    break

            if blind_sala != None:
                break
        else:
            print("Não tem sala vazia")

    if "2040" == blind_sala:
        print("Esta na sala certa")
        return True
    else:
        print("Esta na sala errada")
        return False



def gira_niquel(x_origem, y_origem):
    posicao_10auto = None
    regiao = (207 + x_origem, 652 + y_origem, 58, 13) # (x, y, largura, altura)
    imagem = r'Imagens\Niquel\10auto.png'
    precisao = 0.9
    posicao_10auto = localizar_imagem(imagem, regiao, precisao)
    if posicao_10auto is not None:  # Verifica se a imagem foi encontrada
        pyautogui.click((x_origem + 233), (y_origem + 660))  # clica no 10auto
        print("foi encontado 10 AUTO")
        gira = True
        return gira
    else:
        print("não tem 10 auto")
        gira = False
        return gira

def gira_10auto(x_origem, y_origem):
    posicao_10auto = None
    regiao = (207 + x_origem, 652 + y_origem, 58, 13) # (x, y, largura, altura)
    imagem = r'Imagens\Niquel\10auto.png'
    precisao = 0.9
    posicao_10auto = localizar_imagem(imagem, regiao, precisao)
    if posicao_10auto is not None:  # Verifica se a imagem foi encontrada
        print("foi encontado 10 AUTO")
        gira = True
        return gira
    else:
        print("não tem 10 auto")
        gira = False
        return gira

def passa_corre_joga(x_origem, y_origem): # para se fazer tarefas
    print("jogando")
    # se nao esta com v azul dentro do quadrado branco e se esta com quadrado branco
    if (not pyautogui.pixelMatchesColor((x_origem + 333), (y_origem + 610), (59, 171, 228), tolerance=1)) \
            and (pyautogui.pixelMatchesColor((x_origem + 333), (y_origem + 610), (255, 255, 255), tolerance=1)):
        pyautogui.click((x_origem + 337), (y_origem + 605))
        time.sleep(0.3)
        print("foi encontado o quadrado")
    else:
        print("nao tem quadrado branco")
        # testa se o valor nao foi aumentado ou seja igual a 40 ou 80
        if pyautogui.pixelMatchesColor((x_origem + 480), (y_origem + 650), (255, 255, 255), tolerance=1): # testa se tem area branca
            print("area de vamor brancoa")
            valor = OCR_tela.valor_apostar(x_origem, y_origem)
            print(valor)
            if (valor == 40) or (valor == 80):
                pyautogui.click((x_origem + 337), (y_origem + 605))# clica no passar
                print("tem que passar")
            else:
                pyautogui.click((x_origem + 528), (y_origem + 605))  # clica no correr
                print("tem que correr")

        # se nao tem area branca com valor
        elif pyautogui.pixelMatchesColor((x_origem + 343), (y_origem + 599), (255, 255, 255), tolerance=1): # testa se tem um v de pagar
            # print("ta com all-in ou ta tudo azul")
            # if pyautogui.pixelMatchesColor((x_origem + 528), (y_origem + 603), (255, 255, 255), tolerance=1):
            print("ta com x branco do correr")
            pyautogui.click((x_origem + 528), (y_origem + 605))  # clica no correr

def joga(x_origem, y_origem, id, senha, url, navegador):

    tarefas_fazer = ('Jogar o caca-niquel da mesa 150 vezes',
                     'Jogar o caca-niquel da mesa 70 vezes',
                     'Jogar o caca-niquel da mesa 10 vezes')

    continua_jogando = True
    meta_atigida = False

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    while continua_jogando:  # permanece joghando
        senta_com_maximo = False
        print('joga mesa')
        Limpa.fecha_tarefa(x_origem, y_origem)
        Limpa.limpa_jogando(x_origem, y_origem)
        sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo)
        print("sentou")

        if sentou:
            print("esta sentado")
            passa_corre_joga(x_origem, y_origem)
            auto10 = gira_10auto(x_origem, y_origem)
            if auto10:
                #Limpa.limpa_abre_tarefa2(x_origem, y_origem)
                Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)
                print('manda recolher')
                Tarefas.recolher_tarefa(x_origem, y_origem)
                print('procura se aidna tem tarefa')

                #continua_jogando, tarefa = Tarefas.comparar_imagens_tarefa(tarefas_fazer, x_origem, y_origem)  # retona se tem cartas vezes ou nao
                continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)
                #continua_jogando = True
                meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)

                if Limpa.limpa_total_fazendo_tarefa(x_origem, y_origem) == "sair da conta":
                    return "sair da conta"
                if HoraT.fim_tempo_tarefa():
                    return
                IP.testa_trocar_IP() # ve se tem que trocar ip

            Limpa.fecha_tarefa(x_origem, y_origem)
            #continua_jogando = True
            print("conmtinua jogando ", continua_jogando)
        else:
            print("ainda nao esta sentado")
            for i in range(2):
                for num_mesa in lista_salas_niquel:
                    print('Mumero da mesa para tentar sentar: ', num_mesa)
                    IP.tem_internet()
                    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                        return "sair da conta"
                    # blind_certo = escolher_blind(x_origem, y_origem, '20/40')
                    blind_certo = sala_minima_niquel(x_origem, y_origem, num_mesa)
                    if blind_certo:
                        duzentos, auto10 = ajuste_valor_niquel(x_origem, y_origem)

                        sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo)

                        if sentou and duzentos and auto10:
                            print('esta tudo ok, slote e sentado')
                            break
            if not sentou:
                print("rodou a lista de mesas 2x, da um F5 para recarregar as mesas")
                IP.tem_internet()
                print('f5')
                pyautogui.press('f5')
                time.sleep(15)

        meta, pontos = Tarefas.tem_tarefa_para_recolher(x_origem, y_origem, id, senha, url, navegador)
        if meta:
            meta_atigida = True

        if (not continua_jogando) or meta_atigida:
            Limpa.limpa_abre_tarefa(x_origem, y_origem, id, senha, url, navegador)
            continua_jogando, tarefa = Tarefas.comparar_listas_fazendo_tarefa(tarefas_fazer, x_origem, y_origem)
            meta_atigida, pontos = Tarefas.meta_tarefas(x_origem, y_origem)
            if (not continua_jogando) or meta_atigida:
                print("FIM")
                if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                    return "sair da conta"
                break
        gira_niquel(x_origem, y_origem)
        time.sleep(1)
    return

def joga_uma_vez(x_origem, y_origem):
    print('joga_uma_vez')

    continua_jogando = True
    jogou_uma_vez = False
    senta_com_maximo = False

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    time_entrou = time.perf_counter()

    while continua_jogando:  # permanece joghando

        print('joga mesa')
        Limpa.fecha_tarefa(x_origem, y_origem)
        Limpa.limpa_jogando(x_origem, y_origem)
        sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo)
        print("sentou")

        if jogou_uma_vez:
            if pyautogui.pixelMatchesColor((x_origem + 663), (y_origem + 538), (86, 169, 68), tolerance=10):  # testa se apareceu as mensagens verdes na parte de baixo
                continua_jogando = False
                print('apareceu a mensagem pode sair')
        else:
            if pyautogui.pixelMatchesColor((x_origem + 333), (y_origem + 604), (255, 255, 255), tolerance=5):
                jogou_uma_vez = True
                print('jougou uma vez')
            time_sair = time.perf_counter()
            tempo_total = time_sair - time_entrou
            print('tempo que esta esperando', tempo_total)
            if tempo_total > 120: # troica de mesa se ficar muito tempo parado sem entrar alguem para jogar
                print("tempo limite atingido sem outro jogador, sai da mesa para tentar em outra")
                Limpa.limpa_total(x_origem, y_origem)
                Limpa.limpa_jogando(x_origem, y_origem)

        if not continua_jogando:
            print("FIM")
            if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                return "sair da conta"
            Limpa.limpa_jogando(x_origem, y_origem)
            return

        if sentou:
            print("esta sentado")
            passa_corre_joga(x_origem, y_origem)
        else:
            if jogou_uma_vez:
                if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
                    return "sair da conta"
                Limpa.limpa_jogando(x_origem, y_origem)
                return

            print("ainda nao esta sentado")
            for i in range(2):
                for num_mesa in lista_salas_niquel:
                    print('Mumero da mesa para tentar sentar: ', num_mesa)
                    IP.tem_internet()
                    Limpa.limpa_jogando(x_origem, y_origem)
                    Limpa.limpa_total(x_origem, y_origem)
                    #blind_certo = escolher_blind(x_origem, y_origem, '20/40')
                    blind_certo = sala_minima_niquel(x_origem, y_origem, num_mesa)
                    if blind_certo:
                        #duzentos, auto10 = ajuste_valor_niquel(x_origem, y_origem)
                        sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo)
                        if sentou:
                            time_entrou = time.perf_counter()
                            print('esta tudo ok, slote e sentado')
                            break
                if sentou:
                    break
            if not sentou:
                print("rodou a lista de mesas 2x, da um F5 para recarregar as mesas")
                IP.tem_internet()
                print('f5')
                pyautogui.press('f5')
                time.sleep(15)

        time.sleep(1)
    return


def dia_de_jogar_mesa(x_origem, y_origem, dia_da_semana, valor_fichas, time_rodou, roleta):
    if dia_da_semana == 6 or dia_da_semana == 5:  # testa se é sabado ou domingo
        if pyautogui.pixelMatchesColor((x_origem + 750), (y_origem + 38), (245, 218, 96), tolerance=10) \
                or pyautogui.pixelMatchesColor((x_origem + 802), (y_origem + 38), (245, 218, 96), tolerance=10) \
                or (100000 < valor_fichas < 300000):
            print('conta para jogar mesa')
            if roleta == 'roleta_2':
                for i in range(20):
                    time_sair = time.perf_counter()
                    tempo_total = time_sair - time_rodou
                    print('tempo que ja clicou no rodou', tempo_total)
                    if tempo_total > 18:
                        print('ja pode sair do r2')
                        break
                    time.sleep(1)
                    pyautogui.doubleClick(x_origem + 683, y_origem + 14)  # clica no icone roleta, ja roda sozinho

            Limpa.limpa_total(x_origem, y_origem)

            print('conta nao esta upada abre os iniciantes')

            joga_uma_vez(x_origem, y_origem)
            time.sleep(2)
            Limpa.iniciantes(x_origem, y_origem)
            Limpa.limpa_total(x_origem, y_origem)
    return





# x_origem, y_origem = Origem_pg.x_y()
# joga(x_origem, y_origem, 0, 0, 0, 0)
# # # passa_corre_joga(x_origem, y_origem)
# #
# # # x_origem, y_origem = Origem_pg.x_y()
# # escolher_blind(x_origem, y_origem, '20/40')
# # print(x_origem, y_origem )
# # senta_com_maximo = False
# # sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo)
# # print(sentou)
#
# #ajuste_valor_niquel(x_origem, y_origem)
# # x_origem, y_origem = Origem_pg.x_y()
# #
# # gira_niquel(x_origem, y_origem)
#
#
# sala_minima_niquel(x_origem, y_origem)
#
# # tem_tarefa = Tarefas.comparar_imagens_tarefa(tarefas_fazer_niquel, x_origem, y_origem)
# # print(tem_tarefa)




