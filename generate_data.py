import os
import cv2
import numpy as np
import pandas as pd
import random

# Parameters
image_size = (128, 128)  # Size of the generated images
num_images = 1000  # Number of images to generate
num_blobs = (1, 5)  # Min and max number of blobs per image
output_dir = "blob_images"
metadata_file = "metadata.csv"

# Define blob colors and categories
blob_categories = {
    (255, 0, 0): "red",
    (0, 255, 0): "green",
    (0, 0, 255): "blue",
    (255, 255, 0): "yellow",
    (255, 0, 255): "magenta",
    (0, 255, 255): "cyan"
}
blob_colors = list(blob_categories.keys())

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Metadata storage
metadata = []

# Generate images
for i in range(num_images):
    img = np.ones((image_size[0], image_size[1], 3), dtype=np.uint8) * 255  # White background
    num_blobs_in_image = random.randint(*num_blobs)
    
    for _ in range(num_blobs_in_image):
        radius = random.randint(5, 20)
        center = (random.randint(radius, image_size[0] - radius), random.randint(radius, image_size[1] - radius))
        color = random.choice(blob_colors)
        
        # Draw the blob
        cv2.circle(img, center, radius, color, -1)
        
        # Store metadata
        metadata.append([f"image_{i}.png", center[0], center[1], radius, blob_categories[color]])
    
    # Save image
    img_path = os.path.join(output_dir, f"image_{i}.png")
    cv2.imwrite(img_path, img)

# Save metadata to CSV
df = pd.DataFrame(metadata, columns=["image", "center_x", "center_y", "radius", "category"])
df.to_csv(metadata_file, index=False)

print(f"Generated {num_images} images and saved metadata to {metadata_file}.")
