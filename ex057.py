print('Programa que verfica se o sexo digitado é valido para o sistema proseeguir.')

sexo = str(input('Digte o seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor digite novamente o seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo ({sexo}) registrado com sucesso!')
    