import json
import os
import pygame
from moviepy.editor import *

size = 1
with open("ticker_setup.json", "r") as f:
    conf = json.load(f)

clip_video = VideoFileClip("media/myvideo.mp4")
value = clip_video.size
print(value)
ratio = value[0] / value[1]

if conf['moving_ticker_center_size'] == "small":
    size = int(conf['resolution_height']/3)
elif conf['moving_ticker_center_size'] == "normal":
    size = int(conf['resolution_height']/2)
elif conf['moving_ticker_center_size'] == "large":
    size = int(conf['resolution_height']/1.5)
elif conf['moving_ticker_center_size'] == "full":
    size = int(conf['resolution_height']/1)


if conf['moving_ticker_localtion'] == "bottom-right":
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((conf['resolution_width'] - (ratio * size)) - 20, (conf['resolution_height'] - size - 20))
elif conf['moving_ticker_localtion'] == "bottom-left":
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, (conf['resolution_height'] - size - 20))
elif conf['moving_ticker_localtion'] == "top-right":
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((conf['resolution_width'] - (ratio * size)) - 20, 0)
elif conf['moving_ticker_localtion'] == "top-left":
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
elif conf['moving_ticker_localtion'] == "top_fix_width":
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)

# CONFIG_DATA["resolution_width"], (CONFIG_DATA['resolution_height']) / 8

if conf['moving_ticker_center_size'] == "full":
    clip = clip_video.resize((ratio * size, size)).without_audio()
elif conf['moving_ticker_center_size'] == "full_width":
    clip = clip_video.resize((conf["resolution_width"], (conf['resolution_height']) / 8)).without_audio()
else:
    clip = clip_video.resize((ratio * size, size)).margin(mar=10, color=(tuple(conf['moving_ticker_color']))).without_audio()



while True:
    clip.preview()
pygame.quit()

