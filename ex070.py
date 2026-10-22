print('Programa que mostra informações sobre os produtos registrados.')

contProduto = 0
somaTotal = 0
maiorMil = 0

while True:
    nome = str(input(f'\nDigite o nome do produto: '))
    preco = float(input(f'Digite o preço do produto: '))
    contProduto += 1
    somaTotal += preco
    if contProduto == 1 or preco < precoMaisBarato:
        nomeMaisBarato = nome
        precoMaisBarato = preco

    if preco > 1000:
        maiorMil += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('\nVocê deseja registrar mais produtos? [S/N]: ')).strip().upper()[0]

    if resposta == 'N':
        break

print('\n{:-^40}'.format('FIM DO PROGRAMA'))
print(f'\nQuantidade de produtos comprados: {contProduto}')
print(f'O valor total da compra foi de: R${somaTotal:.2f}')
print(f'Quantidade de produtos com valor superior a R$1000,00: {maiorMil}')
print(f'O produto mais barato foi {nomeMaisBarato}, custando R${precoMaisBarato:.2f}')