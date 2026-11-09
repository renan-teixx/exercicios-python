print('Programa que adiciona apenas valores únicos em uma lista e a apresenta em ordem crescente.')

numeros = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado, portanto, não será adicionado na lista.')
    r = str(input('Digite "N" para encerrar o programa, ou qualquer outra tecla para continuar: '))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Veja os valores digitados e em ordem crescente: {numeros}')