from math import trunc, sqrt
from random import random, randrange

from PIL import Image, ImageDraw, ImageColor, ImageFilter

# 3440 x 1440

def draw_diagon_screen(final_width, final_height):
    SUPERSAMPLE = 8
    SPLITSIZE = 30
    LINE_WIDTH = 2
    #WIDTH_RUN = (final_width - final_height)*SUPERSAMPLE
    BRIGHT_1 = randrange(95.0, 100.0)
    BRIGHT_2 = randrange(95.0, 100.0)
    HUE_1 = randrange(250.0, 360.0)
    HUE_2 = randrange(250.0, 360.0)
    XITION_STOP = randrange(45.0, 90.0)
    XITION_START = randrange(10.0, XITION_STOP - 10.0)

    img = Image.new('RGB', (final_width*SUPERSAMPLE, final_height*SUPERSAMPLE), color='black')
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]

    perc_complete = 0
    for i in range(0, width, SPLITSIZE*SUPERSAMPLE):

        draw.line([(0, height), (i, 0)], fill="white", width=LINE_WIDTH*SUPERSAMPLE)
        draw.line([(width, 0), (i, height)], fill="white", width=LINE_WIDTH*SUPERSAMPLE)
        new_perc_complete = trunc(100 * i / width)
        if new_perc_complete > perc_complete:
            perc_complete = new_perc_complete
            print(perc_complete)

    img2 = img.resize((final_width, final_height), Image.ANTIALIAS)
    img2.save('output_images/diagon.png')
