#
# import win32gui
#
# # Constante para o nome do navegador
# NOME_NAVEGADOR = "Google Chrome"
#
# def encontrar_janela_navegador():
#     """Encontra a janela do navegador desejado."""
#     try:
#         janelas_encontradas = []
#         win32gui.EnumWindows(enum_windows_callback, janelas_encontradas)
#         handle_navegador = None
#         for handle in janelas_encontradas:
#             titulo_janela = win32gui.GetWindowText(handle)
#             if NOME_NAVEGADOR in titulo_janela:
#                 handle_navegador = handle
#                 #return handle
#
#         if handle_navegador:
#             #print("Handle da janela do navegador:", handle_navegador)
#             ativar_janela(handle_navegador)
#             return
#         else:
#             print("Nenhuma janela do navegador encontrada.")
#             return
#     except Exception as e:
#         print("Ocorreu um erro ao encontrar a janela do navegador:", str(e))
#     return
#
#
# def ativar_janela(handle):
#     """Ativa a janela com o handle especificado."""
#     try:
#         if handle is not None and handle != 0:
#             win32gui.SetForegroundWindow(handle)
#     except Exception as e:
#         print("Ocorreu um erro ao ativar a janela:", str(e))
#     return
# def enum_windows_callback(hwnd, results):
#     """Callback function used with EnumWindows() to append window handles to results list."""
#     try:
#         results.append(hwnd)
#     except Exception as e:
#         print("Ocorreu um erro ao ativar a janela:", str(e))
#     return
# # Encontra a janela do navegador
# #handle_navegador = encontrar_janela_navegador()
#
#
#
#
#
# # import win32con
# # import win32gui
# #
# #
# # def enum_windows_callback(hwnd, results):
# #     """Callback function used with EnumWindows() to append window handles to results list."""
# #     results.append(hwnd)
# #
# # # Nome da janela do navegador que você deseja encontrar
# # nome_navegador = "Google Chrome"
# #
# # # Lista para armazenar os handles das janelas encontradas
# # janelas_encontradas = []
# #
# # # Chama a função EnumWindows() da biblioteca win32gui para obter os handles das janelas
# # win32gui.EnumWindows(enum_windows_callback, janelas_encontradas)
# #
# # # Itera sobre a lista de handles das janelas para encontrar a janela do navegador desejado
# # for handle in janelas_encontradas:
# #     titulo_janela = win32gui.GetWindowText(handle)
# #     if nome_navegador in titulo_janela:
# #         print("Handle da janela do navegador:", handle)
# #         #break
# #
# #         if handle != 0:
# #             # Tornar a janela ativa e superior
# #             #Esta linha faz com que a janela com o handle especificado seja trazida para o primeiro plano e se torne a janela ativa
# #             win32gui.SetForegroundWindow(handle)
# #             #Essa linha restaura a janela (caso esteja minimizada) e a exibe em seu tamanho normal.
# #             #win32gui.ShowWindow(handle, win32con.SW_RESTORE)
# #             #Esta linha mostra a janela especificada na tela. O parâmetro SW_SHOWNA é usado para exibir a janela sem ativá-la ou torná-la ativa.
# #             #win32gui.ShowWindow(handle, win32con.SW_SHOWNA)
# #             #Essa linha move a janela para a posição (0, 0) da tela e define sua largura para 1440 pixels e sua altura para 1045 pixels. O último argumento True indica que a janela deve ser redesenhada para refletir as alterações.
# #             #win32gui.MoveWindow(handle, 0, 0, 1440, 1050, True)
#
