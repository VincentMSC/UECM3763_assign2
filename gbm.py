# Import the library
import pylab as p

# Define all parameters
S0 = 39
mu = 0.1 / S0
sigma = 0.26 / S0
path = 1000
n = 1000

# Create Brownian paths, with 1000 paths
t = p.linspace(0,3,n+1)
dB = p.randn(path, n+1)/p.sqrt(n)
dB[:,0] = 0
B = dB.cumsum(axis = 1)

# Simulate stock prices by Geometric Brownian motion
a = mu - sigma ** 2 / 2
S = p.zeros_like(B)
S[:,0] = S0
S[:,1:] = S0 * p.exp(a*t[1:] + sigma*B[:,1:])

# Select 5 Brownian motions to plot into the graph
S_plot = p.zeros([5,1001])
S_plot[0:5,:] = S[0:5,:]
p.plot(t, S_plot.transpose())
p.title('Geometric Brownian Motion')
p.xlabel('Time, t')
p.ylabel('S(t)')

# Find the mean, variance, probability, and its expected value
print("Computation of mean, variance, P[S(3) > 39] and E[S(3)|S(3) > 39] from the simulation:")
Mean = sum(S[:,1000]) / path
print("Mean, E[S(3)] = ", Mean)
Var = p.sum(S[:,1000] ** 2) / path - Mean**2
print("Variance, Var[S(3)] = ", Var)
P = sum(S[:,1000] > 39) / path
print("P[S(3) > 39] =", P)
Exp = sum(S[:,1000])
print("E[S(3)|S(3) > 39] =", Exp)
print("\nTheoretical variance:")
Var_a = S0**2 * p.exp(2*mu*t[n]+sigma**2*t[n]) * (p.exp(sigma**2 * t[n]) - 1)
print("Variance, Var[S(3)] = ", Var_a)