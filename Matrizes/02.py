# Faça uma função que receba por parâmetro, uma matriz B(9,9) de reais e retorna a soma dos elementos das linhas pares de B.

"""
  Faça um procedimento que receba uma matriz A(10,10), por parâmetro, e realize as seguintes trocas:
a) a linha 2 com a linha 8;
b) a coluna 4 com a coluna 10;
c) a diagonal principal com a secundária;
d) a linha 5 com a coluna 10;
e) O procedimento deve retornar a matriz alterada.
"""

import random

def linha2para8(a: list):
  linha2 = []
  linha8 = []

  for i in range(10):
    linha2.append(a[1][i])
    linha8.append(a[7][i])

  for i in range(10):
    a[1][i] = linha8[i]
    a[7][i] = linha2[i]
  
  return a

def mudarDuasColunas(a: list, c1: int, c2: int):
  colx = []
  coly = []

  for i in range(10):
    colx.append(a[i][c1 - 1])
    coly.append(a[i][c2 - 1])

  for i in range(10):
    a[i][c1 - 1] = colx[i]
    a[i][c2 - 1] = coly[i]
  
  return a

def alterarMatriz(a: list):
  #a = linha2para8(a)
  a = mudarDuasColunas(a, 4, 10)
  #a = mudarDuasColunas(a, 5, 10)
  return a

def printarMatrizLinhas(matriz):
  for i in range(len(matriz)):
    print(matriz[i])

matrizA = [0] * 10

for i in range(10):
    matrizA[i] = [0] * 10

for i in range(10):
  for j in range(10):
    matrizA[i][j] = random.randint(0, 20)

printarMatrizLinhas(matrizA)
matrizA = alterarMatriz(matrizA)
print('')
printarMatrizLinhas(matrizA)