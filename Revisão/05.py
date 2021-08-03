# 5.Crie um funçãoque receba um array de inteiros e imprimao menor, o maior e a média dos valores;

def numerosArray (n: list):
  soma = 0
  for i in range(len(n)):
    if (i == 0):
      menor = n[i]
      maior = n[i]
    soma += n[i]

    if (n[i] < menor):
      menor = n[i]

    if (n[i] > maior):
      maior = n[i]

  media = soma / len(n)

  res = {"menor": menor, "maior": maior, "media": media}
  print(res)

a = [0, 5, 10, 5]
numerosArray(a)