from math import trunc, sqrt, pi, sin, cos
from random import random, randrange

from PIL import Image, ImageDraw, ImageColor, ImageFilter


class VelocityScreen:



    class Zeem:
        def __init__(self, x, y, r):
            self.x = x
            self.y = y
            self.r = r

    class Velgen:
        def __init__(self, x, y, vx, vy):
            self.x = x
            self.y = y
            self.vx = vx
            self.vy = vy

    def __init__(self):
        self.n_frames = 400
        self.n_zeems = 60  # the colored objects
        self.supersample = 4
        self.space_btw_velgens = 100 * self.supersample
        self.movement = 600.0 * self.supersample
        self.brightness_max = 40.0
        self.radius = 6

    def __vel_push(self, a_xy, b_xy):
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

        # Initial layout of velocity values
        velgens_xy = []
        n_x_velgen = width / self.space_btw_velgens + 1
        n_y_velgen = height / self.space_btw_velgens + 1
        for i in range(0, n_x_velgen):
            for j in range(0, n_y_velgen):
                x = i * self.space_btw_velgens
                y = j * self.space_btw_velgens
                theta = random(2*pi)
                vx = self.movement * cos(theta)
                vy = self.movement * sin(theta)
                velgens_xy.append(self.Velgen(x, y, vx, vy))

        # layout of zeems
        zeems_xy = []
        for i_zeem in range(0, self.n_zeems):
            zeems_xy.append(self.Zeem(randrange(width), randrange(height), self.radius))

        perc_complete = 0
        for i_frame in range(0, self.n_frames):
            for i_zeem in range(0, self.n_zeems):
                brightness = self.brightness_max * i_frame / self.n_frames
                hue = i_zeem*240.0/self.n_zeems
                if hue > 90:
                    hue += 90
                if hue > 280:
                    hue += 30
                # # show zeems
                draw.ellipse([(zeems_xy[i_zeem].x - self.radius, zeems_xy[i_zeem].y - self.radius),
                              (zeems_xy[i_zeem].x + self.radius, zeems_xy[i_zeem].y + self.radius)],
                             fill="hsl({}, 100%, {}%)".format(hue, brightness))

                # # move zeems once according to velocity values
                x_push, y_push = self.__vel_push(plorgs_xy[i_plorg], zeems_xy[i_zeem])
                    #print(x_push, y_push, strength)
                    zeems_xy[i_zeem].x += x_push * self.movement / self.n_frames
                    zeems_xy[i_zeem].y += y_push * self.movement / self.n_frames

            new_perc_complete = trunc(100 * i_frame / self.n_frames)
            if new_perc_complete > perc_complete:
                perc_complete = new_perc_complete
                print(perc_complete)

        img2 = img.resize((trunc(width/self.supersample), trunc(height/self.supersample)), Image.LANCZOS)
        img2.save('output_images/output-gravity-{}.png'.format(randrange(100000,999999)))
