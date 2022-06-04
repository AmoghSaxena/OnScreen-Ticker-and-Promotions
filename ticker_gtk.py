import os
import json
import pygame
from PIL import Image

with open("ticker_setup.json", "r") as f:
    conf = json.load(f)

conf['static_ticker_font_height'] = int(conf['static_ticker_font_size'] * 3)
conf['static_ticker_font'] = 'Ubuntu'

if 'bottom' in conf['position_static_ticker']:
    y_length = conf['resolution_height'] - conf['static_ticker_font_height']
elif 'top' in conf['position_static_ticker']:
    y_length = 0
if 'right' in conf['position_static_ticker']:
    x_length = conf['resolution_width'] - conf['static_ticker_font_length']
elif 'left' in conf['position_static_ticker']:
    x_length = 0
#
if 'center' not in conf['position_static_ticker']:
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x_length, y_length)

pygame.init()

if 'fullscreen' not in conf['position_static_ticker']:
    screen = pygame.display.set_mode((conf['static_ticker_font_length'], conf['static_ticker_font_height']))
else:
    screen = pygame.display.set_mode((conf['resolution_width'], conf['resolution_height']))
# set the pygame window name
pygame.display.set_caption('StaticTicker')

# font = pygame.font.SysFont(conf['static_ticker_font'], conf['static_ticker_font_size'])
# text = font.render(conf['static_ticker_message'], 1, tuple(conf['static_ticker_font_color']))

fonting = pygame.font.SysFont(conf['static_ticker_font'], conf['static_ticker_font_size'])
texting = fonting.render(conf['static_ticker_message'], 1, tuple(conf['static_ticker_font_color']))

# text = font.render("score: " + str(score), 1, (10, 10, 10))
textpos = texting.get_rect(centerx=screen.get_width() / 2)

textRect = texting.get_rect()
textRect.center = (conf['static_ticker_font_length'] // 2, conf['static_ticker_font_height'] // 2)
print(textRect)
print(tuple(textRect)[1])
while True:
    screen.fill(tuple(conf['static_ticker_bgcolor']))
    if conf['static_ticker_logo'] == True:
        picture = pygame.image.load(conf['BASE_DIR'] + '/media/res_logo_gtk.png')
        screen.blit(texting, ((conf["static_ticker_font_height"]), tuple(textRect)[1]))
        screen.blit(picture, (0, 0))
    if conf['static_ticker_logo'] == False:
        screen.blit(texting, (textRect))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True