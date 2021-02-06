from math import trunc, sqrt
from random import random, randrange

from PIL import Image, ImageDraw, ImageColor, ImageFilter


class GravityScreen:

    class Zeem:
        def __init__(self, x, y, r, hue):
            self.x = x
            self.y = y
            self.r = r
            self.hue = hue

    def __init__(self):
        self.n_frames = 800
        self.n_zeems = 12000  # the colored objects
        self.n_plorgs = 6  # the invisible repulsors
        self.brightness_max = 30.0
        self.movement = 120.0
        self.supersample = 4
        self.radius = 30

    def __repulse(self, a_xy, b_xy):
        xd = b_xy.x - a_xy.x
        yd = b_xy.y - a_xy.y
        r = sqrt(xd ** 2 + yd ** 2)
        x_push = xd / r
        y_push = yd / r
        strength = 4.0 / r ** 2
        return x_push, y_push, strength

    def draw_screen(self, final_width, final_height):
        img = Image.new('RGB', (final_width*self.supersample, final_height*self.supersample), color='black')
        draw = ImageDraw.Draw(img)
        width = img.size[0]
        height = img.size[1]

        zeems_xy = []
        for i_zeem in range(0, self.n_zeems):
            hue = i_zeem*30.0/self.n_zeems + 259.0
                # if hue > 90:
                #     hue += 90
                # if hue > 280:
                #     hue += 30
            zeems_xy.append(self.Zeem(randrange(width), randrange(height), self.radius, hue))

        plorgs_xy = []
        for i_plorg in range(0, self.n_plorgs):
            plorgs_xy.append(self.Zeem(randrange(width), randrange(height), 0.0, 0.0))

        perc_complete = 0
        for i_frame in range(0, self.n_frames):
            for i_zeem in range(0, self.n_zeems):
                brightness = self.brightness_max * i_frame / self.n_frames
                draw.ellipse([(zeems_xy[i_zeem].x - self.radius, zeems_xy[i_zeem].y - self.radius),
                               (zeems_xy[i_zeem].x + self.radius, zeems_xy[i_zeem].y + self.radius)],
                               fill="hsl({}, 100%, {}%)".format(zeems_xy[i_zeem].hue, brightness))
                # draw.point((zeems_xy[i_zeem].x, zeems_xy[i_zeem].y),fill="hsl({}, 100%, {}%)".format(i_zeem*45.0/self.n_zeems + 20, brightness))
                #draw.point((zeems_xy[i_zeem].x, zeems_xy[i_zeem].y),
                           # fill="hsl({}, 100%, {}%)".format(i_zeem * 99.0 / self.n_zeems + 225.0, brightness))
                           # fill="hsl({}, 100%, {}%)".format(i_zeem * 360.0 / self.n_zeems, brightness))
                for i_plorg in range(0, self.n_plorgs):
                    x_push, y_push, strength = self.__repulse(plorgs_xy[i_plorg], zeems_xy[i_zeem])
                    #print(x_push, y_push, strength)
                    zeems_xy[i_zeem].x += x_push * self.movement / self.n_frames
                    zeems_xy[i_zeem].y += y_push * self.movement / self.n_frames

            new_perc_complete = trunc(100 * i_frame / self.n_frames)
            if new_perc_complete > perc_complete:
                perc_complete = new_perc_complete
                print(f"{perc_complete}% complete")

        img2 = img.resize((trunc(width/self.supersample), trunc(height/self.supersample)), Image.LANCZOS)
        img2.save('output_images/output-gravity-{}.png'.format(randrange(100000,999999)))
