#
# import PySimpleGUI as sg
#
# # Defina as posições iniciais e finais em x e y
# x_ini, y_ini, x_fim, y_fim = (742, 244, 793, 260)
#
#
# layout = [[sg.Text('Região', font='Any 20')],
#           [sg.Button('Exit')]]
#
# window = sg.Window('Transparent Window',
#                    layout,
#                    no_titlebar=True,
#                    location=(x_ini, y_ini),
#                    size=(x_fim - x_ini, y_fim - y_ini),
#                    finalize=True,
#                    element_justification='c',
#                    alpha_channel=0.5,  # Define a transparência da janela
#                    transparent_color='green')  # Define a cor de transparência
#
# # Move a janela para a posição
# window.TKroot.geometry("+{}+{}".format(x_ini, y_ini ))
#
# while True:
#     event, values = window.read()
#     if event == sg.WINDOW_CLOSED or event == 'Exit':
#         break
#
# window.close()
#
