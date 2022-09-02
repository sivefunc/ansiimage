from PIL import Image
from os import get_terminal_size

ESC = chr(27)
CSI = ESC + '['

def image_to_ansi(image_path):
    """
    return a list containing every character on the image, by replacing
    every single RGB pixel of the image to an ansi escape sequence
    """

    img = Image.open(image_path)
    columns, rows = get_terminal_size()
    resized_img = img.resize((columns, rows - 1))
    rgb_img = resized_img.convert(mode='RGB')

    pixels = list(rgb_img.getdata())
    
    ansi_image = []
    hor_ch = 0
    for pixel in pixels:
        if hor_ch == columns: # Generate new row
            ansi_image.append('\n')
            hor_ch = 0

        r,g,b = pixel
        ansi_image.append(f'{CSI}48;2;{r};{g};{b}m ')
        hor_ch += 1
    
    return ansi_image
