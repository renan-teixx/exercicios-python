print('Programa que calcula a média do aluno e verifica se está aprovado, de recuperação ou reprovado.')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2
print(f'A sua média é de {media:.1f} pontos.')

if 7 > media >= 5: 
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO.')
else:
    print('O aluno está APROVADO.')
    