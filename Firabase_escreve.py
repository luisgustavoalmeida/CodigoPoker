#
# import pyrebase
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
# # Define listas de arranjos de computadores
# arranjo1_pc = ('Comandos1/PC01',
#                'Comandos1/PC04',
#                'Comandos1/PC07',
#                'Comandos1/PC10',
#                'Comandos1/PC13',
#                'Comandos1/PC16',
#                'Comandos1/PC19',
#                'Comandos1/PC22',
#                'Comandos1/PC25'
#                )
#
# arranjo2_pc = ('Comandos2/PC02',
#                'Comandos2/PC05',
#                'Comandos2/PC08',
#                'Comandos2/PC11',
#                'Comandos2/PC14',
#                'Comandos2/PC17',
#                'Comandos2/PC20',
#                'Comandos2/PC23',
#                'Comandos2/PC26'
#                )
#
# arranjo3_pc = ('Comandos3/PC03',
#                'Comandos3/PC06',
#                'Comandos3/PC09',
#                'Comandos3/PC12',
#                'Comandos3/PC15',
#                'Comandos3/PC18',
#                'Comandos3/PC21',
#                'Comandos3/PC24',
#                'Comandos3/PC27'
#                )
#
#
# def enviar_comando_coletivo(arranjo, comando):
#
#     """Envie nesta fonção dois parametros que pode ser a tiplae dos arranjo dos conputadores "arranjo3_pc" ou
#     uma lista do com um unico item "['Comandos3/PC03']" que contenha o caminho e nome do computado a ser atualizado.
#     o segundo paremetro a ser recebido deve ser o comando que deve ser executado pelo arranjo de computadores ou pelo
#     computador individual ex "senta", "passa" ..."""
#
#     atualizacoes = {}
#     for caminho in arranjo:
#         # Define a chave do dicionário como o caminho e o valor como o comando
#         atualizacoes[caminho] = comando
#     db.update(atualizacoes) # responsável por atualizar os dados no banco de dados Firebase
#
# # enviar_comando_coletivo(['Comandos3/PC03'],"teerfszxdfv")
#
#
#
#
#
#
