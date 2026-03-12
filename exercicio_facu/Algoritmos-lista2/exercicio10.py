salario = float(input("Digite o seu salário: "))
financiamento = float(input("Digite o valor do financiamento: "))

financiamento_concedido = salario * 5

if financiamento <= financiamento_concedido:
    print("Financiamento Concedido")
else:
    print("Financiamento Negado")