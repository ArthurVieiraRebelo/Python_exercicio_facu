salario_atual = float(input("Digite seu salario atual: "))
quantidade_de_meses= float(input("Digite quantos messes você trabalha na empresa: "))

if quantidade_de_meses < 0:
    print("Qunatidade invalida!")
else:
    if quantidade_de_meses <=12:
        salario_ate_1ano = salario_atual * 1.1
        print(f"Seu novo salário será de: R${salario_ate_1ano}")
    else:
         if quantidade_de_meses > 12:
            salario_1ano_mais = salario_atual * 1.2
            print(f"Seu novo salário será de: R${salario_1ano_mais}")
