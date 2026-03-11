salario_bruto = float(input("Digite qual o seu salario Bruto: "))
valor_hora = float(input("Digite qual o valor que você recebeu a mais por horas extras: "))
horas_extras = int(input("Digite qual a quantidade de horas extras: "))

salario_liquido = (salario_bruto + valor_hora * horas_extras ) * 92/100

input(f"Seu salario liquido é de: {salario_liquido}")