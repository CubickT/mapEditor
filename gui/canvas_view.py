import tkinter as tk
from PIL import Image, ImageTk

from models.palette import Palette
from models.region import Region

class CanvasView(tk.Canvas):

    def __init__(self, parent, image_path, palette: Palette):
        self.image_path = image_path

        self.image = Image.open(image_path).convert("RGB")
        self.width, self.height = self.image.size
        super().__init__(parent, width=self.width, height=self.height)

        self.palette = palette
        self.click_callback = None


        self.tk_image = ImageTk.PhotoImage(self.image)
        self.image_id = self.create_image(0, 0, anchor='nw', image=self.tk_image)

        self.bind("<Button-1>", self._on_click)

        self.highlight_id = None

    def set_on_click_callback(self, callback):
        self.click_callback = callback

    def _on_click(self, event):
        x = event.x
        y = event.y
        if not (0 <= x < self.image.width and 0 <= y < self.image.height):
            return
        
        r, g, b = self.image.getpixel((x, y))
        hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()

        region: Region = self.palette.find_by_color(hex_color)
        
        if region is not None:
            self._highlight_click(x,y)
            self.click_callback(region)


    def _highlight_click(self, x , y):
        if self.highlight_id:
            self.delete(self.highlight_id)

        radius = 5
        self.highlight_id = self.create_oval(
            x - radius, y - radius,
            x + radius, y + radius,
            outline='red', width=5
        )

    def clear_highlight(self):
        if self.highlight_id:
            self.delete(self.highlight_id)
            self.highlight_id = None