import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img_path= 'sample_image.jpg'
image = Image.open(img_path)
    
# Convert image to RGB (if not already in RGB format)
image = image.convert('RGB')
    
# Get the width and height of the image
width, height = image.size
    
# Initialize a list to store the pixel values
pixels = []
    
    # Iterate over each pixel in the image
for y in range(height):
    for x in range(width):
        r, g, b = image.getpixel((x, y))
        pixels.append(max(r, g, b))
print(pixels)