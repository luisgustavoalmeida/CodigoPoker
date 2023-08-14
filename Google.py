# deve se instlar a biblioteca
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

from __future__ import print_function

import os
import os.path
import pickle
import socket
#import httplib2
from httplib2 import ServerNotFoundError
from google.auth.exceptions import TransportError
import re
import time
import datetime
import IP

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Define o escopo, desta forma tem permição total a plania e ao google drive
SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] # permite que a aplicação tenha acesso de leitura e escrita a planilhas do Google Sheets.

# ID da planilha
planilha_id = '1cEeMrBRVLnw7qtjiA63dK5q_HNvmJaCC5kNudzDjLgM'


# Obter o nome do computador
nome_computador = socket.gethostname()
# Obter o nome de usuário
nome_usuario = os.getlogin()
# nome do computador e do usuario
nome_completo = socket.gethostname() + "_" + os.getlogin()

# cada computador tem uma conta gmail
# crendencial 0 : lga.gustavo.a@gmail.com senha: LGlg32379089@
# crendencial 1 : gayaluisaalmeida@gmail.com senha: Lg1405lG
# crendencial 2 : luis.gustavo@engenharia.ufjf.br senha: LGlg32379089@#
#cria um dicionario para separar as credenciais, ou seja uma credencial APi para cada computador


dicionari_token_credencial_n = {'PC-I5-8600K_PokerIP':  ("token1.json", "credentials0.json", 1),
                                'PC-I5-8600K_lgagu':    ("token2.json", "credentials0.json", 2),
                                'PC-I5-8600K_Poker':    ("token3.json", "credentials0.json", 3),

                                'PC-I5-9400A_PokerIP':  ("token4.json", "credentials1.json", 4),
                                'PC-I5-9400A_lgagu':    ("token5.json", "credentials1.json", 5),
                                'PC-I5-9400A_Poker':    ("token6.json", "credentials1.json", 6),

                                'PC-I5-9400B_PokerIP':  ("token7.json", "credentials2.json", 7),
                                'PC-I5-9400B_lgagu':    ("token8.json", "credentials2.json", 8),
                                'PC-I5-9400B_Poker':    ("token9.json", "credentials2.json", 9),

                                'PC-I5-9400C_PokerIP':  ("token10.json", "credentials3.json", 10),
                                'PC-I5-9400C_lgagu':    ("token11.json", "credentials3.json", 11),
                                'PC-I5-9400C_Poker':    ("token12.json", "credentials3.json", 12),

                                'PC-R5-7600A_PokerIP':  ("token13.json", "credentials4.json", 13),
                                'PC-R5-7600A_lgagu':    ("token14.json", "credentials4.json", 14),
                                'PC-R5-7600A_Poker':    ("token15.json", "credentials4.json", 15),

                                'PC-I5-13400A_PokerIP': ("token16.json", "credentials0.json", 16),
                                'PC-I5-13400A_lgagu':   ("token17.json", "credentials0.json", 17),
                                'PC-I5-13400A_Poker':   ("token18.json", "credentials0.json", 18),

                                'PC-i3-8145U_PokerIP':  ("token19.json", "credentials5.json", 19),

                                'PC-I7-9700KF_PokerIP': ("token22.json", "credentials5.json", 22),
                                'PC-I7-9700KF_lgagu':   ("token23.json", "credentials5.json", 23),
                                'PC-I7-9700KF_Poker':   ("token24.json", "credentials5.json", 24),

                                'PC-I7-11850H_PokerIP': ("token25.json", "credentials5.json", 25),
                                'PC-I7-11850H_lgagu': ("token26.json", "credentials5.json", 26),
                                'PC-I7-11850H_Poker': ("token27.json", "credentials5.json", 27)
                                }


# dicionari_PC_usuario = {'PC-I5-8600K_PokerIP': 1, 'PC-I5-8600K_lgagu': 2, 'PC-I5-8600K_Poker': 3,
#                         'PC-I5-9400A_PokerIP': 4, 'PC-I5-9400A_lgagu': 5, 'PC-I5-9400A_Poker': 6,
#                         'PC-I5-9400B_PokerIP': 7, 'PC-I5-9400B_lgagu': 8, 'PC-I5-9400B_Poker': 9,
#                         'PC-I5-9400C_PokerIP': 10, 'PC-I5-9400C_lgagu': 11, 'PC-I5-9400C_Poker': 12,
#                         'PC-R5-7600A_PokerIP': 13, 'PC-R5-7600A_lgagu': 14, 'PC-R5-7600A_Poker': 15,
#                         'PC-I7-11850H_PokerIP': 16, 'PC-I7-11850H_lgagu': 17, 'PC-I7-11850H_Poker': 18,
#                         'PC-i3-8145U_PokerIP': 19,
#                         'PC-I7-9700KF_PokerIP': 22, 'PC-I7-9700KF_lgagu': 23, 'PC-I7-9700KF_Poker': 24}

dicionari_PC_IP = {'PC-I5-8600K': "IP!F3",
                   'PC-I5-9400A': "IP!F6",
                   'PC-I5-9400B': "IP!F9",
                   'PC-I5-9400C': "IP!F12",
                   'PC-R5-7600A': "IP!F15",
                   'PC-I5-13400A': "IP!F18",
                   'PC-i3-8145U': "IP!F21",
                   'PC-I7-9700KF': "IP!F24",
                   'PC-I7-11850H': "IP!F27"}



valor_dicionario = dicionari_token_credencial_n[nome_completo]
valor_pc = valor_dicionario[2] # numero do computador
token = valor_dicionario[0]  # pega o primeiro item da tupla
credentials = valor_dicionario[1]  # pega o segundo item da tuplas


def credencial():
    #IP.tem_internet()
    """Mostra o uso básico da Sheets API.
    Imprime valores de uma planilha de amostra.
    """

    # valor_dicionario = dicionari_token_credencial_n[nome_completo]
    # token = valor_dicionario[0]  # pega o primeiro item da tupla
    # credentials = valor_dicionario[1]  # pega o segundo item da tuplas
    # return token, credentials
    creds = None
    #token, credentials = token_credential()

    # O arquivo token.json armazena os tokens de acesso e atualização do usuário
    # e é criado automaticamente quando o fluxo de autorização é concluído pela
    # primeira vez.
    if os.path.exists(token):
        creds = Credentials.from_authorized_user_file(token, SCOPES)

    # Se não houver credenciais (válidas) disponíveis, deixe o usuário efetuar login.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials, SCOPES)
            creds = flow.run_local_server(port=0)
        # Salve as credenciais para a próxima execução
        with open(token, 'w') as token_nome:
            token_nome.write(creds.to_json())

    return creds

cred = credencial()
service = build('sheets', 'v4', credentials=cred)

def primeira_celula_vazia3(guia):

    print('primeira celula vazia')
    global cred
    global service
    regiao = f"{guia}!D:D"  # 'R1!D:D'
    # Chame a API Sheets
    sheet = service.spreadsheets()
    while True:
        try:
            result = sheet.values().get(
                spreadsheetId=planilha_id,
                range=regiao,
                majorDimension="COLUMNS",
                valueRenderOption="UNFORMATTED_VALUE"
            ).execute()
            values = result.get('values', [[]])[0]

            try:
                i = values.index("")
                return f"D{i+1}"
            except ValueError:
                i = len(values)
                return f"D{i+1}"
        except:
            print(f"Ocorreu um erro ao obter o valor da célula:")
            print("Erro primeira_celula_vazia. Tentando novamente em 5 segundos...")
            time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


linha_vazia_anterior = 2  # Inicializa a variável global
intervalo_de_busca = 500
guia_antiga = None

def primeira_celula_vazia(guia):
    global linha_vazia_anterior  # Indica que vamos utilizar a variável global
    global intervalo_de_busca
    global guia_antiga
    print('primeira celula vazia')
    global cred
    global service
    if guia_antiga != guia:
        guia_antiga = guia
        linha_vazia_anterior = 2

        # Chame a API Sheets
    sheet = service.spreadsheets()

    while True:
        print('linha vazia: ', linha_vazia_anterior)
        try:
            result = sheet.values().get(
                spreadsheetId=planilha_id,
                range=f"{guia}!D{linha_vazia_anterior}:D{linha_vazia_anterior + intervalo_de_busca}",
                majorDimension="COLUMNS",
                valueRenderOption="UNFORMATTED_VALUE"
            ).execute()
            values = result.get('values', [[]])[0]
            #print(values)

            # Montar uma lista com os 50 valores do intervalo
            try:
                i = values.index("")
                #print(i)
                linha_vazia_anterior += i  # Atualiza a variável global com a próxima linha vazia
                print('linha encontrada: ', linha_vazia_anterior)
                endereco = f"D{linha_vazia_anterior}"
                print(endereco)
                return f"D{linha_vazia_anterior}"

            except ValueError:
                i = len(values)
                #print(i)
                if i < intervalo_de_busca + 1:
                    linha_vazia_anterior += i  # Atualiza a variável global com a próxima linha vazia
                    print('linha encontrada: ', linha_vazia_anterior)
                    endereco = f"D{linha_vazia_anterior}"
                    print(endereco)
                    return f"D{linha_vazia_anterior}"

                else:
                    linha_vazia_anterior += intervalo_de_busca

        except Exception as e:
            print(f"Ocorreu um erro ao obter o valor da célula:", e)
            print("Erro primeira_celula_vazia. Tentando novamente em 5 segundos...")
            time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


def primeira_celula_vazia0(guia):
    global linha_vazia_anterior  # Indica que vamos utilizar a variável global
    global intervalo_de_busca
    global guia_antiga
    print('primeira celula vazia')
    global cred
    global service
    if guia_antiga != guia:
        guia_antiga = guia
        linha_vazia_anterior = 2

        # Chame a API Sheets
    sheet = service.spreadsheets()

    while True:
        print('linha vazia: ', linha_vazia_anterior)
        try:
            result = sheet.values().get(
                spreadsheetId=planilha_id,
                range=f"{guia}!D{linha_vazia_anterior}:D{linha_vazia_anterior + intervalo_de_busca}",
                majorDimension="COLUMNS",
                valueRenderOption="UNFORMATTED_VALUE"
            ).execute()
            values = result.get('values', [[]])[0]
            print(values)

            # Montar uma lista com os 50 valores do intervalo
            try:
                i = values.index("")
                print(i)

                if nome_usuario == "lgagu":
                    i += 1
                elif nome_usuario == "Poker":
                    i += 2

                linha_vazia_anterior += i  # Atualiza a variável global com a próxima linha vazia
                print('linha encontrada: ', linha_vazia_anterior)
                endereco = f"D{linha_vazia_anterior}"
                print(endereco)
                celula_vazia = celula_esta_vazia(guia, endereco)
                if celula_vazia:
                    return f"D{linha_vazia_anterior}"

            except ValueError:
                i = len(values)
                if i < intervalo_de_busca + 1:

                    if nome_usuario == "lgagu":
                        i += 1
                    elif nome_usuario == "Poker":
                        i += 2

                    linha_vazia_anterior += i  # Atualiza a variável global com a próxima linha vazia
                    print('linha encontrada: ', linha_vazia_anterior)
                    endereco = f"D{linha_vazia_anterior}"
                    print(endereco)
                    celula_vazia = celula_esta_vazia(guia, endereco)
                    if celula_vazia:
                        return f"D{linha_vazia_anterior}"

                else:
                    linha_vazia_anterior += intervalo_de_busca

        except Exception as e:
            print(f"Ocorreu um erro ao obter o valor da célula:", e)
            print("Erro primeira_celula_vazia. Tentando novamente em 5 segundos...")
            time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)



def escrever_celula(valor, guia, endereco):
    print("escrever_celula")
    global cred
    global service
    regiao = f"{guia}!{endereco}"  # 'R1!B150'
    while True:
        try:
            # Define o corpo da solicitação de atualização
            value_input_option = 'USER_ENTERED'
            values = [[valor]]
            data = {'values': values}
            result = service.spreadsheets().values().update(
                spreadsheetId=planilha_id,
                range=regiao,
                valueInputOption=value_input_option,
                body=data).execute()
            break
            #print('{0} células atualizadas.'.format(result.get('updatedCells')))
        #except (socket.gaierror, TransportError, ServerNotFoundError) as error:
        except:
            print(f"Ocorreu um erro ao obter o valor da célula:")
            print("Erro escrever_celula. Tentando novamente em 5 segundos...")
            #time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)

def escrever_valores(valores, guia, endereco):
    #recebe uma lista de valores como argumento valores. Essa lista será usada para preencher três células adjacentes.
    #Os valores serão escritos nas células adjacentes começando pela célula especificada em endereco.

    global cred
    global service
    regiao = f"{guia}!{endereco}"  # 'R1!B150'
    while True:
        try:
            # Define o corpo da solicitação de atualização
            value_input_option = 'USER_ENTERED'
            values = [valores]  # Lista de valores a serem escritos nas células
            data = {'values': values}
            result = service.spreadsheets().values().update(
                spreadsheetId=planilha_id,
                range=regiao,
                valueInputOption=value_input_option,
                body=data).execute()
            break
            #print('{0} células atualizadas.'.format(result.get('updatedCells')))
        # except (socket.gaierror, TransportError, ServerNotFoundError) as error:
        except:
            print(f"Ocorreu um erro ao obter o valor da célula:")
            print("Erro escrever_valores. Tentando novamente em 5 segundos...")
            time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


def escrever_valores_lote(valores, guia, linha):
    global cred
    global service
    range_start = f"{guia}!E{linha}:H{linha}"
    data = {
        'range': range_start,
        'majorDimension': 'ROWS',
        'values': [valores]
    }

    while True:
        try:
            result = service.spreadsheets().values().batchUpdate(
                spreadsheetId=planilha_id,
                body={
                    'valueInputOption': 'USER_ENTERED',
                    'data': [data]
                }
            ).execute()
            break

        except:
            print(f"Ocorreu um erro ao escrever os valores:")
            print("Erro escrever_valores_lote. Tentando novamente em 3 segundos...")
            time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)

def reservar_linha(guia, endereco):
    print("reservar_linha")
    global linha_vazia_anterior

    values = None
    id = ""
    senha = ""
    linha = ""
    contagem_ip = ""
    #print(valor)
    if valor_pc is not None:

        escrever_celula(valor_pc, guia, endereco)
        linha = endereco[1:]
        #time.sleep(0.3)
        #values, id, senha, contagem_ip = lote_valor(guia, linha)
        time.sleep(1)
        values, id, senha, contagem_ip = lote_valor(guia, linha)
        try:
            values = int(values)
            if valor_pc == values:
                print("Não teve concorrencia pela celula")
                return True, id, senha, linha, contagem_ip  # Retorna o valor testado, id, senha e linha
            else:
                print("Pego por outro computador")
                linha_vazia_anterior += 40
                return False, id, senha, linha, contagem_ip
            #print("values :",values)
        except:
            linha_vazia_anterior += 40
            return False, id, senha, linha, contagem_ip

    else:
        print('A chave não existe no dicionário')

# def reservar_linha(guia, endereco):
#     print("reservar_linha")
#     global linha_vazia_anterior
#
#     values = None
#     id = ""
#     senha = ""
#     linha = ""
#     contagem_ip = ""
#     #print(valor)
#     if valor_pc is not None:
#
#         escrever_celula(valor_pc, guia, endereco)
#         linha = endereco[1:]
#         #time.sleep(0.3)
#         #values, id, senha, contagem_ip = lote_valor(guia, linha)
#
#         values = pega_valor(guia, endereco)
#         try:
#             values = int(values)
#             if valor_pc != values: # testa se no meio do tempo putro computador ja pegou o id
#                 print("Pego por outro computador", values)
#                 linha_vazia_anterior += 40
#                 return False, id, senha, linha, contagem_ip
#             time.sleep(1)
#             values, id, senha, contagem_ip = lote_valor(guia, linha)
#             try:
#                 values = int(values)
#                 if valor_pc == values:
#                     print("Não teve concorrencia pela celula")
#                     return True, id, senha, linha, contagem_ip  # Retorna o valor testado, id, senha e linha
#                 else:
#                     print("Pego por outro computador")
#                     linha_vazia_anterior += 40
#                     return False, id, senha, linha, contagem_ip
#                 #print("values :",values)
#             except:
#                 linha_vazia_anterior += 40
#                 return False, id, senha, linha, contagem_ip
#         except:
#             linha_vazia_anterior += 40
#             return False, id, senha, linha, contagem_ip
#     else:
#         print('A chave não existe no dicionário')

def lote_valor(guia, linha):

    global cred
    global service
    regiao1 = f"{guia}!B{linha}:D{linha}" # regiao com a informação id senha e numero computador
    #print(regiao1)
    regiao2 = f"{dicionari_PC_IP[nome_computador]}" # pega a contagem de ip
    #print(regiao2)
    regiao = [regiao1, regiao2]

    #print(regiao)

    while True:

        try:
            result = service.spreadsheets().values().batchGet(
                spreadsheetId=planilha_id,
                ranges=regiao
            ).execute()

            value_ranges = result.get('valueRanges', [])
            values = []

            for range_data in value_ranges:
                range_values = range_data.get('values', [])
                if range_values:
                    values.extend(range_values[0])

            print("Os valores são:", values)

            if len(values) >= 4:
                id = values[0]
                senha = values[1]
                valor = values[2]
                cont_IP = values[3]
                #print(cont_IP)
                return valor, id, senha, cont_IP

        except:
            print(f"Ocorreu um erro ao obter os valores:")
            print("Erro função lote_valor...")
            time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)

def pega_valor(guia, endereco):
    print('pega_valor')
    global cred
    global service
    regiao = f"{guia}!{endereco}"  # 'R1!B150'
    while True:
        try:
            # Faz a requisição para obter os valores da célula
            result = service.spreadsheets().values().get(
                spreadsheetId=planilha_id,
                range=regiao).execute()
            # Extrai o valor da célula e retorna
            values = result.get('values', [])
            print("o valor escrito na celula é :", values[0][0])
            return values[0][0]

        # except (socket.gaierror, TransportError, ServerNotFoundError) as error:
        except:
            print(f"Ocorreu um erro ao obter o valor da célula:")
            print("Erro pega_valor. Tentando novamente em 5 segundos...")
            time.sleep(5)
            IP.tem_internet()
            #return None
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)

def celula_esta_vazia(guia, endereco):
    print('celula_esta_vazia')
    global cred
    global service
    celula = f"{guia}!{endereco}"
    print(celula)

    try:
        result = service.spreadsheets().values().get(
            spreadsheetId=planilha_id,
            range=celula,
            valueRenderOption="UNFORMATTED_VALUE"
        ).execute()

        # Verifica se a lista de valores não está vazia antes de acessar o primeiro elemento
        values = result.get('values', [])
        print(values)
        if len(values) == 0:
            return True
        else:
            return False

    except Exception as e:
        print(f"Ocorreu um erro celula esta vasia:", e)
        return False


def zera_cont_IP(endereco):

    global cred
    global service

    cred = credencial()
    service = build('sheets', 'v4', credentials=cred)

    letra = endereco[0]  # obtém a primeira letra do endereço
    numero = int(endereco[1:])  # obtém o número do endereço
    endereco2 = letra + str(numero - 1)  # cria a variável com o endereço imediatamente inferior
    endereco1 = letra + str(numero - 2)  # cria a variável com o endereço duas posições abaixo
    regiao1 = f"IP!{endereco1}"  # 'R1!F1'
    regiao2 = f"IP!{endereco2}"  # 'R1!F2'
    while True:
        try:
            result = service.spreadsheets().values().get(
                spreadsheetId=planilha_id,
                range=regiao1).execute()
            values = result.get('values', [])
            if len(values) > 0:
                value = values[0][0]
                data = {'values': [[value]]}
                result = service.spreadsheets().values().update(
                    spreadsheetId=planilha_id,
                    range=regiao2,
                    valueInputOption='USER_ENTERED',
                    body=data).execute()
                print('{0} células atualizadas.'.format(result.get('updatedCells')))
                return
        # except (socket.gaierror, TransportError, ServerNotFoundError) as error:
        except:
            print(f"Ocorreu um erro ao obter o valor da célula:")
            #time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)

def pega_ID_senha(guia, endereco):
    global cred
    global service
    linha = re.sub("[^0-9]", "", endereco)# pega a linha
    regiao = f"{guia}!B{linha}:C{linha}"  # 'R1!B2:C2'
    while True:
        try:
            # Faz a requisição para obter os valores das células
            result = service.spreadsheets().values().get(
                spreadsheetId=planilha_id,
                range=regiao).execute()
            # Extrai os valores das células B2 e C2
            values = result.get('values', [])
            print("O ID e senhas são :",values)
            if len(values) == 1:
                id = values[0][0]
                senha = values[0][1]
                return id, senha, linha
        # except (socket.gaierror, TransportError, ServerNotFoundError) as error:
        except:
            print(f"Ocorreu um erro ao obter o valor da célula:")
            print("Erro pega_ID_senha. Tentando novamente em 5 segundos...")
            time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


def escrever_IP_banido():

    global cred
    global service
    ip, com_internet = IP.meu_ip()
    data_hora_atual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # nome_computador = socket.gethostname()
    # nome_usuario = os.getlogin()
    print('\n\n ip banido \n')
    print(ip)
    print('\n\n')

    while True:
        try:
            # Define o corpo da solicitação de pesquisa da célula vazia
            range_ = 'Ban!A:A'
            result = service.spreadsheets().values().get(
                spreadsheetId=planilha_id,
                range=range_).execute()
            values = result.get('values', [])

            # Encontra a primeira célula vazia na coluna A
            primeira_celula_vazia = len(values) + 1

            # Define o intervalo da célula a ser atualizada
            range_atualizar = f'Ban!A{primeira_celula_vazia}:D{primeira_celula_vazia}'

            # Define o corpo da solicitação de atualização
            value_input_option = 'USER_ENTERED'
            values = [[ip, data_hora_atual, nome_usuario, nome_computador]]  # valores que deseja adicionar
            data = {'values': values}
            result = service.spreadsheets().values().update(
                spreadsheetId=planilha_id,
                range=range_atualizar,
                valueInputOption=value_input_option,
                body=data).execute()

            # Exibe a quantidade de células atualizadas
            print('{0} células atualizadas.'.format(result.get('updatedCells')))
            break
        except Exception as error:
            print("Ocorreu um erro ao escrever na célula:")
            print(f"Erro: {str(error)}")
            print("Tentando novamente em 5 segundos...")
            time.sleep(5)
            IP.tem_internet()
            cred = credencial()
            service = build('sheets', 'v4', credentials=cred)


def credenciais(guia):
    print("credenciais")
    reservado = False

    while True:# pega a peimira celula vazia e pega as credenciais para entrar

        endereco = primeira_celula_vazia(guia)

        reservado, id, senha, linha, cont_IP = reservar_linha(guia, endereco)

        if reservado:
            try:
                cont_IP = int(cont_IP)
                return id, senha, linha, cont_IP
            except Exception as error:
                print(error)
                time.sleep(5)
                continue

        print('tentar credenciaias')


def marca_horario(guia, linha):
    endereco = f"G{linha}"
    hora_atual = datetime.datetime.now().strftime('%H:%M:%S')
    escrever_celula(hora_atual,guia,endereco)

def marca_banida(status, guia, linha):
    endereco = f"G{linha}"
    escrever_celula(status, guia, endereco)
    endereco = f"L{linha}"
    escrever_celula(status, guia, endereco)

def marca_caida(status, guia, linha):
    endereco = f"D{linha}"
    escrever_celula('x', guia, endereco)
    endereco = f"G{linha}"
    escrever_celula(status, guia, endereco)
    endereco = f"L{linha}"
    escrever_celula(status, guia, endereco)


def marca_ip(guia, linha):
    endereco = f"H{linha}"
    ip, com_internete = IP.tem_internet()
    escrever_celula(ip, guia, endereco)

def marca_ficha(guia, linha, valor_fichas):
    endereco = f"E{linha}"
    escrever_celula(valor_fichas, guia, endereco)

def marca_pontuacao(guia, linha, pontuacao_tarefas):
    endereco = f"F{linha}"
    escrever_celula(pontuacao_tarefas, guia, endereco)

def marca_informacoes(valores, guia, linha):
    endereco = f"E{linha}"
    escrever_valores(valores, guia, endereco)

def apagar_numerodo_pc(valores, guia, linha):
    endereco = f"D{linha}"
    escrever_valores(valores, guia, endereco)


#credencial()


# guia = "R1"
#
# credenciais(guia)
# linha = 3
# marca_horario(guia,linha)

#

#creds = credencial()
#escrever_celula("14", "R1", "G8") # conteudo, guia , endereço B150

#zera_cont_IP("F15")

#credenciais('R4')
#testa_valor("R4", 'D2')