from math import trunc, sqrt
from random import random, randrange

from PIL import Image, ImageDraw, ImageColor, ImageFilter


class DiagonScreen:

    def __init__(self):
        self.supersample = 8
        self.splitsize = 30
        self.line_width = 2

    def draw_screen(self, final_width, final_height):

        img = Image.new('RGB', (final_width*self.supersample, final_height*self.supersample), color='black')
        draw = ImageDraw.Draw(img)
        width = img.size[0]
        height = img.size[1]

        perc_complete = 0
        for i in range(0, width, self.splitsize*self.supersample):

            draw.line([(0, height), (i, 0)], fill="white", width=self.line_width*self.supersample)
            draw.line([(width, 0), (i, height)], fill="white", width=self.line_width*self.supersample)
            new_perc_complete = trunc(100 * i / width)
            if new_perc_complete > perc_complete:
                perc_complete = new_perc_complete
                print(perc_complete)

        img2 = img.resize((final_width, final_height), Image.ANTIALIAS)
        img2.save('output_images/diagon.png')
