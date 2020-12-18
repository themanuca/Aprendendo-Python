soma = 0
i = 0

while i != 10:
    num = float(input('Digite: '))
    if num > 0:
        soma += num
        i += 1
    else:
        print('Negativo não permitido')

media = soma / 10

print(media)





'''while i <= 10:
    num = float(input('Digite um valor '))
    if num > 0:  # positivos
        soma = soma + num
        i += 1
    else:
        print('valor negativo não é aceito. Tente novamente.')

media = soma / 10
print(f'A soma é {soma}')
print(f'A media é {media}')'''