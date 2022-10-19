import cv2
import numpy as np

img = cv2.imread('peonies.jpg')

int_matrix = np.ones(img.shape, dtype= "uint8") * 80

brightened = cv2.add(img, int_matrix)
cv2.imwrite("bright.jpg", brightened)

darkened = cv2.subtract(img, int_matrix)
cv2.imwrite("dark.jpg", darkened)