# 8.Crie um funçãoque receba dois arrays de números inteiros como parâmetros e retorne um novo array que contenha apenas os elementos que sejam comuns aos dois arrays (ou seja, aintersecçãodos arrays).Exemplo de entrada:[1,2,3,4,5], [1,2,9,5,10]Saída: [1,2,5]

def concatenarArray(a1: list, a2: list):
  concatenacao = []
  for i in range(len(a1)):    
    for j in range(len(a2)):
      if (a1[i] == a2[j]):
        concatenacao.append(a1[i])

  print(concatenacao)

a = [1,2,3,4,5,6, 7]
b = [6,7,8,9,10]
concatenarArray(a, b)