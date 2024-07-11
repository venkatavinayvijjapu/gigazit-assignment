# Image to Pixel Conversion

This project demonstrates two approaches for converting an image into its pixel representation: direct pixel extraction and leveraging a pre-trained segmentation model.

## Approaches

### 1. Direct Pixel Extraction

It starts by loading the image from the specified file path (`'sample_image.jpg'`) using the `Image.open` function from the Pillow library. The image is then converted to the RGB color space with the `convert('RGB')` method to ensure consistency in pixel values. The width and height of the image are retrieved using the `size` attribute. An empty list named `pixels` is initialized to store the maximum RGB values. The code then iterates over each pixel in the image using nested loops: the outer loop iterates over the height (rows) and the inner loop over the width (columns). For each pixel, the RGB values are extracted using the `getpixel` method, and the maximum value among the R, G, and B components is appended to the `pixels` list. Finally, the list of maximum RGB values is printed. This approach effectively captures the most prominent color intensity at each pixel location.

#### Libraries Used
-  Python (3.x recommended)
- Pillow (PIL)
- NumPy
- Matplotlib
- OpenCV

### 2. Pixel Extraction using CV2

This Python script processes an image to extract the maximum RGB value for each pixel. It begins by importing the necessary libraries, OpenCV (`cv2`) for image processing and NumPy (`np`) for numerical operations. The `extract_max_rgb` function takes an image file path as input, reads the image using OpenCV, and converts the image from its default BGR color space to the RGB color space. It then calculates the maximum value for each pixel across the RGB channels using NumPy's `max` function. The resulting 2D array of maximum values is flattened into a 1D list of pixel values. The `main` function specifies the path to the input image, calls the `extract_max_rgb` function to get the pixel data, and prints this data to the console. The script is executed by calling the `main` function when the script is run as the main module.

#### Libraries Used
-  Python (3.x recommended)
- CV2
- NumPy

### 3. Using Pre-trained Model

This Python script applies a pre-trained semantic segmentation model to an image and visualizes the results. It starts by importing the necessary libraries: PyTorch (`torch`) and Torchvision (`models`, `transforms`) for model handling and image preprocessing, PIL for image operations, and Matplotlib for visualization. The `apply_segmentation` function loads the DeepLabV3 model with a ResNet-101 backbone, which is pre-trained on a segmentation task. It defines a series of image transformations to convert the image into a tensor and normalize it. The input image is read using PIL, converted to RGB, preprocessed, and formed into a mini-batch as required by the model. If a GPU is available, the image and model are moved to the GPU for faster processing. The segmentation model is then applied to the input image, and the output predictions are converted to a NumPy array.

The `visualize_segmentation` function takes the original image and the segmentation map to create a color-coded segmentation overlay. It reads the original image, converts it to a NumPy array, and generates a random color map to visualize different segments. The function then overlays the segmentation map on the original image and displays both the original and segmented images side by side using Matplotlib. The script concludes with a main block that defines the input image path, applies the segmentation model, and visualizes the segmentation output. This approach allows users to see the model's segmentation results on any input image.

#### Libraries Used
- opencv(CV2)
- numpy
- pytorch
- torchvision
- Pillow
- Matplotlib

## Visulaization:

The Repository consist of the codes for Pixel to image representationa and Original Image and the segmented Image Representation.


## Advantages and Disadvantages

### Direct Pixel Extraction
- **Advantages:** Simple and straightforward. Works for any image.
- **Disadvantages:** Does not provide any higher-level understanding of the image content.

### Pre-trained Segmentation Model
- **Advantages:** Provides a higher-level understanding of the image by grouping pixels.
- **Disadvantages:** Requires more computational resources and may need specific preprocessing steps.
