# @author   Lucas Cardoso de Medeiros
# @since    24/08/2023
# @version  1.0


"""A website that finds the most common colours in an uploaded image.

One of my favourite websites to go to when I'm designing anything is a colour palette website called Flat UI Colors.
https://flatuicolors.com/palette/defo

It's a really simple static website that shows a bunch of colours and their HEX codes. I can copy the HEX codes and
use it in my CSS or any design software.

On day 76, you learnt about image processing with NumPy. Using this knowledge and your developer skills (that means
Googling), build a website where a user can upload an image, and you will tell them what are the top 10 most common
colours in that image. This is a good example of this functionality:
http://www.coolphptools.com/color_extract#demo"""

from tkinter import filedialog
from PIL import Image
from sklearn.cluster import KMeans
import tkinter as tk
import numpy as np
import warnings

FONT = ("Helvetica", 12)
FONT_BUTTON = ("Helvetica", 10)
TABLE_FONT = ("Helvetica", 11)
TABLE_COLUMN_WIDTH = 20
TABLE_MAX_ROWS = 10
DEFAULT_NUM_COLORS = 10

warnings.filterwarnings("ignore")


class ImageColorExtractor:
    def __init__(self):
        self.image = None
        self.num_colors = DEFAULT_NUM_COLORS

        self.root = tk.Tk()
        self.root.title("Image Color Extractor")
        self.root.geometry("700x850")

        self.label = tk.Label(self.root, text="Choose an image file to extract colors", font=FONT)
        self.label.pack(pady=10)

        self.upload_button = tk.Button(self.root, text="Upload File", command=self.extract_colors, font=FONT_BUTTON)
        self.upload_button.pack(pady=10)

        self.num_colors_label = tk.Label(self.root, text="Number of colors:", font=FONT)
        self.num_colors_label.pack(pady=10)

        self.num_colors_entry = tk.Entry(self.root, font=FONT)
        self.num_colors_entry.pack(pady=5)
        self.num_colors_entry.insert(0, str(self.num_colors))  # Set the default value

        self.extract_button = tk.Button(self.root, text="Extract Colors", command=self.extract_colors, font=FONT_BUTTON)
        self.extract_button.pack(pady=15)

        self.result_label = tk.Label(self.root, text="", font=FONT)
        self.result_label.pack(pady=25)

        self.color_frame = tk.Frame(self.root)
        self.color_frame.pack()

    def extract_colors(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if not file_path:
            return

        try:
            self.num_colors = int(self.num_colors_entry.get())
        except ValueError:
            self.num_colors = DEFAULT_NUM_COLORS

        self.image = Image.open(file_path)
        self.result_label.config(text=f"{self.num_colors} most frequent colors:")

        # noinspection PyTypeChecker
        image_array = np.asarray(self.image)  # Convert image to NumPy array
        h, w, _ = image_array.shape
        pixel_list = image_array.reshape((h * w, 3))  # Reshape image array to a list of pixels

        kmeans = KMeans(n_clusters=self.num_colors)  # Use KMeans clustering to group similar colors
        kmeans.fit(pixel_list)

        most_common_colors = kmeans.cluster_centers_  # Get the most common colors (cluster centers)
        counts = np.bincount(kmeans.labels_)  # Calculate the count of each color in the image
        percentages = (counts / len(pixel_list)) * 100  # Calculate the percentage appearance of each color

        # Sort colors by percentage appearance in descending order
        sorted_indices = np.argsort(percentages)[::-1]
        sorted_colors = most_common_colors[sorted_indices]
        sorted_percentages = percentages[sorted_indices]

        for widget in self.color_frame.winfo_children():
            widget.destroy()  # Clear previous colors

        # Create the table headers
        color_header = tk.Label(
            self.color_frame,
            text="Color",
            padx=10,
            pady=5,
            width=TABLE_COLUMN_WIDTH,
            font=TABLE_FONT)

        hex_header = tk.Label(
            self.color_frame,
            text="Color Code",
            padx=10,
            pady=5,
            width=TABLE_COLUMN_WIDTH,
            font=TABLE_FONT)

        percentage_header = tk.Label(
            self.color_frame,
            text="Percentage",
            padx=10,
            pady=5,
            width=TABLE_COLUMN_WIDTH,
            font=TABLE_FONT)

        color_header.grid(row=0, column=0)
        hex_header.grid(row=0, column=1)
        percentage_header.grid(row=0, column=2)

        num_rows = self.num_colors
        if num_rows > TABLE_MAX_ROWS:
            num_rows = TABLE_MAX_ROWS

        for i in range(num_rows):
            color = sorted_colors[i].astype(int)
            color_code = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
            percentage = f"{sorted_percentages[i]:.2f}%"

            color_label = tk.Label(
                self.color_frame,
                bg=color_code,
                padx=10,
                pady=5,
                width=TABLE_COLUMN_WIDTH,
                height=2,
                font=TABLE_FONT)

            hex_label = tk.Label(
                self.color_frame,
                text=color_code,
                padx=10,
                pady=5,
                width=TABLE_COLUMN_WIDTH,
                font=TABLE_FONT)

            percentage_label = tk.Label(
                self.color_frame,
                text=percentage,
                padx=10,
                pady=5,
                width=TABLE_COLUMN_WIDTH,
                font=TABLE_FONT)

            color_label.grid(row=i, column=0, padx=5)
            hex_label.grid(row=i, column=1, padx=5)
            percentage_label.grid(row=i, column=2, padx=5)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ImageColorExtractor()
    app.run()
