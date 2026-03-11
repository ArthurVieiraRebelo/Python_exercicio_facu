consumo_de_quilowatts = float(input("Quantos quilowatts você gastou: "))
valor_do_quilowatts = float(input("Qual o valor do quilowatt: "))

valor_a_pagar = (consumo_de_quilowatts * valor_do_quilowatts ) * (18/100 + 1)

input(f"O valor da conta de energia é: R${valor_a_pagar}")