dia_nascimento = int(input("Entre com o dia de seu nascimento(dd): "))
mes_nascimento = int(input("Entre com o mês de seu nascimento(mm): "))
ano_nascimento = int(input("Entre com o ano de seu nascimento(aaaa): "))
dia_atual = int(input("Entre com a dia de hoje(dd): "))
mes_atual = int(input("Entre com o mês de hoje(mm): " ))
ano_atual = int(input("Entre com o ano de hoje(aaaa): " ))
idade_ano = ano_atual - ano_nascimento - 1
idade_meses = 12 - mes_nascimento - mes_atual + 12
idade_dias = idade_ano * 365
idade_semanas = idade_ano * 53
print("Sua idade é", idade_ano, "anos")
print("Sua idade em meses é", idade_meses, "meses")
print("Sua idade em dias é", idade_dias, "dias")
print("Sua idade em samanas é", idade_semanas, "semanas")