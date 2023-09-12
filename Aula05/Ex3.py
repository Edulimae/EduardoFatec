preco = float(input("Entre como valor líquido do produto R$ "))
origem = int(input("Digite código de origem 1-Sul 2-Norte 3-Nordeste 4-Centro-Oeste 5-Sudeste "))
if origem == 1:
    preco1 = preco * 1.11
    print(f"O valor do produto recebido do Sul é R$ {preco1:9.2f}")
elif origem == 2:
    preco2 = preco * 1.13
    print(f"O valor do produto recebido do Norte é R$ {preco2:9.2f}")
elif origem == 3:
    preco3 = preco * 1.09
    print(f"O valor do produto recebido do Nordeste é R$ {preco3:9.2f}")
elif origem == 4:
    preco4 = preco * 1.12
    print(f"O valor do produto recebido do Sul é R$ {preco4:9.2f}")
elif origem == 5:
    preco5 = preco * 1.18
    print(f"O valor do produto recebido do Sudeste é R$ {preco5:9.2f}")

else:
    print("Esta opção não é válida!")
