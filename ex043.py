print('Programa que calcula o IMC.')

peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal!')
elif 18.5 <= imc <= 25:
    print('Você está na faixa de peso IDEAL!')
elif 25 <= imc <= 30:
    print('Você está em SOBREPESO!')
elif 25 <= imc <= 30:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA!')
    