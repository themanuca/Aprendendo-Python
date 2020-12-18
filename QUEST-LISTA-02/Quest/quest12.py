import math

logaritmando = int(input('Digite um numero: '))

if (logaritmando < 0):
    print('Número invalido')

if (logaritmando > 0):
    base = 10
    x = math.log10(logaritmando)
    x1 = math.log2(logaritmando)

print('O valor de X com base 10 é', x, 'e com base 2 é', x1)



    