import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from collections import defaultdict

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
    
     average_absorbance_bright_spots = np.mean(bright_spots_nonzero)
    corrected_absorbance_bright_spots = average_absorbance_bright_spots - baseline_absorbance
    
     return corrected_absorbance_bright_spots

# Function to calculate average absorbance for the background
def analyze_background_with_baseline(gray_img, baseline_absorbance):
    _, bright_spots_mask = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY)
    background_mask = cv2.bitwise_not(bright_spots_mask)
    background_only = cv2.bitwise_and(gray_img, background_mask)
    background_nonzero = background_only[background_only > 0]
    
     average_absorbance_background = np.mean(background_nonzero)
    corrected_absorbance_background = average_absorbance_background - baseline_absorbance
    
     return corrected_absorbance_background

# Baseline absorbance from water sample
water_image_path = "water_baseline.jpg"
water_gray_img = preprocess(water_image_path)
water_baseline_absorbance = np.mean(water_gray_img)

# Store image paths for each concentration
image_paths = {
    "0.1%": ["0.1/0.1_1", "0.1/0.1_2", "0.1/0.1_3", "0.1/0.1_4", "0.1/0.1_5"],
    "0.2%": ["0.2/0.2_1", "0.2/0.2_2", "0.2/0.2_3", "0.2/0.2_4", "0.2/0.2_5"],
    "0.4%": ["0.4/0.4_1", "0.4/0.4_2", "0.4/0.4_3", "0.4/0.4_4", "0.4/0.4_5"],
    "0.8%": ["0.8/0.8_1", "0.8/0.8_2", "0.8/0.8_3", "0.8/0.8_4", "0.8/0.8_5"],
     "1.6%": ["1.6/1.6_1", "1.6/1.6_2", "1.6/1.6_3", "1.6/1.6_4", "1.6/1.6_5"],
     "3.2%": ["3.2/3.2_1", "3.2/3.2_2", "3.2/3.2_3", "3.2/3.2_4", "3.2/3.2_5"],
     "6.4%": ["6.4/6.4_1", "6.4/6.4_2", "6.4/6.4_3", "6.4/6.4_4", "6.4/6.4_5"]
}

absorbance_results = defaultdict(list)

# Loop through each concentration group and its images
for concentration, paths in image_paths.items():
    for img_path in paths:
        gray_img = preprocess(img_path)
        
        # Calculate the absorbance for both bright spots and background, and choose one or both
        bright_spots_absorbance = analyze_bright_spots_with_baseline(gray_img, water_baseline_absorbance)
        background_absorbance = analyze_background_with_baseline(gray_img, water_baseline_absorbance)
        
        # Add the chosen absorbance value (e.g., bright spots or background) to the results
        absorbance_results[concentration].append(bright_spots_absorbance)

# Calculate average absorbance for each concentration
average_absorbance_per_concentration = {}
for concentration, absorbances in absorbance_results.items():
    average_absorbance_per_concentration[concentration] = np.mean(absorbances)

# Output results
for concentration, avg_absorbance in average_absorbance_per_concentration.items():
    print(f"Average Absorbance for {concentration}: {avg_absorbance}")

### Next step: plot graph using matplotlib for concentration vs absorbance
# Use linear regression if linear and obtain equation
# Use Lagrange or spline interpolation if nonlinear
