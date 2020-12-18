valor = float(input('O valor a ser negociado: '))
estado = int(input('Estado: \n'
'MG - 1 \n'
'SP - 2 \n'
'RJ - 3 \n'
'MS - 4 \n'
 ': '))

mg = valor * 7 / 100
sp = valor * 12 / 100
rj = valor * 15 / 100
ms = valor * 8 / 100


if (estado == 1):
    resultado = valor + mg
    print('O valor é', resultado)

if (estado == 2):
    resultado = valor + sp
    print('O valor é', resultado)

if (estado == 3):
    resultado = valor + rj
    print('O valor é', resultado)

if(estado == 4):
    resultado = valor + ms
    print('O valor é', resultado)

