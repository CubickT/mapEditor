import json, os
from models.palette import Palette
from services.image_parser import extract_unique_colors, closest_color_name
from models.region import Region



class PaletteLoader:

    @staticmethod
    def load_from_json(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return Palette.from_jsonable(data)
    
    @staticmethod
    def save_to_json(palette,filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            try:
                json.dump(palette.to_jsonable(), f, indent=2, ensure_ascii=False)
            except Exception as e:
                print(f"Ошибка сериализации: {e}")

    @staticmethod
    def generate_from_image(image_path):

        unique_rgb = extract_unique_colors(image_path)
        sorted_rgb = sorted(unique_rgb)

        regions = []

        for idx, (r,g,b) in enumerate(sorted_rgb):
            hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()
            name = idx
            id = idx
            region  = Region(id, name, hex_color, params={})
            regions.append(region)
            
        palette =  Palette(regions)
        return palette