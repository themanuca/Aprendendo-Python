a = float(input('Valor de lado A: '))
b = float(input('Valor de B: '))
c = float(input('Valor de C: '))


existi = b-c < a < b+c

if (existi == True):
    if(a==b and b==c):
        print('==============================')
        print('equilatero')
        print('==============================')

if(existi==True):
    if(a!=b and b!=c and a!=c):
        print('==============================')
        print('escaleno')
        print('==============================')

if(existi==True):
    if(a==b or b==c or c==a):
        print('==============================')
        print('Isóceles')
        print('==============================')

if(existi==False):
    print('==============================')
    print('Medidas não podem ser um triangulo')
    print('==============================')
