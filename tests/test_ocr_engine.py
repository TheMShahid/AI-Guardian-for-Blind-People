from io import BytesIO

from PIL import Image

from ai_guardian.perception import ocr_engine


def create_test_image():
    image = Image.new("RGB", (100, 60), color="white")

    buffer = BytesIO()
    image.save(buffer, format="PNG")

    return buffer.getvalue()


def test_ocr_returns_success_when_text_is_recognized(monkeypatch):
    def mock_ocr(*args, **kwargs):
        return "AI Guardian"

    monkeypatch.setattr(
        ocr_engine.pytesseract,
        "image_to_string",
        mock_ocr
    )

    result = ocr_engine.extract_text(create_test_image())

    assert result["status"] == "SUCCESS"
    assert result["text"] == "AI Guardian"


def test_ocr_returns_no_text_when_result_is_empty(monkeypatch):
    def mock_ocr(*args, **kwargs):
        return "   "

    monkeypatch.setattr(
        ocr_engine.pytesseract,
        "image_to_string",
        mock_ocr
    )

    result = ocr_engine.extract_text(create_test_image())

    assert result["status"] == "NO_TEXT"
    assert result["text"] == ""


def test_ocr_returns_failed_when_engine_raises_exception(monkeypatch):
    def mock_ocr(*args, **kwargs):
        raise RuntimeError("Simulated OCR failure")

    monkeypatch.setattr(
        ocr_engine.pytesseract,
        "image_to_string",
        mock_ocr
    )

    result = ocr_engine.extract_text(create_test_image())

    assert result["status"] == "FAILED"
    assert result["text"] == ""
    assert "error" in result
