# Escreva um algoritmo que leia um vetor de 10 posições e mostre-o ordenado em ordem crescente utilizando o método BubleSort. Escreva a quantidade de comparações que foram realizadas.

def ordenarVetor(v: list):
  comp = 0
  for n in range(len(v) - 1, 0, -1):
    for i in range(n):
      if (v[i] > v[i + 1]):
        comp += 1
        temp = v[i]
        v[i] = v[i + 1]
        v[i + 1] = temp
  return {'vetor ordenado': v, 'quantidade de comparações': comp}

def lerVetor(p: int):
  res = []
  for i in range(p):
    n = float(input('Digite um número: '))
    res.append(n)
  return res

vetor = lerVetor(5)
res = ordenarVetor(vetor)
print(res)