
#%%
def means(v: np.ndarray):
  ma = np.sum(v)/len(v)
  mh = len(v)/(np.sum(1/v))
  mg = np.float_power(np.prod(v), 1/len(v))
  return ma, mh, mg

#%%
def epsilon():
  epsilon = 0.5;
  unidad  = 1.0;
  valor   = unidad + epsilon;
  while valor > unidad:
      epsilon = epsilon/2;
      valor   = unidad + epsilon;
  
  return epsilon*2;

#%%
print(f"El epsilon de la maquina es: {epsilon()}")
print(f"La diferencia entre {np.finfo(float).eps - epsilon()}")
eps = epsilon()
compara = lambda a, b: "Iguales" if a == b else "Diferentes"
x1 = [1+eps, eps/2, 1 + eps/2, 1-eps/2, 1-eps/4, 1-eps/2, eps**2, eps**5, eps + eps**2, eps-eps**3]
x2 = [1, 0, 1, 1, 1, 1-eps, 0, 0, eps, eps]
print('\n'.join(f"{a} {b} {compara(a, b)}" for (a, b) in zip(x1, x2)))

#%%
import matplotlib.pyplot as plt

def elipse(a, b, c, n):
  theta = np.linspace(0, 2*np.pi, 2*n)
  x = a*np.cos(theta) + c[0]
  y = b*np.sin(theta) + c[1]
  plt.plot(x, y)

elipse(4, 4, (1, 2), 3)
elipse(4, 4, (1, 2), 50)
elipse(5, 2, (-4, 2), 50)