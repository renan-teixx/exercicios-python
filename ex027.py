print('Programa que mostra o primeiro e o último nome digitados pelo usuário.')

nome = str(input('Digite o seu nome completo: ')).strip()

# Observação: como já vimos anteriormente, o split() separa a string em pedaços e os coloca em uma lista, a partir dos espaços vazios entre os caracteres digitados na sring
nomeDividido = nome.split()

print(f'O seu primeiro nome é: {nomeDividido[0]}')
print(f'O seu último nome é: {nomeDividido[len(nomeDividido) - 1]}')
    