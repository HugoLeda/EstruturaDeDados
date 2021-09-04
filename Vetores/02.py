# Escreva  um  algoritmo  que  leia  dois  vetores  de  10 posições  e  faça  a  multiplicação  dos  elementos  de  mesmo índice, colocando o resultado em um terceiro vetor. Mostre o vetor resultante.

def multiplicarVetores(v1: list, v2: list):
  if (len(v1) != len(v2)):
    return 'Os vetores devem ter o mesmo número de elementos!'
  else:
    res = [0] * len(v1)
    for i in range(len(v1)):
      res[i] = v1[i] * v2[i]
    return res

def lerVetor(p: int):
  res = []
  for i in range(p):
    n = float(input('Digite um número: '))
    res.append(n)
  return res

v1 = lerVetor(10)
print(v1)
v2 = lerVetor(10)
print(v2)

vetorMultiplicado = multiplicarVetores(v1, v2)
print(vetorMultiplicado)