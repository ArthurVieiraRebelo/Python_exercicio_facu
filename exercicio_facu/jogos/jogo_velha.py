import random

def jogada_computador(jogada1, jogada2):
    tabuleiro[jogada1][jogada2] = "o"
    return tabuleiro

computador = False
jogador = False
velha = False
jogada1 = 0
jogada2 = 0

comecar = random.randint(1 , 2)
tabuleiro = [ ["*", "*" , "*"],
              ["*", "*" , "*"],
              ["*", "*", "*"] ]
while computador != True or jogador != True or velha != True:
    if comecar == 1:
        tabuleiro[1][1]
        print(tabuleiro)
        jogada1 = input("Digite em qual coluna você quer jogar: ")
        jogada2 = input("Digite em qual linha você quer jogar: ")
        jogada_computador(jogada1, jogada2)
        print(tabuleiro)
