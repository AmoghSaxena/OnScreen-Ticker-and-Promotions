import json
import os
import pygame
from moviepy.editor import *

size = 1
clip_video = VideoFileClip("media/myvideo.mp4")
value = clip_video.size
print(value)
ratio = value[0] / value[1]
with open("ticker_setup.json", "r") as f:
    conf = json.load(f)

if conf['moving_ticker_center_size'] == "normal":
    size = 2
elif conf['moving_ticker_center_size'] == "small":
    size = 4
elif conf['moving_ticker_center_size'] == "large":
    size = 1.5


if conf['moving_ticker_localtion'] == "bottom-right":
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((conf['resolution_width'] - (ratio * size)) - 20, (conf['resolution_height'] - size - 20))
elif conf['moving_ticker_localtion'] == "bottom-left":
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, (conf['resolution_height'] - size - 20))
elif conf['moving_ticker_localtion'] == "top-right":
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((conf['resolution_width'] - (ratio * size)) - 20, 0)
elif conf['moving_ticker_localtion'] == "top-left":
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)

if conf['moving_ticker_center_size'] == "full":
    clip = clip_video.resize((int(conf['resolution_width']), int(conf['resolution_height'])))
else:
    clip = clip_video.resize((conf['resolution_height']/size) * ratio, (conf['resolution_height']/size)).margin(mar=10, color=(tuple(conf['moving_ticker_color'])))

while True:
    clip.preview()
pygame.quit()




# def ticker_animated_sides():
#     with open("ticker_setup.json", "r") as f:
#         conf = json.load(f)
#
#     # size = int(conf['resolution_height']/3)
#
#
#
#     # Size of animated Ticker
#
#     while True:
#         clip.preview()
#
#
#
#
#
# def ticker_animated_center():
#     global size
#     with open("ticker_setup.json", "r") as f:
#         conf = json.load(f)
#
#
#         elif conf['moving_ticker_center_size'] == "full":
#             clip = VideoFileClip('media/myvideo.mp4').resize((int(conf['resolution_width']), int(conf['resolution_height'])))
#
#     clip = VideoFileClip('media/myvideo.mp4').resize((int(conf['resolution_width']/size), int(conf['resolution_height']/size))).margin(mar=10, color=(110, 5, 27)) # Size of animated Ticker
#
#     while True:
#         clip.preview()
#
#     pygame.quit()
#
# with open("ticker_setup.json", "r") as f:
#     conf = json.load(f)
#
# if conf['moving_ticker_localtion'] == "center":
#     ticker_animated_center()
# else:
#     ticker_animated_sides()