import os
import json
import pygame
from PIL import Image
from PIL import ImageGrab

with open("ticker_setup.json", "r") as f:
    conf = json.load(f)


def static_ticker():
    pygame.init()

    if 'fullscreen' not in conf['position_static_ticker']:
        if conf['static_ticker_logo'] == True:
            # image = Image.open(conf['BASE_DIR'] + '/media/res_logo_gtk.png')
            # image_width = image.size[0]
            # image_height = image.size[1]
            screen = pygame.display.set_mode((image_width, image_height))
        else:
            screen = pygame.display.set_mode((conf['static_ticker_font_length'], conf['static_ticker_font_height']))
    elif 'top_fix_width' in conf['position_static_ticker'] or 'bottom_fix_width' in conf['position_static_ticker']:
        screen = pygame.display.set_mode((conf['resolution_width'], conf['resolution_width']/(conf['static_image_ratio'])))
    else:
        screen = pygame.display.set_mode((conf['resolution_width'], conf['resolution_height']))

    if 'fullscreen' in conf['position_static_ticker']:
        screen = pygame.display.set_mode((conf['resolution_width'], conf['resolution_height']))
    # set the pygame window name
    pygame.display.set_caption('StaticTicker')

    fonting = pygame.font.Font(f"{conf['BASE_DIR']}/fonts/NotoSans.ttf", conf['static_ticker_font_size'])
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


def static_ticker_center():
    pygame.init()

    # conf['static_ticker_font_height'] = int(conf['static_ticker_font_size'] * 3.5)
    # conf['static_ticker_font'] = 'Ubuntu'
    space_image = int((int(conf['static_ticker_font_size'] * 3.5) - conf['static_ticker_font_height'])/2)

    screen = pygame.display.set_mode((int(conf['static_ticker_font_size'] * 3.5), int(conf['static_ticker_font_size'] * 3.5) + int(conf['static_ticker_font_height']/3)))
    # set the pygame window name
    pygame.display.set_caption('StaticTicker')

    font_size_for_center = int(conf['static_ticker_font_size'] / 2.4)
    print(font_size_for_center)

    fonting = pygame.font.Font(f"{conf['BASE_DIR']}/fonts/NotoSans.ttf", font_size_for_center)
    texting = fonting.render(conf['static_ticker_message'], 1, tuple(conf['static_ticker_font_color']))

    textpos = texting.get_rect(centerx=screen.get_width() / 2)

    textRect = texting.get_rect()
    textRect.center = (conf['static_ticker_font_length'] // 2, conf['static_ticker_font_height'] // 2)
    print(textpos)
    print(tuple(textpos)[1])
    while True:
        screen.fill(tuple(conf['static_ticker_bgcolor']))
        picture = pygame.image.load(conf['BASE_DIR'] + '/media/res_logo_gtk.png')
        screen.blit(texting, (tuple(textpos)[0],(int(conf['static_ticker_font_size'] * 3.7))))
        screen.blit(picture, (space_image, space_image))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True






if conf['static_ticker_logo'] == True:
    image = Image.open(conf['BASE_DIR'] + '/media/res_logo_gtk.png')
    image_width = image.size[0]
    image_height = image.size[1]

if 'bottom' in conf['position_static_ticker']:
    y_length = conf['resolution_height'] - conf['static_ticker_font_height']
elif 'top' in conf['position_static_ticker']:
    y_length = 0
if 'right' in conf['position_static_ticker']:
    if conf['static_ticker_logo'] == True:
        x_length = conf['resolution_width'] - image_width
    else:
        x_length = conf['resolution_width'] - conf['static_ticker_font_length']
elif 'left' in conf['position_static_ticker']:
    x_length = 0
if 'fullscreen' in conf['position_static_ticker']:
    x_length = 0
    y_length = 0
#

if 'top_fix_width' in conf['position_static_ticker']:
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
    static_ticker()

elif 'bottom_fix_width' in conf['position_static_ticker']:
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, conf['resolution_height'] - conf['resolution_width']/(conf['static_image_ratio']))
    static_ticker()

elif 'center' not in conf['position_static_ticker']:
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x_length, y_length)
    static_ticker()

elif 'fullscreen' in conf['position_static_ticker']:

    static_ticker()

if 'center' in conf['position_static_ticker']:
    static_ticker_center()