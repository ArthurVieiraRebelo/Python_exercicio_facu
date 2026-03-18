#Desenvolva um algoritmo para que, dados dois valores inteiros entre 1 e 10 lidos, calcule e imprima: a média dos números
# caso a soma deles for menor que 8, seu produto caso a soma seja igual a 8 ou a divisão do maior pelo menor caso a soma
# dos valores for maior que 8.

numero1 = int(input("Digite um Número: "))
numero2 = int(input("Digite outro Número: "))

soma = numero1 + numero2
media = soma / 2
mult = numero1 * numero2

if numero1 > 10:
    print("Números inválidos")
else:
    if numero1 < 1:
        print("Números inválidos")
    else:
        if numero2 > 10:
            print("Números inválidos")
        else:
            if numero2 < 1:
                print("Números inválidos")
            else:
                if soma < 8:
                    print(media)
                else:
                    if soma == 8:
                        print(mult)
                    else:
                        if numero1 > numero2:
                            print(numero1/numero2)
                        else:
                            print(numero2/numero1)