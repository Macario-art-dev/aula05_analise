for i in range(1,6):
    nome = input(f"{i}º Nome: ")
    p1= float(input("prova01:" ))
    p2=float(input("prova02:" ))
    p3=float(input("prova03:" ))
    md = (p1+p2+p3)/3
    if md >=7:
        sit = "ap"
    elif md >=6:
        sit = "rec"
    else:
        sit = "rp"
    print("n\----Resultado----")
    print(f"Aluno: {i}")        
    print(f"Nome: {nome}")        
    print(f"Prova1: {p1}")        
    print(f"Prova2: {p2}")        
    print(f"Prova3: {p3}")        
    print(f"Média: {md}")        
    print(f"Situação: {sit}")        
        