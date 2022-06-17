import json
import os
from PIL import Image
import pygame
from moviepy.editor import *


with open("ticker_setup.json", "r") as f:
    conf = json.load(f)


def static_ticker():
    image = Image.open(f"""{conf['BASE_DIR']}/media/logo_gtk.png""")
    image = image.resize((conf["resolution_width"], conf["resolution_height"]), Image.ANTIALIAS)
    image.save(fp=f"""{conf['BASE_DIR']}/media/res_logo_gtk.png""")

    screen = pygame.display.set_mode((conf['resolution_width'], conf['resolution_height']))
    while True:
        screen.fill(255,255,255)
        picture = pygame.image.load(conf['BASE_DIR'] + '/media/res_logo_gtk.png')
        screen.blit(picture, (0, 0))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

static_ticker()