import cv2
import numpy as np

def extract_max_rgb(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert image from BGR (default in OpenCV) to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Get the maximum value for each pixel across the RGB channels
    max_values = np.max(image_rgb, axis=2)
    
    # Flatten the 2D array of max values into a 1D list
    pixels = max_values.flatten().tolist()
    
    return pixels

def main():
    # Path to the input image
    image_path = 'sample_image.jpg'
    
    # Extract pixel data
    pixel_data = extract_max_rgb(image_path)
    
    # Output the pixel data
    print("Pixel Data:")
    print(pixel_data)

if __name__ == "__main__":
    main()
