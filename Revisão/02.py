# 2.Implemente um algoritmo que exiba a soma de todos os números primos de 1 a 400;

import numpy as np

primos = [2]

def primo(i: int):

  res = False

  for x in range(i + 1):
    if ((x != 1) and (x != i) and (x != 0)):
      resto = i % x      
      if (resto != 0):
        res = True
      else:        
        return False

  return res

for i in range(401):
  if (primo(i)):
    primos.append(i)
  

soma = np.sum(primos)
print(soma)