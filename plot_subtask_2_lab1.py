import matplotlib.pyplot as plt
import numpy as np

#We define parameters
lambda_ = 0.002
beta = 0.3
mu = 0.001
gamma = 0.05
h = 0.01
alphaI1=0.01
alpha2=0.1

#Initial conditions
S = [0.9]
I1 = [0.05]
T = [0.05]
R=[0]
N = [S[0] + I1[0] + T[0]+R[0]]
R0=(beta*S[0])/(mu+gamma+alphaI1)
# We define the differential equations at each step
def dS(S, I1, N):
    return mu*N - beta * S * I1 - mu * S

def dI1(S, I1, N):
    return beta * S * I1 - (mu + gamma) * I1 - alphaI1*I1

def dT(I1, T):
    return gamma * I1 - mu * T - alpha2*T
def dR(I1,T,R):
    return alphaI1*I1+alpha2*T-mu*R
# Simulate the epidemic using the aproximation f'=f+h*f'
for t in range(1000000):
    S.append(S[-1] + h * dS(S[-1], I1[-1], N[-1]))
    I1.append(I1[-1] + h * dI1(S[-1], I1[-1], N[-1]))
    T.append(T[-1] + h * dT(I1[-1], T[-1]))
    R.append(R[-1] + h * dR(I1[-1],T[-1],R[-1]))
    N.append(S[-1] + I1[-1] + T[-1] + R[-1])
    
# Plotting the results

plt.plot(S, label='S')
plt.plot(I1, label='I1')
plt.plot(T, label='T')
plt.plot(R, label='R')
plt.plot(N, label='N')
plt.legend()





#to uncomment
"""plt.stackplot(range(len(S)), S, I1, T, R, labels=['S', 'I1', 'T', 'R'])
plt.legend()
#plt.title(r'$\lambda$={0}, $\beta$={1}, $\mu$={2}, $\gamma$={3}, $h$={4}, $\alpha_{{I1}}$={5}, $\alpha_{{I2}}$={6}, R_0={7:.3f}'.format(lambda_, beta, mu, gamma, h, alphaI1, alphaI2, R0))
"""
plt.title(r'$\lambda$={0}, $\beta$={1:.2f}, $\mu$={2}, $\gamma$={3}, $h$={4}, $\alpha_{{I1}}$={5}, $\alpha_{{T}}$={6}, R_0={7:.3f}'.format(lambda_, beta, mu, gamma, h, alphaI1, alpha2, R0))
plt.show()
