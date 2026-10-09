# O Sleep foi importado apenas para ter um efeito legal na saída
from time import sleep

print('Programa que cria um menu de opções para uma calculadora simples.')

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

opcao = 0

while opcao != 5:

    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Saber o maior valor
    [ 4 ] Mudar números digitados 
    [ 5 ] Sair do programa''')

    opcao = int(input('Digite a opção escolhida: '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é = {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é = {produto:.2f}')
    elif opcao == 3:
        if n1 >= n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior valor é: {maior}')
    elif opcao == 4:
        print('Você deverá informar os número novamente.')
        n1 = float(input('Digite novamente o primeiro valor: '))
        n2 = float(input('Digite novamente o segundo valor: '))
    elif opcao == 5:
        print('Finalizando o programa...')
        sleep(2)
        print('Programa finalizado.')
    else:
        print('Opção inválida, tente novamente.')
    print('=-=' * 10)
