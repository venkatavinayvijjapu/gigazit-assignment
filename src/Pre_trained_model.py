import torch
from torchvision import models, transforms
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def apply_segmentation(image_path):
    # Load the pre-trained DeepLabV3 model
    model = models.segmentation.deeplabv3_resnet101(pretrained=True).eval()

    # Define the image transformations
    preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    # Load the image
    input_image = Image.open(image_path).convert("RGB")
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)  # Create a mini-batch as expected by the model

    # Move the input to the GPU for speed if available
    if torch.cuda.is_available():
        input_batch = input_batch.to('cuda')
        model.to('cuda')

    # Apply the segmentation model
    with torch.no_grad():
        output = model(input_batch)['out'][0]
    output_predictions = output.argmax(0)

    return output_predictions.cpu().numpy()

def visualize_segmentation(image_path, segmentation_map):
    # Load the image
    input_image = Image.open(image_path).convert("RGB")
    input_image = np.array(input_image)

    # Create a color map for the segmentation
    colormap = np.random.randint(0, 255, (21, 3), dtype=np.uint8)
    segmentation_image = colormap[segmentation_map]

    # Overlay the segmentation on the original image
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(input_image)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Segmented Image")
    plt.imshow(segmentation_image)
    plt.axis('off')

    plt.show()
    print(segmentation_image)

if __name__ == "__main__":
    # Define the input image path
    input_image_path = 'sample_image.jpg'

    # Apply the segmentation model
    segmentation_map = apply_segmentation(input_image_path)

    # Visualize the segmentation output
    visualize_segmentation(input_image_path, segmentation_map)