# @author   Lucas Cardoso de Medeiros
# @since    17/08/2023
# @version  1.0

"""Using what you have learnt about Tkinter, you will create a desktop application with a Graphical User Interface (
GUI) where you can upload an image and use Python to add a watermark logo/text. Normally, you would have to use an
image editing software like Photoshop to add the watermark, but your program is going to do it automatically."""

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk


WATERMARK_TEXT = "Watermark Text"
LOGO_PATH = "logo.png"

TEXT_WATERMARKED_PATH = "text_watermarked_image.png"
LOGO_WATERMARKED_PATH = "logo_watermarked_image.png"
MAX_TEXT_SIZE = 14
FONT = "arial.ttf"
FONT_SIZE = 30


class WatermarkApp:
    def __init__(self, root, watermark_text, watermark_logo_path):
        self.image = None
        self.photo = None
        self.watermark_logo = watermark_logo_path
        if len(watermark_text) > MAX_TEXT_SIZE:
            self.watermark_text = watermark_text[MAX_TEXT_SIZE:]
        else:
            self.watermark_text = watermark_text

        self.root = root
        self.root.title("Watermark App")

        self.canvas = tk.Canvas(root, width=750, height=750)
        self.canvas.pack()

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.watermark_text_button = tk.Button(root, text="Add Text Watermark", command=self.add_text_watermark)
        self.watermark_text_button.pack()

        self.watermark_logo_button = tk.Button(root, text="Add Logo Watermark", command=self.add_image_watermark)
        self.watermark_logo_button.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            self.image = Image.open(file_path)
            self.image.thumbnail((750, 750))
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def add_text_watermark(self):
        if hasattr(self, 'image'):
            watermark = Image.new("RGBA", self.image.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(watermark)
            font = ImageFont.truetype(FONT, FONT_SIZE)
            x, y = 0, 0
            while y < self.image.height:
                while x < self.image.width:
                    draw.text((x, y), self.watermark_text, font=font, fill=(255, 255, 255, 128))
                    x += 250
                y += 100
                x = 0
            watermarked_image = Image.alpha_composite(self.image.convert("RGBA"), watermark)
            watermarked_image.save(TEXT_WATERMARKED_PATH)
            watermarked_image.show()

    def add_image_watermark(self):
        if hasattr(self, 'image') and self.watermark_logo:
            watermark = Image.open(self.watermark_logo)
            watermark = watermark.resize((100, 100), Image.Resampling.LANCZOS)
            transparent_layer = Image.new("RGBA", self.image.size, (0, 0, 0, 0))
            x, y = self.image.width - watermark.width, self.image.height - watermark.height
            transparent_layer.paste(watermark, (x, y))
            watermarked_image = Image.alpha_composite(self.image.convert("RGBA"), transparent_layer)
            watermarked_image.save(LOGO_WATERMARKED_PATH)
            watermarked_image.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root, WATERMARK_TEXT, LOGO_PATH)
    root.mainloop()
