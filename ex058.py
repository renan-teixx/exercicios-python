from random import randint

print('Programa que faz um jogo de adivinhação com o usuário usando while.')

computador = randint(0, 10)

print('Vou pensar em um número inteiro entre 0 e 10, tente adivinhar qual é.')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('\nDigite o seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('O número que pensei é maior do que esse... Tente novamente.\n')
        elif jogador > computador:
            print('O número que pensei é menor do que esse... Tente novamente.\n')
print(f'\nO número que eu havia pensado era {computador}.')
print(f'Você acertou na {palpites}ª tentativa, parabéns!')