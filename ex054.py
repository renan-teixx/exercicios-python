from datetime import date

print('Programa que mostra maioridade de pessoas cadastradas.')

atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}º pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print(f'Ao todo tivemos {totmaior} pessoas maiores de idade.')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade.')