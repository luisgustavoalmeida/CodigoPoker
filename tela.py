# import tkinter as tk
#
# def button_name(text):
#     print(text)
#
# # Crie uma janela do Tkinter
# janela = tk.Tk()
#
# # Defina a posição da janela para 0x0
# janela.geometry("+0+0")
# # Defina o tamanho da janela para 1000 x 500
# janela.geometry("1920x1020")
#
# # Crie o primeiro arranjo
# primeiro_arranjo = tk.Frame(janela)
#
# # Crie a área de informações do primeiro arranjo
# primeiro_letreiro = tk.Label(primeiro_arranjo, text="Esta é a área de informações do primeiro arranjo de computadores")
# primeiro_letreiro.pack(side="top", fill="both", expand=True)
# # Defina a borda do letreiro
# primeiro_letreiro.config(bd=1, relief="solid")
#
#
#
# # Crie 6 colunas com 20 botões cada coluna no primeiro arranjo
# primeiro_colunas = []
# for i in range(10):
#   coluna = tk.Frame(primeiro_arranjo)
#   for j in range(15):
#     botao = tk.Button(coluna, text="Botão %d" % (i * 20 + j))
#     botao.config(command=lambda button=botao: button_name(button.cget("text")))
#     botao.pack()
#   primeiro_colunas.append(coluna)
#
# # Coloque as colunas no primeiro arranjo
# for coluna in primeiro_colunas:
#   coluna.pack(side="left", fill="both", expand=True)
#
# # Crie o segundo arranjo
# segundo_arranjo = tk.Frame(janela)
#
# # Crie a área de informações do segundo arranjo
# segundo_letreiro = tk.Label(segundo_arranjo, text="Esta é a área de informações do segundo arranjo de computadores")
# segundo_letreiro.pack(side="top", fill="both", expand=True)
# # Defina a borda do letreiro
# segundo_letreiro.config(bd=1, relief="solid")
#
# # Crie 6 colunas com 20 botões cada coluna no segundo arranjo
# segundo_colunas = []
# for i in range(10):
#   coluna = tk.Frame(segundo_arranjo)
#   for j in range(200, 215):
#     botao = tk.Button(coluna, text="Botão %d" % (i * 20 + j))
#     botao.config(command=lambda button=botao: button_name(button.cget("text")))
#     botao.pack()
#   segundo_colunas.append(coluna)
#
# # Coloque as colunas no segundo arranjo
# for coluna in segundo_colunas:
#   coluna.pack(side="left", fill="both", expand=True)
#
# # Crie o terceiro arranjo
# terceiro_arranjo = tk.Frame(janela)
#
# # Crie a área de informações do terceiro arranjo
# terceiro_letreiro = tk.Label(terceiro_arranjo, text="Esta é a área de informações do terceiro arranjo de computadores")
# terceiro_letreiro.pack(side="top", fill="both", expand=True)
# # Defina a borda do letreiro
# terceiro_letreiro.config(bd=1, relief="solid")
#
# # Crie 6 colunas com 20 botões cada coluna no terceiro arranjo
# terceiro_colunas = []
# for i in range(10):
#   coluna = tk.Frame(terceiro_arranjo)
#   for j in range(15):
#     botao = tk.Button(coluna, text="Botão %d" % (i * 20 + j))
#     # Defina a ação do botão
#     botao.config(command=lambda button=botao: button_name(button.cget("text")))
#     botao.pack()
#   terceiro_colunas.append(coluna)
#
# # Coloque as colunas no terceiro arranjo
# for coluna in terceiro_colunas:
#   coluna.pack(side="left", fill="both", expand=True)
#
# # Coloque os arranjos na tela
# primeiro_arranjo.pack(side="left", fill="both", expand=True)
# segundo_arranjo.pack(side="left", fill="both", expand=True)
# terceiro_arranjo.pack(side="left", fill="both", expand=True)
#
# # Exiba a janela
# janela.mainloop()
# #
# #
