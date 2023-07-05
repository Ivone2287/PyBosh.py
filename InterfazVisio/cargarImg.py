
from PIL import Image
import numpy as np
import cv2

A=np.load("C:/Users/6hs8de/Desktop/imgCrop.npy")
print(A)
im = Image.fromarray(A, 'RGB')
im.show()
