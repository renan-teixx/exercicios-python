print('Programa que mostra a tabuada de um número usando laço de repetição "for".')

numero = int(input('Digite um número para saber a sua tabuada: '))
cont = 0
for cont in range(1, 11, 1):
    print(f'{numero} x {cont} = {numero*cont}')
    