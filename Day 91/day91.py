# @author   Lucas Cardoso de Medeiros
# @since    23/08/2023
# @version  1.0


"""Write a Python script that takes a PDF file and converts it into speech.

Too tired to read? Build a python script that takes a PDF file, identifies the text and converts the text to speech.
Effectively creating a free audiobook. AI text-to-speech has come so far. They can sound more lifelike than a real
audiobook. Using what you've learnt about HTTP requests, APIs and Python scripting, create a program that can convert
PDF files to speech. You right want to choose your own Text-To-Speech (TTS) API."""


from tkinter import filedialog
from gtts import gTTS
import tkinter as tk
import PyPDF2


FONT = ("Helvetica", 12)


class PdfToAudioConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pdf to Audio Converter")
        self.root.geometry("750x250")

        self.upload_button = tk.Button(self.root, text="Upload PDF File", command=self.upload_pdf)
        self.upload_button.pack(pady=50)

        self.label = tk.Label(self.root, text="Choose a PDF file to convert to audio", font=FONT)
        self.label.pack()

    def upload_pdf(self):
        pdf_file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if pdf_file_path:
            self.convert_pdf_to_audio(pdf_file_path)

    def convert_pdf_to_audio(self, pdf_file_path):
        self.label.config(text=f"Converting pdf file to .mp3 ...")

        text = ""
        pdf = PyPDF2.PdfReader(pdf_file_path)

        for page in pdf.pages:
            text += page.extract_text()

        audio_file_path = pdf_file_path.replace(".pdf", ".mp3")
        tts = gTTS(text, lang="en", slow=False)
        tts.save(audio_file_path)

        self.label.config(text=f"Conversion to .mp3 file complete!\n\nCheck the file: {audio_file_path}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = PdfToAudioConverter()
    app.run()
