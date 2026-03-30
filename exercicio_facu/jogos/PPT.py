from random import *

pedra_papel_tesoura = int(input("Digite um numero de 0 a 2, 0 = Pedra, 1 = Tesoura, 2 = Papel: "))

player = pedra_papel_tesoura

computador = randint(0,2)

if player > 2 and player < 0:
    print("Número invalido")
else:
    if player > computador:
        condicao = "Você Venceu!"
    else:
        if player < computador:
           condicao = "Mais sorte da próxima vez"
        else:
            condicao = "Empate"
    print("O computador escolheu: " ,computador)
    print(condicao)
