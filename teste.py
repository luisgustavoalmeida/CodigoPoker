def joga_ate_lv_7(x_origem, y_origem):
    print('joga_ate_lv_7')

    # xp2.pega_2xp(x_origem, y_origem)

    global lista_salas_jogar
    blind_mesa = None
    sentou = False
    continua_jogando = True
    jogou_uma_vez = False
    humano = False
    cont_jogou = 0
    senta_com_maximo = False
    cont_limpa_jogando = 0
    sala_atual = None
    pular_sala = False

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    xp2.pega_2xp(x_origem, y_origem)

    time_entrou = time.perf_counter()
    Limpa.fecha_tarefa(x_origem, y_origem)
    Limpa.limpa_jogando(x_origem, y_origem)
    sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa, True)

    while continua_jogando:  # permanece joghando

        # print('joga mesa')

        if cont_limpa_jogando > 40:
            cont_limpa_jogando = 0
            Limpa.fecha_tarefa(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)
            sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa, True)
        cont_limpa_jogando += 1

        # print("Sentou :", sentou)

        if jogou_uma_vez:
            if pyautogui.pixelMatchesColor((x_origem + 663), (y_origem + 538), (86, 169, 68), tolerance=20):
                # testa se apareceu as mensagens verdes na parte de baixo
                level_conta = OCR_tela.level_conta(x_origem, y_origem)
                cont_jogou += 1
                print("Jogou vezes igua a: ", cont_jogou)
                if level_conta >= 10:
                    level_conta = OCR_tela.level_conta(x_origem, y_origem)
                    if level_conta >= 10:
                        break

                if cont_jogou % 5 == 0:  # testa se tem que trocar ip a casa 5 jogadas
                    IP.testa_trocar_IP()  # ve se tem que trocar ip

                jogou_uma_vez = False
                time_entrou = time.perf_counter()
                if not cadeiras_celular(x_origem, y_origem):
                    print('Sair da mesa fim da jogada com humanos na mesa')
                    humano = True
        else:
            if pyautogui.pixelMatchesColor((x_origem + 663), (y_origem + 538), (86, 169, 68), tolerance=20):
                for i in range(20):
                    # print(i)
                    time.sleep(0.3)
                    if not cadeiras_celular(x_origem, y_origem):
                        print('Sair da mesa fim da jogada com humanos na mesa')
                        humano = True
                        break

        # else:
        time_sair = time.perf_counter()
        tempo_total = time_sair - time_entrou
        # print('tempo que esta esperando', tempo_total)
        if tempo_total > 60:  # troica de mesa se ficar muito tempo parado sem entrar alguem para jogar
            print("tempo limite atingido sem outro jogador, sai da mesa para tentar em outra")
            Limpa.limpa_total(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)
            pular_sala = True
        # time.sleep(0.3)

        if humano:
            print('Jogador humano na mesa, troca de mesa')
            jogou_uma_vez = False
            humano = False
            pular_sala = True
            Limpa.limpa_total(x_origem, y_origem)
            Limpa.limpa_jogando(x_origem, y_origem)

        if sentou:
            # print("esta sentado")
            (jogou, humano) = passa_corre_joga(x_origem, y_origem, valor_aposta1, valor_aposta2)
            if jogou:
                jogou_uma_vez = True
            # print('jogou_uma_vez: ', jogou_uma_vez)
            # print('humano: ', humano)

        else:
            humano = False
            print("ainda nao esta sentado")
            for i in range(2):
                for indice, dicionario in enumerate(lista_salas_jogar):

                    if indice == sala_atual and pular_sala:
                        continue  # Pule a primeira iteração, começando pelo segundo item

                    num_mesa = list(dicionario.keys())[0]  # Obtendo a chave do dicionário
                    valor_tupla = dicionario[num_mesa]  # Obtendo a tupla associada à chave
                    blind_mesa = valor_tupla[0]  # Obtendo a string da tupla
                    valor_aposta1 = valor_tupla[1]  # Obtendo o primeiro número da tupla
                    valor_aposta2 = valor_tupla[2]  # Obtendo o segundo número da tupla

                    # print('procura mesa')
                    # print(lista_salas_jogar)
                    print('Mumero da mesa para tentar sentar: ', num_mesa)
                    IP.tem_internet()
                    Limpa.limpa_jogando(x_origem, y_origem)
                    Limpa.limpa_total(x_origem, y_origem)
                    blind_certo, sala_existe = sala_minima_niquel(x_origem, y_origem, num_mesa, blind_mesa)

                    if not sala_existe:
                        # print(lista_salas_jogar)
                        # Remover o primeiro item da lista usando pop(0)
                        primeiro_item = lista_salas_jogar.pop(0)
                        # Adicionar o primeiro item de volta à lista usando append(), colocando-o no final
                        lista_salas_jogar.append(primeiro_item)
                        # print(lista_salas_jogar)

                    if blind_certo:
                        sentou = sentar_mesa(x_origem, y_origem, senta_com_maximo, blind_mesa, True)
                        if sentou:
                            time_entrou = time.perf_counter()
                            print('esta tudo ok, slote e sentado')
                            sala_atual = indice
                            pular_sala = False
                            break
                        else:
                            time_entrou = 0

                if i == 1:
                    pular_sala = False

                if sentou:
                    break
                else:
                    time_entrou = 0

            if not sentou:
                time_entrou = 0
                print("rodou a lista de mesas 2x, da um F5 para recarregar as mesas")
                IP.tem_internet()
                print('f5')
                pyautogui.press('f5')
                time.sleep(15)

    if Limpa.limpa_total(x_origem, y_origem) == "sair da conta":
        return "sair da conta"

    Limpa.limpa_jogando(x_origem, y_origem)
    return
