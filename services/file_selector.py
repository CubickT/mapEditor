import tkinter as tk
from tkinter import filedialog

class FileSelector:

    def __init__(self, master):
        self.master = master
        self.master.withdraw()

        self.image_path = None 
        self.json_path = None

    def show_select_file(self):
        self.top = tk.Toplevel(self.master)
        self.top.title("Select Files")
        self.top.geometry("200x200")
        self.top.resizable(False, False)

        text_label = tk.Label(self.top, text="Стандартные файлы: \n \"mapMask.png\" и \"regions.json\"")
        text_label.pack(pady= 10)

        btn_image = tk.Button(self.top,text="Выберете ПНГ карты", command = self.pick_image_path)
        btn_image.pack(pady= 10)

        btn_json = tk.Button(self.top,text= "Выберите JSON карты", command = self.pick_json_path)
        btn_json.pack(pady = 10)

        btn_ok = tk.Button(self.top, text="Готово", command=self.top.destroy)
        btn_ok.pack(pady=10)

        self.master.wait_window(self.top)



    def pick_image_path(self):
        path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if path:
            self.image_path = path
            print(f"Выбрано изображение: {path}")
    
    def pick_json_path(self):
        path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if path:
            self.json_path = path
            print(f"Выбран json: {path}")