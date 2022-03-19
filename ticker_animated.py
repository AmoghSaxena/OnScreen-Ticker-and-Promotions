import json
import os
import pygame
from moviepy.editor import *

def ticker_animated_right():
    with open("ticker_setup.json", "r") as f:
        conf = json.load(f)

    size = int(conf['resolution_height']/4.9)

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((conf['resolution_width'] - size), (conf['resolution_height'] - size)) # Size of animated ticker
    clip = VideoFileClip('media/myvideo.mp4').resize((size, size)) # Size of animated Ticker

    while True:
        clip.preview()

    pygame.quit()

def ticker_animated_left():
    with open("ticker_setup.json", "r") as f:
        conf = json.load(f)

    size = int(conf['resolution_height']/4.9)

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, (conf['resolution_height'] - size)) # Size of animated ticker
    clip = VideoFileClip('media/myvideo.mp4').resize((size, size)) # Size of animated Ticker

    while True:
        clip.preview()

    pygame.quit()


def ticker_animated_center():
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
if conf['moving_ticker_localtion'] == "right":
    ticker_animated_right()
elif conf['moving_ticker_localtion'] == "left":
    ticker_animated_left()
elif conf['moving_ticker_localtion'] == "center":
    ticker_animated_center()
