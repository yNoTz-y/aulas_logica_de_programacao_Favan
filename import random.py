import random
while True:
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    resultado = n1 * n2
    print(f"quanto e {n1} vezes {n2}:")
    resposta = int(input("qual sera o resultado:"))
    if resposta == n1 * n2:
        print("ACERTOU!")
    else:
        print("errou")
    continuar = str(input("vc deseja continuar jogando(S/N) \n"))
    if continuar != 'S' != 's':
        break   