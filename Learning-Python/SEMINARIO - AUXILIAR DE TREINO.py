print('==========================')
print('SEU AUXILIADOR NOS TREINOS')
print('=================')
print('Semana de Treino')
print('=================')

print('1 - Segunda - Feira')
print('2 - Terça - Feira')
print('3 - Quarta - Feira')
print('4 - Quinta - Feira')
print('5 - Sexta - Feira')


escolha = int(input('Escolha o dia de seu treino:  '))

treinoA = ['Supino reto barra', 'LEG 45', 'Supino inclinado', 'Agachamento Sumô','Des. Articulado', ]
treinoB = ['Remada Baixa aberta', 'Stiff', 'Remada Cavalinho', 'Flexo Vertical', 'Pulldown']
concluidas = [] 

def segunda (concluidas, treinoA, treinoB):

    print('================')
    print('SEGUNDA - FEIRA')
    print('================')
    print('1 - Iniciando o treino ')
    print('2 - Concluindo o treino')
    print('3 - Não Conlcuída')

    esco1 = int(input( ': '))
    
    if esco1 == 1:
        print('===============================')
        print('Seu treino de hoje é ', treinoA)
        print('===============================')
    
        
        final = (input('Concluiu ? S/N : '))
        
        if (final == 'S' or final == 's' ):
            print('Exercíco da Segunda Concluído')
            concluidas.append('Segunda Concluída')

        if final == 'N' or final == 'n':
            print('Exercíco da Segunda não concluído')
            concluidas.append('Segunda Não Concluída')

        
   
        
    if esco1 == 2:
        print('Exercício da Segunda Concluído')
        concluidas.append('Segunda Concluída')

    if esco1 == 3:
        print('Exercício da Segunda Não Concluído')
        concluidas.append('Segunda não Concluída')


'''if escolha == 1:
    segunda(concluidas, treinoA, treinoB)

else:
    concluidas.append('Segunda não Concluída')'''

###################################################################################

def terca(concluidas, treinoB):
    print('==============================')
    print('TERÇA - FEIRA')   
    print('==============================')
    print('1 - Iniciando o treino ')
    print('2 - Concluindo o treino')
    print('3 - Não Conlcuída')

    esco1 = int(input( ': '))
    
    if esco1 == 1:
        print('===============================')
        print('Seu treino de hoje é ', treinoB)
        print('===============================')
        final = input('Concluiu ? S/N: ')

        if final == 'S' or final == 's':
            print('Terça concluída')
            concluidas.append('Terça concluídas')

        if final == 'N' or final =='n':
            print('Terça não concluída')
            concluidas.append('Terça não concluída')

    
    if esco1 == 2:
        print('Terça concluída')
        concluidas.append('Terça concluída')

    if esco1 == 3:
        print('Terça não concluída')
        concluidas.append('Terça não concluída')



'''if escolha == 2:
    terca(concluidas, treinoB)

else:
    concluidas.append('Terça não concluída')'''



###################################################################################


def quarta (concluidas, treinoA):
    print('==============================')
    print('QUARTA - FEIRA')   
    print('==============================')
    print('1 - Iniciando o treino ')
    print('2 - Concluindo o treino')
    print('3 - Não Conlcuída')

    esco1 = int(input( ': '))
    
    if esco1 == 1:
        print('===============================')
        print('Seu treino de hoje é ', treinoA)
        print('===============================')
        final = input('Concluiu ? S/N: ')

        if final == 'S' or final == 's':
            print('Quarta concluída')
            concluidas.append('Quarta concluídas')

        if final == 'N' or final =='n':
            print('Quarta não concluída')
            concluidas.append('Quarta não concluída')

    
    if esco1 == 2:
        print('Quarta concluída')
        concluidas.append('Quarta concluída')

    if esco1 == 3:
        print('Quarta não concluída')
        concluidas.append('Quarta não concluída')

'''if escolha == 3:
    quarta(concluidas, treinoA)

else:
    concluidas.append('Quarta não concluída')'''



###############################################################################################

def quinta(concluidas, treinoB):
    print('==============================')
    print('QUINTA - FEIRA')   
    print('==============================')
    print('1 - Iniciando o treino ')
    print('2 - Concluindo o treino')
    print('3 - Não Conlcuída')

    esco1 = int(input( ': '))
    
    if esco1 == 1:
        print('===============================')
        print('Seu treino de hoje é ', treinoB)
        print('===============================')
        final = input('Concluiu ? S/N: ')

        if final == 'S' or final == 's':
            print('Quinta concluída')
            concluidas.append('Quinta concluídas')

        if final == 'N' or final =='n':
            print('Quinta não concluída')
            concluidas.append('Quinta não concluída')

    
    if esco1 == 2:
        print('Quinta concluída')
        concluidas.append('Quinta concluída')

    if esco1 == 3:
        print('Quinta não concluída')
        concluidas.append('Quinta não concluída')

'''if escolha == 4:
    quinta(concluidas, treinoB)

else:
    concluidas.append('Quinta não concluída')'''



###############################################################################################

def sexta (concluidas, treinoA):
    print('==============================')
    print('SEXTA - FEIRA')   
    print('==============================')
    print('1 - Iniciando o treino ')
    print('2 - Concluindo o treino')
    print('3 - Não Conlcuída')

    esco1 = int(input( ': '))
    
    if esco1 == 1:
        print('===============================')
        print('Seu treino de hoje é ', treinoA)
        print('===============================')
        final = input('Concluiu ? S/N: ')

        if final == 'S' or final == 's':
            print('Sexta concluída')
            concluidas.append('Sexta concluída')

        if final == 'N' or final =='n':
            print('Sexta não concluída')
            concluidas.append('Sexta não concluída')

    
    if esco1 == 2:
        print('Sexta concluída')
        concluidas.append('Sexta concluída')

    if esco1 == 3:
        print('Sexta não concluída')
        concluidas.append('Sexta não concluída')

'''if escolha == 5:
    sexta(concluidas, treinoA)

else:
    concluidas.append('Sexta não concluída')'''

#############################################################################################

def conclu (concluidas, treinoA, treinoB):
    print('===============================')
    print('==============================')
    print('Gostaria de saber o relatorio da sua semana de treino ?')
    print('===============================')
    print('===============================')
    print('Saber quais sãos os exercício ?')
    print('===============================')
    print('===============================')
    print('===============================')
    print('1 - Relatório')
    print('2 - Exercício')

    esco1 = int(input(': '))

    if esco1 == 1:
        print('==============')
        print(concluidas[0] )
        print('===============================')
        print(concluidas[1] )
        print('===============================')
        print(concluidas[2] )
        print('===============================')
        print(concluidas[3] )
        print('===============================')
        print(concluidas[4] )
        print('==============')

    def exercio(treinoA, treinoB):
        print('==============')
        print('Treino A')
        print('==========')
        print(treinoA[0])
        print('==========')
        print(treinoA[1])
        print('==========')
        print(treinoA[2])
        print('==========')
        print(treinoA[3])
        print('==========')
        print(treinoA[4])
        print('==============')

    if esco1 == 2:
        exercio(treinoA, treinoB)

    def exercio2(treinoA, treinoB):
        print('==============')
        print('Treino B')
        print('==============')
        print(treinoB[0])
        print('==============')
        print(treinoB[1])
        print('==============')
        print(treinoB[2])
        print('==============')
        print(treinoB[3])
        print('==============')
        print(treinoB[4])

    if esco1 == 2:
        exercio2(treinoA, treinoB)
        
        
for i in range(len(concluidas)):
    if concluidas[i] == 'Sexta concluída' or concluidas[i] == 'Sexta não concluída':    
        conclu (concluidas, treinoA, treinoB)



if escolha == 1:
    segunda(concluidas, treinoA, treinoB)
    terca(concluidas, treinoB)
    quarta(concluidas, treinoA)
    quinta(concluidas, treinoB)
    sexta(concluidas, treinoA)
    conclu (concluidas, treinoA, treinoB)

else:
    concluidas.append('Segunda não concluída')

if escolha == 2:
    terca(concluidas, treinoB)
    quarta(concluidas, treinoA)
    quinta(concluidas, treinoB)
    sexta(concluidas, treinoA)
    conclu (concluidas, treinoA, treinoB)

else:
    concluidas.append('Terça não concluída')

if escolha == 3:
    quarta(concluidas, treinoA)
    quinta(concluidas, treinoB)
    sexta(concluidas, treinoA)
    conclu (concluidas, treinoA, treinoB)

else:
    concluidas.append('Quarta não concluída')

if escolha == 4: 
    quinta(concluidas, treinoB)
    sexta(concluidas, treinoA)
    conclu (concluidas, treinoA, treinoB)
    
else:
    concluidas.append('Quinta não concluída')

if escolha == 5:
    sexta(concluidas, treinoA)
    conclu (concluidas, treinoA, treinoB)


















    


