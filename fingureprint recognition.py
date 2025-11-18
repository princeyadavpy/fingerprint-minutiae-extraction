import cv2
import numpy as np
from skimage.morphology import skeletonize
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt


def preprocess_fingerprint(img_path):
    # Load image
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian Blur to reduce noise
    img_blur = cv2.GaussianBlur(img, (5, 5), 0)

    # Otsu Thresholding
    thresh = threshold_otsu(img_blur)
    binary = img_blur > thresh

    # Skeletonize the binary image
    skeleton = skeletonize(binary)

    return skeleton


def extract_minutiae(skeleton):
    minutiae_endings = []
    minutiae_bifurcations = []

    # Check each pixel in the skeleton
    for y in range(1, skeleton.shape[0] - 1):
        for x in range(1, skeleton.shape[1] - 1):
            if skeleton[y, x]:  # white pixel (ridge)
                # Count 8-connected neighbors
                neighbors = np.sum(skeleton[y-1:y+2, x-1:x+2]) - 1

                if neighbors == 1:
                    minutiae_endings.append((x, y))  # Ridge Ending
                elif neighbors >= 3:
                    minutiae_bifurcations.append((x, y))  # Bifurcation

    return minutiae_endings, minutiae_bifurcations


def show_minutiae(skeleton, endings, bifurcations):
    plt.imshow(skeleton, cmap='gray')

    # Plot ridge endings (red)
    for x, y in endings:
        plt.plot(x, y, 'ro', markersize=3)

    # Plot bifurcations (blue)
    for x, y in bifurcations:
        plt.plot(x, y, 'bo', markersize=3)

    plt.title("Minutiae Points (Red = Endings, Blue = Bifurcations)")
    plt.show()


if __name__ == "__main__":
    img_path = "download.jpeg"

    # Preprocess and extract minutiae
    skeleton = preprocess_fingerprint(img_path)
    endings, bifurcations = extract_minutiae(skeleton)

    print("Ridge Endings:", len(endings))
    print("Bifurcations:", len(bifurcations))

    # Show results
    show_minutiae(skeleton, endings, bifurcations)
