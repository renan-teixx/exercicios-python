from random import randint

print('Programa que joga JOKENPO com o usuário.')

usuario = int(input('''\nObserve as opções:\n 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
\nDigite o número correspondente ao que você quer jogar: '''))

computador = randint(0, 2)

print(f'\nResposta do usuário: {usuario}')
print(f'Resposta do computador: {computador}\n')

if usuario < 0 or usuario > 2:
    print('Você digitou uma resposta inválida, portanto, não há resultado.')
elif usuario == computador:
    print('EMPATE!')
elif (usuario == 0 and computador == 1) or (usuario == 1 and computador == 2) or (usuario == 2 and computador == 0):
    print('VOCÊ PERDEU!')
else:
    print('VOCÊ GANHOU!')