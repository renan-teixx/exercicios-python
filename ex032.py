from datetime import date
print('Programa que mostra se o ano digitado é bissexto.')

ano = int(input('Digite o ano que você quer analisar, ou digite o número 0 para saber sobre o ano atual da sua máquina: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO É BISSEXTO!')
    