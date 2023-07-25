# # # # lista =['rico tab bien odio ia Lana nina iodo iii ua ind ias de 50', 'ua a nn ao Cidia ias ini fundir insira E en,',
# # # #         'unas boina ia iara ia caia so uniiitn tias', 'iu da age dai ain adiantado iria daria',
# # # #         'ia a nao tis io dial us iria vãs,', 'TA AAm e mA a Eg NE eRr aaA', 'ESET EN) TN RI E e RR E',
# # # #         '& 1000 PN ke. São', 'S +500 BP +11)', "em es = ou CO'", '1000 A)1000 A', '6 +2000 P+30', 'C200  BPD0 |',
# # # #         '* +500 B 10', 'l; *1000 [A', '6 2000 B 30', 'B 500 B 10', 'C200  BPD0', '& 500 B 10', '3 +500 A/)',
# # # #         'E 27 a/) =', '6 500 B 10', 'B 500 A/)', '& 1000 A)', 'Sum CEPE.', 'pc ai fa', '6 500 R/', 'º +500 /',
# # # #         'E 27 a =', 'pacos ra', '4 500 Po', 'pç ai fa', 'paços ra', '& 500 [A', '& 1000 P', '1000 UA)', 'B +s00 A',
# # # #         '& 1000 A', '1000 [A', 'pião SO', 'poça fo', '2000 B0', '1000 A)', '200 BP0', 'poça fa', 'B 500 /',
# # # #         '2000 BP', '500 Bi)', '2000 PD', 'POA fo', '100 Pn', '200 PD', '500 Bi', '200 BP', '0 BA /', ') [A;/',
# # # #         'poo P0', 'SM Pt', 'os“ 3', '500 A', '|||.', ') R/', ') ”', '/ -', '/ ”', 'P0', '[A', 'B0', ')', '/']
# # # #
# # # # print(len(lista))
# # # #
# # # # lista_sem_duplicados = list(set(lista))
# # # #
# # # # print(len(lista_sem_duplicados))
# # # #
# # # # lista_ordenada = sorted(lista_sem_duplicados, key=len, reverse=True)
# # # #
# # # # print(lista_ordenada)
# # # #
# # # #
# # #
# # #
# # # # troca_tarefa = ['Ganhar 10 maos em uma mesa com blinds acima de 25',
# # # #                 'Ganhar um premio em um torneio de eliminacao',
# # # #                 'Jogar 20 mão em uma mesa com blinds acima de 25',
# # # #                 'Participe de um campeonato de eliminação 1 vezes',
# # # #                 'Participe de um campeonato de eliminação 2 vezes',
# # # #                 'Participe de um campeonato de eliminação 3 vezes',
# # # #                 'Tirar Sequencia 1 vezes em mesas com blinds maiores que 25',
# # # #                 'Tirar trinca 1 vez em mesa com blinds maiores que 25',
# # # #                 'Tirar um flush ou quaquer mãos superior 1 vez em mesas com blinds laiores que 25',
# # # #                 'Ganhar 10 mãos em uma mesa com blinds acima de 50',
# # # #                 'Ganhar 20 mãos em uma mesa com blinds acima de 50',
# # # #                 'Ganhar 30.000 fichas em mesas com blinds acima da 50',
# # # #                 'Jogar 20 mão em uma mesa com blinds acima de 50',
# # # #                 'Jogar 40 mão em uma mesa com blinds acima de 50',
# # # #                 'Tirar Flush ou qualquer mão superior 1 vez em mesas com blindes maiores que 25',
# # # #                 'Tirar Sequencia 2 vezes em mesas com blinds maiores que 50',
# # # #                 'Tirar trinca 1 vez em mesas com blinds maiores que 50',
# # # #                 'Ganhar 20 mãos em uma mesa com blinds acima de 100',
# # # #                 'Ganhar 100.000 fichas em mesas com blinds acima de 50',
# # # #                 'Ganhar 200.000 fichas em mesas com blindes acima da 100',
# # # #                 'Jogar 20 mão em uma mesa com blinds acima de 100',
# # # #                 'Jogar 40 mão em uma mesa com blinds acima de 100',
# # # #                 'Tirar Flush ou qualquer mão superior 1 vez em mesas com blindes maiores que 50',
# # # #                 'Tirar Flush ou qualquer mão superior 2 vez em mesas com blindes maiores que 100',
# # # #                 'Tirar Sequencia 2 vezes em mesas com blinds maiores que 100',
# # # #                 'Tirar trinca 2 vez em mesas com blinds maiores que 100']
# # # #
# # # # for i in range(len(troca_tarefa)):
# # # #     troca_tarefa[i] = troca_tarefa[i].replace('ç', 'c').replace('í', 'i').replace('ê', 'e').replace('-', ' ').replace('ã', 'a')
# # # #     troca_tarefa[i] = troca_tarefa[i].replace('\n', ' ').rstrip('.')
# # # #     troca_tarefa[i] = ' '.join(troca_tarefa[i].split())
# # # #
# # # # print(troca_tarefa)
# # #
# # #
# # #
# # # # import time
# # # # inicio = time.time()
# # # # #inicio = time.perf_counter()
# # # # time.sleep(2)
# # # # fim = time.time()
# # # # #fim = time.perf_counter()
# # # #
# # # # # Calcula a diferença de tempo
# # # # tempo_total = fim - inicio
# # # #
# # # # # Imprime o tempo total em segundos
# # # # print("Tempo total: ", tempo_total, "segundos")
# # #
# # #
# # #
# # # # import pyautogui
# # # #
# # # # try:
# # # #     # Localize a janela do ExpressVPN com base na classe 'ahk_class'
# # # #     expressvpn_window = pyautogui.getWindowsWithTitle('ExpressVPN')[0]
# # # #     print(expressvpn_window)
# # # #
# # # #
# # # #     # Traz a janela para o primeiro plano (caso esteja minimizada ou oculta)
# # # #     expressvpn_window.activate()
# # # #
# # # #     # Aguarde um pequeno intervalo para garantir que a janela esteja completamente ativada
# # # #     pyautogui.sleep(1)
# # # #
# # # #     # Use 'Alt + Esc' para alternar entre as janelas e, assim, exibir a interface do ExpressVPN
# # # #     #pyautogui.hotkey('alt', 'esc')
# # # #
# # # # except Exception as e:
# # # #     print("Erro ao abrir a interface do ExpressVPN:", e)
# # #
# # #
# # #
# import subprocess
# import pyautogui
# import time
# import pygetwindow as gw
# import time
#
# #Caminho para o executável da VPN
#
# caminho_executavel_vpn = "C:/Program Files (x86)/ExpressVPN/expressvpn-ui/ExpressVPN.exe"
# conexao_vpn_x = 1100
# conexao_vpn_y = 440
#
#
#     # Caminho para o executável da VPN
#
#
# while True:
#
#     print('abre a vpn')
#     try:
#         vpn_window = gw.getWindowsWithTitle('ExpressVPN')[0]
#         print(vpn_window)
#         # vpn_window.activate()
#         # Verificar se a janela está visível antes de movê-la
#         if vpn_window.left == 1100 and vpn_window.top == 440:
#             conexao_vpn_vpn_x = vpn_window.left
#             conexao_vpn_vpn_y = vpn_window.top
#             print("A posição da janela é (930, 440).")
#             break
#         if vpn_window.left < 0 and vpn_window.top < 0:
#             print('esta minizada')
#             subprocess.Popen(caminho_executavel_vpn)
#         else:
#             vpn_window.activate()
#             # Mover a janela da VPN para a posição desejada (x, y) da tela
#             conexao_vpn_vpn_x = 1100
#             conexao_vpn_vpn_y = 440
#
#             vpn_window.moveTo(conexao_vpn_vpn_x, conexao_vpn_vpn_y)
#     except Exception as e:
#         print("Erro ao abrir a VPN:", e)
#         subprocess.Popen(caminho_executavel_vpn)
#         time.sleep(5)
#         continue
#     time.sleep(0.5)
#
# while True:
#     print('refazendo conexao')
#     # testa se esta verde e ligado
#     if pyautogui.pixelMatchesColor((conexao_vpn_vpn_x + 189), (conexao_vpn_vpn_y + 186), (15, 134, 108), tolerance=10) \
#             or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (77, 182, 172), tolerance=10):
#         pyautogui.click(conexao_vpn_x + 189, conexao_vpn_y + 186)
#         print('desligou')
#         for i in range(100):
#             # testa se esta vermelho e desligado
#             if pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (126, 15, 83), tolerance=10) \
#                     or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (164, 17, 94), tolerance=10):
#                 time.sleep(0.5)
#                 print('VPN Desconectado')
#                 break
#             time.sleep(0.5)
#
#     # testa se esta vermelho e desligado
#     elif pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (126, 15, 83), tolerance=10) \
#             or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (164, 17, 94), tolerance=10):
#         pyautogui.click(conexao_vpn_x + 189, conexao_vpn_y + 186)
#         print('ligou')
#         for i in range(100):
#             # testa se esta vermelho e desligado
#             if pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (15, 134, 108), tolerance=10) \
#                     or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (77, 182, 172), tolerance=10):
#                 print('VPN Conectado')
#                 break
#             time.sleep(0.5)
#         if pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (15, 134, 108), tolerance=10) \
#                 or pyautogui.pixelMatchesColor((conexao_vpn_x + 189), (conexao_vpn_y + 186), (77, 182, 172), tolerance=10):
#             print('VPN Conectado')
#             # Minimizar a janela
#             vpn_window.minimize()
#             break
# #
# #
# #
# # import requests
# # import pyautogui
# # import time
# # def f5_quando_internete_ocila():
# #
# #     conectado = True
# #     while True:
# #         print('f5_quando_internete_ocila')
# #         try:
# #             response = requests.get('http://www.google.com', timeout=5)
# #             print(response)
# #
# #             if response.status_code == 200 or response.status_code == 429:
# #                 print("Conexão com a internet ativa.")
# #                 if not conectado:
# #                     try:
# #                         pyautogui.press('f5')
# #                         time.sleep(15)
# #                     except Exception as e:
# #                         print('erro autogui: ', e)
# #
# #                 #entrou_corretamente, stataus = Seleniun.teste_logado(id, senha, url, navegador)
# #                 return True
# #         except Exception as e:
# #             print("Sem conexão com a internet...")
# #             print(e)
# #             time.sleep(5)
# #             conectado = False
# #
# # #f5_quando_internete_ocila()
# #
# # import random
# # def tem_internet():
# #     cont_erro2 = 0
# #     cont_erro = 0
# #     #print('tem_internet')
# #
# #     sites = [
# #         'http://www.google.com',
# #         'http://www.facebook.com',
# #         'http://www.twitter.com',
# #         'http://www.youtube.com',
# #         'http://www.instagram.com',
# #         'http://www.linkedin.com',
# #         'http://www.github.com',
# #         'http://www.reddit.com',
# #         'http://www.amazon.com',
# #         'http://www.netflix.com'
# #     ]
# #
# #
# #     com_internete = True
# #     while com_internete:
# #         print('testa a internete')
# #         cont_erro2 += 1
# #         site_aleatorio = random.choice(sites)
# #         print(site_aleatorio)
# #         try:
# #             response = requests.get(site_aleatorio, timeout=10)
# #             print(response)
# #             if response.status_code == 200:
# #                 print("Conexão com a internet ativa.")
# #                 #com_internete = False
# #                 #return True
# #         except Exception as e:
# #             print("Sem conexão com a internet. Encerrando os testes...")
# #             print(e)
# #             time.sleep(3)
# #             cont_erro += 1
# #             continue
# #
# #
