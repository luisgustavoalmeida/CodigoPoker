import Firebese
import time
dado = 0
while True:
    time.sleep(5)
    variavel = Firebese.obter_dado()
    if variavel != dado:
        dado = variavel
        Firebese.escrever_dado(dado)
    print('ta rodando')
    print(variavel)
    pass