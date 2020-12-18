import math

a = float(input('Valor A: '))
b = float(input('Valor B: '))
c = float(input('Valor C: '))

delta = b**2 - 4*a*c
raiz = math.sqrt(delta)

x1 = -b + raiz / 2*a
x2 = -b - raiz / 2*a

if (delta > 0):
    raiz = math.sqrt(delta)
    x1 = -b + raiz / 2*a
    x2 = -b - raiz / 2*a
    
    print(x1, x2)

if (a == 0):
    print('Não é equação de segundo grau')

if (delta < 0):
    print('Não existe raiz')

if ( delta == 0):
    print('Valor da raiz é ', x1)
    print('Raiz única ')
