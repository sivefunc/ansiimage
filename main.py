from sys import stdout
from parser import parser
from ImageToAnsi import image_to_ansi

ESC = chr(27)
CSI = ESC + '['

write = stdout.write
image_path = parser().image_path

def main():
    for pixel in image_to_ansi(image_path):
        write(pixel)

if __name__ == '__main__':
    try:
        
        main()

    except FileNotFoundError:
        write(f'Image not found, maybe wrong path? -> {image_path}\n')

    finally:
        write(f'{CSI}0m')
