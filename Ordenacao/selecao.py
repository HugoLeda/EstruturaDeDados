# Escreva um algoritimo que leia o nome e a altura de 10 alunos e os organize por ordem crescente de tamanho utilizando o selection sort, ao final exiba o nome e as alturas de forma organizada.

def ordenarAlunos(alunos: list):
  for i in range(len(alunos)):
    menor = i
    
    for elDireita in range((i + 1), len(alunos)):
      if (alunos[elDireita][1] < alunos[menor][1]):
        menor = elDireita
    
    alunos[menor], alunos[i] = alunos[i], alunos[menor]
  
  return alunos

def registrarAlunos(qtd: int):
  alunos = []
  for i in range(qtd):
    nome = input('Digite o nome do aluno: ')
    altura = round(float(input('Digite a altura do aluno (em metros): ')), 2)
    aluno = [nome, altura]
    alunos.append(aluno)
  return alunos

alunos = registrarAlunos(10)
alunos = ordenarAlunos(alunos)
print(alunos)