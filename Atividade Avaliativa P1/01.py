""""
  Um número de série qualquer possui nove dígitos mais dois dígitos de controle (DCs). Esses dois dígitos, chamados DC1 e DC2, são calculados utilizando os números de uma sequência NS, da seguinte maneira:1: Multiplica-se cada um dos nove dígitos do NS, da direita para a esquerda, por um peso que começa em 2 e é incrementado de 1 a cada dígito, somando-se todos os produtos obtidos. Esse resultado deve ser dividido por 11. Se o resto da divisão for menor que 2, o DC1 será 0, caso contrário, o DC1 será 11 subtraído do resto obtido.2: Deve ser repetido o processo anterior considerando agora um número de dez dígitos formado pelos nove dígitos do NS à esquerda e o DC1 como sendo o dígito mais à direita do número. Ou seja, o DC1 deverá ser multiplicado pelo peso 2 e os demais dígitos com por um peso variando de 3 até 11.
  
  a)Escreva uma função que gere 9 dígitos aleatórios e utilizando os requisitos acima faça o cálculo dos 2 últimos dígitos, DC1 e DC2.

  b) Escreva uma função que a partir de 2 DCS gerem os 9 dígitos da NS necessários para validar o cálculo.
"""

from random import randint

def gerarDc(sequencia: list):
  if (len(sequencia) == 9 or len(sequencia) == 10):
    pesos = [0] * len(sequencia)
    peso = 1

    for i in range(len(pesos), 0, -1):
      peso += 1
      pesos[i - 1] = peso

    soma = 0

    for i in range(len(sequencia)):
      soma += sequencia[i] * pesos[i]
    
    resto = soma % 11    
    if (resto < 2):
      dc = 0
    else:
      dc = 11 - resto

    return dc
  
  else:
    return 'ERRO, sequência inválida!'

def a():
  sequencia = []
  
  for i in range(9):
    n = randint(0, 9)
    sequencia.append(n)
  
  dc1 = gerarDc(sequencia)
  sequencia.append(dc1)
  
  dc2 = gerarDc(sequencia)
  sequencia.append(dc2)

  print(f'DC1: {dc1}\nDC2: {dc2}\nSequencia: {sequencia}')

def b(dc1: int, dc2: int):
  

#a()