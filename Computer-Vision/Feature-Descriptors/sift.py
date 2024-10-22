# Import the necessary libraries
import cv2                   # OpenCV for image processing
from cv2 import imread        # To read images from the filesystem
from matplotlib import pyplot as plt  # Matplotlib for displaying the image

# Read the input image from a file
img = imread('images.jpg')    # 'images.jpg' is the image file being loaded

# Convert the image to grayscale
# SIFT works better on grayscale images as it detects intensity-based features
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a SIFT (Scale-Invariant Feature Transform) object
sift = cv2.SIFT_create()

# Detect keypoints and compute the descriptors using SIFT
# Keypoints are points in the image where significant features are found
# Descriptors are vectors that describe the local image patches around the keypoints
keypoints, descriptors = sift.detectAndCompute(imgGray, None)

# Draw keypoints on the grayscale image
# This will highlight the detected keypoints on the image
sift_image = cv2.drawKeypoints(imgGray, keypoints, img)

# Create a new figure using Matplotlib
plt.figure()

# Display the image with keypoints
plt.imshow(sift_image, cmap='gray')  # Use grayscale color mapping to display the image

# Save the output image with keypoints to the 'output' directory
plt.savefig('output/sift_image')     # Save the resulting image
