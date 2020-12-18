basemaior = float(input('Digite o valor da base maior: '))
basemenor = float(input('Digite o valor da base menor: '))
altura = float(input('Digite o valor da altura: '))

if basemaior > 0 and basemenor > 0:
    a = basemaior + basemenor * altura / 2
    print('Área de um trapézio é', a)

else:
    print('Valores não bate')

