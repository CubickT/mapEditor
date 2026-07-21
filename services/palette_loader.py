import json
from PIL import Image

from models.palette import Palette
from models.region import Region
from services.image_parser import extract_unique_colors, get_neighbors

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
            except (TypeError, OSError) as e:
                print(f"Ошибка сериализации: {e}")

    @staticmethod
    def generate_from_image(image_path):

        unique_rgb = extract_unique_colors(image_path)
        sorted_rgb = sorted(unique_rgb)

        regions = []

        for idx, (r,g,b) in enumerate(sorted_rgb):
            hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()
            name = idx
            region_id = idx
            region  = Region(region_id, name, hex_color, params={})
            regions.append(region)
            
        palette =  Palette(regions)

        image = Image.open(image_path).convert("RGB")
        get_neighbors(image, palette)
        
        return palette
