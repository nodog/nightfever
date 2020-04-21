from math import trunc, sqrt
from random import random, randrange

from PIL import Image, ImageDraw, ImageColor, ImageFilter

# 3440 x 1440

def draw_straws_screen(final_width, final_height):
    BRIGHT_1 = randrange(5.0, 20.0)
    BRIGHT_2 = randrange(5.0, 20.0)
    HUE_1 = randrange(250.0, 360.0)
    HUE_2 = randrange(250.0, 360.0)
    XITION_STOP = randrange(45.0, 90.0)
    XITION_START = randrange(10.0, XITION_STOP - 10.0)

    img = Image.new('RGB', (final_width, final_height), color='black')
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]

    perc_complete = 0
    for j in range(0, height):
        split_width = (XITION_START + randrange(XITION_STOP - XITION_START))/100.0*width
        draw.line([(0, j), (split_width, j)], fill="hsl({}, 100%, {}%)".format(HUE_1, BRIGHT_1))
        draw.line([(split_width, j), (width - 1, j)], fill="hsl({}, 100%, {}%)".format(HUE_2, BRIGHT_2))
        new_perc_complete = trunc(100 * j / height)
        if new_perc_complete > perc_complete:
            perc_complete = new_perc_complete
            print(perc_complete)

    img.save('output_images/straws-{}_{}_{}_{}_{}_{}.png'.format(BRIGHT_1, BRIGHT_2, HUE_1, HUE_2, XITION_START, \
                                                                 XITION_STOP))
