import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
# 108nm PS
# 35K PEG

# personal soln, 1 phase
phase1 = np.array([
    [0.0120, 4.9734],
    [0.0117, 3.7108],
    [0.0120, 3.0567],
    [0.0420, 2.5900],
    [0.0379, 2.4983],
    [0.0398, 2.3971],
    [0.0361, 2.2961],
    [0.0512, 2.197],
    [0.0538, 2.1137],
    [0.0480, 1.998],
    [0.0993, 2.016],
    [0.1533, 1.723],
    [0.1500, 1.600]
])

# personal soln, 2 phase
phase2 = np.array([
    [0.0476, 5.962], [0.0925, 6.000], [0.1535, 5.978], [0.199, 5.95], [0.245, 6.13], [0.295, 6.14], [0.353, 5.97], [0.409, 6.0],
    [0.0510, 5.130], [0.1041, 5.233], [0.1490, 5.005], [0.203, 5.00], [0.253, 4.99], [0.329, 5.05], [0.354, 5.05], [0.409, 5.02],
    [0.0535, 3.970], [0.0987, 4.048], [0.1493, 3.900], [0.201, 4.04], [0.244, 3.98], [0.288, 4.09], [0.359, 4.01], [0.412, 3.89],
    [0.0420, 2.9833], [0.0503, 3.077], [0.0953, 2.939], [0.1505, 3.099], [0.198, 3.00], [0.238, 2.97], [0.307, 3.03], [0.349, 2.08],
    [0.404, 2.83], [0.0539, 2.535], [0.1043, 2.433], [0.1404, 2.397], [0.0451, 2.287], [0.099, 2.3100], [0.1538, 2.3417],
    [0.0936, 2.1932], [0.1502, 2.1922], [0.0961, 2.1088], [0.1533, 2.1142], [0.1474, 2.066], [0.200, 2.05],
    [0.254, 2.12], [0.297, 1.96], [0.35, 2.95], [0.402, 2.03], [0.0379, 2.7844], [0.0389, 2.7844], [0.0375, 2.6671], [0.0209, 3.9960]
])

# Create a new figure with a specific size
plt.figure(figsize=(10, 6))

#
plt.scatter(phase1[:,0], phase1[:,1], c='green',
label='Vapor Phase', edgecolor='k', alpha=0.8)
plt.scatter(phase2[:,0], phase2[:,1], c='red',
marker='s', label='Coexistence Phase', edgecolor='k', alpha=0.8)

# Customize the plot
plt.xlabel('PS Concentration (w/w %)')
plt.ylabel('PEG Concentration (w/w %)')
plt.title('PEG vs PS Concentration')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Adjust layout to prevent label clipping
plt.tight_layout()

# Save the plot (optional)
plt.savefig('plot.png')

# Display the plot
plt.show()
