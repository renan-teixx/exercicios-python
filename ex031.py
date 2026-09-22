print('Programa que calcula o preço de uma viagem. Serão cobrados R$0,50 por km para viagens de até 200Km e R$0,45 por km para viagens mais longas')

distanciaViagem = float(input('Digite a distância em Km da viagem: '))

if distanciaViagem <= 200:
    valorViagem = distanciaViagem * 0.50
else:
    valorViagem = distanciaViagem * 0.45 

print(f'O valor da viagem é de R${valorViagem:.2f}')
    