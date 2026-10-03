print('Programa que verifica se uma frase digitada é palíndromo.')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

'''
Obersevação: Também é possível fazer esse exercício de maneira mais simples, sem usar o laço for. Da seguinte maneira:

inverso = junto [::-1]
(fazendo desse jeito, a linha 6 desse código se tornaria desnecessária, podendo ser apagada)
'''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
