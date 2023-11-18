# Importa a biblioteca necessária
import pyrebase
import time
import datetime  # Adicionado para manipulação de datas

# Configuração dos bancos de dados
config3 = {
    "apiKey": "AIzaSyBMhul_wFoi-7LFtS6PP22vCi8Op3RYIlE",
    "authDomain": "poker-dados-2.firebaseapp.com",
    "databaseURL": "https://poker-dados-2-default-rtdb.firebaseio.com",
    "projectId": "poker-dados-2",
    "storageBucket": "poker-dados-2.appspot.com",
    "messagingSenderId": "712512083103",
    "appId": "1:712512083103:web:6afab600554fdf1287beaa"
}

config2 = {
    "apiKey": "AIzaSyDDzQMVxpKKqBZrDlhA9E4sInXB5toVRT8",
    "authDomain": "pokerdados-6884e.firebaseapp.com",
    "databaseURL": "https://pokerdados-6884e-default-rtdb.firebaseio.com",
    "projectId": "pokerdados-6884e",
    "storageBucket": "pokerdados-6884e.appspot.com",
    "messagingSenderId": "240019464920",
    "appId": "1:240019464920:web:a746cddaf41f43642aadad"
}

config1 = {
    "apiKey": "AIzaSyBWJEh-hD6UIkpMz8J4V2Es4mP2AtuHx9k",
    "authDomain": "poker-dados.firebaseapp.com",
    "databaseURL": "https://poker-dados-default-rtdb.firebaseio.com",
    "projectId": "poker-dados",
    "storageBucket": "poker-dados.appspot.com",
    "messagingSenderId": "968238353891",
    "appId": "1:968238353891:web:b0026783a590efa99c24d6"
}

# Variável para armazenar a última data de acesso
ultima_data_acesso = None


def escolher_configuracao_e_db():
    """
    Escolhe a configuração do banco com base na data atual.

    Retorna:
    tuple: Configuração do banco de dados e referência ao banco.
    """
    global db
    global configuracao_banco
    dia_atual = datetime.datetime.now().day

    if dia_atual <= 10:
        configuracao = config2
        print('Sera usado o bando 2')
    elif 10 < dia_atual <= 20:
        configuracao = config1
        print('Sera usado o bando 1')
    else:
        configuracao = config3
        print('Sera usado o bando 3')


    # Inicializa o Firebase com a configuração escolhida
    firebase = pyrebase.initialize_app(configuracao)
    db = firebase.database()

    return configuracao, db


# Escolhe a configuração do banco com base na data atual
configuracao_banco, db = escolher_configuracao_e_db()


def unir_e_atualizar_dados():
    # Inicializa os bancos de dados
    firebase_3 = pyrebase.initialize_app(config3)
    firebase_2 = pyrebase.initialize_app(config2)
    firebase_1 = pyrebase.initialize_app(config1)

    # Obtém referências para os bancos de dados
    db_1 = firebase_1.database()
    db_2 = firebase_2.database()
    db_3 = firebase_3.database()

    try:
        # Obtém os dados da referência 'ips' em ambos os bancos
        dados_1 = db_1.child('ips').get().val()
        dados_2 = db_2.child('ips').get().val()
        dados_3 = db_3.child('ips').get().val()

        # Se as listas de IPs estão vazias ou não existem, inicializa listas vazias
        if dados_1 is None:
            dados_1 = []
        if dados_2 is None:
            dados_2 = []
        if dados_3 is None:
            dados_3 = []

        # Combina os dados de ambos os bancos
        dados_combinados = dados_1 + dados_2 + dados_3

        # Remove IPs duplicados
        dados_combinados = [dict(t) for t in {tuple(d.items()) for d in dados_combinados}]

        # Remove IPs que estão na lista por mais de 24 horas
        dados_combinados = [ip_info for ip_info in dados_combinados if time.time() - ip_info['timestamp'] <= 24 * 3600]

        # Atualiza a referência 'ips' nos dois bancos
        db_1.child('ips').set(dados_combinados)
        db_2.child('ips').set(dados_combinados)
        db_3.child('ips').set(dados_combinados)

        print("Dados unidos, duplicatas removidas e IPs antigos removidos. Atualização concluída!")

    except Exception as e:
        print(f"Erro ao unir e atualizar dados: {e}")


def verifica_e_adiciona_ip(ip):
    global ultima_data_acesso
    global db
    global configuracao_banco

    print('Testa se IP já foi usado')

    # Obtém a lista atual de IPs do Firebase
    lista_ips = db.child('ips').get().val()

    # Se a lista de IPs está vazia ou não existe, inicializa uma lista vazia
    if lista_ips is None:
        lista_ips = []

    # Verifica se a última data de acesso é nula ou se o dia mudou desde o último acesso
    if ultima_data_acesso is None or ultima_data_acesso.day != datetime.datetime.now().day:
        # Escolhe a configuração do banco com base na data atual
        nova_configuracao, novo_db = escolher_configuracao_e_db()

        # Atualiza a referência e o banco se a configuração mudou
        if nova_configuracao != configuracao_banco:
            print("Configuração do banco alterada. Unindo e atualizando dados.")
            unir_e_atualizar_dados()
            configuracao_banco, db = nova_configuracao, novo_db

        # Atualiza a última data de acesso
        ultima_data_acesso = datetime.datetime.now()

    # Remove IPs que estão na lista por mais de 24 horas
    lista_ips = [ip_info for ip_info in lista_ips if time.time() - ip_info['timestamp'] <= 24 * 3600]

    # Verifica se o IP já está na lista
    for ip_info in lista_ips:
        if ip_info['ip'] == ip:
            print(f"IP {ip} já está na lista.")
            return False  # O IP já está na lista, retorna False

    # Adiciona o IP à lista com o timestamp atual
    lista_ips.append({
        'ip': ip,
        'timestamp': time.time()
    })

    # Atualiza a lista de IPs no Firebase
    db.child('ips').set(lista_ips)
    print(f"IP {ip} adicionado à lista de IPs.")
    return True  # O IP não estava na lista, retorna True e foi adicionado

# # Chama a função para verificar e adicionar IP (substitua pelo IP desejado)
# verifica_e_adiciona_ip('1.1.1.1')

# unir_e_atualizar_dados()
#
#unir_e_atualizar_dados()


















# # Importa a biblioteca necessária
# import pyrebase
# import time
#
# # Configuração do Firebase
# config2 = {
#   "apiKey": "AIzaSyDDzQMVxpKKqBZrDlhA9E4sInXB5toVRT8",
#   "authDomain": "pokerdados-6884e.firebaseapp.com",
#   "databaseURL": "https://pokerdados-6884e-default-rtdb.firebaseio.com",
#   "projectId": "pokerdados-6884e",
#   "storageBucket": "pokerdados-6884e.appspot.com",
#   "messagingSenderId": "240019464920",
#   "appId": "1:240019464920:web:a746cddaf41f43642aadad"
# }
#
# config = {
#     "apiKey": "AIzaSyBWJEh-hD6UIkpMz8J4V2Es4mP2AtuHx9k",
#     "authDomain": "poker-dados.firebaseapp.com",
#     "databaseURL": "https://poker-dados-default-rtdb.firebaseio.com",
#     "projectId": "poker-dados",
#     "storageBucket": "poker-dados.appspot.com",
#     "messagingSenderId": "968238353891",
#     "appId": "1:968238353891:web:b0026783a590efa99c24d6"
# }
#
#
#
# # Inicializa o Firebase
# firebase = pyrebase.initialize_app(config3)
#
# # Obtém uma referência para o banco de dados
# db = firebase.database()
#
#
# def verifica_e_adiciona_ip(ip):
#     """
#     Verifica se um IP está na lista de IPs no Firebase e adiciona se não estiver.
#
#     Parâmetros:
#     ip (str): Endereço de IP a ser verificado e adicionado.
#
#     Retorna:
#     bool: True se o IP foi adicionado à lista, False se já estava na lista.
#
#     Características Relacionadas ao Tempo:
#     - A função remove IPs da lista que foram adicionados há mais de 24 horas.
#     - Cada IP na lista é armazenado com um timestamp indicando o momento em que foi adicionado.
#
#     Como Usar:
#     ip = '192.168.1.1'  # Substitua pelo IP que deseja verificar/adicionar
#     resultado = verifica_e_adiciona_ip(ip)
#     if resultado:
#         print(f"O IP {ip} foi adicionado à lista de IPs.")
#     else:
#         print(f"O IP {ip} já está na lista de IPs.")
#     """
#
#
#     print('Testa se IP ja fou usado')
#
#     # Obtém a lista atual de IPs do Firebase
#     lista_ips = db.child('ips').get().val()
#
#     # Se a lista de IPs está vazia ou não existe, inicializa uma lista vazia
#     if lista_ips is None:
#         lista_ips = []
#
#     # Remove IPs que estão na lista por mais de 24 horas
#     lista_ips = [ip_info for ip_info in lista_ips if time.time() - ip_info['timestamp'] <= 20 * 3600]
#
#     # Verifica se o IP já está na lista
#     for ip_info in lista_ips:
#         if ip_info['ip'] == ip:
#             print(f"IP {ip} já está na lista.")
#             return False  # O IP já está na lista, retorna False
#
#     # Adiciona o IP à lista com o timestamp atual
#     lista_ips.append({
#         'ip': ip,
#         'timestamp': time.time()
#     })
#
#     # Atualiza a lista de IPs no Firebase
#     db.child('ips').set(lista_ips)
#     print(f"IP {ip} adicionado à lista de IPs.")
#     return True  # O IP não estava na lista, retorna True e foi adicionado
#
#
# verifica_e_adiciona_ip('192.168.1.1')