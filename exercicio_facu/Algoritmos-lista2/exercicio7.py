#Faça a leitura do salário atual e do tempo de serviço de um funcionário. A seguir, calcule o seu salário reajustado.
# Funcionários com até 1 ano de empresa, receberão aumento de 10%. Funcionários com mais de um ano de tempo de serviço,
# receberão aumento de 20%.

salario_atual = float(input("Digite seu salario atual: "))
quantidade_de_anos= float(input("Digite quantos anos você trabalha na empresa: "))

if quantidade_de_anos < 0:
    print("Qunatidade de anos invalida!")
else:
    if quantidade_de_anos <= 1 :
        salario_ate_1ano = salario_atual * 1.1
        print(f"Seu novo salário será de: R${salario_ate_1ano}")
    else:
         if quantidade_de_anos > 1:
            salario_1ano_mais = salario_atual * 1.2
            print(f"Seu novo salário será de: R${salario_1ano_mais}")
