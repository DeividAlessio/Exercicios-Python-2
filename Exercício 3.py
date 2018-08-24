num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')
num3 = input('Digite um terceiro numero: ')
if num1>num2 and num1>num3:
    print +num1
elif num2>num1 and num2>num3:
    print +num2
elif num3>num2 and num3>num1:
    print +num3
else:
    print('Houve um empate triplo!')
