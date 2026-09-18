print('Programa que mostra o valor do produto digitado com 5% de desconto.')

valorProduto = float(input('Digite o valor do produto: R$'))

valorProdutoFinal = valorProduto - (valorProduto * 0.05)

print(f'Valor original do produto: R${valorProduto}\nValor com 5% de desconto: R${valorProdutoFinal:.2f}')
