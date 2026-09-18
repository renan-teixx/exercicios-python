# import math
print('Programa que calcula a hipotenusa de um triângulo.')

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

hi = (co ** 2 + ca ** 2) ** (1/2)
# Também é possível fazer esse exercicio importando a classe math e usando o seguinte método: 
# hi = math.hypot(co, ca)

print(f'A hipotenusa é: {hi:.2f}')