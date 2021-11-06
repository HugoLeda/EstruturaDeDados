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

    def insert(self, valor):
        # Ordinary Binary Search Insertion
        novoNodo = Nodo(valor)
        novoNodo.pai = None
        novoNodo.esquerda = self.nil
        novoNodo.direita = self.nil
        novoNodo.rubro = True  # new node must be rubro

        pai = None
        atual = self.raiz
        while atual != self.nil:
            pai = atual
            if novoNodo.valor < atual.valor:
                atual = atual.esquerda
            elif novoNodo.valor > atual.valor:
                atual = atual.direita
            else:
                return

        # Set the pai and insert the new node
        novoNodo.pai = pai
        if pai == None:
            self.raiz = novoNodo
        elif novoNodo.valor < pai.valor:
            pai.esquerda = novoNodo
        else:
            pai.direita = novoNodo

        # Fix the tree
        self.fix_insert(novoNodo)

    def fix_insert(self, novoNodo):
        while novoNodo != self.raiz and novoNodo.pai.rubro:
            if novoNodo.pai == novoNodo.pai.pai.direita:
                u = novoNodo.pai.pai.esquerda  # uncle
                if u.rubro:
                    u.rubro = False
                    novoNodo.pai.rubro = False
                    novoNodo.pai.pai.rubro = True
                    novoNodo = novoNodo.pai.pai
                else:
                    if novoNodo == novoNodo.pai.esquerda:
                        novoNodo = novoNodo.pai
                        self.rotate_direita(novoNodo)
                    novoNodo.pai.rubro = False
                    novoNodo.pai.pai.rubro = True
                    self.rotate_esquerda(novoNodo.pai.pai)
            else:
                u = novoNodo.pai.pai.direita  # uncle

                if u.rubro:
                    u.rubro = False
                    novoNodo.pai.rubro = False
                    novoNodo.pai.pai.rubro = True
                    novoNodo = novoNodo.pai.pai
                else:
                    if novoNodo == novoNodo.pai.direita:
                        novoNodo = novoNodo.pai
                        self.rotate_esquerda(novoNodo)
                    novoNodo.pai.rubro = False
                    novoNodo.pai.pai.rubro = True
                    self.rotate_direita(novoNodo.pai.pai)
        self.raiz.rubro = False

    def exists(self, valor):
        curr = self.raiz
        while curr != self.nil and valor != curr.valor:
            if valor < curr.valor:
                curr = curr.esquerda
            else:
                curr = curr.direita
        return curr

    # rotate esquerda at node x
    def rotate_esquerda(self, x):
        y = x.direita
        x.direita = y.esquerda
        if y.esquerda != self.nil:
            y.esquerda.pai = x

        y.pai = x.pai
        if x.pai == None:
            self.raiz = y
        elif x == x.pai.esquerda:
            x.pai.esquerda = y
        else:
            x.pai.direita = y
        y.esquerda = x
        x.pai = y

    # rotate direita at node x
    def rotate_direita(self, x):
        y = x.esquerda
        x.esquerda = y.direita
        if y.direita != self.nil:
            y.direita.pai = x

        y.pai = x.pai
        if x.pai == None:
            self.raiz = y
        elif x == x.pai.direita:
            x.pai.direita = y
        else:
            x.pai.esquerda = y
        y.direita = x
        x.pai = y

    def __repr__(self):
        lines = []
        print_tree(self.raiz, lines)
        return '\n'.join(lines)


def print_tree(node, lines, level=0):
    if node.valor != 0:
        print_tree(node.esquerda, lines, level + 1)
        lines.append('-' * 4 * level + '> ' +
                     str(node.valor) + ' ' + ('r' if node.rubro else 'b'))
        print_tree(node.direita, lines, level + 1)


def get_nums(num):
    random.seed(1)
    nums = []
    for _ in range(num):
        nums.append(random.randint(1, num-1))
    return nums


def main():
    tree = ArvoreRN()
    for x in range(1, 51):
        tree.insert(x)
    print(tree)


main()