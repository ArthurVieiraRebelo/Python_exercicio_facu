
def perguntar_jogada():
    jogada1 = int(input("Digite em qual linha você quer jogar: "))
    jogada2 = int(input("Digite em qual coluna você quer jogar: "))
    return jogada1, jogada2

def mostra_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for elemento in linha:
            print(elemento, end=" ")
        print()

def jogada_humano(jogada1, jogada2):
    if tabuleiro[jogada1][jogada2] != "x":
        tabuleiro[jogada1][jogada2] = "o"
    else:
        print("Esse já está ocupado, escolha outro!")

    return tabuleiro

def verificar_linha(tabuleiro):
    ganhar = 0
    linha_vazia = 0
    coluna_vazia = 0
    for i in range(0,3) :
        ganhar = 0
        for j in range(0, 3):
            if tabuleiro[i][j] == "o":
                ganhar += 1
            else:
                if tabuleiro[i][j] == "*":
                    linha_vazia = i
                    coluna_vazia = j
        if ganhar == 2:
            tabuleiro[linha_vazia][coluna_vazia] = "x"
    return tabuleiro

def coluna_0_de_cima_baixo(tabuleiro):
    linha_vazia = 0
    coluna_vazia = 0
    coluna = -1
    coluna_fim = 0
    for a in range(0,3):
        ganhar = 0
        coluna += 1
        coluna_fim += 1
        for i in range(0,3):
            for j in range(coluna, coluna_fim):
                if tabuleiro[i][j] == "o":
                    ganhar += 1
                else:
                    if tabuleiro[i][j] == "*":
                        linha_vazia = i
                        coluna_vazia = j
        if ganhar == 2:
            tabuleiro[linha_vazia][coluna_vazia] = "x"
    return tabuleiro

def verificar_se_pode_ganhar_linha(tabuleiro):
    ganhar = 0
    linha_vazia = 0
    coluna_vazia = 0
    for i in range(0, 3):
        ganhar = 0
        for j in range(0, 3):
            if tabuleiro[i][j] == "x":
                ganhar += 1
            else:
                if tabuleiro[i][j] == "*":
                    linha_vazia = i
                    coluna_vazia = j
        if ganhar == 2:
            tabuleiro[linha_vazia][coluna_vazia] = "x"



jogou = False

tabuleiro = [ ["x", "*" , "*"],
              ["x", "*" , "x"],
              ["*", "o", "o"] ]
mostra_tabuleiro(tabuleiro)
verificar_se_pode_ganhar_linha(tabuleiro)
mostra_tabuleiro(tabuleiro)