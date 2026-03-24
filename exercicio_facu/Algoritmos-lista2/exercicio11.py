#Escreva um programa para calcular e mostrar o salário semanal de uma pessoa, determinado pelas condições que seguem.
#Se o número de horas trabalhadas for inferior ou igual a 40, a pessoa recebe R$15,00 por hora, senão a pessoa recebe
#R$600,00 mais R$21,00 para cada hora trabalhada acima de 40 horas. O programa deve pedir o número de horas trabalhadas
#como entrada e deve dar o salário como saída.

horas_trabalhadas = int(input("Digite quantos horas trabalhadas na semana: "))

if horas_trabalhadas < 0:
    print("Horas invalidas")
else:
    if horas_trabalhadas <= 40:
        salario = horas_trabalhadas * 15
    else:
        if horas_trabalhadas > 40:
            horas_a_mais = horas_trabalhadas - 40
            salario = horas_a_mais * 21 + 600
    print(f"Você receberá na semana: R${salario}")
