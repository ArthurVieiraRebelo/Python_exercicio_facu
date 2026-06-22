def perguntar_jogada():
    jogada1 = int(input("Digite em qual linha você quer jogar: "))
    jogada2 = int(input("Digite em qual coluna você quer jogar: "))
    if jogada1 < 0 or jogada1 > 2 or jogada2 < 0 or jogada2 > 2:
        while jogada1 < 0 or jogada1 > 2 or jogada2 < 0 or jogada2 > 2:
            print("Escolha entre 0 e 2")
            jogada1 = int(input("Digite em qual linha você quer jogar: "))
            jogada2 = int(input("Digite em qual coluna você quer jogar: "))
    jogado , tabuleiro = jogada_humano(jogada1, jogada2)
    while jogado == False:
        jogada1 = int(input("Digite em qual linha você quer jogar: "))
        jogada2 = int(input("Digite em qual coluna você quer jogar: "))
        jogado = jogada_humano(jogada1, jogada2)

    return jogada1, jogada2

def mostra_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for elemento in linha:
            print(elemento, end=" ")
        print()


def jogada_humano(jogada1, jogada2):
    jogado = False
    if tabuleiro[jogada1][jogada2] == "x":
        print("Esse já está ocupado, escolha outro!")
    else:
        if tabuleiro[jogada1][jogada2] == "o":
            print("Você já jogou nesse")
        else:
            tabuleiro[jogada1][jogada2] = "o"
            jogado = True


    return jogado, tabuleiro

def verificar_se_pode_ganhar_linha(tabuleiro):
    jogou = False
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
            jogou = True
    return jogou

def verificar_se_pode_ganhar_coluna(tabuleiro, jogou):
    linha_vazia = 0
    coluna_vazia = 0
    coluna = -1
    coluna_fim = 0
    for a in range(0, 3):
        ganhar = 0
        coluna += 1
        coluna_fim += 1
        for i in range(0, 3):
            for j in range(coluna, coluna_fim):
                if tabuleiro[i][j] == "x":
                    ganhar += 1
                else:
                    if tabuleiro[i][j] == "*":
                        linha_vazia = i
                        coluna_vazia = j
        if ganhar == 2 and jogou == False:
            tabuleiro[linha_vazia][coluna_vazia] = "x"
            jogou = True
    return jogou

def verificar_linhas(tabuleiro, jogou):
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
            jogou = True
    return jogou

def verificar_colunas(tabuleiro, jogou):
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
            jogou = True
    return jogou

def verificar_se_pode_ganhar_diagonal_principal(tabuleiro, jogou):
    ganhar = 0
    linha_vazia = 0
    coluna_vazia = 0
    for i in range(0, 3):
        if tabuleiro[i][i] == "x":
            ganhar += 1
        else:
            if tabuleiro[i][i] == "*":
                linha_vazia = i
                coluna_vazia = i
    if ganhar == 2:
        tabuleiro[linha_vazia][coluna_vazia] = "x"
        jogou = True
    return jogou

def verificar_se_pode_ganhar_diagonal_secundaria(tabuleiro, jogou):
    ganhar = 0
    linha_vazia = 0
    coluna_vazia = 0
    for i in range(len(tabuleiro)):
        j = len(tabuleiro) - i - 1
        if tabuleiro[i][j] == "x":
            ganhar += 1
        else:
            if tabuleiro[i][j] == "*":
                linha_vazia = i
                coluna_vazia = j
    if ganhar == 2:
        tabuleiro[linha_vazia][coluna_vazia] = "x"
        jogou = True
    return jogou

def diagonal_principal(tabuleiro):
    ganhar = 0
    linha_vazia = 0
    coluna_vazia = 0
    for i in range(0, 3):
                if tabuleiro[i][i] == "o":
                    ganhar += 1
                else:
                    if tabuleiro[i][i] == "*":
                        linha_vazia = i
                        coluna_vazia = i
    if ganhar == 2:
        tabuleiro[linha_vazia][coluna_vazia] = "x"

def verificar_se_jogador_win(tabuleiro):

    for i in range(0, 3):
        jogador_win = False
        ganhar = 0
        for j in range(0, 3):
            if tabuleiro[i][j] == "o":
                ganhar += 1
        if ganhar == 3:
            jogador_win = True

    coluna = -1
    coluna_fim = 0
    for a in range(0, 3):
        ganhar = 0
        coluna += 1
        coluna_fim += 1
        for i in range(0, 3):
            for j in range(coluna, coluna_fim):
                if tabuleiro[i][j] == "o":
                    ganhar += 1
            if ganhar == 3:
                jogador_win = True

    ganhar = 0

    for i in range(0, 3):
        if tabuleiro[i][i] == "o":
            ganhar += 1
    if ganhar == 3:
            jogador_win = True

    return jogador_win

def verificar_se_maquina_win(tabuleiro):
    for i in range(0, 3):
        maquina_win = False
        ganhar = 0
        for j in range(0, 3):
            if tabuleiro[i][j] == "x":
                ganhar += 1
        if ganhar == 3:
            maquina_win = True

    coluna = -1
    coluna_fim = 0
    for a in range(0, 3):
        ganhar = 0
        coluna += 1
        coluna_fim += 1
        for i in range(0, 3):
            for j in range(coluna, coluna_fim):
                if tabuleiro[i][j] == "x":
                    ganhar += 1
            if ganhar == 3:
                maquina_win = True

    ganhar = 0

    for i in range(0, 3):
        if tabuleiro[i][i] == "x":
            ganhar += 1
    if ganhar == 3:
            maquina_win = True

    return maquina_win

recomecar = "sim"
velha = 0
maquina = 0
humano = 0

while recomecar == "sim" or recomecar == "s":

    tabuleiro = [["*", "*", "*"],
                ["*", "*", "*"],
                ["*", "*", "*"]]
    rodada = 0
    #Round 0
    print(f"Round {rodada}: ")
    if rodada == 0:
            tabuleiro[1][1] = "x"
            mostra_tabuleiro(tabuleiro)
            jogada1, jogada2 = perguntar_jogada()
            mostra_tabuleiro(tabuleiro)
    rodada += 1

    #Round 1
    print(f"Round {rodada}: ")
    if rodada == 1:
        if tabuleiro[jogada1][jogada2] != tabuleiro[0][0]:
            print("Jogada da Computador:")
            tabuleiro[0][0] = "x"
            mostra_tabuleiro(tabuleiro)
        else:
            if tabuleiro[jogada1][jogada2] != tabuleiro[0][2]:
                print("Jogada da Computador:")
                tabuleiro[0][2] = "x"
                mostra_tabuleiro(tabuleiro)
        jogada1, jogada2 = perguntar_jogada()
        mostra_tabuleiro(tabuleiro)
        rodada += 1

    #Round 2
    print(f"Round {rodada}: ")
    if rodada == 2:
        print("Jogada da Computador:")
        jogou = verificar_se_pode_ganhar_linha(tabuleiro)
        jogou = verificar_se_pode_ganhar_coluna(tabuleiro, jogou)
        jogou = verificar_se_pode_ganhar_diagonal_principal(tabuleiro, jogou)
        jogou = verificar_se_pode_ganhar_diagonal_secundaria(tabuleiro, jogou)
        jogou = verificar_linhas(tabuleiro,jogou)
        verificar_colunas(tabuleiro, jogou)
        mostra_tabuleiro(tabuleiro)
        jogada1, jogada2 = perguntar_jogada()
        mostra_tabuleiro(tabuleiro)
        verificar_se_jogador_win(tabuleiro)
        verificar_se_maquina_win(tabuleiro)
        rodada += 1

    #Round 3
    if verificar_se_maquina_win(tabuleiro) == True:
        print("O computador ganhou!")
        maquina += 1
    else:
        if verificar_se_jogador_win(tabuleiro) == True:
            print("Você ganhou!")
            humano += 1
        else:
            print(f"Round {rodada}: ")
            print("Jogada da Computador:")
            jogou = verificar_se_pode_ganhar_linha(tabuleiro)
            verificar_se_pode_ganhar_coluna(tabuleiro, jogou)
            mostra_tabuleiro(tabuleiro)
            jogada1, jogada2 = perguntar_jogada()
            mostra_tabuleiro(tabuleiro)
            verificar_se_jogador_win(tabuleiro)
            verificar_se_maquina_win(tabuleiro)
            rodada += 1

    #Round 4
    if verificar_se_maquina_win(tabuleiro) == True:
        print("O computador ganhou!")
        maquina += 1
    else:
        if verificar_se_jogador_win(tabuleiro) == True:
            print("Você ganhou!")
            humano += 1
        else:
            print("Jogada da Computador:")
            print(f"Round {rodada}: ")
            print("Jogada da Computador:")
            for i in range(0,3):
                for j in range(0,3):
                    if tabuleiro[i][j] == "*":
                        tabuleiro[i][j] = "x"
            mostra_tabuleiro(tabuleiro)
            print("Deu velha!")
            velha += 1




    recomecar = input("Deseja jogar novamente? [S/N] ")
    recomecar = recomecar.lower()
    if recomecar == "sim":
        recomecar = "s"
    else:
        if recomecar == "n" or recomecar == "nao":
            print(f"Deu velha: {velha} vezes, O computador ganhou: {maquina} vezes e Você ganhou: {humano} vezes")




