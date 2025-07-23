# OCR Text Extractor
This script extracts text from images using Tesseract OCR and saves the output as `.txt` files in a separate folder.
# Project Structure
```OCR_Image_to_Text_Extractor/
├── Images/                # Put your image files here (jpg, png, jpeg)
├── results/               # This will be auto-created after running the script
├── image_to_text_ocr.py   # Main Python script
├── README.md              # Instructions and setup guide
```
# What This Script Does
- Looks inside the `Images/` folder
- Extracts text from each image using OCR
- Saves the text as a `.txt` file inside the `results/` folder
# Install Required Python Libraries
Run this command in your terminal:
```bash
pip install opencv-python pytesseract pillow numpy
```
# Install Tesseract OCR Engine (Mandatory)
Tesseract is the actual OCR engine used by this script. Without this, it won’t extract any text.
# macOS (using Homebrew):
```bash
brew install tesseract
```
# Windows:
Download from: https://github.com/tesseract-ocr/tesseract  
During installation, make sure to check the box that adds Tesseract to your system PATH.
# Add Your Images
Place `.jpg`, `.png`, or `.jpeg` files inside the `Images/` folder.
Example:
```
Images/
├── sample_image.jpg
├── sample_image2.jpg
```
# Run the Script

In terminal, go to the project folder and run:
```bash
python image_to_text_ocr.py
```
# Example Output

Input:
```
Images/sample1.jpg
```

Output:
```
results/sample1.txt
```
The `.txt` file will contain the extracted text from the image.
