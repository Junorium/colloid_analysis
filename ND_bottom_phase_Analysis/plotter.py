import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# (x=PS conc), (y=avg_intensity)
x = [2.83, 3.89, 5.02]
y = [21.52880676, 13.62331268, 9.144121094]

# Error (stdev)
yerr = [7.310773488, 3.448576038, 1.375668368]

# Fit regression line
coefficients = np.polyfit(x, y, 1)
regression_line = np.poly1d(coefficients)

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Create the plot
plt.figure(figsize=(8, 6))
plt.errorbar(x, y, yerr=yerr, fmt='o', capsize=5, capthick=2)
# plt.plot(x, regression_line(x), '-')

# Add regression equation to the plot
# equation = f'y = {slope:.3f}x + {intercept:.3f}'
# plt.text(0.2, 22, equation, fontsize=12)  # Adjusted position to fit within the graph
pearson_text = f'r = {r_value:.3f}'
plt.text(0.09, 23, pearson_text, fontsize=12)  # Adjust position as needed


# Customize the plot
plt.xlabel('PEG Concentration (w/w%)')
plt.ylabel('Average Intensity (from 0 to 4096)')
plt.title('Average Pixel Intensity vs PEG Concentration')
plt.grid(True)
plt.legend()
plt.ylim(0)  # Set y-axis to start at 0

# Display the plot
plt.show()
