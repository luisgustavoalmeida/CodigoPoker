# pip install pyrebase5
import time
import socket
import os
import pyrebase

config = {
  "apiKey": "AIzaSyDDzQMVxpKKqBZrDlhA9E4sInXB5toVRT8",
  "authDomain": "pokerdados-6884e.firebaseapp.com",
  "databaseURL": "https://pokerdados-6884e-default-rtdb.firebaseio.com",
  "projectId": "pokerdados-6884e",
  "storageBucket": "pokerdados-6884e.appspot.com",
  "messagingSenderId": "240019464920",
  "appId": "1:240019464920:web:a746cddaf41f43642aadad"
}

global dado_global

# Obter o nome do computador
nome_computador = socket.gethostname()
# Obter o nome de usuário
nome_usuario = os.getlogin()
# nome do computador e do usuario
nome_completo = socket.gethostname() + "_" + os.getlogin()

dicionari_pc = {'PC-I5-8600K_PokerIP':  'PC01',
                'PC-I5-8600K_lgagu':    'PC02',
                'PC-I5-8600K_Poker':    'PC03',

                'PC-I5-9400A_PokerIP':  'PC04',
                'PC-I5-9400A_lgagu':    'PC05',
                'PC-I5-9400A_Poker':    'PC06',

                'PC-I5-9400B_PokerIP':  'PC07',
                'PC-I5-9400B_lgagu':    'PC08',
                'PC-I5-9400B_Poker':    'PC09',

                'PC-I5-9400C_PokerIP':  'PC10',
                'PC-I5-9400C_lgagu':    'PC11',
                'PC-I5-9400C_Poker':    'PC12',

                'PC-R5-7600A_PokerIP':  'PC13',
                'PC-R5-7600A_lgagu':    'PC14',
                'PC-R5-7600A_Poker':    'PC15',

                'PC-I7-11850H_PokerIP': 'PC16',
                'PC-I7-11850H_lgagu':   'PC17',
                'PC-I7-11850H_Poker':   'PC18',

                'PC-i3-8145U_PokerIP':  'PC19',

                'PC-I7-9700KF_PokerIP': 'PC20',
                'PC-I7-9700KF_lgagu':   'PC21',
                'PC-I7-9700KF_Poker':   'PC22',

                'Thiago-PC_Thiago': 'PC23'
                }


# Inicializa o Firebase
firebase = pyrebase.initialize_app(config)

# Obtém uma referência para o banco de dados
db = firebase.database()

nome_pc = str(dicionari_pc[nome_completo])
print(nome_pc)

caminho_resposta = "Resposta/" + nome_pc
print(caminho_resposta)

# Referência para o nó do Firebase que você deseja observar
ref = firebase.database().child(f"Comandos")  # colocar o caminho de onde vem os comandos


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
        alterar_dado_novo(dado_atualizado)

    except Exception as e:
        print("Erro ao processar atualização:", e)

# Registrar o observador usando o método "stream"
# A função "on" irá chamar a função "on_update" sempre que ocorrer uma edição no nó referenciado
ref.stream(on_update)

# Função para realizar escrita no Firebase
def escrever_dado(dado):
    try:
        db.child(caminho_resposta).set(dado)
        print(f"Dado '{dado}' escrito com sucesso no nó '{caminho_resposta}'.")
    except Exception as e:
        print("Erro ao escrever dado no Firebase:", e)

# Função para realizar leitura do Firebase
def ler_dado(no):
    try:
        dado = db.child(no).get().val()
        if dado:
            print(f"Dado lido do nó '{no}': {dado}")
        else:
            print(f"Nó '{no}' não possui nenhum dado.")
    except Exception as e:
        print("Erro ao ler dado do Firebase:", e)


def obter_dado():
    global dado_global
    return dado_global

def alterar_dado_novo(valor):
    global dado_global
    dado_global = valor


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