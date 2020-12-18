salario = float(input('Digite seu salario: '))
prestacao = float(input('Digite o valor da prestação: '))

valor = salario * 20 / 100


if (prestacao > valor ):
    print('Emprestimo não concedido')
    print('Valor acima de ', valor)
else:
    print('Emprestimo aprovado')