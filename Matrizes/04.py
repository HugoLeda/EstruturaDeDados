#  Faça um procedimento que receba por parâmetro, uma matriz A(6,6) e multiplica cada linha pelo elemento da diagonal principal daquela linha. O procedimento deve retornar a matriz alterada.

import random

def manipularMatriz(a: list):
  for i in range(len(a)):
    elementoDiagonal = a[i][i]
    for j in range(len(a)):
      resultado = a[i][j] * elementoDiagonal
      a[i][j] = resultado
  return a

def printarMatrizLinhas(matriz):
  for i in range(len(matriz)):
    print(matriz[i])
  print('\n')

a = [0] * 6

for i in range(len(a)):
  a[i] = [random.randint(0, 10)] * 6


printarMatrizLinhas(a)
a = manipularMatriz(a)
printarMatrizLinhas(a)