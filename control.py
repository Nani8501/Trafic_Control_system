import numpy as np
from CannyEdgeDetector import *
import cv2

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def applyCanny(filename):
    imgs = []
    img = mpimg.imread(filename)
    img = rgb2gray(img)
    imgs.append(img)
    edge = CannyEdgeDetector(imgs, sigma=1.4, kernel_size=5, lowthreshold=0.09, highthreshold=0.20, weak_pixel=100)
    imgs = edge.detect()
    for i, img in enumerate(imgs):
        if img.shape[0] == 3:
            img = img.transpose(1,2,0)
    cv2.imwrite("static/gray/test.png",img)
    temp = []
    img1 = mpimg.imread('static/gray/test.png')
    img2 = mpimg.imread('static/gray/refrence.png')
    temp.append(img1)
    temp.append(img2)
    return temp

def pixelcount():
    img = cv2.imread('static/gray/processed_file.png', cv2.IMREAD_GRAYSCALE)
    sample_pixels = np.sum(img == 255)
    
    img = cv2.imread('static/gray/reference_file.png', cv2.IMREAD_GRAYSCALE)
    refrence_pixels = np.sum(img == 255)
    print("Pixel count:",sample_pixels, refrence_pixels)
    return sample_pixels, refrence_pixels

def timeAllocation(sample_pixels, refrence_pixels):
    avg =(sample_pixels/refrence_pixels) *100
    if avg >= 90:
        return "Traffic is very high allocation green signal time : 60 secs"
    if avg > 85 and avg < 90:
        return "Traffic is high allocation green signal time : 50 secs"
    if avg > 75 and avg <= 85:
        return "Traffic is moderate green signal time : 40 secs"
    if avg > 50 and avg <= 75:
        return "Traffic is low allocation green signal time : 30 secs"
    if avg <= 50:
        return "Traffic is very low allocation green signal time : 20 secs"
