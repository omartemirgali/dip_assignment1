import cv2, os
import numpy as np
from scipy.interpolate import UnivariateSpline

def blur_image(img_path):
    img = cv2.imread(img_path)
    blurred = cv2.blur(img, (5, 5))
    cv2.imwrite(os.path.join('static/filtered_images/', os.path.basename(img_path)), blurred)

def sepia(img_path):
    img = cv2.imread(img_path)
    res = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res = np.array(res, dtype=np.float64)
    res = cv2.transform(res, np.matrix([[0.393, 0.769, 0.189],
                                        [0.349, 0.686, 0.168],
                                        [0.272, 0.534, 0.131]]))
    res[np.where(res > 255)] = 255
    res = np.array(res, dtype=np.uint8)
    res = cv2.cvtColor(res, cv2.COLOR_RGB2BGR)
    cv2.imwrite(os.path.join('static/filtered_images/', os.path.basename(img_path)), res)

increase_table = UnivariateSpline(x=[0, 64, 128, 255], y=[0, 75, 155, 255])(range(256))
decrease_table = UnivariateSpline(x=[0, 64, 128, 255], y=[0, 45, 95, 255])(range(256))

def warm(img_path):
    img = cv2.imread(img_path)
    b, g, r  = cv2.split(img)
    r = cv2.LUT(r, increase_table).astype(np.uint8)
    b = cv2.LUT(b, decrease_table).astype(np.uint8)
    output_image = cv2.merge((b, g, r))
    cv2.imwrite(os.path.join('static/filtered_images/', os.path.basename(img_path)), output_image)

def cold(img_path):
    img = cv2.imread(img_path)
    b, g, r = cv2.split(img)
    r = cv2.LUT(r, decrease_table).astype(np.uint8)
    b = cv2.LUT(b, increase_table).astype(np.uint8)
    output_image = cv2.merge((b, g, r))
    cv2.imwrite(os.path.join('static/filtered_images/', os.path.basename(img_path)), output_image)