
from ai_guardian.perception.image_validator import validate_image
from ai_guardian.perception.ocr_engine import extract_text


def read_image(image_bytes):
    """
    Validate an image and extract its printed text.
    """

    # Step 1: Validate image
    validation = validate_image(image_bytes)

    if not validation["valid"]:
        return {
            "status": "INVALID_IMAGE",
            "text": "",
            "error": validation["error"]
        }

    # Step 2: Run OCR
    result = extract_text(image_bytes)

    return result
