
from io import BytesIO
from PIL import Image, UnidentifiedImageError


MAX_IMAGE_SIZE_MB = 10
SUPPORTED_FORMATS = ("JPEG", "PNG")


def validate_image(image_bytes):
    """
    Validate an uploaded image before OCR processing.

    Returns image metadata if valid, otherwise an error.
    """

    if not image_bytes:
        return {
            "valid": False,
            "error": "No image was provided."
        }

    max_size = MAX_IMAGE_SIZE_MB * 1024 * 1024

    if len(image_bytes) > max_size:
        return {
            "valid": False,
            "error": "Image exceeds the 10 MB size limit."
        }

    try:
        image = Image.open(BytesIO(image_bytes))
        image.verify()

        # Reopen because verify() invalidates the image object.
        image = Image.open(BytesIO(image_bytes))

        if image.format not in SUPPORTED_FORMATS:
            return {
                "valid": False,
                "error": "Only JPEG and PNG images are supported."
            }

        return {
            "valid": True,
            "format": image.format,
            "width": image.width,
            "height": image.height,
            "size_bytes": len(image_bytes)
        }

    except (UnidentifiedImageError, OSError):
        return {
            "valid": False,
            "error": "The uploaded file is not a valid image."
        }
