import numpy as np
import matplotlib.pyplot as plt
"""
Defining the parameters of the torus universe
"""
r=0.5
R=1.0
H0=1
t=np.linspace(0,2*np.pi,1000)
x=np.linspace(-(R+r),R+r,1000)

#Curvature term of the torus	
K=[(np.cos(u)/(r*(R + r*np.cos(u))))/2 for u in t]

#Defining the Scale factor of the Universe(a)	
def B(theta):
	B=np.sqrt(2*r*R*np.cos(theta) + (r**2 + R**2))
	return B
	
a=[B(i) for i in t]

#Defining A to use as a coefficient
A=[((a[j])**2 - (r**2 + R**2))/(2*r*R) for j in range(len(a))]

#Defining the omega0m parameter
omega0m=[(1 + A[k]/(r*(R + r*A[k]))) for k in range(len(a))] 

#Defining the potential term
Pot=[omega0m[l]/4*a[l] for l in range(len(a))]

#Defining the classical kinetic energy term
CKen=[omega0m[m]/2*a[m] for m in range(len(a))]

#Defining the total energy term
Toten=[Pot[n] + CKen[n] - K[n] for n in range(len(a))]

"""
Plotting
"""
print(Toten)
K0=[-K[p] for p in range(0,1000)]
plt.plot(x, K0, color='green',label='Energy due to Curvature term',linestyle='dashed')
plt.plot(x, Pot, color='red',label='Energy due to self gravitation',linestyle='dashed')
plt.plot(x, CKen, color='yellow',label='Energy from a Kinetic term',linestyle='dashed')
plt.plot(x, Toten, color='black',label='Total energy of the system as a function of distance')
plt.axvline(x=0, c="grey", linestyle='dashed')
plt.axhline(y=0, c="grey", linestyle='dashed')
plt.xlabel("Scale Factor")
plt.ylabel("Energy")
plt.legend(loc='best')
plt.suptitle("Variation of Energy with respect to distance for a Torus")
plt.savefig('Torus energy variation.png')
plt.show()
