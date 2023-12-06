# # Importa a biblioteca necessária
# import time
#
# import pyrebase
#
# # Configuração dos bancos de dados
# config3 = {
#     "apiKey": "AIzaSyBMhul_wFoi-7LFtS6PP22vCi8Op3RYIlE",
#     "authDomain": "poker-dados-2.firebaseapp.com",
#     "databaseURL": "https://poker-dados-2-default-rtdb.firebaseio.com",
#     "projectId": "poker-dados-2",
#     "storageBucket": "poker-dados-2.appspot.com",
#     "messagingSenderId": "712512083103",
#     "appId": "1:712512083103:web:6afab600554fdf1287beaa"
# }
#
# config2 = {
#     "apiKey": "AIzaSyDDzQMVxpKKqBZrDlhA9E4sInXB5toVRT8",
#     "authDomain": "pokerdados-6884e.firebaseapp.com",
#     "databaseURL": "https://pokerdados-6884e-default-rtdb.firebaseio.com",
#     "projectId": "pokerdados-6884e",
#     "storageBucket": "pokerdados-6884e.appspot.com",
#     "messagingSenderId": "240019464920",
#     "appId": "1:240019464920:web:a746cddaf41f43642aadad"
# }
#
# config1 = {
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
# def unir_e_atualizar_dados():
#     # Inicializa os bancos de dados
#     firebase_3 = pyrebase.initialize_app(config3)
#     firebase_2 = pyrebase.initialize_app(config2)
#     firebase_1 = pyrebase.initialize_app(config1)
#
#     # Obtém referências para os bancos de dados
#     db_1 = firebase_1.database()
#     db_2 = firebase_2.database()
#     db_3 = firebase_3.database()
#
#     try:
#         # Obtém os dados da referência 'ips' em ambos os bancos
#         dados_1 = db_1.child('ips').get().val()
#         dados_2 = db_2.child('ips').get().val()
#         dados_3 = db_3.child('ips').get().val()
#
#         # Se as listas de IPs estão vazias ou não existem, inicializa listas vazias
#         if dados_1 is None:
#             dados_1 = []
#         if dados_2 is None:
#             dados_2 = []
#         if dados_3 is None:
#             dados_3 = []
#
#         # Combina os dados de ambos os bancos
#         dados_combinados = dados_1 + dados_2 + dados_3
#
#         # Remove IPs duplicados
#         dados_combinados = [dict(t) for t in {tuple(d.items()) for d in dados_combinados}]
#
#         # Remove IPs que estão na lista por mais de 24 horas
#         dados_combinados = [ip_info for ip_info in dados_combinados if time.time() - ip_info['timestamp'] <= 24 * 3600]
#
#         # Atualiza a referência 'ips' nos dois bancos
#         db_1.child('ips').set(dados_combinados)
#         db_2.child('ips').set(dados_combinados)
#         db_3.child('ips').set(dados_combinados)
#
#         print("Dados unidos, duplicatas removidas e IPs antigos removidos. Atualização concluída!")
#
#     except Exception as e:
#         print(f"Erro ao unir e atualizar dados: {e}")
#
#
# unir_e_atualizar_dados()
