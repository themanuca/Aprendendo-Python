def preço_novo():
    print("========================")
    print("Atualização de preço")
    print("========================")

    valorantigo = float(input('Digite o valor antigo: '))
    #####################################################
    porcento5 = '5%'
    porcento10 = '10%'
    porcento15 = '15%'
    ######################################################
    
    entre50a100 = valorantigo >= 50 and valorantigo <= 100
    acimade100 = valorantigo >= 100

    #######################################################
    ate50 = valorantigo + valorantigo * 5 / 100
    de50e100 = valorantigo + valorantigo * 10 / 100
    acima100 = valorantigo + valorantigo * 15 / 100
    #######################################################
    
    if valorantigo <=50:
        print("Seu produto sofreu um pequeno reajuste de {}".format(porcento5))
        print("Preço do produto é de {}".format(ate50))

    if entre50a100:
        print("Seu produto sofreu um pequeno reajuste de {}".format(porcento10))
        print("Preço do produto é de {}".format(de50e100))

    if acimade100:
        print("Seu produto sofreu um pequeno reajuste de {}".format(porcento15))
        print("Preço do produto é de {}".format(acima100))

if (__name__ == "__main__"):
    preço_novo()


    

     