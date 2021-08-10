# 5. Faça uma função que recebe por parâmetro um valor inteiro e positivo e retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso contrário.

def primo(n: int):
  if (n < 0):
    return 'ERRO: informe um valor inteiro e positivo!'
  
  res = True
  i = 2

  while (i < n):
    resto = n % i
    if (resto == 0):
      res = False
  
  return res

n = int(input('Informe um valor inteiro e positivo: '))
res = primo(n)
print(res)