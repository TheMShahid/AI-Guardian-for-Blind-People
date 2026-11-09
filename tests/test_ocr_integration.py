from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
import pytesseract

from ai_guardian.perception.image_reader import read_image


def create_text_image():
    image = Image.new("RGB", (1200, 300), color="white")
    draw = ImageDraw.Draw(image)

    font_path = (
        "/usr/share/fonts/truetype/liberation/"
        "LiberationSans-Bold.ttf"
    )

    font = ImageFont.truetype(font_path, size=110)

    draw.text(
        (50, 70),
        "GUARDIAN 123",
        fill="black",
        font=font
    )

    buffer = BytesIO()
    image.save(buffer, format="PNG")

    return buffer.getvalue()


def test_real_tesseract_recognizes_text():
    pytesseract.get_tesseract_version()

    result = read_image(create_text_image())

    assert result["status"] == "SUCCESS"
    assert "GUARDIAN 123" in " ".join(
        result["text"].upper().split()
    )
