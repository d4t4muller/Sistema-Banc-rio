menu = """

Bem vindo ao MyBank >> Seu banco de confiança <<

Para prosseguir escolha sua melhor opção: 

[S]acar
[D]epositar
[E]xtrato
[Q]uit


"""
saldo = 0
limite = 500
extrato = ""
numero_de_saque = 0

LIMITE_DIARIO = 3


while True:
    opcao = input(menu)


    if opcao == "D":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo+= valor 
            extrato += f"Depósito : R$ {valor:.2f}\n"

        else:
            print("Operação falhou ! O valor informado é inválido.")

    elif opcao == "S":
        valor = float(input("Informe o valor so saque :  "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite 

        excedeu_saque = numero_de_saque >= LIMITE_DIARIO

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente. ")

        elif excedeu_limite:
            print("Limite de operações diarias realizadas, por favor volte amanhã")

        elif excedeu_saque:
            print("MyBank agradece pelo entusiamo mas o limite diario é de R$ 500,00")

        elif valor > 0:
            saldo -=valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saque += 1

        else:
            print("Valor informado inválido, refaça a operação")

    elif opcao == "E":
        print("\n===================== EXTRATO ====================")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("==================================================")

    elif opcao == "Q":
        print("o MyBank agradeçe pela sua confiança !")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
