def credencial():
    #IP.tem_internet()
    """Mostra o uso básico da Sheets API.
    Imprime valores de uma planilha de amostra.
    """
    creds = None
    # O arquivo token.json armazena os tokens de acesso e atualização do usuário
    # e é criado automaticamente quando o fluxo de autorização é concluído pela
    # primeira vez.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # Se não houver credenciais (válidas) disponíveis, deixe o usuário efetuar login.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials0.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Salve as credenciais para a próxima execução
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    # print(creds)
    # salvar_credenciais(creds)
    return creds