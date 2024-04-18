# SISTEMA BANCÁRIO COM AS OPERAÇÕES: SACAR, DEPOSITAR, E VISUALIZAR EXTRATO #

main = """
       
BEM VINDO AO SISTEMA AQUINOX
       
    Operações disponíveis:
    
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair     
   
Digite a operação deseja: """

LIMITE_VALOR_SAQUE = 500
LIMITE_SAQUE = 3
numero_saque = 0
saldo_conta = 0
extrato = ""

while True:
    
    option = input(main)

    if option == "1":
        valor_depositado = float(input("Informe o valor para depósito: "))
        if valor_depositado > 0:
            print (f"Valor depositado com sucesso: R${valor_depositado:.2f}")
            saldo_conta += valor_depositado
            extrato += f"Depósito: R${valor_depositado:.2f}\n"
        else:
            print ("Valor inválido, refaça a operação e informe um número positivo!")
        
    elif option == "2":
        if numero_saque < LIMITE_SAQUE:
            valor_saque = float(input("Informe o valor para saque: "))
            if valor_saque > 0 and valor_saque <= saldo_conta and valor_saque <= 500:
                print ("O saque foi realizado com sucesso :)")
                saldo_conta -= valor_saque
                numero_saque += 1
                extrato += f"Saque: R${valor_saque:.2f}\n"
            elif valor_saque > saldo_conta:
                print ("Operação inválida: Saldo insuficiente para saque!")
            elif valor_saque > LIMITE_VALOR_SAQUE:
                print ("Operação inválida: Valor de saque excedido!")
        else:
            print ("Operação inválida: Limite diário de saques excedido!")
            
    elif option == "3":
        print ("\n============== EXTRATO ==============")
        print ("Não foram realizados transações." if not extrato else extrato)
        print (f"\nSaldo: R$ {saldo_conta:.2f}")
        print ("=====================================")
            
    elif option == "0":
        break
    
    else:
        print ("Operação inválida! Por favor, selecione novamente a operação desejada.")