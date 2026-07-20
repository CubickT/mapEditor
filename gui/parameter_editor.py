import tkinter as tk
from tkinter import ttk

from models.region import Region

class ParameterEditor(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.region_selected: Region = None
        self.params = {}
        self.param_vars = {}
        self.save_callback = None

        ttk.Label(self, text="Имя региона:").grid(row=0, column=0, sticky=tk.W)
        self.name_var = tk.StringVar(master = parent, value = "")
        self.name_entry = ttk.Entry(self, textvariable=self.name_var, width=25)
        self.name_entry.grid(row=0, column=1, sticky=tk.W)

        self.save_btn = ttk.Button(self, text="Сохранить имя", command=self.save_name)
        self.save_btn.grid(row=1, column=0, columnspan=2, pady=10)

        ttk.Label(self, text="ID региона:").grid(row=2, column=0, sticky=tk.W)
        self.id_var = tk.StringVar(master = parent, value= "")
        ttk.Label(self, textvariable=self.id_var).grid(row=2, column=1, sticky=tk.W)

        ttk.Button(self, text="Добавить парам.", command= self._add_param).grid(row=3, column=0, columnspan=1, pady=10)
        self.param_name = tk.StringVar(master= parent, value="")
        ttk.Entry(self, textvariable=self.param_name, width= 25 ).grid(row=3, column= 1, pady=10)

        self.params_frame = ttk.LabelFrame(self, text="Параметры (params)", padding=5)
        self.params_frame.grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E, pady=10)

        self.params_container = ttk.Frame(self.params_frame)
        self.params_container.pack(fill=tk.BOTH, expand=True)

        self.save_param_btn = ttk.Button(self, text="Сохранить параметры", command=self.save_params)
        self.save_param_btn.grid(row=5, column=0, columnspan=2, pady=10)

    def _init_params(self):

        for widget in self.params_container.winfo_children():
            widget.destroy()

        for idx, (key, value) in enumerate(self.params.items()):
            
            if key not in self.param_vars:
                self.param_vars[key] = tk.StringVar(master=self.params_container, value=value)
            else:
                self.param_vars[key].set(value)

            ttk.Label(self.params_container, text= key + ":").grid(row=idx,column=0,pady=10)
            ttk.Entry(self.params_container, textvariable=self.param_vars[key], width= 25).grid(row=idx, column= 1,pady=10)

            param_delete = ttk.Button(self.params_container, text="Удалить", command= lambda k = key: self._delete_param(k))


            param_delete.grid(row=idx, column=2, pady=5, padx=5)

    def set_region(self, region):

        if region:
            self.region_selected = region
            self.name_var.set(region.name)
            self.id_var.set(region.id)
            self.params = region.params
            self._init_params()
        else:
            self.region_selected = None
            self.name_var.set("")
            self.id_var.set("")
            self.params = {}
            self._init_params()

    def set_save_callback(self, callback):
        self.save_callback = callback

    def save_name(self):
        if self.region_selected is None:
            print("Ошибка сохранения, не задан регион")
            return
        
        new_name = self.name_var.get().strip()
        if new_name:
            self.region_selected.name = new_name
        else:
            print("Пустое имя")
            return
            
        print(f"Регион '{self.region_selected.name}' (ID {self.region_selected.id}) сохранён в объекте")
        self.save_callback()

    def _add_param(self):
        name = self.param_name.get().strip()

        if name == "":
            print("Пустой параметр")
            return

        self.params[name] = ""
        self.param_vars[name] = tk.StringVar(master=self.params_container, value="")
        print(self.params)
        self._init_params()

    def save_params(self):
        if self.region_selected is None:
            print("Ошибка сохранения, не задан регион")
            return
        
        for key, var in self.param_vars.items():
            self.params[key] = var.get()

        self.region_selected.params = self.params
        print(f"Регион '{self.region_selected.name}' (ID {self.region_selected.id}) сохранён в объекте. Параметры: {self.region_selected.params}")
        
    def _delete_param(self, param_name):
        if param_name not in self.params:
            return
        
        del self.params[param_name]
        if param_name in self.param_vars:
            del self.param_vars[param_name]

        self._init_params()
        print(f"Параметр '{param_name}' удалён. Текущие параметры: {self.params}")
