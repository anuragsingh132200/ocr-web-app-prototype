# ocr.py
from transformers import pipeline

def extract_text_from_image(image_path):
    # Load the OCR model
    ocr_model = pipeline("image-to-text", model="microsoft/trocr-base-handwritten")
    
    # Perform OCR on the image
    with open(image_path, "rb") as image_file:
        extracted_text = ocr_model(image_file)
    
    return extracted_text[0]['generated_text']