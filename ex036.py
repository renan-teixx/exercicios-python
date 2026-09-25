print('Programa que calcula se é possível realizar o empréstimo bancário, só sendo possível se a prestação mensal não exceder 30% do salário.')

valorCasa = float(input('Digite o valor da casa que deseja comprar R$'))
salario = float(input('Digite o seu salário R$'))
anosPagamento = int(input('Digite em quantos anos você irá pagar esse imóvel: '))
prestacao = valorCasa / (anosPagamento * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de R${valorCasa:.2f} em {anosPagamento} anos com R${salario} de salário, a prestação será de R${prestacao:.2f}')

if prestacao <= minimo:
    print('O empréstimo pode ser CONCEDIDO!')
else:
    print('O empréstimo está NEGADO!')
