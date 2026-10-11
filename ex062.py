print('Programa que calcula quantos termos de uma PA o usuario quiser, usando while')

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Digite quantos termos a mais você gostaria de ver (Digite 0 para encerrar o programa): '))
print(f'Progressão finalizada com {total} termos mostrados.')
    