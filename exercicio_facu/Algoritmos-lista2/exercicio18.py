#Escreva um programa que receba dois números reais e um código de seleção do usuário. Se o código digitado for 1,
# faça o programa adicionar os dois números previamente digitados e mostrar o resultado; se o código de seleção for 2,
# os números devem ser multiplicados; se o código de seleção for 3, o primeiro número deve ser dividido pelo segundo.
# Se nenhuma das opções acima for escolhida, mostrar "Código inválido".

numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite um numero: "))
code = int(input("Digite um Código: "))

adicao = numero1 + numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

if code < 1:
    print("Codigo invalido")
else:
    if code > 3:
        print("Codigo invalido")
    else:
        if code == 1:
            print(adicao)
        else:
            if code == 2:
                print(multiplicacao)
            else:
                if code == 3:
                    print(divisao)
