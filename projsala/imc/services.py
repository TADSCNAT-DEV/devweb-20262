def calcular_imc(altura,peso):
    imc=peso/(altura*altura)
    if imc < 18.5:
        classificacao = 'Abaixo do peso'
    elif imc < 24.9:
        classificacao = 'Peso normal'
    elif imc < 29.9:
        classificacao = 'Sobrepeso'
    else:
        classificacao = 'Obesidade'

    return imc,classificacao