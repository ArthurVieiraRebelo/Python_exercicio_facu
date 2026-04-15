branco = 0
nulo = 0
hugo = 0
arthur = 0
felipe = 0
mateus = 0
print("1,2,3,4 = voto para os respectivos candidatos; 5 = voto nulo; 6 = voto em branco.")
voto = int(input("Digite o número correspondente ao seu voto: "))
while voto != 0:

    if voto > 6 or voto < 0:
        print("Número inválido")
    else:
        if voto == 6:
            branco +=1
        else:
            if voto == 5:
                nulo += 1
            else:
                if voto == 4:
                    hugo += 1
                else:
                    if voto == 3:
                        arthur += 1
                    else:
                        if voto == 2:
                            felipe += 1
                        else:
                            mateus += 1
    print("1,2,3,4 = voto para os respectivos candidatos; 5 = voto nulo; 6 = voto em branco.")
    voto = int(input("Digite o número correspondente ao seu voto: "))
print(f"O candidato hugo recebeu {hugo} votos, O candidato Arthur recebeu {arthur} votos, O candidato Felipe recebeu {felipe} votos, "
      f"O candidato Mateus recebeu {mateus} votos")
print(f"O total de votos nulos foi de {nulo} votos")
print(f"O total de votos em branco foi de {branco} votos")
