quantidade_de_pessoas = int(input("Qual a população? "))

salario_total = 0
filhos_total = 0
maior_salario = 0
pessoas_ate_1000 = 0

for i in range(1, quantidade_de_pessoas + 1):
    salario = float(input(f"Digite o salário da pessoa {i}: "))
    filhos = int(input(f"Quantos filhos a pessoa {i} tem? "))
    if salario > maior_salario:
        maior_salario = salario
    if salario <= 1000:
        pessoas_ate_1000 += 1
    salario_total += salario
    filhos_total += filhos

media_salarial = salario_total / quantidade_de_pessoas
media_filhos = filhos_total / quantidade_de_pessoas
percentual_ate_1000 = (pessoas_ate_1000 / quantidade_de_pessoas) * 100

print(f"A média dos salários é {media_salarial}")
print(f"A média do número de filhos são {media_filhos}")
print(f"O maior salário é de R${maior_salario}")
print(f"O percentual de pessoas com salário até R$1.000 é de {percentual_ate_1000}%")
