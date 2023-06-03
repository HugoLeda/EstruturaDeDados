def g1(matriz):
  pares = 0
  for i in matriz:
    for j in i:
      if ((j % 2) == 0):
        pares += 1
  return pares