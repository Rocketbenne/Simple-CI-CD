
#   Short Program to Test the Correctness of the CI/CD-System

import numpy as np
import matplotlib.pyplot as plt
import csv

# Parameters
A = 5
Theta_0 = np.pi / 2
phi = 0
N = 16

# Given function x[n]
def function(n):
    return A*np.cos(Theta_0 * n + phi)

# Initialization of arrays with size N
n = np.zeros(N)
samples = np.zeros(N)

# Calculate each sample
for i in range(N):
    n[i] = i
    samples[i] = function(i)
    # Prints generated sample-values
    print("x[", i, "] = ", samples[i])

# Plot the samples
plt.stem(n, samples)
plt.xlabel('n')
plt.ylabel('x[n]')

plt.grid()
plt.savefig('Test-Program')
#plt.show()

# Write values to a .csv file
filename = 'Test_Program.csv'

file = open(filename, 'w')

fields = ['n', 'x[n]']
writer = csv.DictWriter(file, fieldnames=fields)
writer.writeheader()

for i, value in enumerate(n):
        writer.writerow({'n': i, 'x[n]': samples[i]})
