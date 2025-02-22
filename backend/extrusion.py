import cv2
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d

# Load the floor plan image
image = cv2.imread('floor2.jpeg', cv2.IMREAD_GRAYSCALE)

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
    if cv2.contourArea(contour) < 100:  # Threshold for small areas
        cv2.drawContours(filtered_image, [contour], -1, 0, -1)  # Remove small contours

# Edge detection on the filtered image
edges = cv2.Canny(filtered_image, threshold1=50, threshold2=150)

# Dilate the edges
kernel = np.ones((3, 3), np.uint8)
dilated_edges = cv2.dilate(edges, kernel, iterations=1)

# Display the original and processed images
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")

plt.subplot(1, 3, 3)
plt.imshow(dilated_edges, cmap='gray')
plt.title("Edge Detection ")

plt.show()

# Extraction of vector points
contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

vector_data = []
for contour in contours:
    for point in contour:
        x, y = point[0]
        vector_data.append((x, y))

# Convert vector data into 3D points
wall_height = 50  # Adjust height as needed

vertices = []
faces = []

for i in range(len(vector_data) - 1):
    x1, y1 = vector_data[i]
    x2, y2 = vector_data[i + 1]

    # Create bottom and top vertices
    v0 = (x1, y1, 0)  # Bottom 1
    v1 = (x2, y2, 0)  # Bottom 2
    v2 = (x1, y1, wall_height)  # Top 1
    v3 = (x2, y2, wall_height)  # Top 2

    # Store vertices
    base_idx = len(vertices)
    vertices.extend([v0, v1, v2, v3])

    # Define two triangles per wall segment
    faces.append([base_idx, base_idx + 1, base_idx + 2])  # Bottom-left triangle
    faces.append([base_idx + 1, base_idx + 3, base_idx + 2])  # Top-right triangle

# Convert to Open3D format
vertices = np.array(vertices, dtype=np.float64)
faces = np.array(faces, dtype=np.int32)

# Create mesh
mesh = o3d.geometry.TriangleMesh()
mesh.vertices = o3d.utility.Vector3dVector(vertices)
mesh.triangles = o3d.utility.Vector3iVector(faces)
mesh.compute_vertex_normals()

# Enable Interactivity (Hover, Rotate, Zoom)
vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(mesh)
vis.run()
vis.destroy_window()


# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import open3d as o3d

# # Load the floor plan image
# image = cv2.imread('floor2.jpeg', cv2.IMREAD_GRAYSCALE)
# if image is None:
#     raise FileNotFoundError("Image not found. Please check the file path.")

# # Apply Gaussian Blur to reduce noise
# blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# # Threshold the image to create a binary image
# _, binary_image = cv2.threshold(blurred_image, 150, 255, cv2.THRESH_BINARY_INV)

# # Find contours
# contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Filter out small contours (likely text or small annotations)
# filtered_contours = []
# for contour in contours:
#     if cv2.contourArea(contour) > 100:  # Threshold for small areas
#         filtered_contours.append(contour)

# # Approximate polygons from contours
# approx_contours = []
# for contour in filtered_contours:
#     epsilon = 0.01 * cv2.arcLength(contour, True)  # Reduce epsilon for sharper walls
#     approx = cv2.approxPolyDP(contour, epsilon, True)
#     if len(approx) <= 80:  # Reduce to 80 points
#         approx_contours.append(approx)

# # Create an empty image to visualize the approximation
# approx_image = np.zeros_like(binary_image)
# cv2.drawContours(approx_image, approx_contours, -1, 255, 2)  # Increase thickness for better visibility

# # Display the original and processed images
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# plt.imshow(image, cmap='gray')
# plt.title("Original Image")

# plt.subplot(1, 2, 2)
# plt.imshow(approx_image, cmap='gray')
# plt.title("Approximated Contours")

# plt.show()

# # Extract vector points
# vector_data = []
# for contour in approx_contours:
#     for point in contour:
#         x, y = point[0]
#         vector_data.append((x, y))

# # Convert vector data into 3D points
# wall_thickness = 5  # Define a wall thickness for better structure
# wall_height = 50
# vertices = []
# faces = []

# for i in range(len(vector_data) - 1):
#     x1, y1 = vector_data[i]
#     x2, y2 = vector_data[i + 1]

#     # Define the four corners of the wall segment with thickness
#     v0 = (x1 - wall_thickness, y1 - wall_thickness, 0)
#     v1 = (x2 + wall_thickness, y2 - wall_thickness, 0)
#     v2 = (x1 - wall_thickness, y1 - wall_thickness, wall_height)
#     v3 = (x2 + wall_thickness, y2 - wall_thickness, wall_height)
#     v4 = (x1 + wall_thickness, y1 + wall_thickness, 0)
#     v5 = (x2 - wall_thickness, y2 + wall_thickness, 0)
#     v6 = (x1 + wall_thickness, y1 + wall_thickness, wall_height)
#     v7 = (x2 - wall_thickness, y2 + wall_thickness, wall_height)

#     base_idx = len(vertices)
#     vertices.extend([v0, v1, v2, v3, v4, v5, v6, v7])

#     # Define the six faces per wall segment
#     faces.extend([
#         [base_idx, base_idx + 1, base_idx + 2], [base_idx + 1, base_idx + 3, base_idx + 2],  # Front face
#         [base_idx + 4, base_idx + 5, base_idx + 6], [base_idx + 5, base_idx + 7, base_idx + 6],  # Back face
#         [base_idx, base_idx + 4, base_idx + 2], [base_idx + 4, base_idx + 6, base_idx + 2],  # Left face
#         [base_idx + 1, base_idx + 5, base_idx + 3], [base_idx + 5, base_idx + 7, base_idx + 3],  # Right face
#         [base_idx + 2, base_idx + 3, base_idx + 6], [base_idx + 3, base_idx + 7, base_idx + 6],  # Top face
#         [base_idx, base_idx + 1, base_idx + 4], [base_idx + 1, base_idx + 5, base_idx + 4]   # Bottom face
#     ])

# # Convert to Open3D format
# vertices = np.array(vertices, dtype=np.float64)
# faces = np.array(faces, dtype=np.int32)

# mesh = o3d.geometry.TriangleMesh()
# mesh.vertices = o3d.utility.Vector3dVector(vertices)
# mesh.triangles = o3d.utility.Vector3iVector(faces)
# mesh.compute_vertex_normals()

# # Visualize in Open3D
# vis = o3d.visualization.Visualizer()
# vis.create_window()
# vis.add_geometry(mesh)
# vis.run()
# vis.destroy_window()


# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import open3d as o3d

# # Load the floor plan image
# image = cv2.imread('floor2.jpeg', cv2.IMREAD_GRAYSCALE)
# if image is None:
#     raise FileNotFoundError("Image not found. Please check the file path.")

# # Apply Gaussian Blur to reduce noise
# blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# # Threshold the image to create a binary image
# _, binary_image = cv2.threshold(blurred_image, 150, 255, cv2.THRESH_BINARY_INV)

# # Find contours
# contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Filter out small contours (likely text or small annotations)
# filtered_contours = []
# for contour in contours:
#     if cv2.contourArea(contour) > 100:  # Threshold for small areas
#         filtered_contours.append(contour)

# # Approximate polygons from contours
# approx_contours = []
# for contour in filtered_contours:
#     epsilon = 0.02 * cv2.arcLength(contour, True)
#     approx = cv2.approxPolyDP(contour, epsilon, True)
#     if len(approx) <= 80:  # Reduce to 80 points
#         approx_contours.append(approx)

# # Create an empty image to visualize the approximation
# approx_image = np.zeros_like(binary_image)
# cv2.drawContours(approx_image, approx_contours, -1, 255, 1)

# # Display the original and processed images
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# plt.imshow(image, cmap='gray')
# plt.title("Original Image")

# plt.subplot(1, 2, 2)
# plt.imshow(approx_image, cmap='gray')
# plt.title("Approximated Contours")

# plt.show()

# # Extract vector points
# vector_data = []
# for contour in approx_contours:
#     for point in contour:
#         x, y = point[0]
#         vector_data.append((x, y))

# # Convert vector data into 3D points
# wall_height = 50
# vertices = []
# faces = []

# for i in range(len(vector_data) - 1):
#     x1, y1 = vector_data[i]
#     x2, y2 = vector_data[i + 1]

#     # Create bottom and top vertices
#     v0 = (x1, y1, 0)
#     v1 = (x2, y2, 0)
#     v2 = (x1, y1, wall_height)
#     v3 = (x2, y2, wall_height)

#     base_idx = len(vertices)
#     vertices.extend([v0, v1, v2, v3])

#     # Define two triangles per wall segment
#     faces.append([base_idx, base_idx + 1, base_idx + 2])
#     faces.append([base_idx + 1, base_idx + 3, base_idx + 2])

# # Convert to Open3D format
# vertices = np.array(vertices, dtype=np.float64)
# faces = np.array(faces, dtype=np.int32)

# mesh = o3d.geometry.TriangleMesh()
# mesh.vertices = o3d.utility.Vector3dVector(vertices)
# mesh.triangles = o3d.utility.Vector3iVector(faces)
# mesh.compute_vertex_normals()

# # Visualize in Open3D
# vis = o3d.visualization.Visualizer()
# vis.create_window()
# vis.add_geometry(mesh)
# vis.run()
# vis.destroy_window()
