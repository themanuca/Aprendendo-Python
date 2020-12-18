import random, math
i = 0
k = 0
while (i != 5):
    n1 = math.ceil(100*random.random())
    n2 = math.ceil(100*random.random())
    print ('Qual é a soma:', n1 ,'+', n2 )

    resulta = int(input('Resultado: '))
    
    i += 1
    if resulta == n1 + n2:
        k += 1
        print('certo', k)
    
    