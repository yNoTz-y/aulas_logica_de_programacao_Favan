lim = int(input("Digite um número: "))

n1 = 1
n2 =1
print(n1)
print (n2)
if lim <=2:
    print("O número deve ser maior que 2")
else:
    for i in range(3, lim + 1):
        resultado = n1 + n2
        print(resultado)
        n1 = n2
        n2 = resultado