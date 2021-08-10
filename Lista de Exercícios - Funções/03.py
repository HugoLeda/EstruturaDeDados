# 3.  Faça  uma  função  que  recebe  por  parâmetro  o  tempo  de duração  de  uma  fábrica expressa em segundos e retorna também por parâmetro esse tempo em horas, minutos e segundos. 

def tempo(segundos: int):
  horas = (segundos / 60) / 60
  minutos = segundos / 60
  res = {"horas": horas, "minutos": minutos, "segundos": segundos}
  return res

seg = int(input('Informe o tempo de duração em segundo: '))
res = tempo(seg)
print(res)