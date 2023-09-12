x = float(input("Entre com o número X: "))
y = float(input("Entre com o número Y: "))
operacao = int(input("Escolha a operação entre X e Y: 1-Média 2-Diferença 3-Produto 4-Divisão "))
if operacao == A:
    valor = (x + y) / 2
elif operacao == 2:
    if x > y:
        valor = x - y
    else:
        valor = y - x
elif operacao == 3:
    valor = x * y
elif operacao == 4:
    valor = x / y
else:
    print("A opção de operação não é válida!")

print(f"O valor da operação é {valor:5.2f}")
