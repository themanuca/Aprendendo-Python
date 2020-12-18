altura = float(input('Digite sua altura: '))
peso = float(input('Digite sua peso: '))

if ( altura <= 1.20 and peso <= 60):
    print('Sua classificação é A')

if(altura <= 1.20 and peso > 60 and peso <=90 ):
    print('Sua classificação é D')

if (altura <= 1.20 and peso > 90):
    print('Sua classificação é G')

if (altura > 1.20 and altura <=1.70 and peso <=60):
    print('Sua classificação é B')

if (altura > 1.20 and altura <=1.70 and peso > 60 and peso <=90):
    print('Sua classificação é E')

if (altura > 1.20 and altura <=1.70 and peso > 90):
    print('Sua classificação H')

if (altura > 1.70 and peso <= 60):
    print('Sua classificação é C')

if(altura > 1.70 and peso > 60 and peso <=90):
    print('Sua classificação é F ')

if(altura > 1.70 and peso > 90):
    print('Sua classificação é I')

#if (altura > 1.20 and altura <= 1.70 and )