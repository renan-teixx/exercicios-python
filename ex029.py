print('Programa que verifica a velocidade do veículo e aplica multa a partir de 80km/h, sendo R$7,00 por cada Km acima do limite')

velocidade = float(input('Digite a velocidade máxima que o veículo atingiu (Km/h): '))

if velocidade > 80:
    valorMulta = (velocidade - 80) * 7
    print(f'Você ultrapassou o limite de velocidade de 80km/h na via, sua multa é de R${valorMulta:.2f}')
else:
    print('Sua velocidade estava dentro do limite da via, boa viagem!')
    