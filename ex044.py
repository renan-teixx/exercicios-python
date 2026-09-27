print('Programa que calcula o valor a ser pago por produtos em uma loja.')

print('\n{:=^40}'.format(' LOJA DE PRODUTOS '))

preco = float(input('Digite o preço das compras: R$'))

print('''\nFORMAS DE PAGAMENTO: 
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('\nDigite a opção escolhida:'))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalParcelas = int(input('Digite a quantidade de parcelas: '))
    parcela = total / totalParcelas
    print(f'Sua compra será parcelada em {totalParcelas}x de R${parcela:.2f} COM JUROS')
else:
    total = 0
    print('Opção inválida de pagamento.')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
    