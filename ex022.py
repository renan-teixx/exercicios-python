print('Programa que mostra diversas informações sobre o nome digitado.')

nome = str(input('Digite o seu nome completo: '))

print(f'\nO seu nome em letras maiúsculas é {nome.upper()}')
print(f'O seu nome em letras minúsculas é {nome.lower()}')

# O len() serve para contar a quantidade de caracteres, o - nome.count() é para que o len não conte os espaços em branco entre os nomes
print(f'O seu nome tem ao todo {len(nome) - nome.count(' ')} letras')

# Essa é uma das formas de apresentar apenas o primeiro nome digitado, usando o find(' ')
# print(f'O seu primeiro nome tem {nome.find(' ')} letras')

# O split() joga os nomes inteiros dentro de uma lista, isso nos permite escolher apenas o primeiro elemento dessa lista e apresentar para o usuário
separa = nome.split()

print(f'O seu primeiro nome é "{separa[0]}", e ele possui {len(separa[0])} letras')