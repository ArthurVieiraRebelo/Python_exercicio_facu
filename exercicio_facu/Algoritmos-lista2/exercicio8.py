#Faça a leitura do ano atual e do ano de nascimento de uma pessoa e exibir sua idade. A seguir, informe
# se a pessoa é bebê (0 a 3 anos), criança (4 a 11 anos), adolescente (12 a 17 anos), adulta (18 a 64 anos)
# ou idosa (65 anos em diante).

ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano que você nasceu: "))

idade = ano_atual - ano_nascimento

print(f"Você tem {idade} anos.")

if idade < 0:
    print("Idade invalida!")
else:
    if idade <= 3:
        print("Você é um bebê!")
    else:
        if idade <= 11:
            print("Você é criança")
        else:
            if idade <= 17:
                print("Você é adolescente")
            else:
                if idade <= 64:
                    print("Você é adulto")
                else:
                    print("Você é idosa")


