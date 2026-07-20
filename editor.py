import json
import tkinter as tk 
from tkinter import simpledialog

from PIL import Image, ImageTk

class RegionEditor:
    def __init__(self, image_path, json_path):
        self.root = tk.Tk()

        self.image_path = image_path
        self.json_path = json_path

        self.img = Image.open(image_path).convert('RGB')
        self.tk_img = ImageTk.PhotoImage(self.img)

        with open(json_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                extractColors(self.image_path, self.json_path)
                with open(self.json_path, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
            else:
                self.data = json.loads(content)

        self.canvas = tk.Canvas(self.root, width=self.img.width, height=self.img.height)
        self.canvas.create_image(0,0, anchor='nw', image=self.tk_img)
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.pack()
        self.info_label = tk.Label(self.root, text="Кликните на область, чтобы изменить имя")
        self.info_label.pack()
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=5)

        self.refresh_btn = tk.Button(
            control_frame,
            text="Обновить палитру (распознать цвета)",
            command=self.refresh_palette
        )
        self.refresh_btn.pack(side=tk.LEFT, padx=5)

        self.root.mainloop()

    def refresh_palette(self):
        extract_colors(self.image_path, self.json_path)
        with open(self.json_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            self.data = json.loads(content)

    def on_click(self, event):
        print(event.x, event.y)
        x = event.x
        y = event.y

        if 0 <= x < self.img.width and 0 <= y < self.img.height:
            r, g, b = self.img.getpixel((x, y))
            hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()
            print(hex_color)
        
        found = None
        for item in self.data:
            if item["color"] == hex_color:
                found = item
                break
        if found is None:
            self.info_label.config(text=f"Цвет {hex_color} не найден в палитре")
            return   
        if found:
            self.edit_box(found)


    def edit_box(self, found):
        current_name = found["name"]
        hex_color = found["color"]
        new_name = simpledialog.askstring(
            "Редактирование",
            f"Цвет: {hex_color}\nТекущее имя: {current_name}\nВведите новое имя:",
            initialvalue=current_name
        )
        
        if new_name is not None:
            found["name"] = new_name
            self.save_data()

    def save_data(self):
        with open(self.json_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
