#Faça a leitura do salário atual e do tempo de serviço de um funcionário. A seguir, calcule o seu salário reajustado.
# Funcionários com até 1 ano de empresa, receberão aumento de 10%. Funcionários com mais de um ano de tempo de serviço,
# receberão aumento de 20%.

salario_atual = float(input("Digite seu salario atual: "))
quantidade_de_anos= int(input("Digite quantos anos você trabalha na empresa: "))

if salario_atual < 0:
    print("Salario inválido")
else:
    if quantidade_de_anos < 0:
        print("Quantidadde de anos invalida!")
    else:
        if quantidade_de_anos <= 1 :
            percentual = 1.1
        else:
            percentual = 1.2
        salario_reajustado = salario_atual * percentual
        print("Seu novo salário será = ", salario_reajustado)
