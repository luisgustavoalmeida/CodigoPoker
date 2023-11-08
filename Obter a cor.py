import time

import pyautogui

import Origem_pg

# Exemplo de uso
x = 215
y = 1000


# x_origem = 322
# # #
# y_origem = 178
#322 178

x_origem, y_origem = Origem_pg.x_y()
print(x_origem, y_origem)
#x_origem, y_origem = Origem_pg.x_y_aviso_sistema()

#pyautogui.pixelMatchesColor((x_origem + 700), (y_origem + 580), (47, 136, 196), tolerance=19)

x = (x_origem + 673)
y = (y_origem + 41)

tolerancia = 0
pyautogui.moveTo(x, y)
cores_contagem = {}
for i in range(100):
    cor = pyautogui.pixel(x, y)
    print(f"A cor RGB do pixel em ({x}, {y}) é {cor}")

    if pyautogui.pixelMatchesColor(x, y, (64, 37, 165), tolerance=tolerancia):
        print('tem a cor, tolerancia :', tolerancia)

    tolerancia = tolerancia + 1

    # Adicione a cor ao dicionário e atualize a contagem
    if cor in cores_contagem:
        cores_contagem[cor] += 1
    else:
        cores_contagem[cor] = 1

    # Aguarde por um curto período de tempo antes de verificar o próximo pixel
    time.sleep(0.1)


# Encontre a cor que mais ocorreu
cor_mais_comum = max(cores_contagem, key=cores_contagem.get)

print(f"A cor que mais ocorreu foi: {cor_mais_comum} com {cores_contagem[cor_mais_comum]} ocorrências.")

