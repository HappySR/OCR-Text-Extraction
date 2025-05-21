import argparse
import os
import sys
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import cv2
import numpy as np

class OCRProcessor:
    """A class to handle OCR processing of images."""
    
    def __init__(self, tesseract_path=None):
        """Initialize the OCR processor.
        
        Args:
            tesseract_path: Optional path to tesseract executable
        """
        # Set tesseract path if provided
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
            
    def preprocess_image(self, image):
        """Apply preprocessing to improve OCR results.
        
        Args:
            image: PIL Image object
            
        Returns:
            Processed PIL Image
        """
        # Convert to grayscale if not already
        if image.mode != 'L':
            image = image.convert('L')
            
        # Increase contrast
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2.0)
        
        # Apply gaussian blur to reduce noise
        image = image.filter(ImageFilter.GaussianBlur(radius=0.5))
        
        # Apply threshold to create binary image
        image = image.point(lambda x: 0 if x < 128 else 255, '1')
        
        return image
        
    def preprocess_image_cv2(self, image_path):
        """Alternative preprocessing using OpenCV.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Processed image as numpy array
        """
        # Read image
        img = cv2.imread(image_path)
        
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Apply threshold to get binary image
        _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Apply dilation and erosion for noise reduction
        kernel = np.ones((1, 1), np.uint8)
        img_processed = cv2.dilate(binary, kernel, iterations=1)
        img_processed = cv2.erode(img_processed, kernel, iterations=1)
        
        # Apply median blur
        img_processed = cv2.medianBlur(img_processed, 3)
        
        return img_processed
    
    def extract_text(self, image_path, use_cv2=True, lang='eng'):
        """Extract text from an image.
        
        Args:
            image_path: Path to the image file
            use_cv2: Whether to use OpenCV preprocessing
            lang: Language for OCR (default: English)
            
        Returns:
            Extracted text as string
        """
        try:
            if not os.path.exists(image_path):
                print(f"Error: Image file not found at {image_path}")
                return ""
                
            if use_cv2:
                # Use OpenCV preprocessing
                img_processed = self.preprocess_image_cv2(image_path)
                text = pytesseract.image_to_string(img_processed, lang=lang)
            else:
                # Use PIL preprocessing
                with Image.open(image_path) as img:
                    img_processed = self.preprocess_image(img)
                    text = pytesseract.image_to_string(img_processed, lang=lang)
            
            return text.strip()
            
        except Exception as e:
            print(f"Error processing image: {e}")
            return ""


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Extract text from images using OCR')
    parser.add_argument('image_path', help='Path to the image file')
    parser.add_argument('--tesseract', '-t', help='Path to tesseract executable')
    parser.add_argument('--lang', '-l', default='eng', help='Language for OCR (default: English)')
    parser.add_argument('--no-cv2', action='store_true', help='Do not use OpenCV preprocessing')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Create OCR processor
    ocr = OCRProcessor(args.tesseract)
    
    # Extract text
    result = ocr.extract_text(args.image_path, not args.no_cv2, args.lang)
    
    # Print result
    if result:
        print("\n--- OCR Result ---")
        print(result)
        print("------------------")
    else:
        print("No text was extracted from the image.")


if __name__ == "__main__":
    main()
