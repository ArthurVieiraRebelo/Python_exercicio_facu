#Escrever uma função calcularQuociente(dividendo,
#divisor), que retorna a divisão inteira (sem casas
#decimais) de dividendo por divisor e outra função
#calcularResto(dividendo, divisor) que retorna o resto.

def calcular_quociente(dividendo, divisor):
    if divisor != 0:
        quociente = dividendo // divisor
    return quociente

def calcular_resto(dividendo, divisor):
    if divisor != 0:
        resto = dividendo % divisor
    return resto

dividendo = int(input("Digite um numero inteiro: "))
divisor = int(input("Digite outro numero inteiro: "))
print(f"A divisão do {dividendo} pelo {divisor} sem casas decimais e arredondando é: {calcular_quociente(dividendo, divisor):.0f}")
print(f"O resto da divisão acima: {calcular_resto(dividendo, divisor)}")
