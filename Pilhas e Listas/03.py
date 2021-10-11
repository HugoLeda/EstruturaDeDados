# Escreva um programa que utilizando uma pilha determina se uma string é um palíndromo ou não, isto é, se pode ser lida da mesma maneira para frente ou para trás.

def inverterPilha(pilha: list):
  global topo
  topoAux = 0
  pilhaAux = []

  for i in range(len(pilha)):
    aux = pilha[topo - 1]
    pilha.pop(topo - 1)
    topo -= 1    

    pilhaAux.append(aux)
    topoAux += 1
  
  return pilhaAux

def pilhasIguais(pilha1: list, pilha2: list):
  res = True

  if (len(pilha1) == len(pilha2)):
    for i in range(len(pilha1)):
      if (pilha1[i] != pilha2[i]):
        res = False
  else:
    res = False

  return res

palavra = input('Escreva uma palavra: ')

pilha = []
topo = 0

for i in range(len(palavra)):
  pilha.append(palavra[i])
  topo += 1

pilha = inverterPilha(pilha)
palavra = list(palavra)

if (pilhasIguais(palavra, pilha)):
  print('A palavra digitada é um palídrono!')
else:
  print('A palavra digitada não é um palídrono!')