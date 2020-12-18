import math
x = int(input('Digite o valor de X: '))
y = int(input('Digite o valor de Y: '))
z = int(input('Digite o valor de z: '))

raiz = x * y * z
dendo = 2
div = 0
while div ==0:
    div = raiz & dendo
    dendo +=1
    if div != 0:


        print('==========')
        print(raiz, 'Geométrica')
        print('==========')

ponderada = x + 2*y + 3*z / 6

print('==========')
print(ponderada, 'Ponderada')
print('==========')

aritmetica = x + y + z / 3

print('==========')
print(aritmetica, 'Aritme')
print('==========')

harmonica = 1/ 1/x + 1/y + 1/z

print(harmonica)









