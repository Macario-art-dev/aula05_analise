print("Menu: ")
print("1 - par ou ímpar")
print("2 - COMPARE O NUMERO")
print("3 - CALCULE O DOBRO")
resposta = "sim"
while resposta == "sim":
    opcao = int(input("escolha uma opção: "))
    match opcao:
        case 1:
            print("par ou impar")
            numero = int(input("numero: "))
            if numero %2 == 0:
                print("par")
            else:
                print(f"{numero} é ímpar")
        case 2:
            print("Comparar os números")
            n1 = int(input("1º Número: "))
            n2 = int(input("2º Número: "))
            if n1 > n2:
                print(f"{n1} é maior que {n2}")
            elif n1<n2:
                print(f"{n1} é menor que {n2}")
            else:
                print(f"{n1} é igual a {n2}")
        case 3:
            print("Dobro")
            num = int(input("Escolha um número: "))
            dobro = num * 2
            print(f"O dobro de {num} é {dobro}")
        case _: 
            print("Dobro ínvalido")
    resposta = input("Deseja continuar? (sim ou não)")
    if resposta != "sim":
        print("programa encerrado")
        break    
