from random import *

print("0 = Pedra, 1 = Tesoura, 2 = Papel")

vitorias_humano = 0
vitorias_computador = 0

quantidades = int(input("Digite quantas vezes você quer jogar? "))
if quantidades < 1 :
    print("Quantidade inválida")
else:
    for i in range(quantidades):
        player= int(input("Digite um numero de 0 a 2: "))

        computador = randint(0,2)

        if player > 2 or player < 0:
            print("Número invalido")
        else:
            if player == computador:
                condicao = "Empate"
            else:
                if (player == 0 and computador == 1) or (player == 1 and computador == 2) or (player == 2 and computador == 0) :
                    condicao = "Você Venceu!"
                    vitorias_humano += 1
                else:
                    condicao = "Mais sorte da proxima vez!"
                    vitorias_computador += 1
            print("O computador escolheu: " ,computador)
            print(condicao)
    empate = quantidades - (vitorias_humano + vitorias_computador)
    print(f"O jogador ganhou no total: {vitorias_humano} , O computador ganhou no total: {vitorias_computador} ")
    if empate > 0:
        print(f"A quantidade de empates foi de {empate}")
    else:
        print("Não teve empates")
