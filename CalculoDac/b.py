# Reproduza os cálculos do DAC utilizando uma lista naqual os dados do Nosso Número sejam gerados aleatoriamente (no arquivo anexo os dados do nosso Numero são: 12345678)

from random import randint

def adicionarNossoNumero(sequencia: list):
  for i in range(8):
    sequencia.append(randint(0, 9))
  return sequencia

def gerarModulo10(sequencia: list):
  modulo10 = [0] * len(sequencia)

  n = 2
  for i in range(len(sequencia) - 1, -1, -1):
    modulo10[i] = n
    if (n == 2):
      n = 1
    else:
      n = 2
  
  return modulo10

def calcularDac(sequencia: list, modulo10: list):
  multiplicacoes = []
  soma = 0
  
  if (len(sequencia) != len(modulo10)):
    return 'ERRO: o módulo10 e a sequência devem ter a mesma quantidade de elementos'
  
  for i in range(len(sequencia)):
    produto = sequencia[i] * modulo10[i]
    produto = str(produto)
    if ( len(produto) == 2 ):
      n1 = int(produto[0])
      n2 = int(produto[1])
      multiplicacoes.append(n1)
      multiplicacoes.append(n2)
    else:
      produto = int(produto)
      multiplicacoes.append(produto)

  for i in multiplicacoes:
    soma += i

  dac = 10 - (soma % 10)

  return dac

valores = [0, 0, 5, 7, 1, 2, 3, 4, 5, 1, 1, 0]
valores = adicionarNossoNumero(valores)
modulo10 = gerarModulo10(valores)
dac = calcularDac(valores, modulo10)

print(f'Sequência: {valores}')
print(f'Módulo 10: {modulo10}')
print(f'DAC: {dac}')