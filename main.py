import tkinter as tk
from tkinter import filedialog
from gui.main_window import MainWindow
from services.file_selector import FileSelector

def main():

    root = tk.Tk()
    root.title('Region Editor')

    file_selector = FileSelector(root)
    file_selector.show_select_file()

    image_path = file_selector.image_path or "mapMask.png"
    json_path = file_selector.json_path or "regions.json"

    print(image_path, json_path)

    root.deiconify()
    
    app = MainWindow(root, image_path, json_path)
    root.mainloop()

if __name__ == "__main__":
    main()
