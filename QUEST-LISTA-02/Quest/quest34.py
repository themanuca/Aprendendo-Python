def aluno():
    print("===============================================")
    falta = int(input('Digite seu número de faltas: '))
    nota = float(input('Digite sua nota: '))
    print("===============================================")

    if nota >= 9 and falta <=20:
        print('Concieto A')

    if nota >= 9 and falta > 20:
        print('Conceito B')

    if nota >= 7.5 and nota <= 8.9 and falta <=20:
        print('Conceito B')

    if nota >= 7.5 and nota <= 8.9 and falta > 20:
        print('Conceito C')

    if nota >= 5 and nota <=7.4 and falta <=20:
        print('Conceito C')

    if nota >= 5 and nota <=7.4 and falta > 20:
        print('Conceito D')

    if nota >=4 and nota <=4.9 and falta <=20:
        print('Conceito C')
    
    if nota >=4 and nota <=4.9 and falta > 20:
        print('Conceito E')

    if nota >= 0 and nota <=3.9 and falta <=20:
        print('Conceito E')

    if nota >=0 and nota <=3.9 and falta > 20:
        print('Conceito E')

if (__name__ == "__main__"):
    aluno()
