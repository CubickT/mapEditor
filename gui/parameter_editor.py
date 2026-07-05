import tkinter as tk
from tkinter import ttk

from models.region import Region

class ParameterEditor(ttk.Frame):
    def __init__(self, parent, palette,):
        super().__init__(parent)

        self.region_selected: Region = None
        self.save_callback = None

        ttk.Label(self, text="Имя региона:").grid(row=0, column=0, sticky=tk.W)
        self.name_var = tk.StringVar(master = parent, value = "")
        self.name_entry = ttk.Entry(self, textvariable=self.name_var, width=25)
        self.name_entry.grid(row=0, column=1, sticky=tk.W)

        ttk.Label(self, text="ID региона:").grid(row=1, column=0, sticky=tk.W)
        self.id_var = tk.StringVar(master = parent, value= "")
        ttk.Label(self, textvariable=self.id_var).grid(row=1, column=1, sticky=tk.W)

        self.params_frame = ttk.LabelFrame(self, text="Параметры (params)", padding=5)
        self.params_frame.grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E, pady=10)

        self.params_container = ttk.Frame(self.params_frame)
        self.params_container.pack(fill=tk.BOTH, expand=True)

        self.save_btn = ttk.Button(self, text="Сохранить изменения", command=self.save_current_region)
        self.save_btn.grid(row=3, column=0, columnspan=2, pady=10)


    def set_region(self, region):

        if region:
            self.region_selected = region
            self.name_var.set(region.name)
            self.id_var.set(region.id)
        else:
            self.region_selected = None
            self.name_var.set("")
            self.id_var.set("")

    def set_save_callback(self, callback):
        self.save_callback = callback

    def save_current_region(self):
        if self.region_selected is None:
            print("Ошибка сохранения, не задан регион")
        
        new_name = self.name_var.get().strip()
        if new_name:
            self.region_selected.name = new_name
        else:
            print("Пустое имя")
            return
            
        print(f"Регион '{self.region_selected.name}' (ID {self.region_selected.id}) сохранён в объекте")
        self.save_callback()

