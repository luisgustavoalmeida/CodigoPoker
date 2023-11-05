# # Importa a biblioteca necessária
# import pyrebase
# import time
#
# # Configuração do Firebase
# config = {
#   "apiKey": "AIzaSyDDzQMVxpKKqBZrDlhA9E4sInXB5toVRT8",
#   "authDomain": "pokerdados-6884e.firebaseapp.com",
#   "databaseURL": "https://pokerdados-6884e-default-rtdb.firebaseio.com",
#   "projectId": "pokerdados-6884e",
#   "storageBucket": "pokerdados-6884e.appspot.com",
#   "messagingSenderId": "240019464920",
#   "appId": "1:240019464920:web:a746cddaf41f43642aadad"
# }
#
# # Inicializa o Firebase
# firebase = pyrebase.initialize_app(config)
#
# # Obtém uma referência para o banco de dados
# db = firebase.database()
#
#
# lista_ips = []
#
# lista_ips = db.child('ips').get().val()
#
# print(lista_ips)
#
#
# def on_update(message):
#     global lista_ips
#     try:
#         if message["event"] == "put":
#             # Se ocorrer uma modificação na lista 'ips' no Firebase,
#             # atualiza a lista_ips local com os novos dados.
#             lista_ips = db.child('ips').get().val()
#             print("Lista de IPs atualizada:", lista_ips)
#     except Exception as e:
#         print("Erro ao processar atualização:", e)
#
#
# try:
#     # Adiciona um observador para a lista 'ips' no Firebase.
#     db.child('ips').stream(on_update)
# except Exception as e:
#     print("Erro ao estabelecer o observador:", e)
#
#
# def verifica_e_adiciona_ip(ip):
#     '''
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
#     '''
#
#     print('Testa se IP ja fou usado')
#
#     global lista_ips
#     # Se a lista de IPs está vazia ou não existe, inicializa uma lista vazia
#     if lista_ips is None:
#         lista_ips = []
#
#     # Remove IPs que estão na lista por mais de 24 horas
#     lista_ips = [ip_info for ip_info in lista_ips if time.time() - ip_info['timestamp'] <= 24 * 3600]
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
# # Mantém o programa em execução para receber atualizações.
# while True:
#     time.sleep(1)
#
#
