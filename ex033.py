print('Programa que mostra o maior e o menor número entre 3 digitados.')

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

# Verificando o menor valor
menorValor = a
if b < a and b < c:
    menorValor = b
if c < a and c < b:
    menorValor = c

# Verificando o maior valor
maiorValor = a
if b > a and b > c:
    maiorValor = b
if c > a and c > b:
    maiorValor = c

print(f'\nO menor valor digitado foi: {menorValor}')
print(f'O maior valor digitado foi: {maiorValor}')
