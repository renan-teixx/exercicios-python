print('Programa que mostra se o número é primo e a quantidade de divisões entre um e ele mesmo.')

numero = int(input('Digite um número: '))
total = 0

for contador in range(1, numero + 1):
    if numero % contador == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(contador, end=' ')

print(f'\n\033[mO número {numero} foi divisível {total} vezes.')

if total == 2:
    print('Portanto, ele É PRIMO!')
else:
    print('Portanto, ele NÃO É PRIMO!')
