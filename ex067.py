print('Programa que mostra a tabuada até um valor negativo ser digitado.')

while True:
    n = int(input('Para saber a tabuada, digite um número: '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('Programa encerrado.')