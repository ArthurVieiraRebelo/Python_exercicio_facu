#Faça um algoritmo que transforme a nota de um aluno em conceito. As notas 10 e 9 receberão conceito A,
# as notas 8 e 7 receberão conceito B, as notas 6 e 5 receberão conceito C e abaixo de 5 conceito D.

nota = int(input("Digite a nota: "))

if nota < 0:
    print("Nota invalida")
else:
    if nota > 10:
        print("Nota invalida")
    else:
        if nota >= 9:
            print("Você tem conceito A")
        else:
            if nota >= 7:
                print("Você tem conceito B")
            else:
                if nota >=5:
                    print("VoCê tem conceito C")
                else:
                    print("Você tem conceito D")