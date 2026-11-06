
from io import BytesIO
from PIL import Image, ImageEnhance


def preprocess_image(image_bytes):
    """
    Convert image to grayscale, resize and improve contrast.
    Returns a processed PIL image.
    """

    image = Image.open(BytesIO(image_bytes)).convert("RGB")

    # Convert to grayscale
    image = image.convert("L")

    # Increase image dimensions
    image = image.resize(
        (image.width * 2, image.height * 2)
    )

    # Improve contrast
    image = ImageEnhance.Contrast(image).enhance(1.5)

    return image
