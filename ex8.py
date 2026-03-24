salario = int(input("Digite o salário: "))
aumento = int(input("Digite o aumento em porcentagem: "))
aumento_calculado = salario * (aumento / 100)
salario_final = salario + aumento_calculado
print(f"O salário final após o aumento é: {salario_final}")