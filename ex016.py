# import math (importação da geral)
from math import trunc # (importação específica do método truncate)
print('Programa que mostra a parte inteira de um número digitado com casas decimais.')

numero = float(input('Digite um número com casas decimais: '))
print(f'O valor digitado foi {numero} e a sua porção inteira é {trunc(numero)}')
# O método 'trunc' ou 'truncate' tem a funcionalidade de retirar as casas decimais de um número float. Podemos usá-lo ao importar a biblioteca math. É possível importar a biblioteca inteira e usar somente o método, escrevendo: math.trunc(variável), ou importar de maneira mais específica, e usar somente o trunc(variavel) na apresentação.