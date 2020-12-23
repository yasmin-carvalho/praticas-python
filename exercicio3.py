""" 3 - Ler dois números, armazenando-os nas variáveis num1 e num2. Verificar se o valor de
num1 é maior que o valor de num2 e, em caso positivo, trocar os conteúdos das variáveis. """

num1 = int (input('Digite o primeiro numero: '))
num2 = int (input('Digite o segundo numero: '))

if num1>num2:
    aux = num1
    num1 = num2
    num2 = aux
    
print('\nNUM1: ' +str(num1)+ '\nNUM2: ' +str(num2))
