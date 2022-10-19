import cv2, os

def blur_image(img_path):
    img = cv2.imread(img_path)
    blurred = cv2.blur(img, (5, 5))
    cv2.imwrite(os.path.join('static/filtered_images/', os.path.basename(img_path)), blurred)
