

hora = (input('ENTRADA (h:m): '))
saida = (input('SAIDA (h:m): '))

horavetor = hora.split(':')
horasaida = saida.split(':')

diferenca = float(horasaida[0]) - float(horavetor[0])
diferencaminuto = float(horasaida[1]) - float(horavetor[1])


difhora = diferenca * 3600
difminuto = diferencaminuto * 60


print(difhora)
minuto_certo = difhora + difminuto

minuto_certo1 = minuto_certo / 60

print(minuto_certo1)

minuto_certo_dif = minuto_certo1 / 60



print(minuto_certo_dif)

if minuto_certo_dif <= 1:
    print('Valor a ser pago é de 1 real')

elif minuto_certo_dif > 1 and minuto_certo_dif <=2:
    print('Valor a ser pago é de 2 reais')

elif minuto_certo_dif > 2 and minuto_certo_dif <=3:
    print('Valor a ser pago é de 3,40')

elif minuto_certo_dif > 3 and minuto_certo_dif <=4:
    print('Valor a ser pago é de 4,80')

elif minuto_certo_dif > 4:

    valorjusto = minuto_certo_dif - 4 
    valorjusto1 = valorjusto * 2 + 4.80

    print('Valor a ser pago é de {}'.format(valorjusto1))
