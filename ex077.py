print('Programa que verifica quais vogais estão presentes em diversas palavras armazenadas em uma tupla.\n')

palavras = ('programador', 'programacao', 'python', 'tuplas',
            'tecnologia', 'computador', 'logica', 'algoritmo',
            'estudar', 'aprender', 'linguagem', 'desenvolvedor')

print('-' * 50)
print(f'{"Verificação de vogais:":^50}')
print('-' * 50)

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')