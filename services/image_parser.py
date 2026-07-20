import math
from collections import defaultdict

from PIL import Image
import webcolors


from models.region import Region
from models.palette import Palette

def extract_unique_colors(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        img.load()
        img = img.convert('RGB')
        pixels = list(img.get_flattened_data())
        uniqueColors = set(pixels)
        return uniqueColors

def rgb_to_hex(color):
    r,g,b = color
    return f"#{r:02x}{g:02x}{b:02x}"

def hex_to_rgb(hex_value):
    hex_value = hex_value.lstrip('#')
    return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))

def closest_color_name(hex_value):
    target_rgb = hex_to_rgb(hex_value)
    css_colors = {}
    for name in webcolors.names():
        css_colors[name] = webcolors.name_to_rgb(name)
    
    min_dist = float('inf')
    closest_name = None
    for name, rgb in css_colors.items():
        dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(target_rgb, rgb)))
        if dist < min_dist:
            min_dist = dist
            closest_name = name
    return closest_name

def get_neighbors(image: Image, palette: Palette):
    print("вызов get_neighbors")

    dirs = [(2,0), (0,2),(0,-2),(-2,0)]
    skipColors = {(0,0,0), (255,255,255), (113,115,126)}

    neighbors_map = defaultdict(set)

    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            color = pixels[x,y]

            if color in skipColors:
                continue
        
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    nColor = pixels[nx, ny]

                    if nColor in skipColors:
                        continue
                    if nColor != color:
                        neighbors_map[color].add(nColor)
    
    for color, neighbor_colors in neighbors_map.items():
        regionColor = rgb_to_hex(color)
        region: Region = palette.find_by_color(regionColor)
        region.neighbors = [palette.find_by_color(rgb_to_hex(c)).name for c in neighbor_colors]
