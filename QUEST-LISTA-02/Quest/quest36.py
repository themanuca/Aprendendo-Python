def comissao():
    print('Saiba de quanto será sua comissão')
    print('=====================================')
    vendas = int(input('Valor de suas vendas mensais: '))

    vendas700 = 700 + vendas * 16 / 100
    vendas650 = 650 + vendas * 14 / 100
    vendas600 = 600 + vendas * 14 / 100
    vendas550 = 550 + vendas * 14 / 100
    vendas500 = 500 + vendas * 14 / 100
    vendas400 = 400 + vendas * 14 / 100

    if vendas >= 100000:
        print('Sua comição é de {} reais'.format(vendas700))

    elif vendas >=80000 and vendas <100000:
        print('Sua comição é de {} reais'.format(vendas650))

    elif vendas >= 60000 and vendas <80000:
        print('Sua comição é de {} reais'.format(vendas600))

    
    elif vendas >= 40000 and vendas <60000:
        print('Sua comição é de {} reais'.format(vendas550))

    elif vendas >= 20000 and vendas <40000:
        print('Sua comição é de {} reais'.format(vendas500))

    else:
        if vendas < 20000:
            print('Sua comição é de {} reais'.format(vendas400))
    




if __name__ == "__main__":
    comissao()