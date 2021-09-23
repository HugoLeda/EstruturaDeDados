""""
  Escreva um algoritmo que implementeas operações de inclusão e de exclusão em  listas.  Considere  que  a  lista  deve  armazenar  números  inteiros. O algoritmo deve conter os seguintes funções:
  a)Inserir no início
  b)Inserir no final
  c)Remover elemento por índice
  d)Remover elemento por valor
  As implementações não devem conter os métodos de manipulação de listas da linguagem de programação.
"""
from random import randint

def inserirInicio(n: int, lista: list):
  res = [0] * (len(lista) + 1)
  res[0] = n

  for i in range(1, (len(lista) + 1), 1):
    res[i] = lista[i - 1]

  return res

def inserirFinal(n: int, lista: list):
  res = [0] * (len(lista) + 1)

  for i in range(len(lista)):
    res[i] = lista[i]

  res[len(lista)] = n

  return res

def removerIndice(indice: int, lista: list):
  res = [0] * (len(lista) - 1)

  desc = 0
  for i in range(len(lista)):
    if (i != indice):
      res[i - desc] = lista[i]
    else:
      desc = 1

  return res

def removerValor(vlr: int, lista: list):
  res = [0] * (len(lista) - 1)

  desc = 0
  for i in range(len(lista)):
    if (lista[i] != vlr):
      res[i - desc] = lista[i]
    else:
      desc = 1

  return res

def gerarLista(tamanho: int):
  res = []

  for i in range(tamanho):
    res.append(randint(0, 50))

  return res

lista = gerarLista(10)
print(lista)

lista = inserirInicio(2, lista)
print(lista)

lista = inserirFinal(3, lista)
print(lista)

lista = removerIndice(2, lista)
print(lista)

lista = removerValor(2, lista)
print(lista)