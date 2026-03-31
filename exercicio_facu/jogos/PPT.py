from random import *

print("0 = Pedra, 1 = Tesoura, 2 = Papel")

player= int(input("Digite um numero de 0 a 2: "))

computador = randint(0,2)

if player > 2 or player < 0:
    print("Número invalido")
else:
    if player == computador:
        condicao = "Empate"
    else:
        if player == 0 and computador == 1 or player == 1 and computador == 2 or player == 2 and computador == 0 :
            condicao = "Você Venceu!"
        else:
            condicao = "Mais sorte da proxima vez!"
    print("O computador escolheu: " ,computador)
    print(condicao)
