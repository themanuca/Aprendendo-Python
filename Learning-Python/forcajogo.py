def forca():
    print('======================')
    print('==JOGO DA FORCA==')
    print('======================')

    palavra_secreta = 'banana'
    letra_acerto = ['_' for letra in palavra_secreta]
    
    '''for letra in palavra_secreta:
        letra_acerto.append("_")'''
    

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = input("Qual a letra ? ")
        chute = chute.strip() #tratamento de espaço

        if chute in palavra_secreta:
            index = 0  
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):#Tratamento da str, poem todas em maiscula
                    letra_acerto[index] = letra
                        
                    
                index += 1
                
        else:
            erros += 1
        
        
        enforcou = erros == 6
        acertou = "_" not in letra_acerto
        print(letra_acerto)



    if acertou:
        print('Você ganhou !!')

    else:
        print('Você perdeu !!')


print('Fim do jogo')

if(__name__ == '__main__'):
    forca()