import json
import os
from PIL import Image
import pygame
from moviepy.editor import *


with open("ticker_setup.json", "r") as f:
    conf = json.load(f)


def dynamic_ticker():
    clip = VideoFileClip('media/myvideo.mp4').resize((int(conf['resolution_width']), int(conf['resolution_height'])))
    while True:
        clip.preview()

    pygame.quit()


def static_ticker():
    background_color = [255,255,255]
    image = Image.open(f"""{conf['BASE_DIR']}/media/logo_gtk.png""")
    image = image.resize((conf["resolution_width"], conf["resolution_height"]), Image.ANTIALIAS)
    image.save(fp=f"""{conf['BASE_DIR']}/media/res_logo_gtk.png""")

    screen = pygame.display.set_mode((conf['resolution_width'], conf['resolution_height']))
    while True:
        screen.fill(tuple(background_color))
        picture = pygame.image.load(conf['BASE_DIR'] + '/media/res_logo_gtk.png')
        screen.blit(picture, (0, 0))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True


if conf['emergency_ticker_style'] == 'static':
    static_ticker()
elif conf['emergency_ticker_style'] == 'dynamic':
    dynamic_ticker()