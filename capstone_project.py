# -*- coding: utf-8 -*-
"""Capstone project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hgCCeMeDlhiyredtkwl5tqwUOBn00w2M
"""

from google.colab import drive
drive.mount('/content/drive')

# Step 2: Install the required libraries

!pip install -U scikit-fuzzy
!pip install opencv-python-headless
!pip install numpy
!pip install opencv-python

!pip install scikit-image --upgrade

!pip install scikit-image

"""#preprossing"""

import numpy as np
from skimage import io, color, util

import cv2

# List of image paths
image_paths = [
    '/content/drive/MyDrive/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/dataset/class 1/10082347.jpg',
    '/content/drive/MyDrive/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/dataset/class 1/10010052.jpg',
    '/content/drive/MyDrive/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/dataset/class 1/10082347.jpg',
    '/content/drive/MyDrive/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/dataset/class 1/10090841.jpg',
    '/content/drive/MyDrive/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/dataset/class 1/10101477.jpg',
    '/content/drive/MyDrive/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/dataset/class 1/10160966.jpg',
    '/content/drive/MyDrive/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/dataset/class 1/10287332.jpg',
    '/content/drive/MyDrive/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/Grayscale-Image-to-RGB-image-converter-using-Transfer-Learning-Method-main/dataset/class 1/10287332.jpg',
]

# Read and display each image using cv2_imshow
from google.colab.patches import cv2_imshow

for image_path in image_paths:
    color_image = cv2.imread(image_path)
    cv2_imshow(color_image)

import matplotlib.pyplot as plt

for image_path in image_paths:
    color_image = cv2.imread(image_path)
    plt.imshow(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))
    plt.axis('on')  # Remove axis labels
    plt.show()

!pip install numpy
import numpy as np

# Define parameters for membership, non-membership, and hesitancy
threshold = 128  # Threshold for crisp image binarization
k = 1.0  # A parameter for hesitancy

for image_path in image_paths:
    # Load a color image
    color_image = cv2.imread(image_path)

    # Initialize arrays for membership, non-membership, and hesitancy
    membership = np.empty_like(color_image, dtype=np.float32)
    non_membership = np.empty_like(color_image, dtype=np.float32)
    hesitancy = np.empty_like(color_image, dtype=np.float32)

    # Convert the color image to intuitionistic fuzzy image
    for i in range(color_image.shape[0]):
        for j in range(color_image.shape[1]):
            pixel_value = color_image[i, j]

            # Calculate membership and non-membership values for each color channel (R, G, B)
            for channel in range(3):
                if pixel_value[channel] <= threshold:
                    membership[i, j, channel] = pixel_value[channel] / threshold
                    non_membership[i, j, channel] = 1.0 - membership[i, j, channel]
                else:
                    membership[i, j, channel] = 1.0 - (pixel_value[channel] - threshold) / (255 - threshold)
                    non_membership[i, j, channel] = 1.0 - membership[i, j, channel]

            # Calculate hesitancy value for the pixel
            hesitancy[i, j] = k * (non_membership[i, j].mean() - membership[i, j].mean())

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Define the function to calculate intuitionistic fuzzy entropy
def calculate_ife_entropy(membership, non_membership):
    # Avoid division by zero
    epsilon = 1e-10

    # Calculate IFE entropy
    entropy = membership * np.log2(membership + epsilon) + non_membership * np.log2(non_membership + epsilon)

    return entropy

# Define a color mapping scheme based on membership levels
blue_color = (255, 0, 0)  # Blue for low membership
green_color = (0, 255, 0)  # Green for medium membership
red_color = (0, 0, 255)  # Red for high membership

for image_path in image_paths:
    # Load a grayscale intuitionistic fuzzy image
    color_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) / 255.0  # Normalize to [0, 1]

    # Calculate intuitionistic fuzzy entropy for each pixel
    membership = color_image
    non_membership = 1.0 - membership

    # Define membership levels (you can adjust the thresholds)
    low_membership_threshold = 0.33
    high_membership_threshold = 0.66

    # Create colorized image based on membership levels
    colorized_image = np.zeros((color_image.shape[0], color_image.shape[1], 3), dtype=np.uint8)

    for i in range(color_image.shape[0]):
        for j in range(color_image.shape[1]):
            if membership[i, j] < low_membership_threshold:
                colorized_image[i, j] = blue_color  # Blue for low membership
            elif membership[i, j] < high_membership_threshold:
                colorized_image[i, j] = green_color  # Green for medium membership
            else:
                colorized_image[i, j] = red_color  # Red for high membership

    # Display the colorized image for this image
    cv2_imshow(colorized_image)

from google.colab.patches import cv2_imshow

for image_path in image_paths:
    # Load a color image
    color_image = cv2.imread(image_path)

    # Initialize arrays for membership, non-membership, and hesitancy
    membership = np.empty_like(color_image, dtype=np.float32)
    non_membership = np.empty_like(color_image, dtype=np.float32)
    hesitancy = np.empty_like(color_image, dtype=np.float32)

    # Convert the color image to intuitionistic fuzzy image
    for i in range(color_image.shape[0]):
        for j in range(color_image.shape[1]):
            pixel_value = color_image[i, j]

            # Calculate membership and non-membership values for each color channel (R, G, B)
            for channel in range(3):
                if pixel_value[channel] <= threshold:
                    membership[i, j, channel] = pixel_value[channel] / threshold
                    non_membership[i, j, channel] = 1.0 - membership[i, j, channel]
                else:
                    membership[i, j, channel] = 1.0 - (pixel_value[channel] - threshold) / (255 - threshold)
                    non_membership[i, j, channel] = 1.0 - membership[i, j, channel]

            # Calculate hesitancy value for the pixel
            hesitancy[i, j] = k * (non_membership[i, j].mean() - membership[i, j].mean())

    # Display the intuitionistic fuzzy image for this image
    cv2_imshow((membership * 255).astype(np.uint8))
    cv2_imshow((non_membership * 255).astype(np.uint8))
    cv2_imshow((hesitancy * 255).astype(np.uint8))

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Define the function to calculate intuitionistic fuzzy entropy
def calculate_ife_entropy(membership, non_membership):
    # Avoid division by zero
    epsilon = 1e-10

    # Calculate IFE entropy
    entropy = membership * np.log2(membership + epsilon) + non_membership * np.log2(non_membership + epsilon)

    return entropy

# Define a color mapping scheme based on membership levels
blue_color = (255, 0, 0)  # Blue for low membership
green_color = (0, 255, 0)  # Green for medium membership
red_color = (0, 0, 255)  # Red for high membership

# Function to colorize membership and non-membership based on the IFE value
def colorize_membership_ife(membership, non_membership, low_membership_threshold, high_membership_threshold):
    if membership < low_membership_threshold:
        return blue_color  # Blue for low membership
    elif membership < high_membership_threshold:
        return green_color  # Green for medium membership
    else:
        return red_color  # Red for high membership

for image_path in image_paths:
    # Load the colorized image (your previous result)
    colorized_image = cv2.imread(image_path)

    # Convert to grayscale
    grayscale_image = cv2.cvtColor(colorized_image, cv2.COLOR_BGR2GRAY) / 255.0

    # Calculate IFE for each pixel
    membership = grayscale_image
    non_membership = 1.0 - membership

    # Define membership levels (you can adjust the thresholds)
    low_membership_threshold = 0.4
    high_membership_threshold = 0.5

    # Create IFE colorized image
    ife_colorized_image = np.zeros((grayscale_image.shape[0], grayscale_image.shape[1], 3), dtype=np.uint8)

    for i in range(grayscale_image.shape[0]):
        for j in range(grayscale_image.shape[1]):
            membership_value = membership[i, j]
            non_membership_value = non_membership[i, j]

            color = colorize_membership_ife(membership_value, non_membership_value, low_membership_threshold, high_membership_threshold)

            ife_colorized_image[i, j] = color

    # Display the IFE colorized image
    cv2_imshow(ife_colorized_image)