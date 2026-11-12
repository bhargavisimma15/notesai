import os

from flask import Flask, flash, render_template, request
from pytesseract import TesseractNotFoundError

from cleaner import clean_text
from keyword_extractor import extract_keywords
from ocr import extract_text_from_image
from organizer import (
    detect_advantages,
    detect_bullet_points,
    detect_definitions,
    detect_disadvantages,
    detect_examples,
    detect_headings,
)
from summarizer import summarize_text


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", os.urandom(24))
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "bmp", "tif", "tiff"}


def analyze_text(text):
    cleaned_text = clean_text(text)
    return {
        "text": cleaned_text,
        "headings": detect_headings(cleaned_text),
        "definitions": detect_definitions(cleaned_text),
        "bullet_points": detect_bullet_points(cleaned_text),
        "examples": detect_examples(cleaned_text),
        "advantages": detect_advantages(cleaned_text),
        "disadvantages": detect_disadvantages(cleaned_text),
        "keywords": extract_keywords(cleaned_text),
        "summary": [
            sentence.strip()
            for sentence in summarize_text(cleaned_text)
            if sentence.strip()
        ],
    }


@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    analysis = None

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        image = request.files.get("image")

        if image and image.filename:
            extension = image.filename.rsplit(".", 1)[-1].lower()
            if "." not in image.filename or extension not in ALLOWED_IMAGE_EXTENSIONS:
                flash("Choose a PNG, JPG, BMP, or TIFF image.")
                return render_template("index.html", text=text, analysis=None)

            try:
                image_text = extract_text_from_image(image.stream)
            except ValueError as error:
                flash(str(error))
                return render_template("index.html", text=text, analysis=None)
            except TesseractNotFoundError:
                flash(
                    "Tesseract OCR is not installed. Install it and add it to "
                    "PATH to read text from images."
                )
                return render_template("index.html", text=text, analysis=None)

            text = "\n".join(part for part in (text, image_text) if part)

        if not text:
            flash("Enter some notes or upload an image to get started.")
        else:
            analysis = analyze_text(text)
            text = analysis["text"]

    return render_template("index.html", text=text, analysis=analysis)


if __name__ == "__main__":
    app.run(debug=True)
