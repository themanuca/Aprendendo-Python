operacao = int(input('Escolha uma operação: \n'
'Adição - 1 \n'
'Subtração - 2 \n'
'Multiplicação - 3 \n'
'Divisão - 4 \n'))
print('=====================')

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

Adição = 1
Subtração = 2
Multiplicação = 3
Divisão = 4

if(operacao == Multiplicação):
    multi = valor1 * valor2
    print('Valor da multiplicação é', multi)

if(operacao == Subtração):
    sub = valor1 - valor2
    print('Valo da subtração é ', sub)
if(operacao == Divisão):
    div = valor1 / valor2
    print('Valor da divisão é', div)

if(operacao == Adição):
    adi = valor1 + valor2
    print('Valor da adição é', adi)

