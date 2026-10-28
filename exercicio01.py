print("operaão entre dois números inteiros")
num = float(input("Digite um algoritimo inteiro: "))
num2 = float(input("Digite um algoritimo inteiro: "))
operacao = input("digite uma das operações (+, -, *, :): ")
match operacao: 
    case "+":
        resultado = num + num2
        print(f"resultado: {resultado}")
    case "-":
        resultado = num - num2
        print(f"resultado: {resultado}")
    case "x":
        resultado = num*num2
        print(f"resultado: {resultado}")
    case ":":
        if num2 !=0:
                resultado = num/num2
                print(f"resultado: {resultado}")
        else:
            print("Erro: divisão por zero não é permitida")
    case _:
        print(("operação inválida"))
while       
    
       