h = float(input('Digite sua altura: '))
sexo = (input('Diga seu sexo: \n'
'Masculino - M \n'
'Feminino - F\n'
': '
))

homem = (72.7 * h) - 58
mulheres = (62.1 * h) - 44.7

if (sexo == 'f' ):
    print('Seu peso idela é ', mulheres)
    

if (sexo == 'm'):
    print('Seu peso ideal é', homem)