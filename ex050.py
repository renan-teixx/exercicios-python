print('Programa que mostra a soma apenas de números pares digitados.')

cont = 0
soma = 0

for cont in range(1,7):
    numero = int(input(f'Digite o {cont}º número: '))
    if numero % 2 == 0:
        soma += numero
print(f'\nVocê informou {cont} números. A soma dos números pares é: {soma}')
