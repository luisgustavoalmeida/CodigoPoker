import Firebase
import time
dado = 0
while True:
    time.sleep(5)
    variavel = Firebase.obter_dado()
    if variavel != dado:
        dado = variavel
        Firebase.escrever_dado(dado)
    print('ta rodando')
    print(variavel)
    pass