ano = int(input('Digite o ano: '))

bi = ano % 4
norm = ano % 100

if (bi == 0 and norm > 0):
    print('O ano é bissexto')

else:
    print('Ano não bissexto')