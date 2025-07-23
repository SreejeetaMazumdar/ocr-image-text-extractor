import cv2
import pytesseract
from PIL import Image
import os
image_path = "sample_image2pyt.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Image not found or cannot be opened.")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    pil_img = Image.fromarray(gray_rgb)

    text = pytesseract.image_to_string(pil_img)

    print("\n--- Extracted Text ---\n")
    print(text)