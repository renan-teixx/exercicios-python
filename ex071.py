print('Programa que calcula a quantidade de cédulas fornecidas ao usuário para um saque em dinheiro.')
# considere que o caixo possui somente cédulas de R$50, R$20, R$10 e R$1

print('=' * 30)
print('{:^30}'.format('BANCO'))
print('=' * 30)

valor = int(input('Digite o valor que você quer sacar (apenas valores inteiros) R$'))
total = valor

cedula = 50
totalCedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break