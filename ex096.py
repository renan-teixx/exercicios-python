print('Programa que calcula a área de um terreno usando função')

def area(l, c):
    a = l * c
    print(f'A área de um terreno de {l}m x {c}m é de {a:.2f}m²')


largura = float(input('Digite a LARGURA (m): '))
comprimento = float(input('Digite o COMPRIMENTO (m): '))
area(largura, comprimento)
