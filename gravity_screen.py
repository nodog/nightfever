from math import trunc, sqrt, atan2, sin
from random import random, randrange, uniform

from PIL import Image, ImageDraw, ImageColor, ImageFilter


class GravityScreen:

    class Zeem:
        def __init__(self, x, y, r, hue, phi):
            self.x = x
            self.y = y
            self.r = r
            self.hue = hue
            self.phi = phi

    def __init__(self):
        self.n_frames = 100
        self.n_zeems = 300000  # the colored objects
        self.n_plorgs = 3  # the invisible repulsors
        self.brightness_max = 30.0
        self.movement = 150.0
        self.supersample = 4
        self.radius = 2

    def __repulse(self, a_xy, b_xy):
        xd = b_xy.x - a_xy.x
        yd = b_xy.y - a_xy.y
        r = sqrt(xd ** 2 + yd ** 2)
        theta = atan2(yd, xd)
        x_push = xd / r
        y_push = yd / r
        # strength = 4.0 * abs(theta) / (3.14 * r ** 2)
        strength = 16.0 * abs(sin(theta + a_xy.phi)) / r ** 0.5
        # print(abs(sin(theta + a_xy.phi)))
        return x_push, y_push, strength

    def draw_screen(self, final_width, final_height):
        img = Image.new('RGB', (final_width*self.supersample, final_height*self.supersample), color='black')
        draw = ImageDraw.Draw(img)
        width = img.size[0]
        height = img.size[1]

        zeems_xy = []
        for i_zeem in range(0, self.n_zeems):
            # red centered around 340-350
            # blue centered around 230
            # purple centered around 280
            # green around 80-100
            hue = i_zeem*44.0/self.n_zeems
            if hue > 42:
                hue += 300
            elif hue > 40:
                hue += 40
            else:
                hue += 255
            zeems_xy.append(self.Zeem(randrange(width), randrange(height), self.radius, hue, 0.0))

        plorgs_xy = []
        for i_plorg in range(0, self.n_plorgs):
            plorgs_xy.append(self.Zeem(randrange(width), randrange(height), 0.0, 0.0, uniform(0.0, 6.28)))

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
                    zeems_xy[i_zeem].x += x_push * strength * self.movement / self.n_frames
                    zeems_xy[i_zeem].y += y_push * strength * self.movement / self.n_frames

            new_perc_complete = trunc(100 * i_frame / self.n_frames)
            if new_perc_complete > perc_complete:
                perc_complete = new_perc_complete
                print(f"{perc_complete}% complete")

        img2 = img.resize((trunc(width/self.supersample), trunc(height/self.supersample)), Image.LANCZOS)
        img2.save('output_images/gravity-{}.png'.format(randrange(100000,999999)))
