"""
This a a program for creating a simulation to show the variation of Scale factor with time with variation of parameters
The program is created by Utkarsh Basu, Maulana Azad College, University of Calcutta (2022)
"""
import numpy as np
from scipy.integrate import quad
import scipy
H0=69.8
G=1
a0=1
#We take the universe to be initially radiation dominated.
"""
Defining the density parameter and subsequently omega parameter for dark energy for the present time
"""
omega0A=0.73
"""
Defining the omega parameter for matter and relativistic particles for the present time using WMAP Data
"""
omega0rel=8.24e-5
omega0m=0.3-omega0rel
#
"""
Defining the scale factor and its first derivative for Universe with Dark Energy but with no curvature
"""
def da1(t):
	da1=H0*(((omega0m/(t**(0.5)))+(omega0rel/(t**(0.5))**2)+(omega0A*(t**(0.5))**2))**(0.5))
	return da1
"""
Integrating da wrt time we get the dependence of the scale factor on time
"""
t=np.linspace(1,15,1000)
a1=[]
for n in t:
	quad1,err1=quad(da1,1,n)
	a1.append(quad1)
#print(a1)
#

"""
Defining the scale factor and its first derivative for Universe with no Dark Energy but with negative curvature
"""
#For open universe without dark energy
omega0subcm=0
omega0relsubcm=0
K1=-1
def da2(t):
	da2=H0*(((omega0subcm/(t**(0.5)))+(omega0relsubcm/(t**(0.5))**2)-K1)**(0.5))
	return da2

"""
Integrating da wrt time we get the dependence of the scale factor on time
"""

a2=[]
for i in t:
	quad2,err=quad(da2,1,i)
	a2.append(quad2)

#print(a2)
#
#
"""
Defining the scale factor and its first derivative for critical density Universe
"""
#For critical density universe
omega0mc=1
omega0relc=0
def da3(t):
	da3=H0*(((omega0mc/(t**(0.5)))+(omega0relc/(t**(0.5))**2))**(0.5))
	return da3

"""
Integrating da wrt time we get the dependence of the scale factor on time
"""

a3=[]
for j in t:
	quad3,err=quad(da3,1,j)
	a3.append(quad3)

#print(a3)
#
#
"""
Defining the scale factor and its first derivative for Universe with positive curvature
"""
#For closed universe without dark energy
omega0msc=3-omega0rel
K2=2
def da4(t):
	da4=H0*(((omega0msc/(t**(0.5)))+(omega0rel/(t**(0.5))**2)-K2)**(0.5))
	return np.real(da4)
	
def da5(t):
	da5=H0*(((omega0msc/(t**(0.5)))+(omega0rel/(t**(0.5))**2)-K2)**(0.5))
	return np.imag(da5)
"""
Integrating da wrt time we get the dependence of the scale factor on time
"""

a4=[]
a5=[]
a6=[]
for k in t:
	quad4,err=quad(da4,1,k)
	a4.append(quad4)
	
for l in t:
	quad5,err=quad(da5,1,l)
	a5.append(quad5)

#print("The list of real numbers is:",a4)
#print("The list of imaginary numbers is:",a5)

for z in range(0,len(a4)):
	a6.append(a4[z]-a5[z])
	
#print("The list of required results is:",a6)

#
"""
Plotting a(t) vs t
"""
import matplotlib.pyplot as plt
plt.plot(t,a1,color='green',label='\u039B CDM')
plt.plot(t,a2,color='red',label='Open Universe')
plt.plot(t,a3,color='orange',label='Newtonian critical density universe')
plt.plot(t,a6,color='black',label='Closed universe')
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel("Time")
plt.ylabel("Scale factor")
plt.ylim([0,200])
plt.xlim([1,4])
plt.suptitle("Changes in Expansion Rate with variation of parameters")
plt.legend(loc='best')
plt.savefig('SfactorChanges.png')
plt.show()
