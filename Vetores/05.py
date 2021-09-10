# Escreva um algoritmo que leia um vetor de 10 posições e mostre-o ordenado em ordem crescenteutilizando o método SelectionSort. Escreva a quantidade de comparações que foram realizadas.

def selectionSort(v: list):
  comp = 0  

  for i in range(0, len(v)):
    menor = i

    for elDireita in range((i + 1), len(v)):
      if (v[elDireita] < v[menor]):
        comp += 1
        menor = elDireita        

    v[i], v[menor] = v[menor], v[i]
  
  return {'vetor ordenado': v, 'quantidade de comparações': comp}

def lerVetor(p: int):
  res = []
  for i in range(p):
    n = float(input('Digite um número: '))
    res.append(n)
  return res

vetor = lerVetor(10)
res = selectionSort(vetor)
print(res)