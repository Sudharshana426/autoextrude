import sys
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import json
#import open3d as o3d

# Ensure a path was passed in as an argument
print(sys.argv)
if len(sys.argv) < 2:
	raise ValueError("No image path provided. Please check the script call.")

# Get the path from the command-line argument
image_path = sys.argv[1]
# Load the floor plan image
image = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded properly
if image is None:
	raise FileNotFoundError("Image not found. Please check the file path.")

# Apply Gaussian Blur to reduce noise
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Threshold the image to create a binary image
_, binary_image = cv2.threshold(blurred_image, 150, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter out small contours (likely text or small annotations)
filtered_image = binary_image.copy()
for contour in contours:
	if cv2.contourArea(contour) < 80:  # Threshold for small areas
		cv2.drawContours(filtered_image, [contour], -1, 0, -1)  # Remove small contours

# Edge detection on the filtered image
edges = cv2.Canny(filtered_image, threshold1=50, threshold2=150)

# Dilate the edges
kernel = np.ones((3, 3), np.uint8)
dilated_edges = cv2.dilate(edges, kernel, iterations=1)

contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

vector_data = []
for cnt in contours:
	ep = 0.01*cv2.arcLength(cnt,True)
	approx = cv2.approxPolyDP(cnt,ep,True)
	
	vector_data.append(approx)
	
jsdata = []
for vc in vector_data:
	ptl = []
	for pt in vc:
		x,y = pt[0]
		ptl.append((int(x),int(y)))
	jsdata.append({"points":ptl})
	
print(json.dumps({'walls':jsdata}))

with open("godot_data.json",'w') as f:
	json.dump({'walls':jsdata},f)
	print("Saved File Nigga!")
