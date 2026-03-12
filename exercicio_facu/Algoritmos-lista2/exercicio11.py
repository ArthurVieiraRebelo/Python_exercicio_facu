horas_trabalhadas = int(input("Digite quantos horas trabalhadas na semana: "))

if horas_trabalhadas < 0:
    print("Horas invalidas")
else:
    if horas_trabalhadas <= 40:
        salario_40 = horas_trabalhadas * 15
        print(f"Você receberá na semana: R${salario_40}")
    else:
        if horas_trabalhadas > 40:
            horas_a_mais = horas_trabalhadas - 40
            salario_40_mais = horas_a_mais * 21 + 600
            print(f"Você receberá na semana: R${salario_40_mais}")
