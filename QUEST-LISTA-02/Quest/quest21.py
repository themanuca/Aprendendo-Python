menu = int(input('Escolha a opção: \n'
'1 - Soma de 2 números.\n'
'2 - Diferença entre 2 números.(Maior para o menor)\n'
'3 - Produto entre 2 números.\n'
'4 - Divisão entre 2 números (O Denominador não pode ser zero \n'
'  : '))

if (menu == 1):
    valor1 = int(input('Digite o valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    soma = valor1 + valor2

    print('O valor da soma é', soma)


if (menu == 2):
    valor1 = int(input('Digite o valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    if (valor1 > valor2):
        soma = valor1 - valor2
        print('A diferença é de: ', soma)
    
    if(valor2 > valor1):
        dif = valor2 - valor1
        print('A diferença é de: ', dif)

if(menu == 3):
    valor1 = int(input('Digite o valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    prod = valor1 * valor2
    print('O produto entre os dois números é de', prod)

if(menu == 4):
    valor1 = int(input('Digite o valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    if(valor1 > valor2):
        div = valor1 / valor2
        print('O resultado da divisão é', div)
    if(valor2 > valor1):
        div = valor2 / valor1
        print('O resuladto da divisão é', div)