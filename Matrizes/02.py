# Faça uma função que receba por parâmetro, uma matriz B(9,9) de reais e retorna a soma dos elementos das linhas pares de B.

import random

def somarLinhasPares(b: list):
  soma = 0
  for i in range(9):
    if (((i + 1) % 2) == 0):
      for j in range(9):
        soma += b[i][j]  
  return soma

matrizB = [0] * 9

for i in range(9):
    matrizB[i] = [random.randint(0, 100)] * 9

def printarMatrizLinhas(matriz):
  for i in range(len(matriz)):
    print(matriz[i])

somaLinhas = somarLinhasPares(matrizB)
printarMatrizLinhas(matrizB)
print(f'Soma das linhas pares: {somaLinhas}')