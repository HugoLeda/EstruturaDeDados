import random

class Nodo:
  def __init__(self, valor):
    self.rubro = False
    self.pai = None
    self.valor = valor
    self.esquerda = None
    self.direita = None

class ArvoreRN:
  def __init__(self):
    self.nil = Nodo(0)
    self.nil.rubro = False
    self.nil.esquerda = None
    self.nil.direita = None
    self.raiz = self.nil

  # método de inserção de pesquisa binária comum
  def inserir(self, valor):
    novoNodo = Nodo(valor)
    novoNodo.pai = None
    novoNodo.esquerda = self.nil
    novoNodo.direita = self.nil
    novoNodo.rubro = True # novo nodo deve ser rubro

    pai = None
    atual = self.raiz

    while (atual != self.nil):
      pai = atual

      if (novoNodo.valor < atual.valor):
        atual = atual.esquerda
      elif (novoNodo.valor > atual.valor):
        atual = atual.direita
      else:
        return
    
    # definir pai e inserir nodo
    novoNodo.pai = pai
    if (pai == None):
      self.raiz = novoNodo
    elif (novoNodo.valor < pai.valor):
      pai.esquerda = novoNodo
    else:
      pai.direita = novoNodo
    
    #fixar na árvore
    self.fixInsert(novoNodo)

  def fixInsert(self, novoNodo: Nodo):
    while (novoNodo != self.raiz and novoNodo.pai.rubro):
      if (novoNodo.pai == novoNodo.pai.pai.direita):
        t = novoNodo.pai.pai.esquerda # tio

        if (t.rubro):
          t.rubro = False
          novoNodo.pai.rubro = False
          novoNodo.pai.pai.rubro = False
          novoNodo = novoNodo.pai.pai
        else:
          if (novoNodo == novoNodo.pai.esquerda):
            novoNodo = novoNodo.pai
            self.girarEsquerda(novoNodo)
          
          novoNodo.pai.rubro = False
          novoNodo.pai.pai.rubro = True
          self.girarDireita(novoNodo.pai.pai)
    self.raiz.rubro = False

  def exists(self, valor):
    atual = self.raiz

    while (atual != self.nil and valor != atual.valor):
      if (valor < atual.valor):
        atual = atual.left
      else:
        atual = atual.direita
    
    return atual

  # girar para a esquerda a partir do nodo X
  def girarEsquerda(self, x: Nodo):
    y = x.direita
    x.direita = y.esquerda

    if (y.esquerda != self.nil):
      y.esquerda.pai = x

    y.pai = x.pai

    if (x.pai == None):
      self.raiz = y
    elif (x == x.pai.esquerda):
      x.pai.esquerda = y
    else:
      x.pai.direita = y
    
    y.esquerda = x
    x.pai = y

  # girar para a direita a partir do nodo X
  def girarDireita(self, x):
    y = x.esquerda
    x.esquerda = y.direita

    if (y.direita != self.nil):
      y.direita.pai = x

    y.pai = x.pai

    if (x.pai == None):
      self.raiz = y
    elif (x == x.pai.direita):
      x.pai.direita = y
    else:
      x.pai.esquerda = y

    y.direita = x
    x.pai = y


def print_tree(node, lines, level=0):
  if node.val != 0:
    print_tree(node.left, lines, level + 1)
    lines.append('-' * 4 * level + '> ' + str(node.val) + ' ' + ('r' if node.red else 'b'))
    print_tree(node.right, lines, level + 1)

def get_nums(num):
  random.seed(1)
  nums = []
  for _ in range(num):
    nums.append(random.randint(1, num-1))
  return nums

def main():
  tree = ArvoreRN()
  for x in range(1, 51):
    tree.inserir(x)
  print(tree)


main()