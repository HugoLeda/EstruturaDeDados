# Faça uma função que receba por parâmetro, uma matriz A(12,12) e retorne um vetor com a soma de cada uma das linhas de A.

import random

def somarLinhas(a: list):
  soma = [0] * len(a)
  somalinha = 0
  
  for i in range(len(a)):
    somalinha = 0
    for j in range(len(a[i])):
      somalinha += a[i][j]
    soma[i] = somalinha
  
  return soma

a = [0] * 5

for i in range(len(a)):
  a[i] = [random.randint(0, 100)] * 12

somaDasLinhas = somarLinhas(a)
print(somaDasLinhas)