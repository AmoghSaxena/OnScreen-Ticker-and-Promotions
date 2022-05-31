import sys
import os
import time
import json
import pygame
from moviepy.editor import *

# Function -> Main Ticker on bottom screen.
def ticker_main():
    with open("ticker_setup.json", "r") as f:
        conf = json.load(f)

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((-1), (conf['resolution_height']) - (int(conf['resolution_height']) / 8))

    main_ticker_font_size = conf['main_ticker_font_size']
    pygame.init()
    pygame.display.set_caption('MainTicker')
    windowSize = [conf['resolution_width'], conf['resolution_height'] / 8]

    if conf['main_ticker_logo'] == True:
        if conf['main_ticker_logo_position'] == "left":
            x = 0  # image
            y = conf['resolution_width'] / 96  # image
        elif conf['main_ticker_logo_position'] == "right":
            x = conf['resolution_width'] - conf['image_size']  # image
            y = conf['resolution_width'] / 96  # image

    a = conf['resolution_width']  # for text
    b = conf['main_ticker_font_height']  # for text

    # message = conf['ticker_message']
    message = conf['main_ticker_message']
    picture = pygame.image.load(conf['BASE_DIR'] + '/media/res_logo.jpg')
    fonting = pygame.font.SysFont(conf['main_ticker_font'], main_ticker_font_size)
    texting = fonting.render(message, 1, tuple(conf['main_ticker_font_color']))
    screen = pygame.display.set_mode(windowSize)
    white = pygame.color.Color(tuple(conf['main_ticker_bgcolor']))

    def right_to_left(a, b, block_skip, time_sleep):
        while True:
            screen.fill(white)
            a = a - block_skip
            time.sleep(time_sleep)
            if a <= conf['main_ticker_font_length']:
                a = (conf['resolution_width'] + int(conf['resolution_width']*0.010))

            screen.blit(texting, (a, b))
            if conf['main_ticker_logo'] == True:
                screen.blit(picture, (x, y))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True

    def left_to_right(a, b, block_skip, time_sleep):
        while True:
            screen.fill(white)
            a = a + block_skip
            time.sleep(time_sleep)
            if a >= (conf['resolution_width'] + int(conf['resolution_width']*0.010)):
                a = conf['main_ticker_font_length']

            screen.blit(texting, (a, b))
            if conf['main_ticker_logo'] == True:
                screen.blit(picture, (x, y))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True

    if conf['main_ticker_motion'] == "right-left":
        right_to_left(a, b, conf['main_block_skip'], conf['main_time_sleep'])
    elif conf['main_ticker_motion'] == "left-right":
        left_to_right(a, b, conf['main_block_skip'], conf['main_time_sleep'])

    pygame.quit()


# Function -> Secondary Ticker moving above the primary(main) ticker
def ticker_optional():
    # optinal_font_n_length()
    with open("ticker_setup.json", "r") as f:
        conf = json.load(f)

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (
    (-1), (conf['resolution_height']) - (int(conf['resolution_height']) / 6))

    optional_ticker_font_size = conf['optional_ticker_font_size']
    pygame.init()
    pygame.display.set_caption('OptionalTicker')
    windowSize = [conf['resolution_width'], conf['resolution_height'] / 6]

    a = conf['resolution_width']  # for text
    b = conf['optional_ticker_font_height']
    # b = int(float(conf['resolution_height'] - (conf['resolution_height'] / 8)) * 0.01)  # for text

    message = conf['optional_ticker_message']

    # picture = pygame.image.load(conf['BASE_DIR']+'/media/res_logo.jpg')
    fonting = pygame.font.SysFont(conf['optional_ticker_font'], optional_ticker_font_size)
    texting = fonting.render(message, 1, tuple(conf['optional_ticker_font_color']))
    screen = pygame.display.set_mode(windowSize)
    white = pygame.color.Color(tuple(conf['optional_ticker_bgcolor']))

    def optional_right_to_left(a, b, block_skip, time_sleep):
        while True:
            screen.fill(white)
            a = a - block_skip
            time.sleep(time_sleep)
            if a <= conf['optional_ticker_font_length']:
                a = (conf['resolution_width'] + int(conf['resolution_width']*0.010))
            screen.blit(texting, (a, b))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True

    def optional_left_to_right(a, b, block_skip, time_sleep):
        while True:
            screen.fill(white)
            a = a + block_skip
            time.sleep(time_sleep)
            if a >= (conf['resolution_width'] + int(conf['resolution_width']*0.010)):
                a = conf['optional_ticker_font_length']

            screen.blit(texting, (a, b))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True

    if conf['optinal_ticker_motion'] == "right-left":
        optional_right_to_left(a, b, conf['optional_block_skip'], conf['optional_time_sleep'])
    elif conf['optinal_ticker_motion'] == "left-right":
        optional_left_to_right(a, b, conf['optional_block_skip'], conf['optional_time_sleep'])

    pygame.quit()




args = sys.argv
if args[1] == '1':
    # To run Optional Ticker
    ticker_optional()
elif args[1] == '2':
    # To run Main Ticker below
    ticker_main()