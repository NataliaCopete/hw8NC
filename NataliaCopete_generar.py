import numpy as np
import matplotlib.pyplot as plt




def sample_1(N):
  valores_posibles=np.array([-10,-5,3,9])
  valores_generados= np.random.choice(valores_posibles,N,p=[0.1,0.4,0.2,0.3])
  return valores_generados

def sample_2(N):
  valores_obtenidos=np.random.exponential(0.5,N)
  return valores_obtenidos

def get_mean(samp_fun,N,M):
  promedios= np.zeros(M)
  for i in range (M):
    valores= samp_fun(N)
    promedios[i]=np.mean(valores)
  return promedios

for i in range(1,4):
  values=get_mean(sample_1,10**i,10000)
  string="sample_1_"+str(10**i)
  np.savetxt(string,values,delimiter=" ")
  

for i in range(1,4):
  values=get_mean(sample_1,10**i,10000)
  string="sample_2_"+str(10**i)
  np.savetxt(string,values,delimiter=" ")





   


