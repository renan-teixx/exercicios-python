print('Programa que calcula área de uma parede e quantidade de litros de tinta necessários para pintá-la.')
# Observação: 1l de tinta consegue pintar 2m² da parede.

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
litrosTinta = area / 2

print(f'A área da parede é de {area:.2f}m²\nSerão necessários {litrosTinta:.2f} litros de tinta para pintá-la')
