import numpy as np
import cv2

a = [[[[1, 2], [3, 4]], [[1, 2], [3, 4]], [[1, 2], [3, 4]]], [[[6, 7], [8, 9]], [[6, 7], [8, 9]], [[6, 7], [8, 9]]]]
b = np.pad(a, (2, 2), 'wrap')
print(b)