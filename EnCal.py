import numpy as np
import matplotlib.pyplot as plt
"""
Defining the Cosmological Parameters
"""
G=1
H0=1
omega0A=0.73
omega0rel=8.24e-5
omega0m=0.27-omega0rel
"""
Defining functions for the various energies
"""
#Classical Kinetic Energy of an expanding universe
def CKEn(a):
	CKEn=H0**2*omega0m/(2*a)
	return CKEn
	
#Energy due to the Cosmological constant	
def  MKEn(a):
	MKEn=(H0**2*omega0A*a**2)/2	
	return MKEn
	
#Gravitational self energy of an expanding universe
def Pot(a):
	Pot=H0**2*omega0m/(4*a)
	return Pot

#Total Energy of the universe considering the various energy terms	
def TotEn(a):
	TotEn=H0**2*a**2*(omega0m/(4*a**3) + omega0m/(2*a**3) + omega0A/2)
	return TotEn


"""
Plotting
"""	
x=np.linspace(0.1,2,1000)
A=[TotEn(l) for l in x]
print(A)
plt.plot(x,Pot(x),color='yellow',label='Gravitational Self Energy',linestyle='dashed')
plt.plot(x,CKEn(x),color='red',label='Matter associated Kinetic energy term',linestyle='dashed')
plt.plot(x,MKEn(x),color='blue',label='\u039B CDM associated energy',linestyle='dashed')
plt.plot(x,TotEn(x),color='black',label='Total Energy of Expanding Energy')
plt.legend(loc='best')
plt.xlabel("Scale Factor")
plt.ylabel("Energy Magnitude")
plt.suptitle("Variation of Total Energy of the Universe with Scale Factor")
plt.savefig('Total_Cosmo_Energy.png')
plt.show()
