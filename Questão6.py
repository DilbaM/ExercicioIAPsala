salario=int (input("Qual o seu salario?"))

if salario > 1500:
    print(f"seu salario foi de {salario} para {salario*10/100+salario}")
else:
    print(f"Seu salário foi de {salario} para {salario*15/100+salario}")