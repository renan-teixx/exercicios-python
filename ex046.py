from time import sleep

print('Programa que faz contagem regressiva de 10 até 0.')

for contadora in range (10, -1, -1):
    print(contadora)
    sleep(0.5)
print('Fim da contagem regressiva!')
