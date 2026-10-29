from random import randint

print('Programa que gera 5 números, armazena em uma tupla e mostra o maior e o menor valor.')

numeros = (randint (1, 10), randint (1, 10), randint (1, 10), randint (1, 10), randint (1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')
    