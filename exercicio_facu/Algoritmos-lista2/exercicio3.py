nota = float(input("Digite a nota do aluno: "))

if 60 <= nota <= 100:
    print("Aprovado")
else:
    if 0 <= nota < 60 :
        print("Reprovado")
    else:
        if (0 > nota) or (nota > 100) :
            print("Nota invalida")