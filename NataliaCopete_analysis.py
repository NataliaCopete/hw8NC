import numpy as np
import matplolib.pyplot as plt

#retorna distribucion normal
def normal_dist(x,prom,sigma):
  return np.random.normal(prom,sigma)

def get_fit(filename):
  datos=np.loadtxt(filename)
  plt.hist(datos)
  desv_valores=std(valores_posibles)
  print normal_dist(promedi_valores,desv_valores)
