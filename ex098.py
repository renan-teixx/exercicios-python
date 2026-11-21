from time import sleep

print('Programa que cria funções para realizar contagens.')

# i = índice, f = fim, p = passo
def contador(i, f, p):

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        print('Não é possível fazer a contagem com o passo 0, portanto, o valor 1 foi atribuído.')

    print('=' * 40)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 40)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
