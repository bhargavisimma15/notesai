# SmartNotes

SmartNotes is a small study-notes project built from the text-cleaning,
organizing, keyword, and summary functions. It can analyze pasted notes and use
OCR to read text from an uploaded image.

## Setup

1. Install Python 3.10 or newer.
2. In a terminal, open the `SmartNotes` folder and install the Python packages:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. To use image OCR, install the Tesseract OCR program separately and add its
   installation folder to your `PATH`. OCR is optional; pasted text works
   without Tesseract.
4. Start the website:

   ```powershell
   python app.py
   ```

5. Open `http://127.0.0.1:5000` in your browser.

To run the command-line example, use `python main.py`. To run the tests, use
`python -m unittest test`.

The organizer uses simple text rules, so it works best with clearly labeled
sections such as `Examples:`, `Advantages:`, and `Disadvantages:`.
