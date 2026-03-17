#Ler um número e informar se ele é positivo, negativo ou neutro (zero).

numero = float(input("Digite um numero: "))

if numero > 0 :
    print("Esse número é positivo")
else:
    if numero < 0 :
        print("Esse número é negativo")
    else:
        if numero == 0 :
            print("Esse número é Neutro")