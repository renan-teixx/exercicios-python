print('Programa que calcula o total a pagar em um aluguel de carros, sabendo que o valor por dia é de R$60,00 e o valor por Km é de R$0,15.')

dias = int(input('Digite quantos dias alugados: '))
km = float(input('Digite quantos km foram rodados: '))

total = (dias * 60) + (km * 0.15)

print(f'O valor total a ser pago é de R${total:.2f}')