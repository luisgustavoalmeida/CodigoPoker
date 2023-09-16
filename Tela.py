# Importe as bibliotecas necessárias
import tkinter as tk
from tkinter import scrolledtext

import Firebese

# Função que será chamada quando um botão for pressionado
def button_name(text):
    print(text)

    # Divide a string em três partes com base no hífen
    partes = text.split("-")

    # Verifica se há três partes após a divisão
    if len(partes) == 3:
        # Atribui cada parte a uma variável
        item1, item2, item3 = partes

        # Imprime os três itens separados
        # print("Item 1:", item1)
        # print("Item 2:", item2)
        # print("Item 3:", item3)

        # Verifica o valor de item1 (primeira parte da string)
        if item1 == "A":
            if item2 == "0":
                # Se item1 é "A" e item2 é "0", é um comando coletivo no arranjo 1
                print("comando coletivo no arranjo 1")
                Firebese.enviar_comando_coletivo(Firebese.arranjo1_pc, item3)
            else:
                # Se item1 é "A" e item2 não é "0", é um comando individual no arranjo 1
                print("comando individual no arranjo 1")
                item2_str = str(item2).zfill(2)
                comando_individual = [f'Comandos1/PC{item2_str}']
                Firebese.enviar_comando_coletivo(comando_individual, item3)

        elif item1 == "B":
            if item2 == "0":
                # Se item1 é "B" e item2 é "0", é um comando coletivo no arranjo 2
                print("comando coletivo no arranjo 2")
                Firebese.enviar_comando_coletivo(Firebese.arranjo2_pc, item3)
            else:
                # Se item1 é "B" e item2 não é "0", é um comando individual no arranjo 2
                print("comando individual no arranjo 2")
                item2_str = str(item2).zfill(2)
                comando_individual = [f'Comandos2/PC{item2_str}']
                Firebese.enviar_comando_coletivo(comando_individual, item3)

        elif item1 == "C":
            if item2 == "0":
                # Se item1 é "C" e item2 é "0", é um comando coletivo no arranjo 3
                print("comando coletivo no arranjo 3")
                Firebese.enviar_comando_coletivo(Firebese.arranjo3_pc, item3)
            else:
                # Se item1 é "C" e item2 não é "0", é um comando individual no arranjo 3
                print("comando individual no arranjo 3")
                item2_str = str(item2).zfill(2)
                comando_individual = [f'Comandos3/PC{item2_str}']
                Firebese.enviar_comando_coletivo(comando_individual, item3)

        else:
            # Se item1 não for "A", "B" ou "C", o arranjo de computadores não está definido
            print("Arranjo de computadores não definido")
    else:
        # Se não houver três partes após a divisão, o texto de entrada não possui o formato esperado
        print("Texto de entrada não possui o formato esperado.")


# Função para criar um botão
def create_button(parent, text):
    # Crie um botão com o texto especificado
    botao = tk.Button(parent, text=text)
    # Associe a função button_name ao botão, passando o texto como argumento
    botao.config(command=lambda t=text: button_name(t))
    # Empacote o botão no widget pai (parent)
    botao.pack(fill="both", expand=True)
    return botao

# Função para criar uma área de texto com barra de rolagem
def create_info_area(parent):
    # Crie uma barra de rolagem vertical
    scrollbar = tk.Scrollbar(parent, orient="vertical")
    # Crie uma área de texto com rolagem, configurando a barra de rolagem
    info_text = scrolledtext.ScrolledText(parent, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    scrollbar.config(command=info_text.yview)
    # Empacote a área de texto e a barra de rolagem
    info_text.pack(side="top", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    return info_text

# Função para adicionar uma nova informação ao histórico de um arranjo específico
def add_info_to_history(info_text, text_widget):
    # Obtenha o texto atual na área de texto
    current_text = text_widget.get("1.0", "end-1c")
    # Limpe a área de texto
    text_widget.delete("1.0", tk.END)
    # Insira a nova informação no topo da área de texto
    text_widget.insert("1.0", info_text + "\n" + current_text)

# Crie uma janela do Tkinter
janela = tk.Tk()

# Defina a posição da janela para 0x0
janela.geometry("+0+0")
# Defina o tamanho da janela para 1000 x 500
janela.geometry("1920x1020")

# Defina o número de colunas e linhas
numero_colunas = 10

numero_linhas = 15

# Crie as áreas de informações
info_labels = []
info_text_widgets = []

# Letras para identificar cada arranjo
arranjo_letters = ["A", "B", "C"]


# Loop para criar os arranjos
for i in range(3):
    arranjo = tk.Frame(janela)  # Cria um novo arranjo (frame)
    info_text_widget = create_info_area(arranjo)  # Cria uma área de informações dentro do arranjo
    info_text_widgets.append(info_text_widget)  # Adiciona a área de informações à lista

    # Loop para criar as colunas e botões dentro de cada arranjo
    for j in range(numero_colunas):
        if 1 <= j <= 9:
            # Aplica a regra de mapeamento para os valores de j
            j = (j - 1) * 3 + 1 + i

        coluna = tk.Frame(arranjo)  # Cria uma nova coluna dentro do arranjo
        for k in range(numero_linhas):
            button_text = f"{arranjo_letters[i]}-{j}-{k}"  # Cria o texto do botão
            create_button(coluna, button_text)  # Cria um botão dentro da coluna
        coluna.pack(side="left", fill="both", expand=True)  # Empacota a coluna

    arranjo.pack(side="left", fill="both", expand=True)  # Empacota o arranjo


# Exiba a janela

# Use a função add_info_to_history para adicionar informações ao histórico de uma área de informações específica
add_info_to_history("Informação 1 do Arranjo 1", info_text_widgets[0])
add_info_to_history("Informação 1 do Arranjo 2", info_text_widgets[1])
add_info_to_history("Informação 1 do Arranjo 3", info_text_widgets[2])

# Inicie o loop principal da interface gráfica
janela.mainloop()
