print('Programa que mostra a primeira e última ocorrência de uma string.')

frase = str(input('Digite uma frase: ')).upper().strip()
frase2 = frase.upper( ).replace('Á', 'A').replace('Ã', 'A').replace('Â', 'A').replace('À', 'A')

print(f'A letra "A" aparece {frase2.count('A')} vezes na frase')
print(f'A primeira letra "A" apareceu na posição {frase2.find('A') + 1}')
print(f'A última letra "A" apareceu na posição {frase2.rfind('A') + 1}')
