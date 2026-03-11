salario_atual = float(input("Digite seu salario atual: "))
quantidade_de_anos = float(input("Digite quantos anos você trabalha na empresa: "))

if 0 < quantidade_de_anos <=1:
    salario_ate_1ano = salario_atual * 1.1
    print(f"Seu novo salário será de: R${salario_ate_1ano}")
else:
    if quantidade_de_anos > 1:
        salario_1ano_mais = salario_atual * 1.2
        print(f"Seu novo salário será de: R${salario_1ano_mais}")