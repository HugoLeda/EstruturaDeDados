""""
1) Implemente uma aplicação que dada uma Pilha implemente funções para:
a) retornar o número de elementos empilhados
b) excluir todos os elementos da pilha
c) inserir elementos na pilha
d) retirar elementos da pilha
e) retorna o elemento que está no topo da pilha
f) alterar elemento que está no topo da pilha
g) verifica se a pilha está vazia
"""

def elEmpilhados(pilha: list):
  global topo
  return topo

def esvaziarPilha(pilha: list):
  global topo
  
  while (topo > 0):
    pilha.remove(pilha[topo-1])
    topo -=1

  return pilha
  
def inserirElPilha(vlr: int, pilha: list):
  global topo

  if (topo >= max):
    return {"ERRO":'A pilha já está cheia!'}
  else:
    pilha.append(vlr)
    topo += 1

  return pilha

def removerElPilha(pilha: list):
  global topo
  
  if (topo >= 1):
    pilha.remove(pilha[topo - 1])
  
  return pilha

def elTopoPilha(pilha: list):
  global topo

  if (topo < 1):
    return {"ERRO": 'Pilha vazia!'}
  else:
    return pilha[topo - 1]

def alterarElTopoPilha(vlr: int, pilha: list):

  pilha = removerElPilha(pilha)
  pilha = inserirElPilha(vlr, pilha)

  return pilha

def pilhaVazia(pilha: list):
  global topo
  
  if (topo == 0):
    return 'A pilha está vazia'
  else:
    return 'A pilha não está vazia'

topo = 0
pilha = []
max = int(input('Digite o tamanho máximo da pilha: '))

menu = "1 - retornar o número de elementos empilhados \n2 - excluir todos os elementos da pilha \n3 - inserir elementos na pilha \n4 - retirar elementos da pilha\n5 - retorna o elemento que está no topo da pilha \n6 - alterar elemento que está no topo da pilha \n7 - verifica se a pilha está vazia\n8 - Encerrar o programa"

executar = True

while (executar == True):
  print(f'Pilha atual: {pilha}')
  print(f'\n***  Menu ***')
  print(menu)
  opcao = int(input('Digite uma opção: '))

  if (opcao == 1):
    print(elEmpilhados(pilha))
  elif (opcao == 2):
    pilha = esvaziarPilha(pilha)
  elif (opcao == 3):
    n = int(input('Digite um valor para ser inserido: '))
    pilha = inserirElPilha(n, pilha)
  elif (opcao == 4):
    pilha = removerElPilha(pilha)
  elif (opcao == 5):
    print(elTopoPilha(pilha))
  elif (opcao == 6):
    n = int(input('Elemento que deseja colocar no topo: '))
    pilha = alterarElTopoPilha(n, pilha)
  elif (opcao == 7):
    print(pilhaVazia(pilha))
  elif (opcao == 8):
    executar = False