# Importa a biblioteca necessária
import pyrebase
import time

# Configuração do Firebase
# config = {
#   "apiKey": "AIzaSyDDzQMVxpKKqBZrDlhA9E4sInXB5toVRT8",
#   "authDomain": "pokerdados-6884e.firebaseapp.com",
#   "databaseURL": "https://pokerdados-6884e-default-rtdb.firebaseio.com",
#   "projectId": "pokerdados-6884e",
#   "storageBucket": "pokerdados-6884e.appspot.com",
#   "messagingSenderId": "240019464920",
#   "appId": "1:240019464920:web:a746cddaf41f43642aadad"
# }

config = {
    "apiKey": "AIzaSyBWJEh-hD6UIkpMz8J4V2Es4mP2AtuHx9k",
    "authDomain": "poker-dados.firebaseapp.com",
    "databaseURL": "https://poker-dados-default-rtdb.firebaseio.com",
    "projectId": "poker-dados",
    "storageBucket": "poker-dados.appspot.com",
    "messagingSenderId": "968238353891",
    "appId": "1:968238353891:web:b0026783a590efa99c24d6"
}


# Inicializa o Firebase
firebase = pyrebase.initialize_app(config)

# Obtém uma referência para o banco de dados
db = firebase.database()


def verifica_e_adiciona_ip(ip):
    """Verifica se um IP está na lista de IPs no Firebase e adiciona se não estiver.

    Parâmetros:
    ip (str): Endereço de IP a ser verificado e adicionado.

    Retorna:
    bool: True se o IP foi adicionado à lista, False se já estava na lista.

    Características Relacionadas ao Tempo:
    - A função remove IPs da lista que foram adicionados há mais de 24 horas.
    - Cada IP na lista é armazenado com um timestamp indicando o momento em que foi adicionado.

    Como Usar:
    ip = '192.168.1.1'  # Substitua pelo IP que deseja verificar/adicionar
    resultado = verifica_e_adiciona_ip(ip)
    if resultado:
        print(f"O IP {ip} foi adicionado à lista de IPs.")
    else:
        print(f"O IP {ip} já está na lista de IPs.")"""


    print('Testa se IP ja fou usado')

    # Obtém a lista atual de IPs do Firebase
    lista_ips = db.child('ips').get().val()

    # Se a lista de IPs está vazia ou não existe, inicializa uma lista vazia
    if lista_ips is None:
        lista_ips = []

    # Remove IPs que estão na lista por mais de 24 horas
    lista_ips = [ip_info for ip_info in lista_ips if time.time() - ip_info['timestamp'] <= 20 * 3600]

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


