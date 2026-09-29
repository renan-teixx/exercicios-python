print('Programa que mostra os números pares entre 0 e 50.')

for n in range(0, 51, 1):
    if n % 2 == 0:
        print(n,end=' ')

'''
A forma mais eficiente de fazer esse programa seria sem usar o cálculo com o % e apenas mostrar os números de 2 em 2, da seguinte forma: 

for n in range(2, 51, 2):
        print(n,end=' ')
'''
