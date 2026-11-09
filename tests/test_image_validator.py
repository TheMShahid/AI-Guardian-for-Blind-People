from io import BytesIO

from PIL import Image

from ai_guardian.perception.image_validator import validate_image


def create_image(image_format="PNG"):
    """Create a small synthetic image for testing."""
    image = Image.new("RGB", (100, 100), color="white")
    buffer = BytesIO()
    image.save(buffer, format=image_format)
    return buffer.getvalue()


def test_valid_png_is_accepted():
    result = validate_image(create_image("PNG"))

    assert result["valid"] is True
    assert result["format"] == "PNG"
    assert result["width"] == 100
    assert result["height"] == 100


def test_valid_jpeg_is_accepted():
    result = validate_image(create_image("JPEG"))

    assert result["valid"] is True
    assert result["format"] == "JPEG"


def test_empty_input_is_rejected():
    result = validate_image(b"")

    assert result["valid"] is False
    assert "error" in result


def test_corrupted_image_is_rejected():
    result = validate_image(b"This is not a valid image")

    assert result["valid"] is False
    assert "error" in result


def test_unsupported_gif_is_rejected():
    result = validate_image(create_image("GIF"))

    assert result["valid"] is False
    assert "error" in result


def test_image_exceeding_size_limit_is_rejected():
    oversized_data = b"x" * (10 * 1024 * 1024 + 1)

    result = validate_image(oversized_data)

    assert result["valid"] is False
    assert "10 MB" in result["error"]



def test_image_exceeding_pixel_limit_is_rejected():
    from io import BytesIO
    from PIL import Image

    image = Image.new("RGB", (4000, 3000), color="white")

    buffer = BytesIO()
    image.save(buffer, format="PNG")

    result = validate_image(buffer.getvalue())

    assert result["valid"] is False
    assert "pixel" in result["error"].lower()
