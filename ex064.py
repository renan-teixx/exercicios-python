print('Programa que soma números até a condição de parada ser digitada.')

# No Python, é possível atribuir um mesmo valor a diferentes variáveis usando a seguinte estrutura:
num = cont = soma = 0

num = int(input('Digite um número [999 para parar a execução do programa]: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar a execução do programa]: '))

print(f'Você digitou {cont} números e a soma entre eles é: {soma}')