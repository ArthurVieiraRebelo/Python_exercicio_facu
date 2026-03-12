ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano que você nasceu: "))

idade = ano_atual - ano_nascimento

print(f"Você tem {idade} anos.")

if idade < 0:
    print("Idade invalida!")
else:
    if idade <= 3:
        print("Você é um bebê!")

