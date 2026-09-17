print('Programa de conversão de moedas.')

real = float(input('Digite quantos reais você tem para realizarmos a conversão: '))

dolar = real / 5.14
euro = real / 5.88

print(f'Com R${real} você poderá comprar: \nUS${dolar:.2f}\n€{euro:.2f}')