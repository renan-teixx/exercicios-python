print("Programa que analisa dados em um tupla.")

num = (int(input('Digite um número: ')),
        int(input('Digite o segundo número: ')),
        int(input('Digite o terceiro número: ')),
        int(input('Digite o quarto número: ')))

print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu na {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')