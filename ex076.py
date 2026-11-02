print('Programa que mostra uma listagem de preços de materiais escolares usando uma única tupla.')

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 119.99,
            'Canetas', 22.00,
            'Livro', 34.99,)

print('-' * 39)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 39)

for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end='')
    else:
        print(f'R${listagem[posicao]:>7.2f}')
print('-' * 39)
