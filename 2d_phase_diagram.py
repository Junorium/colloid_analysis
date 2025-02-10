import numpy as np
import matplotlib.pyplot as plt

# Define the datasets

# liam phase 2
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

# liam phase 1
dataset2 = np.array([
    [0.197, 8.01],
    [0.217, 9.71]
])

# phase 1 actual
dataset3_actual = np.array([
    [0.172, 1.0],
    [0.205, 2.2],
    [0.204, 4.0],
    [0.082, 2.1],
    [0.208, 2.0],
    [0.398, 2.1],
    [0.788, 2.1],
    [0.992, 1.9],
])

# phase 2 actual
dataset4_actual = np.array([
    [0.197, 8.01],
    [0.217, 9.71]
])

# Create a new figure with a specific size
plt.figure(figsize=(10, 6))

# Plot dataset1 in blue with circular markers
plt.scatter(dataset1[:, 0], dataset1[:, 1], color='blue', label='Dataset 1', 
           marker='o', s=100)

# Plot dataset2 in red with circular markers
plt.scatter(dataset2[:, 0], dataset2[:, 1], color='red', label='Dataset 2', 
           marker='o', s=100)

# Customize the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Comparison of Two Datasets')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Adjust layout to prevent label clipping
plt.tight_layout()

# Save the plot (optional)
plt.savefig('plot.png')

# Display the plot
plt.show()
