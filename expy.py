peso = float(input('qual seu peso? '))
altura = float(input('qual sua altura? '))
imc = peso/(altura*altura)
print('o seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('abaixo do peso')
elif  18.5 <= imc < 25:
    print('peso ideal')
elif 25 <= imc < 30:
    print('sobrepeso')
elif 30 <= imc < 40:
    print('obesidade')
elif imc > 40:
    print('obesidade mórbida')