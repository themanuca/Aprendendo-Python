nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

no1 = nota1 * 2
no2 = nota2 * 3
no3 = nota3 * 5

media = no1 + no2 + no3
meida1 = media / 3



if(meida1 >= 0):
    if(meida1 <= 2.9 ):
        print('Aluno reprovado')

if (meida1 >= 3):
    if (meida1 <= 4.9):
        print('Aluno de recuperação')

if (meida1 >= 5.0 ):
    print('Aluno aprovado')