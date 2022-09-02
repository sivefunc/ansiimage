import argparse

def parser():
    parser = argparse.ArgumentParser(
            prog="AnsiImage",
            usage="%(prog)s [Image]",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description="Simple Unix terminal image viewer")

    parser.add_argument(
            '-v','--version',
            action='version',
            version="""
%(prog)s v1.0.0
Copyright (C) 2022 Sivefunc
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by a human""")

    parser.add_argument(
            'image_path', 
            type=str,
            help='path of the image',
            metavar='image')
    
    args = parser.parse_args()
    return args
