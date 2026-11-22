print('Programa que mostra o maior e menor valor usando função.')


def maiorMenorValores(listaNumeros):

    maiorValor = max(numeros)
    menorValor = min(numeros)

    print(f'O maior valor é: {maiorValor}\nO menor valor é: {menorValor}')


numeros = []

while True:
    numeros.append(int(input('Digite um número inteiro: ')))
    resposta = str(input('Quer digitar mais valores? [S/N]: '))
    if resposta in 'Nn':
        break

maiorMenorValores(numeros)
    