import io, os
import pytesseract

from PIL import Image

def extract_text_from_image(image_bytes: bytes):
    """Extract image from the given path"""
    image_obj = Image.open(io.BytesIO(image_bytes))

    if os.name == 'nt':
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    result = pytesseract.image_to_string(image_obj, lang="eng")

    return result