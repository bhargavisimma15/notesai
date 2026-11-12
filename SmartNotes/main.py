from cleaner import clean_text
from keyword_extractor import extract_keywords
from organizer import (
    detect_advantages,
    detect_bullet_points,
    detect_definitions,
    detect_disadvantages,
    detect_examples,
    detect_headings,
)
from summarizer import summarize_text

text = """Python is easy to learn.
Java is powerful.
C is fast."""


cleaned_text = clean_text(text)
print("Cleaned notes:")
print(cleaned_text)
print("\nHeadings:", detect_headings(cleaned_text))
print("Definitions:", detect_definitions(cleaned_text))
print("Bullet points:", detect_bullet_points(cleaned_text))
print("Examples:", detect_examples(cleaned_text))
print("Advantages:", detect_advantages(cleaned_text))
print("Disadvantages:", detect_disadvantages(cleaned_text))
print("Keywords:", extract_keywords(cleaned_text))
print("Summary:", summarize_text(cleaned_text))
