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

  for i in range(len(a)):
    colx.append(a[i][c1 - 1])
    coly.append(a[i][c2 - 1])

  for i in range(len(a)):
    a[i][c1 - 1] = colx[i]
    a[i][c2 - 1] = coly[i]
  
  return a

def inverterDiagonais(a: list):
  principal = []
  secundaria = []

  for i in range(len(a)):
    for j in range(len(a)):
      if (i == j):
        principal.append(a[i][j])        

  condicao = True
  co = 0
  while(condicao == True):
    secundaria.append(a[co][(len(a) -1) - co])
    a[co][(len(a) -1) - co] = principal[len(principal) - 1]
    co = co + 1
    if (co == (len(a))):
      condicao = False

  for i in range(len(a)):
    for j in range(len(a)):
      if (i == j):
        a[i][j] = secundaria[i]
  
  return a

def alterarMatriz(a: list):
  a = linha2para8(a)
  a = mudarDuasColunas(a, 4, 10)
  a = inverterDiagonais(a)
  a = mudarDuasColunas(a, 5, 10)

  return a

def printarMatrizLinhas(matriz: list):
  for i in range(len(matriz)):
    print(matriz[i])

matrizA = [random.randint(0, 100)] * 10

for i in range(10):
    matrizA[i] = [random.randint(0, 100)] * 10

matrizA = alterarMatriz(matrizA)
printarMatrizLinhas(matrizA)