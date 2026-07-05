import tkinter as tk
from tkinter import filedialog, messagebox
from gui.main_window import MainWindow
from services.file_selector import FileSelector

def main():
    
    root = tk.Tk()
    root.title('Region Editor')

    base_image_path = "mapMask.png"
    base_json_path = "regions.json"

    try:
        open(base_image_path)
    except:
        messagebox.showwarning(title="Файлы по умолчанию",
                            message="Отустсвуют файлы по умолчанию -" \
                            "\"mapMask.png\" и \"regions.json\" должны быть в той же папке, что и main.exe." \
                            "\nДобавьте их или выберете свои")

    file_selector = FileSelector(root)
    file_selector.show_select_file()




    image_path = file_selector.image_path or base_image_path
    json_path = file_selector.json_path or base_json_path

    print(image_path, json_path)

    root.deiconify()
    
    app = MainWindow(root, image_path, json_path)
    root.mainloop()

if __name__ == "__main__":
    main()
