# Fingerprint Minutiae Extraction

Simple Python script to preprocess fingerprint images, skeletonize them, and detect minutiae points (ridge endings & bifurcations).

## Features
- Preprocessing with Gaussian Blur + Otsu threshold
- Skeletonization of fingerprint
- Minutiae detection using 8-neighbor check
- Visualization of endings (red) and bifurcations (blue)

## Requirements
pip install opencv-python numpy scikit-image matplotlib

## Usage
1. Put your fingerprint image in the same folder (e.g., download.jpeg).
2. Run:
   python fingerprint_minutiae.py

## Author
Prince Yadav

