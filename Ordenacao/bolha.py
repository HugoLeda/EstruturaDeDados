# Escreva um algoritimo que leia o nome e a altura de 10 alunos e os organize por ordem crescente de tamanho utilizando o buble sort, ao final exiba o nome e as alturas de forma organizada.

def ordenarAlunos(alunos: list):
  for i in range(len(alunos) - 1, 0, -1):
    for j in range(i):
      if (alunos[j][1] > alunos[j + 1][1]):
        temp = alunos[j]
        alunos[j] = alunos[j + 1]
        alunos[j + 1] = temp
  return alunos

def registrarAlunos(qtd: int):
  alunos = []
  for i in range(qtd):
    nome = input('Digite o nome do aluno: ')
    altura = round(float(input('Digite a altura do aluno (em metros): ')), 2)
    aluno = [nome, altura]
    alunos.append(aluno)
  return alunos

alunos = registrarAlunos(5)
alunos = ordenarAlunos(alunos)
print(alunos)