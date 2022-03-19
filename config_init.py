import os
import json
import time
import sys
from PIL import Image
from pathlib import Path
from colorama import Fore
from PIL import ImageGrab

args = sys.argv
BASE_DIR = Path(__file__).resolve().parent

with open("config.json", "r") as f:
    conf = json.load(f)
CONFIG_DATA = conf
resize_condition = False
CONFIG_DATA["BASE_DIR"] = str(BASE_DIR)


# Function to check the resolution size of the screen
def resolution():
    print("Resolution : ", end=' ')
    resolution.width, resolution.height = ImageGrab.grab().size
    CONFIG_DATA["resolution_width"] = resolution.width
    CONFIG_DATA["resolution_height"] = resolution.height
    print(Fore.YELLOW + f"""{resolution.width} x {resolution.height}""" + Fore.RESET)


def resize():
    # convert the logo to the resolution dependent
    print("Resizing the logo -> ", end=' ')
    resize.square = int(float(resolution.width) / 17.45)
    image = Image.open(f"""{BASE_DIR}/media/logo.png""")
    image = image.resize((resize.square, resize.square), Image.ANTIALIAS)
    image.save(fp=f"""{BASE_DIR}/media/res_logo.png""")
    CONFIG_DATA["image_size"] = resize.square
    print(Fore.YELLOW + "Done" + Fore.RESET)


def gtk_worker():
    if CONFIG_DATA["position_static_ticker"] == "top-left":
        CONFIG_DATA['gtk_ticker_pos_y'] = 0
        CONFIG_DATA['gtk_ticker_pos_x'] = 0

    elif CONFIG_DATA["position_static_ticker"] == "top-right":
        CONFIG_DATA['gtk_ticker_pos_y'] = 0
        CONFIG_DATA['gtk_ticker_pos_x'] = CONFIG_DATA['resolution_width']

    elif CONFIG_DATA["position_static_ticker"] == "bottom-right":
        CONFIG_DATA['gtk_ticker_pos_y'] = CONFIG_DATA['resolution_height']
        CONFIG_DATA['gtk_ticker_pos_x'] = CONFIG_DATA['resolution_width']

    elif CONFIG_DATA["position_static_ticker"] == "bottom-left":
        CONFIG_DATA['gtk_ticker_pos_y'] = CONFIG_DATA['resolution_height']
        CONFIG_DATA['gtk_ticker_pos_x'] = 0


def resize_gtk():
    # convert the logo to the resolution dependent
    print("Resizing the logo -> ", end=' ')
    resize.square = int(float(resolution.width) / 17.45)
    image = Image.open(f"""{BASE_DIR}/media/logo_gtk.png""")
    image = image.resize((resize.square, resize.square), Image.ANTIALIAS)
    image.save(fp=f"""{BASE_DIR}/media/res_logo_gtk.png""")
    CONFIG_DATA["image_size"] = resize.square
    print(Fore.YELLOW + "Done" + Fore.RESET)

def bgcolor():
    print("Backfround color set to : ", end=' ')

    print(Fore.LIGHTGREEN_EX + "Done" + Fore.RESET)


def png_jpg():
    # This function convert Transparent Background PNG to JPG with dominant background color
    print("Image converting to JPG -> ", end=' ')
    im = Image.open(f"""{BASE_DIR}/media/res_logo.png""")
    fill_color = (tuple(CONFIG_DATA['main_ticker_bgcolor']))  # your new background color
    im = im.convert("RGBA")  # it had mode P after DL it from OP
    if im.mode in ('RGBA', 'LA'):
        background = Image.new(im.mode[:-1], im.size, fill_color)
        background.paste(im, im.split()[-1])  # omit transparency
        im = background
    im.convert("RGB").save(f"""{BASE_DIR}/media/res_logo.jpg""")
    print(Fore.YELLOW + "Done" + Fore.RESET)


def dump():
    print("Dumping Data into Json File -> ", end=' ')
    with open("ticker_setup.json", "w") as outfile:
        outfile.write(json.dumps(CONFIG_DATA, indent=3))
    print(Fore.YELLOW + "Done" + Fore.RESET)


if __name__ == '__main__':
    start_time = time.time()
    resolution()


    if CONFIG_DATA['static_ticker_condition'] == True:
        gtk_worker()
        if CONFIG_DATA['static_ticker_logo'] == True:
            resize_gtk()

    if CONFIG_DATA['main_ticker_condition'] == True:
        bgcolor()
        png_jpg()

        if CONFIG_DATA['main_ticker_logo'] == True:
            resize()

        if CONFIG_DATA['optional_ticker_condition'] == True:
            print("Hi")



    dump()
    print("NEW CONFIG DATA IS: ", CONFIG_DATA)
    print("Execution took : " + Fore.RED + "--- %s seconds ---" % (time.time() - start_time) + Fore.RESET)
