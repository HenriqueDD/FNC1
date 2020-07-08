import requests
from datetime import date, timedelta
nome = input(str('Nome Completo: '))
CPF = input(str('Insira seu CPF:'))
data_coleta = date.today()
data = data_coleta.strftime("%d/%m/%Y")
prazo = timedelta(days=5)
data_entrega = data_coleta + prazo
print (f' Sua ficha de cadastro está completa! Abaixo segue seus dados e informações do exame: Nome: {nome} CPF: {CPF} Retirada Exame: {data_entrega.strftime("%d/%m/%Y")}')

if len(CPF) != 11:
    print('Quantidade de numeros invalida')
    exit()

    
