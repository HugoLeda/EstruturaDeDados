"""
  Faça um procedimento que receba uma matriz A(10,10), por parâmetro, e realize as seguintes trocas:
a) a linha 2 com a linha 8;
b) a coluna 4 com a coluna 10;
c) a diagonal principal com a secundária;
d) a linha 5 com a coluna 10;
e) O procedimento deve retornar a matriz alterada.
"""

import random

def alterarMatriz(a: list):
  linha2 = []
  linha8 = []
  for i in range(10):
    linha2.append(a[1][i])
    linha8.append(a[7][i])
  for i in range(10):
    a[1][i] = linha8[i]
    a[7][i] = linha2[i]

a = [0] * 10
for i in a:
  a.append([0] * 10)

print(a)