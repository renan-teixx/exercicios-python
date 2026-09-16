print('Programa que realiza a conversão de medidas a partir de um valor em metros.')

medida = float(input('Digite a medida em metros: '))

mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000

print(f'{medida}m correspondem a:\n{mm:.0f}mm (milímetros)\n{cm:.0f}cm (centímetros)\n{dm:.0f}dm (decímetros)\n{dam}dam (decâmetros)\n{hm}hm (hectômetros)\n{km}km (quilômetros)')