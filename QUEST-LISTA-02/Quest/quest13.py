nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))

nota1 = nota1 * 1
nota2 = nota2 * 1
nota3 = nota3 * 2

media = nota1 + nota2 + nota3 / 3

if (media >= 60 ):
    print('Parabéns, aluno aprovado')

else:
    print('Aluno reprevado')
