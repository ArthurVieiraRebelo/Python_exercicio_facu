#A taxa de juros aplicada em fundos depositados em um banco é determinada pelo tempo em que estes ficam depositados.
# Para um banco em particular, a seguinte tabela é usada:
# Tempo em depósito:
#   Taxa de juro:
#       Maior ou igual a 5 anos:
#           0,95
#       Menor que 5 anos mas maior ou igual a 4 anos:
#           0,90
#       Menor que 4 anos mas maior ou igual a 3 anos:
#           0,85
#       Menor que 3 anos mas maior ou igual a 2 anos:
#           0,75
#       Menor que 2 anos mas maior ou igual a 1 ano:
#           0,65
#       Menor que 1 ano:
#           0,55
#Usando esta informação, escreva um programa que receba o tempo em que os fundos foram mantidos em depósito e informe
#a taxa de juros correspondente.

tempo_mantido = float(input("Digite quantos anos você deixou seu dinheiro mantido no fundo: "))

if tempo_mantido < 0:
    print("Tempo inválido")
else:
    if tempo_mantido < 1:
        print("Sua taxa de juros é de 0,55%")
    else:
        if tempo_mantido < 2:
            print("Sua taxa de juros é de 0,65%")
        else:
            if tempo_mantido < 3:
                print("Sua taxa de juros é de 0,75%")
            else:
                if tempo_mantido < 4:
                    print("Sua taxa de juros é de 0,85%")
                else:
                    if tempo_mantido < 5:
                        print("Sua taxa de juros é de 0,90%")
                    else:
                        if tempo_mantido >= 5:
                            print("Sua taxa de juros é de 0,95%")
