from PIL import Image, ImageTk
import webcolors
import math

def extract_unique_colors(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        img.load()
        img = img.convert('RGB')
        pixels = list(img.get_flattened_data())
        uniqueColors = set(pixels)
        return uniqueColors

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