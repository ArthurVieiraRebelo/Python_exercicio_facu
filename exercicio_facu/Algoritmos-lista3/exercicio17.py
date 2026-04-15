intervalo = 0
fora_intervalo = 0
for i in range(1, 11):
    numero = int(input("Digite um número: "))
    if numero > 9 and numero <= 20:
        intervalo = intervalo + 1
    else:
        fora_intervalo = fora_intervalo + 1
print(f"Dos 10 números digitados {intervalo} estão no intervalo entre [10,20] e {fora_intervalo} estão fora do intervalo")

