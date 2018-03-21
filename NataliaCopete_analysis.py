import numpy as np
import matplolib.pyplot as plt

#retorna distribucion normal
def normal_dist(x,prom,sigma):
  return np.sqrt(1/(2*np.sigma**2))*np.exp((-(x-prom)**2)/(sigma**2))

def get_fit(filename):
  datos=np.loadtxt(filename)
  plt.hist(datos)
  mean=np.mean(datos)
  desv=np.std(datos)
  print normal_dist(datos,mean,desv)
