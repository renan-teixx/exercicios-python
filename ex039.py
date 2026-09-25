from datetime import date

print('Programa que mostra informações sobre o alistamento militar.')

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Ainda faltam {saldo} ano(s) para o alistamento.\nEle será em {ano}.')
else:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você deveria ter se alistado há {saldo} anos.\nEle devia ter ocorrido em {ano}.')
    