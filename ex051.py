print('Programa que mostra os 10 primeiros termos de uma progressão aritimética.')

primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimoTermo = primeiroTermo + (10 - 1) * razao

for contadora in range(primeiroTermo, decimoTermo + razao, razao):
    print(contadora, end=' ')
    