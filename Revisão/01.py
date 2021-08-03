# 1.Implemente um algoritmo que exiba a soma de todos os números pares de 1 a 200;

soma = 0
for i in range(201):
  resto = i % 2
  if (resto == 0):
    soma += i

print('Soma dos números pares até 200:', soma)