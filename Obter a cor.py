# import time
#
# import pyautogui
#
# import Origem_pg
#
# # Exemplo de uso
# x = 215
# y = 1000
#
#
# # x_origem = 322
# # # #
# # y_origem = 178
# #322 178
#
# x_origem, y_origem = Origem_pg.x_y()
# print(x_origem, y_origem)
# #x_origem, y_origem = Origem_pg.x_y_aviso_sistema()
#
# #pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 580), (47, 136, 196), tolerance=19)
#
#
#
# x = (x_origem + 545)
# y = (y_origem + 105)
#
#
#
#
# tolerancia = 0
# pyautogui.moveTo(x, y)
# for i in range(100):
#     cor = pyautogui.pixel(x, y)
#     print(f"A cor RGB do pixel em ({x}, {y}) é {cor}")
#
#
#
#     if pyautogui.pixelMatchesColor(x, y, (22, 21, 23), tolerance=tolerancia):
#         print('tem a cor, tolerancia :', tolerancia)
#
#
#     time.sleep(0.2)
#
