print('Programa que verifica se o usuário nasceu em uma cidade que comece com "Santo".')

cidade = str(input('Digite a cidade que você nasceu: ')).strip()
print(cidade[:5].upper() == 'SANTO')