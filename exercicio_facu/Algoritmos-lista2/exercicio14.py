#Desenvolva um algoritmo que leia o nome de um aluno, suas notas em 2 provas e em um trabalho
# (todas com valores entre 0 e 10) e sua frequência, definindo e imprimindo se ele foi aprovado, reprovado ou se fará prova final.
# O aluno será reprovado se faltou mais de 15 aulas. Será aprovado se não for reprovado por falta e sua média for
# maior ou igual a 6,0. Caso tenha média menor, deverá fazer prova final. O cálculo da média deve ser feito com peso 3
# para a primeira prova, 5 para a segunda prova e 2 para o trabalho.

nome = input("Digite seu nome: ")
nota_prova1 = float(input("Digite sua nota na prova: "))
nota_prova2 = float(input("Digite sua nota na segunda prova: "))
nota_trabalho = float(input("Digite sua nota no trabalho: "))
frequencia = int(input("Digite sua frequência"))

media_ponderada = (nota_prova1 * 3) + (nota_prova2 * 5) + (nota_trabalho * 2) / 10

if frequencia > 15:
    print("Reprovado!")
else:
    if media_ponderada >= 6:
        print("Aprovado!")
    else:
        print("Você fara a prova final!")