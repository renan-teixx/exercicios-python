print('Programa que organiza números digitados em listas específicas.')

lista = []
listaPar = []
listaImpar = []
n = 0

while True:
    lista.append(int(input('Digite um número: ')))
    if lista[n] % 2 == 0:
        listaPar.append(lista[n])
    else:
        listaImpar.append(lista[n])
    n += 1
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)

print(f'A lista completa é: {lista}')
print(f'A lista somente com números PARES é: {listaPar}')
print(f'A lista somente com número ÍMPARES é: {listaImpar}')
