# Escreva um algoritmo que leia um vetor de 80 elementos inteiros. Encontre e mostre o menor elemento e sua posição no vetor.

def menorElemento(v: list):
  menor = v[0]
  index = 0

  for i in range(len(v)):
    if (v[i] < menor):
      menor = v[i]
      index = i

  return {'elemento': menor, 'posição': index}

def lerVetor(p: int):
  res = []
  for i in range(p):
    n = int(input('Digite um número: '))
    res.append(n)
  return res

vetor = lerVetor(10)
res = menorElemento(vetor)
print(res)