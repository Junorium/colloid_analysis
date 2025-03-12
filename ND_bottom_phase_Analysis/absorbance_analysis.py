import os
import numpy as np
import cv2
from PIL import Image
import csv

# Function to load and convert image to grayscale
def preprocess(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    gray_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    return gray_img

# Function to calculate the average pixel value of an image
def calculate_average_pixel_value(gray_img):
    return np.mean(gray_img)

# Directory containing BMP files
input_directory = "./Samples_2"  # Replace with your folder path
output_csv = "average_pixel_values_2.csv"

# List to store results
results = []

# Loop through all BMP files in the directory
for filename in os.listdir(input_directory):
    if filename.endswith(".bmp"):
        file_path = os.path.join(input_directory, filename)
        gray_img = preprocess(file_path)  # Convert image to grayscale
        avg_pixel_value = calculate_average_pixel_value(gray_img)  # Calculate average pixel value

        # Append result as a tuple (filename, avg_pixel_value)
        results.append((filename, avg_pixel_value))

# Write results to a CSV file
with open(output_csv, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["File Name", "Average Pixel Value"])  # Header row

    for filename, avg_pixel_value in results:
        csv_writer.writerow([filename, avg_pixel_value])

print(f"Results saved to {output_csv}")