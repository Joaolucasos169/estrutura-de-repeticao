# Seu programa deverá conter o seguinte menu:

# Charada 1
# Charada 2
# Charada 3
# Desistir

# Cada opção deverá exibir uma pergunta para o usuário que deverá responder com um palpite. 
# Em caso de acerto o programa deverá parabenizar o usuário e retornar ao menu principal, o usuário só poderá errar 3 vezes.

# Exemplo:
# 1. Usuário seleciona opção "Charada 1"
# 2. O programa imprime "O que é o qué é, quanto mais se tira mais se aumenta?"
# 3. O usuário deve tentar responder a pergunta
# 4. Se acertar a resposta ele é parabenizado
# 5. "Parabéns a resposta correta é 'buraco'!"
erros = 0

while True:
    print('''Escolha uma charada: 
   Charada: 1
   Charada: 2
   Charada: 3
   Desistir: 0
    ''')
    
    charada = input("Escolha uma opção: ")
    
    if (charada == "1"):
        while True:
            print("O que é o qué é, quanto mais se tira mais se aumenta? ")
            resposta = input("Qual é a resposta? ")
            if resposta == "buraco":
                print("Você acertou, Parabéns!")
                break
            else:
                print("Você errou!")
                erros += 1
                if erros == 3:
                    break
                
    elif (charada == "2"):
        while True:
            print("O que é que tem cabeça, mas não tem cabelo? ")
            resposta = input("Qual é a resposta? ")
            if resposta == "dedo":
                print("Você acertou, Parabéns!")
                break
            else:
                print("Você errou!")
                erros += 1
                if erros == 3:
                    break
         
    elif (charada == "3"):
        while True:
            print("O que é o que é, cai em pé e corre deitado")
            resposta = input("Qual é a resposta? ")
            if resposta == "chuva":
                print("Você acertou, Parabéns!")
                break
            else:
                print("Você errou!")
                erros += 1
                if erros == 3:
                    break
            
    elif (charada == "0"):
        print("Você desistiu!")
        break
    
    else:
        print("Opção invalida!")
        
    if (erros == 3):
        print("Você esgotou todas as suas tentativas!")
        break