# 4.Crie um array de inteiros contendo os vinte primeiros números primos;

primos = [2]

def primo(i: int):

  res = False

  for x in range(i + 1):
    if ((x != 1) and (x != i) and (x != 0)):
      resto = i % x      
      if (resto != 0):
        res = True
      else:        
        return False

  return res

i = 3
while (len(primos) < 20):
  if (primo(i)):
    primos.append(i)
  i += 1

print(primos)