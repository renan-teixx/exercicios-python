print('Programa que calcula o aumento no salário do funcionário. Salários menores ou iguais R$1.250,00 receberão 15% de aumento, e salários maiores 10%.')

salario = float(input('Digite o salário do funcionário R$'))

if salario <= 1250:
    novoSalario = salario + (salario * 15 / 100)
else:
    novoSalario = salario + (salario * 10 / 100)
print(f'O salário agora é de R${novoSalario:.2f}!')
