numero_perfeito = 0
numero = 1

while numero_perfeito < 3:
    divisor = 0
    numero += 1
    for i in range(1, numero):
        teste = (numero % i) == 0
        if teste == True:
            divisor += i
    if divisor == numero:
        print(numero)
        numero_perfeito += 1

