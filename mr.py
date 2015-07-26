# Import the library
import pylab as p

# Define all parameters
path = 1000
n = 1000

# Create Brownian paths, with 1000 paths
dB = p.randn(path, n+1)/p.sqrt(n)
dB[:,0] = 0
B = dB.cumsum(axis = 1)
t = p.linspace(0,1,n+1)
dt = 1 / n

# Simulating the mean reversal process using the definition of differences
R = p.zeros([1000,1001])
R[:,0] = 3
for c in range(n):
    R[:,c+1] = R[:,c] + (0.064 - R[:,c]) * dt + 0.27 * R[:,c] * (B[:,c+1] - B[:,c])

# Select 5 simulation for display
R_plot = p.zeros([5,1001])
R_plot[0:5,:] = R[0:5,:]
p.plot(t,R_plot.transpose())
p.title('Mean Reversal Process')
p.xlabel('Time, $t$')
p.ylabel('$R(t)$')

# Calculate mean and probability
Mean = p.sum(R[:,1000]) / path
print("Mean from the simulation, E[R(1)] =", Mean)
P = p.sum(R[:,n] > 2) / path
print("Probability from the simulation, P[R(1) > 2] =", P)