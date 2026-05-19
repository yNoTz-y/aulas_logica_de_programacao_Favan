# Importa o módulo 'random', que possui funções para gerar números aleatórios
import random

# Inicializa uma lista vazia chamada 'm1', que será a nossa matriz 3x3
m1 = []

# Loop externo: vai rodar 3 vezes (com 'i' valendo 0, 1 e 2), representando as LINHAS da matriz
for i in range(3):
    
    # Cria uma linha com três zeros [0, 0, 0] e a adiciona (append) à lista 'm1'
    m1.append([0] * 3)
    
    # Loop interno: vai rodar 3 vezes (com 'j' valendo 0, 1 e 2), representando as COLUNAS da matriz
    for j in range(3):
        
        # Substitui o zero da posição atual [linha i][coluna j] por um número inteiro aleatório entre 1 e 50
        m1[i][j] = random.randint(1, 50)

# Imprime a matriz completa no console (uma lista de listas) após preencher todos os valores
print(m1)

# Calcula a soma dos elementos onde o índice da linha é igual ao da coluna: [0][0], [1][1] e [2][2]
# Isso utiliza uma "list comprehension" para extrair esses valores e a função sum() para somá-los
sum_diagonal = sum(m1[i][i] for i in range(3))

# Imprime o resultado final da soma da diagonal principal usando uma f-string para formatar o texto
print(f"Soma da diagonal principal: {sum_diagonal}")

# Calcula a soma dos elementos da diagonal secundária: [0][2], [1][1] e [2][0]
sum_secondary_diagonal = sum(m1[i][2-i] for i in range(3))
# Calcula o determinante de uma matriz 3x3 usando a regra de Sarrus
determinant = (m1[0][0] * m1[1][1] * m1[2][2] + 
               m1[0][1] * m1[1][2] * m1[2][0] + 
               m1[0][2] * m1[1][0] * m1[2][1] - 
               m1[0][2] * m1[1][1] * m1[2][0] - 
               m1[0][0] * m1[1][2] * m1[2][1] - 
               m1[0][1] * m1[1][0] * m1[2][2])

print(f"Determinante da matriz: {determinant}")
# Imprime o resultado da soma da diagonal secundária
print(f"Soma da diagonal secundária: {sum_secondary_diagonal}")