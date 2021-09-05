# Escreva  um  algoritmo  que  leia  e  mostre  um  vetor  de  20  elementos inteiros.  a  seguir,  conte  quantos  valores pares existem no vetor.

def qtdPares(v: list):
  pares = 0
  for i in v:
    if ((i % 2) == 0):
      pares += 1
  return pares

def lerVetor(p: int):
  res = []
  for i in range(p):
    n = float(input('Digite um número: '))
    res.append(n)
  return res

lista = lerVetor(20)
print(f'A quantidade de números pares na lista é: {qtdPares(lista)}')