# 2. Faça uma função que recebe, por parâmetro, a altura (alt) e o sexo de uma pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a fórmula peso ideal = 72.7 x alt -58 e, para mulheres, peso ideal = 62.1 x alt -44.7.

def pesoIdeal (h: float, s: str):
  s = s[0].upper()
  if (s == 'F'):
    res = round((62.1 * h) - 44.7, 3)
  elif (s == 'M'):
    res = round((72.7 * h) - 58, 3)
  else:
    res = 'Sexo inválido, não foi possível calcular!'
  return res

sexo = input('Informe o sexo: ')
sexo = sexo[0].upper()
altura = float(input('Informe a altura em metros: '))

pi = pesoIdeal(sexo, altura)

print(f'Altura: {altura}\nSexo: {sexo}\nPeso Ideal: {pi}')  