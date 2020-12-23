import math

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

if a!=0:
    delta = (b**2) - 4*a*c
    if delta > 0:
        x1 = ((-b + math.sqrt(delta)) / (2*a))
        x2 = ((-b - math.sqrt(delta)) / (2*a))
        print('Equação possui duas raízes reais: \n')
        print('X1: ' +str(x1)+ '\nX2: ' +str(x2))
    
    elif delta==0:
        x1 = ((-b + math.sqrt(delta)) / (2*a))
        print('Equação possui uma raíz real: \n')
        print('X1: '+str(x1))
    else:
        print('\nEquação não possui raízes reais!\n')

else:
    print('\nDigite o valor de A diferente de 0\n')
    