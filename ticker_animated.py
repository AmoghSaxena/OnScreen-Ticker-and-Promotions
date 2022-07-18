import json
import os
import pygame
from moviepy.editor import *

size = 1

def ticker_animated_sides():
    with open("ticker_setup.json", "r") as f:
        conf = json.load(f)

    size = int(conf['resolution_height']/4.9)

    if conf['moving_ticker_localtion'] == "bottom-right":
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((conf['resolution_width'] - size), (conf['resolution_height'] - size))
    elif conf['moving_ticker_localtion'] == "bottom-left":
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, (conf['resolution_height'] - size))
    elif conf['moving_ticker_localtion'] == "top-right":
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((conf['resolution_width'] - size), 0)
    elif conf['moving_ticker_localtion'] == "top-left":
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)

    clip = VideoFileClip("media/myvideo.mp4")
    value = clip.size
    print(value)
    print(value[0])
    print(value[0])


    clip = VideoFileClip('media/myvideo.mp4').resize((size, size))# Size of animated Ticker

    while True:
        clip.preview()

    pygame.quit()



def ticker_animated_center():
    global size
    with open("ticker_setup.json", "r") as f:
        conf = json.load(f)

        if conf['moving_ticker_center_size'] == "normal":
            size = 2
        elif conf['moving_ticker_center_size'] == "small":
            size = 4
        elif conf['moving_ticker_center_size'] == "large":
            size = 1.5
        elif conf['moving_ticker_center_size'] == "full":
            size = 1

    clip = VideoFileClip('media/myvideo.mp4').resize((int(conf['resolution_width']/size), int(conf['resolution_height']/size))) # Size of animated Ticker

    while True:
        clip.preview()

    pygame.quit()

with open("ticker_setup.json", "r") as f:
    conf = json.load(f)

if conf['moving_ticker_localtion'] == "center":
    ticker_animated_center()
else:
    ticker_animated_sides()