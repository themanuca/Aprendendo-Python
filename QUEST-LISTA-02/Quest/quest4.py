import math
valor = float(input('Digite um número: '))

if (valor > 0):
    raiz = math.sqrt(valor)
    quad = valor*valor
    print('Seu valor ao quadrado é', quad, 'e sua raiz é' ,raiz)
else:
    print('Valor digitado não é positivo')
