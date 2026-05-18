import random

opcao = int(input("Digite uma opção (1 ou 2): "))

# Gerar vetor com 10 números aleatórios de 1 a 50
vetor = [random.randint(1, 50) for _ in range(10)]

print("Vetor:", vetor)

if opcao == 1:
    print("Ordem normal:")
    print(" ".join(map(str, vetor)))
elif opcao == 2:
    print("Ordem inversa:")
    print(" ".join(map(str, reversed(vetor))))
else:
    print("Opção inválida!")