# 14. Faça um funçãoque recebepor parâmetro um valor N e calculetabuada de 1 até N. Mostre a tabuada na forma: 1 x N = N 

def tabuada(n):
  for i in range(0, 11, 1):
    print(f'{i} x {n} = {i * n}')

n = float(input('Informe um valor para ver sua tabuada: '))
tabuada(n)