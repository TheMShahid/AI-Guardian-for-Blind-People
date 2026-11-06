
from io import BytesIO
import pytesseract
from PIL import Image

from ai_guardian.perception.image_preprocessor import preprocess_image


def extract_text(image_bytes):
    """
    Preprocess an image and extract printed English text.
    Returns a structured OCR result.
    """

    try:
        # Step 1: Preprocess image
        image = preprocess_image(image_bytes)

        # Step 2: Extract text using Tesseract
        recognized_text = pytesseract.image_to_string(
            image,
            lang="eng",
            config="--psm 6"
        ).strip()

        # Step 3: Check OCR result
        if not recognized_text:
            return {
                "status": "NO_TEXT",
                "text": ""
            }

        return {
            "status": "SUCCESS",
            "text": recognized_text
        }

    except Exception:
        return {
            "status": "FAILED",
            "text": "",
            "error": "OCR processing failed."
        }
