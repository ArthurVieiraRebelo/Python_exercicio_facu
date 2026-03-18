# Desenvolva um algoritmo que pergunte um código e de acordo com o valor digitado seja apresentado o cargo correspondente.
# Caso o usuário digite um código que não esteja na tabela, mostrar uma mensagem de código inválido. Utilize a tabela abaixo:
#Código        Cargo
#101           Vendedor
#102           Atendente
#103            Auxiliar Técnico
#104            Assistente
#105            Coordenador de Grupo
#106            Gerente

code = int(input("Digite o Código: "))

if code < 101:
    print("Codigo invalido")
else:
    if code > 106:
        print("Codigo invalido")
    else:
        if code == 101:
            print("Vendedor")
        else:
            if code == 102:
                print("Atendente")
            else:
                if code == 103:
                    print("Auxiliar Técnico")
                else:
                    if code == 104:
                        print("Assistente")
                    else:
                        if code == 105:
                            print("Coordenador de Grupo")
                        else:
                            print("Gerente")
