def g3(matriz):
  controle = False
  for i in matriz:
    pares = 0
    impares = 0
    for j in i:
      if ((j % 2) == 0):
        pares += 1
      else:
        impares += 1
    if (pares > impares):
      controle = True
  return controle    
  