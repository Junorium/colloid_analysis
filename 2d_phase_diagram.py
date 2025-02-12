import numpy as np
import matplotlib.pyplot as plt
# 108nm PS
# 35K PEG

# personal soln, 1 phase
dataset1 = np.array([
    [0.172, 1.0],
    [0.205, 2.2],
    [0.204, 4.0],
    [0.082, 2.1],
    [0.208, 2.0],
    [0.398, 2.1],
    [0.788, 2.1],
    [0.992, 1.9],
])

# personal soln, 2 phase
dataset2 = np.array([
    [0.197, 8.01],
    [0.217, 9.71]
])

# liam soln, 2 phase
dataset3 = np.array([
    [0.225, 5.0],
    [0.225, 4.0],
    [0.225, 3.0],
    [0.225, 2.4],
    [0.225, 2.6],
    [0.225, 2.8],
    [0.135, 6.0],
    [0.090, 6.0],
])

# liam soln, 1 phase
dataset4 = np.array([
    [0.225, 2.0],
    [0.225, 1.0],
    [0.225, 2.2],
    [0.045, 4.0],
    [0.045, 6.0]
])

# Create a new figure with a specific size
plt.figure(figsize=(10, 6))

# Plot dataset1 in blue with circular markers
plt.scatter(dataset1[:, 0], dataset1[:, 1], color='blue', label='1 phase', 
           marker='o', s=100)

# Plot dataset2 in red with circular markers
plt.scatter(dataset2[:, 0], dataset2[:, 1], color='red', label='2 phase', 
           marker='o', s=100)

plt.scatter(dataset3[:, 0], dataset3[:, 1], color='red', label='2 phase liam', 
           marker='X', s=50)

plt.scatter(dataset4[:, 0], dataset4[:, 1], color='blue', label='1 phase liam', 
           marker='X', s=50)

# Customize the plot
plt.xlabel('PS Concentration (mass %)')
plt.ylabel('PEG Concentration (mass %)')
plt.title('PEG vs PS Concentration')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Adjust layout to prevent label clipping
plt.tight_layout()

# Save the plot (optional)
plt.savefig('plot.png')

# Display the plot
plt.show()
