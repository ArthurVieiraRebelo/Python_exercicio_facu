nota = float(input("Digite a nota do aluno: "))

aprovado = 60 <= nota <= 100
reprovado = 0 <= nota > 60

if aprovado == True:
    print("Aprovado!")
else:
    if reprovado == True:
        print("Reprovado!")
    else:
        if nota > 100 or nota < 0 :
            print("Nota invalida!")
