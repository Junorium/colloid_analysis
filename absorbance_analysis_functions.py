import numpy as np
import cv2
from PIL import Image
from collections import defaultdict
import matplotlib.pyplot as plt

# Function to load and convert image to grayscale
def preprocess(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    gray_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    return gray_img


# Function to calculate average absorbance for the bright spots
def analyze_bright_spots_with_baseline(gray_img, baseline_absorbance):
    _, bright_spots_mask = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY)
    bright_spots = cv2.bitwise_and(gray_img, bright_spots_mask)
    bright_spots_nonzero = bright_spots[bright_spots > 0]

    if len(bright_spots_nonzero) > 0:
        average_absorbance_bright_spots = np.mean(bright_spots_nonzero)
        corrected_absorbance_bright_spots = average_absorbance_bright_spots - baseline_absorbance
    else:
        corrected_absorbance_bright_spots = 0  # No bright spots detected

    return corrected_absorbance_bright_spots


# Function to calculate average absorbance for the background
def analyze_background_with_baseline(gray_img, baseline_absorbance):
    _, bright_spots_mask = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY)
    background_mask = cv2.bitwise_not(bright_spots_mask)
    background_only = cv2.bitwise_and(gray_img, background_mask)
    background_nonzero = background_only[background_only > 0]

    if len(background_nonzero) > 0:
        average_absorbance_background = np.mean(background_nonzero)
        corrected_absorbance_background = average_absorbance_background - baseline_absorbance
    else:
        corrected_absorbance_background = 0  # No background pixels detected

    return corrected_absorbance_background


# Baseline absorbance from water sample
# Need to iterate through other five images for possible differences
water_image_path = "bg1.jpg"
water_gray_img = preprocess(water_image_path)
water_baseline_absorbance = np.mean(water_gray_img)

# Store image paths for each concentration
# Currently not including 6.4%
image_paths = {
    "0.1%": ["0.1/0.1_1", "0.1/0.1_2", "0.1/0.1_3", "0.1/0.1_4", "0.1/0.1_5"],
    "0.2%": ["0.2/0.2_1", "0.2/0.2_2", "0.2/0.2_3", "0.2/0.2_4", "0.2/0.2_5"],
    "0.4%": ["0.4/0.4_1", "0.4/0.4_2", "0.4/0.4_3", "0.4/0.4_4", "0.4/0.4_5"],
    "0.8%": ["0.8/0.8_1", "0.8/0.8_2", "0.8/0.8_3", "0.8/0.8_4", "0.8/0.8_5"],
    "1.6%": ["1.6/1.6_1", "1.6/1.6_2", "1.6/1.6_3", "1.6/1.6_4", "1.6/1.6_5"],
    "3.2%": ["3.2/3.2_1", "3.2/3.2_2", "3.2/3.2_4", "3.2/3.2_5"],
    "6.4%": ["6.4/6.4_1", "6.4/6.4_2", "6.4/6.4_3"]
}

absorbance_results_bright_spots = defaultdict(list)
absorbance_results_background = defaultdict(list)

# Loop through each concentration group and its images
for concentration, paths in image_paths.items():
    for img_path in paths:
        gray_img = preprocess(f'{img_path}.jpg')

        # Calculate the absorbance for both bright spots and background
        bright_spots_absorbance = analyze_bright_spots_with_baseline(gray_img, water_baseline_absorbance)
        background_absorbance = analyze_background_with_baseline(gray_img, water_baseline_absorbance)

        # Store results for bright spots and background
        absorbance_results_bright_spots[concentration].append(bright_spots_absorbance)
        absorbance_results_background[concentration].append(background_absorbance)

# Calculate average absorbance for each concentration
average_absorbance_bright_spots_per_concentration = {}
average_absorbance_background_per_concentration = {}

for concentration, absorbances in absorbance_results_bright_spots.items():
    average_absorbance_bright_spots_per_concentration[concentration] = np.mean(absorbances)

for concentration, absorbances in absorbance_results_background.items():
    average_absorbance_background_per_concentration[concentration] = np.mean(absorbances)

# Output results
print("Average Absorbance for Bright Spots (Corrected):")
for concentration, avg_absorbance in average_absorbance_bright_spots_per_concentration.items():
    print(f"{concentration}: {avg_absorbance}")

print("\nAverage Absorbance for Background (Corrected):")
for concentration, avg_absorbance in average_absorbance_background_per_concentration.items():
    print(f"{concentration}: {avg_absorbance}")

### PLOTTING

# Extract concentrations and corresponding average absorbance values
concentrations = [float(c.strip('%')) for c in average_absorbance_background_per_concentration.keys()]
absorbances = list(average_absorbance_background_per_concentration.values())

plt.figure(figsize=(8,6))
plt.scatter(concentrations, absorbances, color='blue', label='Absorbance')

# Perform linear regression
slope, intercept = np.polyfit(concentrations, absorbances, 1)  # Degree 1 for linear
regression_line = np.array(concentrations) * slope + intercept

# Calculate R^2
y_actual = np.array(absorbances)
y_predicted = regression_line
ss_residual = np.sum((y_actual - y_predicted) ** 2)  # Residual sum of squares
ss_total = np.sum((y_actual - np.mean(y_actual)) ** 2)  # Total sum of squares
r_sq = 1 - (ss_residual / ss_total)

# Plot regression line
plt.plot(concentrations,
         regression_line,
         color='red',
         label=f'Regression Line (y = {slope:.2f}x + {intercept:.2f}), R-sq = {r_sq:.2f}')

plt.xlabel('Concentration (%)')
plt.ylabel('Average Absorbance')
plt.title('Concentration vs Absorbance with Linear Regression')
plt.legend()
plt.savefig('conc_abs_background.png', format='png')
plt.show()