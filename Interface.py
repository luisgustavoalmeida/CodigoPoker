import tkinter as tk

# Crie uma janela do Tkinter
window = tk.Tk()

window.geometry("480x765")

# Crie 30 botões
buttons = []
botoes_por_coluna = 11
for i in range(botoes_por_coluna * 3):
    buttons.append(tk.Button(window, text="Botão %d" % i))


# Organize os botões em 3 colunas
for i in range(botoes_por_coluna):
    buttons[i].grid(row=i, column=0)
    buttons[i + botoes_por_coluna].grid(row=i, column=1)
    buttons[i + botoes_por_coluna * 2].grid(row=i, column=2)


# Defina a ação dos botões
for button in buttons:
    button.config(command=lambda button=button: change_variable(button.cget("text")))
    # Largura e altura
    button.config(width=20, height=1)
    # Espaçar os botões entre eles
    button.grid_configure(padx=2, pady=2)
    # Coloque bordas nos botões
    button.config(bd=3)


# Defina as variáveis
a = 0
b = 0
c = 0

# Defina a função de alteração das variáveis
def change_variable(text):
    global a, b, c
    if text == "Botão 0":
        a = a + 1
    elif text == "Botão 1":
        b = b + 1
    elif text == "Botão 2":
        c = c + 1
    print(text)


# Exiba a janela
window.mainloop()
