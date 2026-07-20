from models.palette import Palette
from services.palette_loader import PaletteLoader
from models.region import Region

import tkinter as tk
from tkinter import ttk

from gui.canvas_view import CanvasView
from gui.palette_list import PaletteList
from gui.parameter_editor import ParameterEditor

import json


class MainWindow:
    def __init__(self, root, image_path, json_path):
        self.root = root
        self.image_path = image_path
        self.json_path = json_path

        self.palette: Palette =self.load_palette()

        self.main_panel = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.main_panel.pack(fill=tk.BOTH, expand=True)

        self.init_palette_list()
        self.init_canvas_view()
        self.init_param_editor()
        
        self.canvas_view.set_on_click_callback(self._on_region_clicked)

        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=5)

        self.refresh_btn = tk.Button(
            control_frame,
            text="Обновить палитру (распознать цвета)",
            command= self.load_palette
        )
        self.refresh_btn.pack(side=tk.LEFT, padx=5)

        self.save_json_btn = tk.Button(
            control_frame,
            text= "Сохранить в JSON",
            command = self.save_pallete
        )
        self.save_json_btn.pack(side=tk.LEFT, padx=5)

        if self.palette.regions:
            self._on_region_selected(self.palette.regions[0])

    def init_palette_list(self):
        self.left_frame = ttk.Frame(self.main_panel, width=200)
        self.main_panel.add(self.left_frame, weight=1)
        self.palette_list = PaletteList(
            self.left_frame,
            self.palette,
            on_select_callback=self._on_region_selected_list
        )

        self.palette_list.pack(fill=tk.BOTH, expand=True)

    def init_canvas_view(self):
        self.canvas_view = CanvasView(self.main_panel, self.image_path, self.palette )
        self.main_panel.add(self.canvas_view, weight=3)

    def init_param_editor(self):
        self.right_frame = ttk.Frame(self.main_panel, width=200)
        self.main_panel.add(self.right_frame, weight=1)
        self.param_editor = ParameterEditor(self.right_frame,self.palette)
        self.param_editor.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.param_editor.set_save_callback(self._on_region_save)

    def _on_region_selected_list(self, region:Region):
        self.canvas_view.clear_highlight()
        self._on_region_selected(region)

    def _on_region_clicked(self, region:Region):
        self.palette_list.select_region(region)
        self._on_region_selected(region)

    def _on_region_selected(self, region:Region):
        self.param_editor.set_region(region)

    def _on_region_save(self):
        self.palette_list._refresh_list()

    def load_palette(self):
        loader = PaletteLoader()

        try:
            palette = loader.load_from_json(self.json_path)
            if not palette.regions:
                raise ValueError("Empty Json")
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            palette = loader.generate_from_image(self.image_path) 
            loader.save_to_json(palette, self.json_path)
        return palette
    
    def save_pallete(self):
        loader = PaletteLoader()
        if self.palette is None:
            print("Ошибка сохранения, пустая палитра")
            return
        
        loader.save_to_json(self.palette, self.json_path)
        print("Палитра сохраненна в файл")