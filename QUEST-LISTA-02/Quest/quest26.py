km = float(input('Digite quantos km foram percorrido: '))
litro = float(input('Digite quantos litros fomra feito por km: '))

consumo = km / litro 

if(consumo < 8 ):
    print('Venda o carro')

if(consumo >= 8):
    if( consumo < 14):
        print('Econômico')

if(consumo > 12):
    print('Super econômico')