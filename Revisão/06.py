# 6.Crie um função que receba dois arrays de números inteiros como parâmetros e retorne um novo array que seja a concatenação deles. Exemplo de entrada:[1,2,3,4,5], [6,7,8,9,10]Saída: [1,2,3,4,5,6,7,8,9,10]

def concatenarArray(a1: list, a2: list):
  concatenacao = []
  for i in range(len(a1)):
    concatenacao.append(a1[i])
  for i in range(len(a2)):
    concatenacao.append(a2[i])

  print(concatenacao)

a = [1,2,3,4,5]
b = [6,7,8,9,10]
concatenarArray(a, b)