# 13. Faça um função que lê 50 valores inteiros e retorna o maior e o menor deles. 

def maiorValor():
  numeros = []
  for i in range(0, 50, 1):
    n = int(input('Informe um número inteiro: '))
    numeros.append(n)
  maior = max(numeros)
  menor = min(numeros)
  return {'maior': maior, 'menor': menor}

res = maiorValor()
print(res)