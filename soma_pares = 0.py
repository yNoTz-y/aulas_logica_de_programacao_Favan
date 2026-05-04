soma_pares = 0
soma_impares = 0
for i in range(1,101,1):
    if i % 2 == 0:
     soma_pares = soma_pares + i
else:
     soma_impares = soma_impares + i
    
print("a soma de numeros pares de 1 a 100 é: ",soma_pares)
print("a soma de numeros impares de 1 a 100 é: ",soma_impares)

    