print('Programa que mostra uma mensagem centralizada usando função.')

def escreva(msg):
    tamanho = len(msg) + 4
    print('=' * tamanho)
    print(f'  {msg}')
    print('=' * tamanho)


escreva('Eu amo programação!')
