from math import trunc, sqrt
from random import random, randrange

from PIL import Image, ImageDraw, ImageColor, ImageFilter


def draw_gravity_screen(final_width, final_height):
    N_FRAMES = 400
    N_ZEEMS = 28800  # the colored objects
    N_PLORGS = 6  # the invisible repulsors
    BRIGHTNESS_MAX = 20.0
    MOVEMENT = 300.0
    SUPERSAMPLE = 4
    img = Image.new('RGB', (final_width*SUPERSAMPLE, final_height*SUPERSAMPLE), color='black')
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    radius = 8

    class Zeem:
        def __init__(self, x, y, r):
            self.x = x
            self.y = y
            self.r = r

    zeems_xy = []
    for i_zeem in range(0, N_ZEEMS):
        zeems_xy.append(Zeem(randrange(width), randrange(height), radius))

    plorgs_xy = []
    for i_plorg in range(0, N_PLORGS):
        plorgs_xy.append(Zeem(randrange(width), randrange(height), 0.0))

    def repulse(a_xy, b_xy):
        xd = b_xy.x - a_xy.x
        yd = b_xy.y - a_xy.y
        r = sqrt(xd ** 2 + yd ** 2)
        x_push = xd / r
        y_push = yd / r
        strength = 4.0 / r ** 2
        return x_push, y_push, strength

    perc_complete = 0
    for i_frame in range(0, N_FRAMES):
        for i_zeem in range(0, N_ZEEMS):
            brightness = BRIGHTNESS_MAX * i_frame / N_FRAMES
            draw.ellipse([(zeems_xy[i_zeem].x - radius, zeems_xy[i_zeem].y - radius),
                           (zeems_xy[i_zeem].x + radius, zeems_xy[i_zeem].y + radius)],
                           fill="hsl({}, 100%, {}%)".format(i_zeem*70.0/N_ZEEMS+80, brightness))
            # draw.point((zeems_xy[i_zeem].x, zeems_xy[i_zeem].y),fill="hsl({}, 100%, {}%)".format(i_zeem*45.0/N_ZEEMS + 20, brightness))
            #draw.point((zeems_xy[i_zeem].x, zeems_xy[i_zeem].y),
                       # fill="hsl({}, 100%, {}%)".format(i_zeem * 99.0 / N_ZEEMS + 225.0, brightness))
                       # fill="hsl({}, 100%, {}%)".format(i_zeem * 360.0 / N_ZEEMS, brightness))
            for i_plorg in range(0, N_PLORGS):
                x_push, y_push, strength = repulse(plorgs_xy[i_plorg], zeems_xy[i_zeem])
                #print(x_push, y_push, strength)
                zeems_xy[i_zeem].x += x_push * MOVEMENT / N_FRAMES
                zeems_xy[i_zeem].y += y_push * MOVEMENT / N_FRAMES

        new_perc_complete = trunc(100 * i_frame / N_FRAMES)
        if new_perc_complete > perc_complete:
            perc_complete = new_perc_complete
            print(perc_complete)

    img2 = img.resize((trunc(width/SUPERSAMPLE), trunc(height/SUPERSAMPLE)), Image.LANCZOS)
    img2.save('output_images/output-gravity-{}.png'.format(randrange(100000,999999)))
