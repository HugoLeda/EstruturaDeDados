# 6. Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias. 

def idadeDias(anos: int, meses: int, dias: int):
  if (anos < 0 or meses < 0 or dias < 0):
    return 'Dados inválidos!'

  totalDias = (anos * 365) + (meses * 30) + dias
  return totalDias

anos = int(input('Informe quantos anos você tem: '))
meses = int(input('Quantos meses completos depois do seu último aniversário você possui: '))
dias = int(input('Quantos dias se passaram desde o último dia equivalente ao dia que você nasceu: '))
totalDias = idadeDias(anos, meses, dias)

print(totalDias)