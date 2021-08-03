# 9.Crie  um funçãoque  receba  dois  arrays  de  números  inteiros  como  parâmetros  e  retorne  um novo  array  que  contenha  auniãodos  elementos  dos  dois  arrays  (eliminando-se  os  elementos repetidos).Exemplo de entrada:[1,2,3,4,5], [4,5,6,7,8]Saída: [1,2,3,4,5,6,7,8]

def concatenarArray(a1: list, a2: list):
  concatenacao = []
  for i in range(len(a1)):
    if (a1[i] not in concatenacao):
      concatenacao.append(a1[i])
  for i in range(len(a2)):
    if (a2[i] not in concatenacao):
      concatenacao.append(a2[i])

  print(concatenacao)

a = [1,2,3,4,5,6, 7]
b = [6,7,8,9,10]
concatenarArray(a, b)
