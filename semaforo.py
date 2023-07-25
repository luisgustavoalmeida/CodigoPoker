'''Para implementar o controle de concorrência em uma planilha do Google Sheets, você pode utilizar a funcionalidade de
trava (lock) fornecida pela API do Google Sheets. Existem duas opções de trava disponíveis: a trava de intervalo
(range lock) e a trava de planilha (sheet lock). A trava de intervalo permite que você bloqueie um intervalo
específico da planilha para que apenas um usuário possa modificá-lo por vez. Já a trava de planilha permite bloquear
a planilha inteira para que apenas um usuário possa acessá-la por vez. Para utilizar as travas, você precisará adicionar
a permissão "https://www.googleapis.com/auth/drive" à lista de escopos do seu aplicativo e, em seguida, criar e
gerenciar as travas por meio da API do Google Sheets. Aqui está um exemplo básico de como usar a trava de intervalo para
bloquear uma célula específica enquanto ela está sendo modificada:
'''

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define o escopo, desta forma tem permição total
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# ID da planilha
planilha_id = '1cEeMrBRVLnw7qtjiA63dK5q_HNvmJaCC5kNudzDjLgM'
# Nome da qui e regiao que sera editada
SAMPLE_RANGE_NAME = 'R1!A2:H'

creds = Credentials.from_authorized_user_file('token.json', SCOPES)

def bloquear_intervalo(planilha_id, inicio_linha, fim_linha, inicio_coluna, fim_coluna, creds):
    try:
        servico = build('sheets', 'v4', credentials=creds)

        # Cria a trava para o intervalo especificado
        requisicao = {
            'addRange': {
                'range': {
                    'sheetId': planilha_id, # ID da planilha
                    'startRowIndex': inicio_linha, # Linha inicial
                    'endRowIndex': fim_linha, # Linha final
                    'startColumnIndex': inicio_coluna, # Coluna inicial
                    'endColumnIndex': fim_coluna # Coluna final
                },
                'lockType': 'EDITING', # Tipo de trava
                'requestingUserCanEdit': False # Define se o usuário atual pode editar a trava
            }
        }
        resposta = servico.spreadsheets().batchUpdate(
            spreadsheetId=planilha_id,
            body={'requests': [requisicao]}).execute()
        print(f'A trava foi criada com sucesso. ID da trava: {resposta["replies"][0]["addRange"]["rangeId"]}')

    except HttpError as erro:
        print(f'Ocorreu um erro ao criar a trava: {erro}')

def desbloquear_intervalo(id_trava):
    try:
        servico = build('sheets', 'v4', credentials=creds)

        # Remove a trava com o ID especificado
        requisicao = {
            'deleteRange': {
                'range': {
                    'sheetId': 0, # ID da planilha
                    'rangeId': id_trava # ID da trava
                }
            }
        }
        resposta = servico.spreadsheets().batchUpdate(
            spreadsheetId=planilha_id,
            body={'requests': [requisicao]}).execute()
        print(f'A trava foi removida com sucesso.')

    except HttpError as erro:
        print(f'Ocorreu um erro ao remover a trava: {erro}')

def verificar_celula_protegida(id_planilha, nome_planilha, intervalo_celula, credenciais):
    service = build('sheets', 'v4', credentials=creds)

    # Obtém as informações de proteção da planilha
    planilha = service.spreadsheets()
    resposta = planilha.get(spreadsheetId=id_planilha).execute()
    planilhas = resposta.get('sheets', [])
    id_planilha_especifica = None
    for p in planilhas:
        if p['properties']['title'] == nome_planilha:
            id_planilha_especifica = p['properties']['sheetId']
            break
    if id_planilha_especifica is None:
        raise Exception(f"Planilha {nome_planilha} não encontrada")
    intervalos_protegidos = []
    for r in resposta['sheets'][0]['protectedRanges']:
        if r['sheetId'] == id_planilha_especifica:
            intervalos_protegidos += r['range']['ranges']

    # Verifica se a célula especificada está protegida
    for r in intervalos_protegidos:
        if r == intervalo_celula:
            return True
    return False



bloquear_intervalo(planilha_id, 1, 3, 1, 3, creds)



'''
Esse código recebe como parâmetros o ID da planilha, o nome da planilha, o intervalo de células e as credenciais do 
usuário autenticado. Ele retorna `True` se a célula estiver protegida e `False` se a célula não estiver protegida.'''

'''Para testar se uma célula está travada ou protegida, você pode utilizar a API Sheets do Google para verificar as 
permissões da planilha e da célula específica. Se a célula estiver protegida, as permissões de edição serão restritas.
Você pode usar o método `get` da API `spreadsheets().get()` para obter as informações da proteção da planilha, que 
incluem as permissões e as células protegidas. Em seguida, você pode verificar se a célula que deseja editar está 
protegida e se a permissão de edição foi concedida. Aqui está um exemplo de código Python que verifica se uma célula 
específica está protegida ou não:'''


