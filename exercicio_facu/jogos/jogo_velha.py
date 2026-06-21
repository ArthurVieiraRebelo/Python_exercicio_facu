import random

def jogada_computador(jogada1, jogada2):
    tabuleiro[jogada1][jogada2] = "o"
    return tabuleiro

def verificar_se_esta_vazio:



computador = False
jogador = False
velha = False
jogada1 = 0
jogada2 = 0
recomecar = "nao"

comecar = random.randint(1 , 2)
tabuleiro = [ ["*", "*" , "*"],
              ["*", "*" , "*"],
              ["*", "*", "*"] ]
while recomecar != "sim" or recomecar != "s":
    if comecar == 1:
        tabuleiro[1][1]
        print(tabuleiro)
        jogada1 = input("Digite em qual coluna você quer jogar: ")
        jogada2 = input("Digite em qual linha você quer jogar: ")
        jogada_computador(jogada1, jogada2)
        print(tabuleiro)
    else:
        if comecar == 2:
            jogada1 = input("Digite em qual coluna você quer jogar: ")
            jogada2 = input("Digite em qual linha você quer jogar: ")
            jogada_computador(jogada1, jogada2)
            print(tabuleiro)


