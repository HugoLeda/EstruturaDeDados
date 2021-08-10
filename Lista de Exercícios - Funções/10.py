"""
10. Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu conceito, conforme a tabela abaixo: 
    Nota        Conceito 
de 0,0 a 4,9       D 
de 5,0 a 6,9       C 
de 7,0 a 8,9       B 
de 9,0 a 10,0      A 
"""

def conceito(media):
  if (media >= 0 and media <= 4.9):
    conceito = 'D'
  elif (media >= 5 and media <= 6.9):
    conceito = 'C'
  elif (media >= 7 and media <= 8.9):
    conceito = 'B'
  elif (media >= 9 and media <= 10):
    conceito = 'A'
  else:
    conceito = 'Média inválida!'
  
  return conceito

media = float(input('Informe a média final do aluno: '))
resultado = conceito(media)

print(f'O conceito desse aluno foi: {resultado}')