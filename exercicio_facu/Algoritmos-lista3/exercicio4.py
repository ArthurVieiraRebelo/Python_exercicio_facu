filhos_total = 0
pessoas_ate_1000 = 0
quantidade_de_pessoas = 0
salario = float(input(f"Digite o salário da pessoa: "))
salario_total = salario
while salario >= 0:
    quantidade_de_pessoas += 1
    filhos = int(input(f"Quantos filhos a pessoa tem? "))
    if salario > maior_salario:
        maior_salario = salario
    if salario <= 1000:
        pessoas_ate_1000 += 1
    salario_total += salario
    filhos_total += filhos
    salario = float(input(f"Digite o salário da pessoa: "))

media_salarial = salario_total / quantidade_de_pessoas
media_filhos = filhos_total / quantidade_de_pessoas
percentual_ate_1000 = (pessoas_ate_1000 / quantidade_de_pessoas) * 100

if quantidade_de_pessoas > 0:
    print(f"A média dos salários é {media_salarial:.2f}")
    print(f"A média do número de filhos são {media_filhos:.2f}")
    print(f"O maior salário é de R${maior_salario:.2f}")
    print(f"O percentual de pessoas com salário até R$1.000 é de {percentual_ate_1000:.2f}%")
