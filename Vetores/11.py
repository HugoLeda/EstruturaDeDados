# Escrever um algoritmo que lê um vetor X(20) e o escreve. Escreva, a seguir, cada um dos valores distintos que aparecem em X dizendo quantas vezes cada valor aparece em X.

def ocorrencias(v: list):
  vldistintos = []

  for i in v:
    if (not i in vldistintos):
      vldistintos.append(i)
    
  qtd = [0] * len(vldistintos)
  
  for i in range(len(vldistintos)):
    for j in v:
      if (vldistintos[i] == j):
        qtd[i] = qtd[i] + 1

  return {'Elementos distintos que apareceram': vldistintos, 'Quantidade de vezes que apareceram': qtd}


def lerVetor(p: int):
  res = []
  for i in range(p):
    n = int(input('Digite um número: '))
    res.append(n)
  return res

vetor = lerVetor(5)
res = ocorrencias(vetor)
print(res)