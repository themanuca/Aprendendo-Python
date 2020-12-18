idade = int(input('Digite sua idade: '))
tempo = int(input('Seu tempo de serviço: '))

if(idade > 64):
    print('==============================')
    print('APOSENTADO')
    print('==============================')

while idade >= 60 and tempo >= 25 or tempo >=30 or idade >=65:
    
    if tempo >= 25:
        print('==============================')
        print('APOSENTADO')
        print('==============================')

    break 

else: 
    print('==============================')
    print('Vai sofrer um pouco mais')
    print('==============================')

"""if(idade >= 65 ):
    print('==============================')
    print('Sua aposentadoria foi aprovada')
    print('==============================')
if(tempo >= 30):
    print('==============================')
    print('Sua aposentadoria foi aprovada')
    print('==============================')
if(tempo >= 25):
    if(idade >= 60):
        print('==============================')
        print('Sua aposentadoria foi aprovada')
        print('==============================')

else:
    print('==============================')
    print('Vai sofrer um pouco mais')
    print('==============================')"""

