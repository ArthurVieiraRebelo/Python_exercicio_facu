#Baseado no ano e peso do modelo de um automóvel, o estado de Nova Jersey determina a sua classe de peso e taxa
# de registro usando a seguinte tabela:

#Ano do modelo          Peso            Classe        Taxa de registro
#                   Menos de 1200 kg      1              16,50
#1970 ou antes     de 1200 a 1700 kg      2              25,50
#                    Mais de 1700 kg      3              46,50

#                   Menos de 1200 kg      4              27,00
#1971 a 1979       de 1200 a 1700 kg      5              30,50
#                    Mais de 1700 kg      6              52,50

#1980 ou depois     Menos de 1600 kg      7              19,50
#                   1600 kg ou mais       8              55,50

#Usando esta informação, escreva um programa que receba o ano e o peso do modelo de um automóvel e calcule e imprima
# a classe de peso e a taxa de registro para o carro.

ano_do_carro = int(input("Digite o ano de seu carro: "))
peso_do_carro = int(input("Digite o seu peso do carro em Kg: "))

if ano_do_carro <= 1970:
    if peso_do_carro < 1200:
        print("A classe dele é 1 e a taxa de registro é 16,50")
    else:
        if peso_do_carro <= 1700:
            print("A classe dele é 2 e a taxa de registro é 25,50")
        else:
            print("A classe dele é 3 e a taxa de registro é 46,50")
else:
    if ano_do_carro <= 1979:
        if peso_do_carro < 1200:
            print("A classe dele é 4 e a taxa de registro é 27,00")
        else:
            if peso_do_carro <= 1700:
                print("A classe dele é 5 e a taxa de registro é 30,50")
            else:
                print("A classe dele é 6 e a taxa de registro é 52,50")
    else:
        if ano_do_carro >= 1980:
            if peso_do_carro < 1600:
                print("A classe dele é 7 e a taxa de registro é 19,50")
            else:
                print("A classe dele é 8 e a taxa de registro é 55,50")