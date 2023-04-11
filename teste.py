salario=float (input("Qual o seu salario?"))
resultado1=float(salario*1.1)
resultado2=float(salario*1.15)
if salario > 1500:
    print(f"seu salario foi de {salario} para {resultado1}")
else:
    print(f"Seu salário foi de {salario} para {resultado2}")