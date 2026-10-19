print('Programa que mostra informações de pessoas cadastradas no sistema.')

pessoa = 0
maiorDezoito = 0
qtdHomens = 0
mulheresMenoresIdade = 0

while True:
    print('-' * 50)
    pessoa += 1
    print(f'Cadastro do {pessoa}º usuário.\n')
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maiorDezoito += 1
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

    if sexo == 'M':
        qtdHomens += 1
    if idade < 18 and sexo == 'F':
        mulheresMenoresIdade += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja registrar mais pessoas? Digite [S/N]: ')).strip().upper()[0]

    if resposta == 'N':
        break

print('\n')
print('~' * 50)
print(f'\nPROGRAMA ENCERRADO.\n\nINFORMAÇÕES:\n')
print(f'Quantidade de pessoas registradas no sistema: {pessoa}')
print(f'Pessoas com mais de 18 anos: {maiorDezoito}')
print(f'Quantidade de homens: {qtdHomens}')
print(f'Quantidade de mulheres menores de 18 anos: {mulheresMenoresIdade}')
    