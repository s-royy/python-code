import pyttsx3
from pypdf import PdfReader
from tkinter.filedialog import askopenfilename

book = askopenfilename()
pdfreader = PdfReader(book)
engine = pyttsx3.init()   

