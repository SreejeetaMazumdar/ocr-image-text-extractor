import os
import cv2
import pytesseract
from PIL import Image
import numpy as np


image_folder = "./Images"
output_folder = "./results"
os.makedirs(output_folder, exist_ok=True)

print(f"\nReading images from: {image_folder}")
print(f"Saving text outputs to: {output_folder}\n")


for filename in os.listdir(image_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(image_folder, filename)
        print(f"Processing: {filename}")

        # Load and preprocess image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Could not open image: {filename}")
            continue

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        pil_img = Image.fromarray(rgb)

        # OCR
        text = pytesseract.image_to_string(pil_img)
        clean_text = text.strip() if text.strip() else "[No text detected]"

        # Save to .txt file
        text_file = os.path.join(output_folder, f"{filename.split('.')[0]}.txt")
        with open(text_file, "w") as f:
            f.write(clean_text)

        print(f"Text saved: {text_file}\n")

print("All images processed successfully.\n")
