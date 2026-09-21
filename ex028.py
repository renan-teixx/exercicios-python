from random import randint # Necessário para fazer a aleatoriedade do programa
from time import sleep # Necessário para adicionar o efeito de loading do computador, para dar a sensação de que o computador está processando a informação digitada

print('Programa que tenta advinhar o número que o usuário pensou.')

numeroComputador = randint(1, 5) # Faz ele aleatorizar um número entre 1 e 5

print('-=-' * 20)
print('\nVou pensar em um número entre 1 e 5. Tente advinhar qual é...\n')
print('-=-' * 20)

numeroJogador = int(input('Em qual número eu pensei? Digite aqui: '))

print('PROCESSANDO INFORMAÇÃO...')
sleep(2) # Faz a resposta final, contida nos if e else abaixo demorar 2 segundos para aparecer

if numeroJogador == numeroComputador:
    print(f'PARABÉNS, VOCÊ VENCEU! Eu também pensei no número {numeroComputador}!')
else:
    print(f'EU VENCI! Eu havia pensado no número {numeroComputador} e você pensou no número {numeroJogador}!')
