from io import BytesIO
from PIL import Image, ImageEnhance, ImageOps


def preprocess_image(image_bytes):
    """
    Correct EXIF orientation, normalize transparency,
    convert to grayscale, resize and improve contrast.
    Returns a processed PIL image.
    """

    image = Image.open(BytesIO(image_bytes))

    # Normalize image orientation using EXIF metadata.
    image = ImageOps.exif_transpose(image)

    # Composite transparent images onto a white background.
    if image.mode in ("RGBA", "LA") or (
        image.mode == "P" and "transparency" in image.info
    ):
        image = image.convert("RGBA")

        background = Image.new(
            "RGBA",
            image.size,
            (255, 255, 255, 255)
        )

        image = Image.alpha_composite(background, image)

    image = image.convert("RGB")
    image = image.convert("L")

    # Increase image dimensions.
    image = image.resize(
        (image.width * 2, image.height * 2)
    )

    # Improve contrast.
    image = ImageEnhance.Contrast(image).enhance(1.5)

    return image
