# Seu programa deverá pedir dois números float e exibir um menu com as opções disponíveis, exemplo:

# Soma +
# Subtração
# Divisão
# Multiplicação
# Sair

# Ao escolher uma das opções o programa irá executar a operação desejada e exibir o resultado na tela. 
#O programa deverá executar ATÉ QUE a pessoa escolha a opção 0. Sair.
# Não permita divisões por 0. 

while True:
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    operacao = input('''Escolha a operação: 
    Soma: +
    Subtração: -
    Divisão: /
    Multiplicação: *
    sair: 0
    ''')
    if (operacao == "+"):
        soma = num1 + num2
        print(f"O resultado da sua soma é: {soma}")
        
    elif (operacao == "-"):
        subtracao = num1 - num2
        print(f"O resultado da sua subtração é: {subtracao}")

    elif (operacao == "/"):
        if (num2 == 0):
            print("Erro! divisão por 0 não permitida.")
        else:
            divisao = num1 / num2
            print(f"O resultado da sua divisão é: {divisao}")

    elif (operacao == "*"):
        multiplicacao = num1 * num2
        print(f"O resultado da sua multiplicação é: {multiplicacao}")
        
    elif (operacao == "0"):
        print(f"Saindo...")
        break
    else:
        print("Digite uma opção valida!")

