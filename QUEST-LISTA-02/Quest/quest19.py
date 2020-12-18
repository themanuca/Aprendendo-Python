num1 = int(input('Digite: '))

div3 = num1 % 3
div5 = num1 % 5
if (div3 == 0):
    print('Numero  divisivel por 3')


if (div5 == 0):
    print('Divisivel por 5')

else:
    print('Não divisivel por 3 nem por 5')