import pyttsx3
from pypdf import PdfReader
from tkinter.filedialog import askopenfilename

book = askopenfilename()
pdfreader = PdfReader(book)
engine = pyttsx3.init()   

for num, page in enumerate(pdfreader.pages):
    text = page.extract_text()
    if not text or not text.strip():
        print(f"Page {num + 1}: no extractable text, skipping.")
        continue
    print(f"Reading page {num + 1}")
    engine.say(text)
    engine.runAndWait()

