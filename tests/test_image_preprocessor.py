from io import BytesIO

from PIL import Image

from ai_guardian.perception.image_preprocessor import preprocess_image


def create_test_image():
    image = Image.new("RGB", (100, 60), color=(120, 150, 180))

    buffer = BytesIO()
    image.save(buffer, format="PNG")

    return buffer.getvalue()


def test_preprocessor_returns_pillow_image():
    result = preprocess_image(create_test_image())

    assert isinstance(result, Image.Image)


def test_preprocessor_converts_image_to_grayscale():
    result = preprocess_image(create_test_image())

    assert result.mode == "L"


def test_preprocessor_doubles_image_dimensions():
    result = preprocess_image(create_test_image())

    assert result.size == (200, 120)


def test_preprocessor_corrects_exif_orientation():
    image = Image.new("RGB", (40, 20), color=(120, 150, 180))

    exif = Image.Exif()
    exif[274] = 6  # Rotate 90 degrees clockwise.

    buffer = BytesIO()
    image.save(buffer, format="JPEG", exif=exif)

    result = preprocess_image(buffer.getvalue())

    assert result.size == (40, 80)
    assert result.mode == "L"


def test_preprocessor_handles_rgba_with_white_background():
    image = Image.new("RGBA", (40, 20), color=(0, 0, 0, 0))
    image.putpixel((0, 0), (0, 0, 0, 255))

    buffer = BytesIO()
    image.save(buffer, format="PNG")

    result = preprocess_image(buffer.getvalue())

    assert result.mode == "L"
    assert result.size == (80, 40)
    assert result.getpixel((20, 20)) == 255


def test_preprocessor_handles_grayscale_input():
    image = Image.new("L", (40, 20), color=150)

    buffer = BytesIO()
    image.save(buffer, format="PNG")

    result = preprocess_image(buffer.getvalue())

    assert result.mode == "L"
    assert result.size == (80, 40)


def test_preprocessor_handles_palette_input():
    image = Image.new("P", (40, 20))

    image.putpalette(
        [255, 255, 255, 0, 0, 0] + [0, 0, 0] * 254
    )

    image.putpixel((0, 0), 1)

    buffer = BytesIO()
    image.save(buffer, format="PNG")

    result = preprocess_image(buffer.getvalue())

    assert result.mode == "L"
    assert result.size == (80, 40)
