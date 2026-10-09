'''
Também é possível resolver esse exercício importando o método factorial do math, e usando ele para calcular automaticamente direto da variavél, veja abaixo:

from math import factorial
factorial(variavel) 
'''

print('Programa que calcula o fatorial de um número.')

fatorial = int(input('Digite um número inteiro positivo para saber o fatorial: '))

while fatorial < 0:
    fatorial = int(input('Você deve digitar um número INTEIRO POSITIVO: '))

soma = 1 
cont = 1

while cont <= fatorial:
    soma = soma * cont
    cont += 1
print(f'{fatorial}! = {soma}')