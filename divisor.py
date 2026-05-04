num_inicio = int(input("digite o inicio do intervalo: "))
num_fim = int(input("digite o final do intervalo: "))
divisor = int(input("digite o numero do divisor: "))
if num_inicio <= num_fim:
  for i in range (num_inicio, num_fim+ 1):
    if i % divisor == 0:
       print(i, end=" ")
else:
    print("lista invalida") 
        