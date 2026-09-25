print('Programa que faz a conversão de base de um número inteiro decimal.')

numero = int(input('Digite um número inteiro para conversão: '))

print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('Opção inválida.')
    