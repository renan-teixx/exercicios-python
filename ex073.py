print('Programa que mostra iformações dos times da serie A (26/10/2026) do brasileirão usando tuplas.')

# Obervação* É importante lembrar que tuplas são IMUTÁVEIS, não sendo possível, portanto, alterar os valores armazenados nela depois da declaração inicial. É por isso que ela não seria ideal para mostrar informações de algo que muda constantemente, como a tabela do campeonato brasileiro, por exemplo. Estamos usando-a apenas para fins de estudos.

# Times organizados na ordem de pontos da tabela de hoje, dia 26 de Outubro de 2026
times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Athletico-PR',
         'Fluminense', 'Atlético-MG', 'Bahia', 'Santos',
         'São Paulo', 'Bragantino', 'Botafogo', 'Coritiba',
         'Vasco da Gama', 'EC Vitória', 'Mirassol', 'Internacional',
         'Corinthians', 'Grêmio', 'Remo', 'Chapecoense')

print('\nLista de times do Brasileirão:\n')
classificacao = 1
for t in times:
    print(f'{classificacao:>2}',' - ', t)
    classificacao += 1

print(f'\nOs primeiros 5 times são: {times[0:5]}')
print(f'\nOs times na zona de rebaixamento são: {times[-4:]}')
print(f'\nA lista dos times em ordem alfabética é: {sorted(times)}')
print(f'\nO CORINTHIANS está na {times.index("Corinthians") + 1}ª posição!')
    