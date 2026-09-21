print('Programa que verifica se a pessoa possui o sobrenome "Silva".')

nome = str(input('Digite o seu nome completo: ')).strip()
print(f'Seu nome tem Silva? {'silva' in nome.lower()}')
# Observação: o 'in' não é um método, é um operador do Python