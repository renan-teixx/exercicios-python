print('Programa que verifica o maior e o menor peso dentre 5 pessoas.\n')

maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso em Kg da {pessoa}ª pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'\nO maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
