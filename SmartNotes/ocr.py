from PIL import Image, UnidentifiedImageError
import pytesseract


def extract_text_from_image(image_file):
    try:
        with Image.open(image_file) as image:
            return pytesseract.image_to_string(image).strip()
    except UnidentifiedImageError as error:
        raise ValueError("The uploaded file is not a supported image.") from error
