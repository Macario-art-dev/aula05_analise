print("\ndigite cinco nomes e suas idade")
for i in range(1,6):
    nome  = input(f"{i}º Nome: ")
    idade = int(input(f"{i}ª Idade: "))
    print(f"{i}º nome: {nome}")
    print(f"{i}º Idade: {idade}")
    print("\n")
print("\nFim do Programa")