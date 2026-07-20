import tkinter as tk
from tkinter import ttk

class PaletteList(ttk.Frame):

    def __init__(self, parent, palette, on_select_callback):

        super().__init__(parent)
        self.palette = palette
        self.call_back = on_select_callback

        ttk.Label(self, text="Regions", font=('', 10, 'bold')).pack(pady=2)

        frame = ttk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(frame, font=('', 9))
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.listbox.bind('<<ListboxSelect>>', self._on_select)
        self.refresh_list()

    def select_region(self, region):
        self.listbox.selection_clear(0, tk.END)

        for i in range(self.listbox.size()):
            if self.listbox.get(i) == str(region.name):
                self.listbox.selection_set(i)
                self.listbox.see(i)

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for region in self.palette.regions:
            display = f"{region.name}"
            self.listbox.insert(tk.END, display)

        if self.palette.regions:
            self.listbox.selection_set(0)

    def _on_select(self):
        selection = self.listbox.curselection()
        if not selection:
            return
        index = selection[0]
        if 0 <= index < len(self.palette.regions):
            region = self.palette.regions[index]
            if self.call_back:
                self.call_back(region)
