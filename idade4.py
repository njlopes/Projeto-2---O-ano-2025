print("Em que ano você nasceu?")
nascimento = input()
nascimento = int(nascimento)
print("Para qual ano você quer saber sua idade?")
idade = input()
idade = int(idade)
idadeEm = idade - nascimento
print("No ano", idade, "você terá", idade - nascimento, "anos!")      
