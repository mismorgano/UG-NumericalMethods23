import numpy as np

#%%
def printElements(arr:list, n:int, format:str):
  if len(arr) <= 2*n:
    print(''.join((format % el) for el in arr))
  else:
    print(''.join((format % el) for el in arr[:n]) + '...' + ''.join((format % el) for el in arr[-n:]) )

#%%
def Lxp1(x:float, n:int):
  total = 0
  for i in range(1, n+1):
    total += 1/i * (x/(x+1))**i
  return total

def printLog(arr:list, n):
  print(*((x, np.log(1+x), Lxp1(x, n), np.abs(np.log(1+x) - Lxp1(x, n))) for x in arr), sep='\n')
  # return (print(x, np.log(1+x), Lxp1(x, n), np.abs(np.log(1+x) - Lxp1(x, n))) for x in arr)


#%%
def comparacion(a, b):
  if a == b:
    print("Los valores de a y b son iguales")
  else:
    print("Los valores de a y b son diferentes")