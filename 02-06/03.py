def g4(matriz):
  controle = False
  zeros = 0
  for i in matriz:            
    for j in i:
      zerosLista = 0
      if (j == 0):
        zerosLista += 1
      if (zerosLista > len(i)):
        zeros += 1
  if (zeros >= len(i)):
    controle = True
  return controle