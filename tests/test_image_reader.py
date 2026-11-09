from io import BytesIO

from PIL import Image

from ai_guardian.perception import image_reader


def create_test_image():
    image = Image.new("RGB", (100, 60), color="white")

    buffer = BytesIO()
    image.save(buffer, format="PNG")

    return buffer.getvalue()


def test_read_image_returns_success_for_valid_image(monkeypatch):
    def mock_extract_text(image_bytes):
        return {
            "status": "SUCCESS",
            "text": "AI Guardian"
        }

    monkeypatch.setattr(
        image_reader,
        "extract_text",
        mock_extract_text
    )

    result = image_reader.read_image(create_test_image())

    assert result["status"] == "SUCCESS"
    assert result["text"] == "AI Guardian"


def test_read_image_rejects_invalid_image_without_running_ocr(monkeypatch):
    def unexpected_ocr_call(image_bytes):
        raise AssertionError("OCR must not run for invalid images")

    monkeypatch.setattr(
        image_reader,
        "extract_text",
        unexpected_ocr_call
    )

    result = image_reader.read_image(b"invalid image data")

    assert result["status"] == "INVALID_IMAGE"
    assert result["text"] == ""
    assert "error" in result


def test_read_image_propagates_ocr_failure(monkeypatch):
    def mock_extract_text(image_bytes):
        return {
            "status": "FAILED",
            "text": "",
            "error": "OCR processing failed."
        }

    monkeypatch.setattr(
        image_reader,
        "extract_text",
        mock_extract_text
    )

    result = image_reader.read_image(create_test_image())

    assert result["status"] == "FAILED"
    assert result["text"] == ""
    assert "error" in result
