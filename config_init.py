import os
import json
import time
import sys
from PIL import Image
from pathlib import Path
from PIL import ImageGrab

args = sys.argv
#BASE_DIR = Path(__file__).resolve().parent
BASE_DIR = "/home/guest/.tickerv2"
with open(f"{BASE_DIR}/config.json", "r") as f:
    conf = json.load(f)
CONFIG_DATA = conf
resize_condition = False
CONFIG_DATA["BASE_DIR"] = str(BASE_DIR)

size = 1
# Function to check the resolution size of the screen
def resolution():
    print("Resolution : ", end=' ')
    resolution.width, resolution.height = ImageGrab.grab().size
    CONFIG_DATA["resolution_width"] = resolution.width
    CONFIG_DATA["resolution_height"] = resolution.height
    print(f"""{resolution.width} x {resolution.height}""")


def resize():
    # convert the logo to the resolution dependent
    print("Resizing the logo -> ", end=' ')
    # resize.square = int(float(resolution.width) / 17.45)
    resize.square = int(float(resolution.height) / 8)
    image = Image.open(f"""{BASE_DIR}/media/logo.png""")
    image = image.resize((resize.square, resize.square), Image.ANTIALIAS)
    image.save(fp=f"""{BASE_DIR}/media/res_logo.png""")
    CONFIG_DATA["image_size"] = resize.square
    print("Done")


def gtk_worker():
    CONFIG_DATA['static_ticker_font_height'] = int(CONFIG_DATA ['static_ticker_font_size'] * 3 )
    CONFIG_DATA['static_ticker_font_length'] = int(float(len(CONFIG_DATA['static_ticker_message']) * CONFIG_DATA['static_ticker_font_size']) / 1.9)
    if CONFIG_DATA['static_ticker_logo']:
        if bool(CONFIG_DATA['static_ticker_message']):
            CONFIG_DATA['static_ticker_font_length'] = CONFIG_DATA['static_ticker_font_length'] + 10 + CONFIG_DATA["static_ticker_font_height"]
        else:
            CONFIG_DATA['static_ticker_font_length'] = CONFIG_DATA['static_ticker_font_length'] + CONFIG_DATA["static_ticker_font_height"]

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

def ticker_animated_center():
    global size
    if CONFIG_DATA['moving_ticker_center_size'] == "normal":
        size = 2
        # global size
    elif CONFIG_DATA['moving_ticker_center_size'] == "small":
        size = 4
        # global size
    elif CONFIG_DATA['moving_ticker_center_size'] == "large":
        size = 1.5
        # global size
    elif CONFIG_DATA['moving_ticker_center_size'] == "full":
        size = 1
        # global size

    CONFIG_DATA['ticker_animated_center_width'] = int(conf['resolution_width'] / size)
    CONFIG_DATA['ticker_animated_center_height'] = int(conf['resolution_height'] / size)

def ticker_speed(speed):
    if speed == "fast":
        ticker_speed.block_skip = 4
        ticker_speed.time_sleep = 0.003
    elif speed == "normal":
        ticker_speed.block_skip = 2
        ticker_speed.time_sleep = 0.006
    elif speed == "slow":
        ticker_speed.block_skip = 2
        ticker_speed.time_sleep = 0.009
    elif speed == "very-slow":
        ticker_speed.block_skip = 2
        ticker_speed.time_sleep = 0.012

def font_n_length(font_name):
    message = CONFIG_DATA['main_ticker_message']
    if CONFIG_DATA['main_ticker_font_size'] == 'x-large':
        font_n_length.ticker_font_size = 115
        font_n_length.main_ticker_hight = -18
    elif CONFIG_DATA['main_ticker_font_size'] == 'large':
        font_n_length.ticker_font_size = 115
        font_n_length.main_ticker_hight = -18
    elif CONFIG_DATA['main_ticker_font_size'] == 'mid':
        font_n_length.ticker_font_size = 100
        font_n_length.main_ticker_hight = -5
    elif CONFIG_DATA['main_ticker_font_size'] == 'small':
        font_n_length.ticker_font_size = 85
        font_n_length.main_ticker_hight = 5
    ############## LIST OF ENGLISH FONTS ################
    if font_name == "english":
        font_n_length.left_length = int(float(len(message) * font_n_length.ticker_font_size) / 1.98) * (-1)
    elif font_name == "hindi":
        font_n_length.left_length = int(float(len(message) * font_n_length.ticker_font_size) / 2.4) * (-1)
    elif font_name == "chinese":
        font_n_length.left_length = int(float(len(message) * font_n_length.ticker_font_size) / 1) * (-1)
    elif font_name == "japnese":
        font_n_length.left_length = int(float(len(message) * font_n_length.ticker_font_size) / 1) * (-1)
    elif font_name == "russian":
        font_n_length.left_length = int(float(len(message) * font_n_length.ticker_font_size) / 1.9) * (-1)
    elif font_name == "arabic":
        font_n_length.left_length = int(float(len(message) * font_n_length.ticker_font_size) / 1.82) * (-1)


def optinal_font_n_length(font_name):
    message = CONFIG_DATA['optional_ticker_message']
    optinal_font_n_length.ticker_font_size = 40
    optinal_font_n_length.optional_ticker_hight = -8
    ############## LIST OF ENGLISH FONTS ################
    if font_name == "english":
        optinal_font_n_length.left_length = int(float(len(message) * optinal_font_n_length.ticker_font_size) / 1.6) * (-1)
    elif font_name == "hindi":
        optinal_font_n_length.left_length = int(float(len(message) * optinal_font_n_length.ticker_font_size) / 2.4) * (-1)
    elif font_name == "chinese":
        optinal_font_n_length.left_length = int(float(len(message) * optinal_font_n_length.ticker_font_size) / 1) * (-1)
    elif font_name == "japnese":
        optinal_font_n_length.left_length = int(float(len(message) * optinal_font_n_length.ticker_font_size) / 1) * (-1)
    elif font_name == "russian":
        optinal_font_n_length.left_length = int(float(len(message) * optinal_font_n_length.ticker_font_size) / 1.9) * (-1)
    elif font_name == "arabic":
        optinal_font_n_length.left_length = int(float(len(message) * optinal_font_n_length.ticker_font_size) / 1.82) * (-1)



def resize_gtk():
    # convert the logo to the resolution dependent
    print("Resizing the logo -> ", end=' ')
    square = CONFIG_DATA['static_ticker_font_height']
    print(f"FONT HEIGHT : {CONFIG_DATA['static_ticker_font_height']}")
    image = Image.open(f"""{BASE_DIR}/media/logo_gtk.png""")
    CONFIG_DATA['image_width'] = image.size[0]
    CONFIG_DATA['image_height'] = image.size[1]
    image_ratio = CONFIG_DATA['image_width'] / CONFIG_DATA['image_height']
    CONFIG_DATA['static_image_ratio'] = image_ratio
    print('Ratio before conversion:', image_ratio)
    if CONFIG_DATA['position_static_ticker'] == "fullscreen":
        image = image.resize((CONFIG_DATA["resolution_width"], CONFIG_DATA["resolution_height"]), Image.ANTIALIAS)
    elif CONFIG_DATA['position_static_ticker'] == "top_fix_width" or CONFIG_DATA['position_static_ticker'] == "bottom_fix_width":
        image = image.resize((int(CONFIG_DATA["resolution_width"]), int(CONFIG_DATA['resolution_width'] / image_ratio)), Image.ANTIALIAS)
    else:
        image = image.resize((int(square * image_ratio), square), Image.ANTIALIAS)
    image.save(fp=f"""{BASE_DIR}/media/res_logo_gtk.png""")
    print("Done")



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
    print("Done")


def dump():
    print("Dumping Data into Json File -> ", end=' ')
    with open(f"{BASE_DIR}/ticker_setup.json", "w") as outfile:
        outfile.write(json.dumps(CONFIG_DATA, indent=3))
    print("Done")


if __name__ == '__main__':
    start_time = time.time()
    resolution()

    # IF STATIC TICKER IS ENABLED
    if CONFIG_DATA['static_ticker_condition'] == True:
        gtk_worker()

        if CONFIG_DATA['static_ticker_logo'] == True:
            resize_gtk()

    # IF MAIN TICKER IS ENABLED
    if CONFIG_DATA['main_ticker_condition'] == True:
        ticker_speed(CONFIG_DATA['main_ticker_speed'])
        CONFIG_DATA['main_block_skip'] = ticker_speed.block_skip
        CONFIG_DATA['main_time_sleep'] = ticker_speed.time_sleep
        if CONFIG_DATA['main_ticker_font'] in ['hindi', 'chinese', 'japnese', 'russian', 'arabic']:
            font_n_length(CONFIG_DATA['main_ticker_font'])
        else:
            font_n_length("english")
        CONFIG_DATA['main_ticker_font_size'] = font_n_length.ticker_font_size
        CONFIG_DATA['main_ticker_font_length'] = font_n_length.left_length
        CONFIG_DATA['main_ticker_font_height'] = font_n_length.main_ticker_hight


        if CONFIG_DATA['main_ticker_logo'] == True:
            resize()
            png_jpg()

        # IF OPTIONAL TICKER IS ENABLED
    if CONFIG_DATA['optional_ticker_condition'] == True:
        ticker_speed(CONFIG_DATA['optional_ticker_speed'])
        CONFIG_DATA['optional_block_skip'] = ticker_speed.block_skip
        CONFIG_DATA['optional_time_sleep'] = ticker_speed.time_sleep

        if CONFIG_DATA['optional_ticker_font'] in ['hindi', 'chinese', 'japnese', 'russian', 'arabic']:
            optinal_font_n_length(CONFIG_DATA['optional_ticker_font'])
        else:
            optinal_font_n_length("english")
        CONFIG_DATA['optional_ticker_font_size'] = optinal_font_n_length.ticker_font_size
        CONFIG_DATA['optional_ticker_font_length'] = optinal_font_n_length.left_length
        CONFIG_DATA['optional_ticker_font_height'] = optinal_font_n_length.optional_ticker_hight

    if CONFIG_DATA['moving_ticker_condition'] == True:
        if CONFIG_DATA['moving_ticker_localtion'] == 'center':
            ticker_animated_center()

#        if CONFIG_DATA['moving_ticker_localtion'] == "bottom_fix_width":
#            CONFIG_DATA['moving_ticker_center_size'] = "full_width"
#
#        if CONFIG_DATA['moving_ticker_localtion'] == "top_fix_width":
#            CONFIG_DATA['moving_ticker_center_size'] = "full_width"



    dump()
    print("NEW CONFIG DATA IS: ", CONFIG_DATA)
    print("Execution took : --- %s seconds ---" % (time.time() - start_time))
