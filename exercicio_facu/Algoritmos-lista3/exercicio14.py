
media_novo = 0
preco_novo_total = 0
total_prod = 0
preco_total = 0

codigo = int(input("Digite o codigo do produto: "))
while codigo >= 0:
    total_prod += 1
    preco = int(input("Digite o preço do produto: "))
    preco_novo = preco * 1.2
    preco_total += preco
    preco_novo_total += preco_novo
    print(f"O preço novo do produto {codigo} é de: R${preco_novo:.2f}")
    codigo = int(input("Digite o codigo do produto: "))

media_antes = preco_total / total_prod
media_novo = preco_novo_total / total_prod

print(f"A média de preços antiga é de {media_antes:.2f} agora é de R${media_novo:.2f}")

