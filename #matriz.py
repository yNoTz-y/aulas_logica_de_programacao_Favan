#matriz
m = [[1,2,3],[4,5,6]]
#print(m) #imprime a matriz
#print(m[1][2])#acessar o elemento 
m1 = [0]*3 #cria uma matriz 3x3
for i in range(3):
    m1[i] = [0]* 3 #preenche a matriz com zeros
print(m1)

import random
m2 = [[10,20,30]], [[40,50,60]]
for i in range(2):
    for j in range (3):
        m2[i][j] = random.randint(1,100) #preenche a matriz com numeros aleatorios
        print(m2)