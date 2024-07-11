import numpy as np
from PIL import Image

def pixel_list_to_image(pixel_list, output_image_path):
    # Convert the list to a NumPy array
    pixel_array = np.array(pixel_list, dtype=int)
    # Convert the NumPy array to an image
    image = Image.fromarray(pixel_array.astype('uint8'), mode='L')
    # Save the image
    image.save(output_image_path)

if __name__ == "__main__":
    # Define input and output paths
    input_pixel_path = pixels
    output_image_path = 'reconstructed_image.jpg'
    
    # Load the pixel list from the text file
    with open(input_pixel_path, 'r') as f:
        pixel_list = [list(map(int, line.split())) for line in f]
    
    # Convert pixel list to image
    pixel_list_to_image(pixel_list, output_image_path)
    
    print(f"Image reconstructed and saved to {output_image_path}")