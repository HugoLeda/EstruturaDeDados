# Dada uma pilha S inverta a ordem de seus elementos usando Pilhas. Ex. [3,7,5,2] ➔ [2,5,7,3]

pilha = []
topo = 0
max = int(input('Digite o tamanho máximo para pilha: '))

def inverterPilha(pilha: list):
  global topo
  topoAux = 0
  pilhaAux = []

  for i in range(len(pilha)):
    aux = pilha[topo - 1]

    pilha.remove(pilha[topo - 1])
    topo -= 1

    pilhaAux.append(aux)
    topoAux += 1

  return pilhaAux

continuar = True

while(continuar == True and topo < max ):
  n = int(input('Digite um valor para empilhar: '))
  pilha.append(n)
  topo += 1

pilha = inverterPilha(pilha)
print(pilha)