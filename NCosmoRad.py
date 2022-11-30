import numpy as np
import matplotlib.pyplot as plt
from sympy import *
t=symbols('t')
a=t**(1/2) #Radiation dominated universe
adot=diff(a,t)
adot2=diff(a,t,2)
rho_mat=a**-3
rho_rad=a**-4
H=(rho_mat+rho_rad)**(1/2)
print("The relation between matter density and time is:",rho_mat)
print("The relation between radiation density and time is:",rho_rad)
print("The relation between Hubble parameter and time is:",H)
H=lambdify(t,H)
rho_mat=lambdify(t,rho_mat)
rho_rad=lambdify(t,rho_rad)
t=np.linspace(0,13.8,1000)
plt.plot(t,rho_mat(t),color='red',label='Matter Density')
plt.plot(t,rho_rad(t),color='blue',label='Radiation Density')
#plt.plot(t,H(t),color='green',label='Hubble Parameter')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("log(t)")
plt.ylabel("log(Density)")
plt.suptitle("Initially Radiation Dominated Universe using Newtonian Cosmology")
plt.legend(loc='best')
plt.savefig('Radiation Dominated Universe.png')
plt.show()

