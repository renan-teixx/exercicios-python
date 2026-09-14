nome = input('Digite o seu nome: ')

# Essa é uma das formas de fazer, usando o '{}' e '.format'
print('É um prazer te conhecer {}! (saída com .format)' .format(nome))

# Também é possível fazer de uma maneira mais simples, usando 'f' antes do texto e colocando as chaves para adicionar a variável 'nome':
print(f'É um prazer te conhecer {nome}! (saída com f e chaves)')
    