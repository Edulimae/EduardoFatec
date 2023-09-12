idade_nadador = int(input("Entre coma a idade do nadador: " ))
if idade_nadador >= 5 :
    if idade_nadador <= 7:
        print("Esse nadador é da classe Infantil")
    elif idade_nadador <= 10:
        print("Esse nadador é da classe Juvenil")
    elif idade_nadador <= 15:
        print("Esse nadador é da classe Adolescente")
    elif idade_nadador <= 30:
        print("Esse nadador é da classe Adulto")
    else:
        print("Esse nadador é da classe Sênior")


else:
    print("Essse pessoa não está em nenhuma classe")

