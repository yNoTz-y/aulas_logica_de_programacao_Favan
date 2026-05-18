import random

vetor = [random.randint(1,50) for _ in range(20)]

num = int(input("digite o numero divisor: "))

numeros = []
divisores = []
for v in vetor:
    if v % num == 0:
        divisores.append(v)
    else:
        numeros.append(v)

print("Vetor:", vetor)
print("Divisíveis por", num, ":", divisores)
print("Não divisíveis por", num, ":", numeros)
    
    