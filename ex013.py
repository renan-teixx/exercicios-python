print('Programa que calcula o reajuste salarial de um funcionário (15% de aumento).')

salario = float(input('Digite o valor do salario: R$'))

salarioReajustado = salario + (salario * 0.15)

print(f'Salário do funcionário anteriormente: R${salario}\nSalário do funcionário após o aumento de 15%: R${salarioReajustado:.2f}')