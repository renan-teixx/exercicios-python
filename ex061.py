print('Programa que calcula os 10 primeiros termos de uma PA usando while')

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM.')