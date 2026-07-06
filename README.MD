# Region map editor
### Not a modding tool!

Small Python app designed to edit maps in the style of Paradox and other grand strategy games, where every region is encoded with a unique color

## How to use
* Select a PNG, or put it in the project folder with a standard name
* Create an empty JSON file
* App will automatically scan your PNG file for unique regions and will fill the JSON with all the regions
* Start editing!
* * Change names
* * Add/Edit custom properties
* * Change color (TODO)

You can name your regions by the closest CSS color, by using **closest_color_name(hex_value)** in **palette_loader.py**, but you wouldn't be able to use the list menu if this function gives regions the same names. I will fix this later

### Standard file names:
* "mapMask.png"
* "regions.json"

## How to build
Download from the releases and run main.exe, or build with any Python builder, I used PyInstaller.

If you are building this yourself, pip install two dependencies - webcolors and pillow, they are listed in **requirements.txt**

[Releases][link]

[link]: https://github.com/CubickT/mapEditor/releases

## Support
This project was created to cater to my own needs and is unlikely to expand further (with the exception of fixing bugs), so feel free to create forks or PRs. Also, if this gains some traction, I may consider adding extra functionality
