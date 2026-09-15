print('Esse programa calcula o dobro, o triplo e a raíz quadrada de um número inteiro digitado.')

numero = int(input('Digite um número inteiro: '))

dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** (1/2)

print(f'O dobro de {numero} é = {dobro}')
print(f'O triplo de {numero} é = {triplo}')
print(f'A raíz quadrada de {numero} é = {raizQuadrada:.2f}')
    