salario_atual = float(input("Digite seu salario atual: R$ "))
porcentagem_de_aumento = float(input("Digite a porcentagem d0 aumento: "))

salario_novo = salario_atual * (porcentagem_de_aumento / 100 + 1)

print(f" Seu novo salario será de: R${salario_novo}")
print(f"O valor do aumento foi de: R${salario_novo - salario_atual}")