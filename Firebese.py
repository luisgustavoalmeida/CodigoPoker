# pip install pyrebase5
import time
import socket
import os
import pyrebase
import re
# importa o dicionário com os nomes dos computadores e o námero referete a cada um
from Google import dicionari_token_credencial_n

config = {
  "apiKey": "AIzaSyDDzQMVxpKKqBZrDlhA9E4sInXB5toVRT8",
  "authDomain": "pokerdados-6884e.firebaseapp.com",
  "databaseURL": "https://pokerdados-6884e-default-rtdb.firebaseio.com",
  "projectId": "pokerdados-6884e",
  "storageBucket": "pokerdados-6884e.appspot.com",
  "messagingSenderId": "240019464920",
  "appId": "1:240019464920:web:a746cddaf41f43642aadad"
}

# Dicionário global para armazenar as variáveis com seus respectivos valores
global_variables = {
    'group1': {'PC01': None, 'PC04': None, 'PC07': None, 'PC10': None, 'PC13': None, 'PC16': None, 'PC19': None, 'PC22': None, 'PC25': None},
    'group2': {'PC02': None, 'PC05': None, 'PC08': None, 'PC11': None, 'PC14': None, 'PC17': None, 'PC20': None, 'PC23': None, 'PC26': None},
    'group3': {'PC03': None, 'PC06': None, 'PC09': None, 'PC12': None, 'PC15': None, 'PC18': None, 'PC21': None, 'PC24': None, 'PC27': None},
}
orderem_chave = {
    'group1': ['PC01', 'PC04', 'PC07', 'PC10', 'PC13', 'PC16', 'PC19', 'PC22', 'PC25'],
    'group2': ['PC02', 'PC05', 'PC08', 'PC11', 'PC14', 'PC17', 'PC20', 'PC23', 'PC26'],
    'group3': ['PC03', 'PC06', 'PC09', 'PC12', 'PC15', 'PC18', 'PC21', 'PC24', 'PC27'],
}
teve_atualizacao = False

def cria_caminho_resposta_fb():
    """Função destinada a manipular o dicionário com os nomes dos computadores
    e criar um caminho para apontar na função callback """

    # Obtenha o nome completo do computador e do usuário
    nome_completo = socket.gethostname() + "_" + os.getlogin()

    # Crie um dicionário com os valores formatados
    dicionari_pc = {}
    for chave, (_, _, valor) in dicionari_token_credencial_n.items():
        # Formate o valor para ter dois dígitos e adicione "PC" antes
        valor_formatado = f"PC{valor:02d}"
        dicionari_pc[chave] = valor_formatado

    # Verifique se o nome completo existe no dicionário
    if nome_completo in dicionari_pc:
        conteudo = dicionari_pc[nome_completo]
        print(f"Conteúdo para {nome_completo}: {conteudo}")

        # Verifique em qual grupo o conteúdo está
        for grupo, membros in global_variables.items():
            if conteudo in membros:
                # Use uma expressão regular para extrair o número após 'group'
                numero_grupo = re.search(r'group(\d+)', grupo).group(1)
                # Use re.sub para substituir "group" por "Comandos"
                grupo_modificado = re.sub(r'group', r'Comandos', grupo)
                print(f"{conteudo} está no grupo {grupo_modificado} ({numero_grupo})")
                caminho_resposta = f'{grupo_modificado}/{conteudo}'
                print(caminho_resposta)
                return caminho_resposta
        else:
            print(f"{conteudo} não está em nenhum dos grupos")
    else:
        print(f"{nome_completo} não encontrado no dicionário")

#  lista com os computadores que vao dar comando nos escravos, colocar nesta lista para funcionar como metre
lista_PC_meste = ('PC-I7-9700KF', 'PC-i3-8145U')

nome_computador = socket.gethostname()

if nome_computador in lista_PC_meste:
    print(f"O nome do computador ({nome_computador}) está na lista de PCs mestres.")
    caminho_resposta = f"Resposta1"
else:
    print(f"O nome do computador ({nome_computador}) não está na lista de PCs mestres.")
    caminho_resposta = cria_caminho_resposta_fb()


# Define listas de arranjos de computadores cada arranjo será uma mesa diferente
arranjo1_pc = ('Comandos1/PC01', 'Comandos1/PC04', 'Comandos1/PC07',
               'Comandos1/PC10', 'Comandos1/PC13', 'Comandos1/PC16',
               'Comandos1/PC19', 'Comandos1/PC22', 'Comandos1/PC25')

arranjo2_pc = ('Comandos2/PC02', 'Comandos2/PC05', 'Comandos2/PC08',
               'Comandos2/PC11', 'Comandos2/PC14', 'Comandos2/PC17',
               'Comandos2/PC20', 'Comandos2/PC23', 'Comandos2/PC26')

arranjo3_pc = ('Comandos3/PC03', 'Comandos3/PC06', 'Comandos3/PC09',
               'Comandos3/PC12', 'Comandos3/PC15', 'Comandos3/PC18',
               'Comandos3/PC21', 'Comandos3/PC24', 'Comandos3/PC27')

# Inicializa o Firebase
firebase = pyrebase.initialize_app(config)

# Obtém uma referência para o banco de dados
db = firebase.database()

def enviar_comando_coletivo(arranjo, comando):

    """Envie nesta fonção dois parametros que pode ser a tiplae dos arranjos dos conputadores "arranjo3_pc" ou
    uma lista do com um unico itêm "['Comandos3/PC03']" que contenha o caminho e nome do computado a ser atualizado.
    O segundo paremetro a ser recebido deve ser o comando que deve ser executado pelo arranjo de computadores ou pelo
    computador individual ex: "senta", "passa" ..."""

    atualizacoes = {}
    for caminho in arranjo:
        # Define a chave do dicionário como o caminho e o valor como o comando
        atualizacoes[caminho] = comando
    db.update(atualizacoes) # responsável por atualizar os dados no banco de dados Firebase

# Referência para o nó do Firebase que você deseja observar
ref = firebase.database().child(caminho_resposta)  # colocar o caminho de onde vem os comandos
# Função de callback para manipular os dados quando houver uma atualização
def on_update(event):
    try:
        print("Atualização detectada:")
        print(event)  # Aqui você pode acessar diretamente os dados atualizados
        # Acessar o valor associado à chave 'data' no dicionário 'event'
        dado_atualizado = event['data']
        caminho_atualizado = event['path']
        print(caminho_atualizado)
        print(dado_atualizado)
        alterar_dado_global(caminho_atualizado, dado_atualizado)

    except Exception as e:
        print("Erro ao processar atualização:", e)

# Registrar o observador usando o método "stream"
# A função "on" irá chamar a função "on_update" sempre que ocorrer uma edição no nó referenciado
ref.stream(on_update)

def alterar_dado_global(nome_variavel, valor):
    global global_variables
    global teve_atualizacao
    grupo = None
    nome_variavel = nome_variavel.replace('/', '')


    # Verifique em qual grupo colocar a variável com base no nome_variavel
    if nome_variavel in orderem_chave['group1']:
        grupo = global_variables['group1']
    elif nome_variavel in orderem_chave['group2']:
        grupo = global_variables['group2']
    elif nome_variavel in orderem_chave['group3']:
        grupo = global_variables['group3']

    if grupo is not None:
        grupo[nome_variavel] = valor
        teve_atualizacao = True
        #print(global_variables)
    else:
        print(f"A variável '{nome_variavel}' não corresponde a nenhum grupo existente.")

# Função para atualizar as informações do dicionário global com os dados do Firebase
def atualizar_dados_globais():
    try:
        # Use db.child() para acessar o nó desejado no Firebase
        dados_firebase = db.child(caminho_resposta).get()

        if dados_firebase.each() is not None:
            for dado in dados_firebase.each():
                chave = dado.key()  # Obtém a chave (nome da variável)
                valor = dado.val()  # Obtém o valor associado à chave
                alterar_dado_global(chave, valor)

    except Exception as e:
        print("Erro ao buscar dados do Firebase:", e)

    # print(f"Atualizado: {chave} -> {valor}")

# Chame a função para atualizar os dados globais com os dados do Firebase
atualizar_dados_globais()

# caminho = "Resposta1/PC01"
#
# def escrever_informacoes_aleatorias():
#
#     # Gere uma informação aleatória (por exemplo, um número aleatório)
#     informacao_aleatoria = random.randint(1, 100)
#     try:
#         # Escreva a informação aleatória no banco de dados Firebase
#         db.child(caminho).set(informacao_aleatoria)
#         print(f"Informação aleatória {informacao_aleatoria} escrita com sucesso em {caminho}")
#     except Exception as e:
#         print(f"Ocorreu um erro ao escrever a informação: {str(e)}")

# def loop_infinito():
#     global global_variables
#     while True:
#         print(global_variables)
#         escrever_informacoes_aleatorias()


#loop_infinito()


# Mantenha o programa em execução para continuar recebendo as atualizações
# while True:
#     time.sleep(10)
#     variavel = obter_dado()
#     print('ta rodando')
#     print(variavel)
#     pass


# escrever_dado("Comandos/PC01/Teste", "Firebase!")
#
# ler_dado("Comandos/PC01/Teste")