print('Programa que separa os digitos de um número digitado.')

numero = int(input('Informe um número inteiro: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'\nUnidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')