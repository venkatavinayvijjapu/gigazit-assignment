import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Plot the original image
image = Image.open(img_path).convert('RGB')
ax1.imshow(image)
ax1.set_title("Original Image")
ax1.axis('off')

pixel_data = np.array(pixels, dtype=np.uint8).reshape((height, width))
    # Plot the processed pixel data
ax2.matshow(pixel_data, cmap='gray')
ax2.set_title("Processed Image (Max RGB Value)")
    
    # Annotate the pixel values
for i in range(pixel_data.shape[0]):
    for j in range(pixel_data.shape[1]):
        value = pixel_data[i, j]
        if value > 0:
            ax2.text(j, i, f"{value}", va='center', ha='center', color='white', fontsize=8, bbox=dict(facecolor='gray', edgecolor='none', pad=1))
    
plt.show()