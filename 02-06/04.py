def fibo(n):
  if (n==1):
    return 0
  elif (n==2):
    return 1
  else:
    return fibo(n-1) + fibo(n-2)
  
def fiboLoop(n):  
  if (n==1) or (n==2):
    print("1")
  else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
  return termo
    