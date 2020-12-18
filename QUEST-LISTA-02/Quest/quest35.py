from datetime import date
def calendario():
    print('DATA :')
    data = int(input('Digite o dia: '))
    mes = int(input('Digite o mês: '))
    ano = int(input('Digite o ano: '))

    
    biss = ano % 4
    anonãobiss = biss != 0 and mes == 2 and data > 28
    anobiss = biss != 0 and mes == 2 and data > 28 and data <=29
    
    if anonãobiss:
        print('Data não válida o ano {} não é bissesto'.format(ano))

    elif anobiss:
        print('Ano bissesto')

    else:
        if biss == 0:
            print('Ano bissesto')


if __name__ == "__main__":
    calendario()