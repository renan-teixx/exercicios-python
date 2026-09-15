print('Esse programa lê o que foi digitado e utiliza métodos para mostrar suas características.')

conteudo = input('Digite algo: ')

# Nesse caso, 'conteudo' é o nosso objeto, e todo objeto possui características e realiza funcionalidades, ou seja, possuem atributos e métodos.

# A função 'input' sempre retorna uma String por padrão
print('O tipo primitivo desse valor é: ', type(conteudo))

# A função 'isspace()' verifica se o conteúdo digitado só possui espaços
print('Só tem espaços? ', conteudo.isspace())

# A função 'isnumeric()' verifica se o conteúdo digitado é numérico (somente números)
print('É um número? ', conteudo.isnumeric())

# A função 'isalpha()' verifica se o conteúdo digitado é alfabético (somente letras)
print('É alfabético? ', conteudo.isalpha())

# A função 'isalnum()' verifica se o conteúdo digitado é alfanumérico (possui letras ou números) 
print('É alfanumérico? ', conteudo.isalnum())

# A função 'isupper()' verifica se o conteúdo digitado só possui caracteres maiúsculos
print('Está totalmente em maiúsculas? ', conteudo.isupper())

# A função 'islower()' verifica se o conteúdo digitado só possui carateres minúsculos
print('Está totalmente em minúsculas? ', conteudo.islower())

# A função 'istitle()' verifica se o conteúdo digitado está capitalizado (possui maiúsculas e minúsculas)
print('Está capitalizada? ', conteudo.istitle())
