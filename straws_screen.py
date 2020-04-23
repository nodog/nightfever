from math import trunc, sqrt
from random import random, uniform, randrange

from PIL import Image, ImageDraw, ImageColor, ImageFilter


# 3440 x 1440
class StrawsScreen:
    """
    draw an image of straws
    """

    def __init__(self):
        self.bright_1 = uniform(5.0, 20.0)
        self.bright_2 = uniform(5.0, 20.0)
        self.hue_1 = uniform(250.0, 360.0)
        self.hue_2 = uniform(250.0, 360.0)
        self.xition_stop = uniform(45.0, 90.0)
        self.xition_start = uniform(10.0, self.xition_stop - 10.0)

    def draw_screen(self, width, height):

        img = Image.new('RGB', (width, height), color='black')
        draw = ImageDraw.Draw(img)

        percent_complete = 0
        for j in range(0, height):
            split_width = uniform(self.xition_start, self.xition_stop) / 100.0 * width
            draw.line([(0, j), (split_width, j)], fill="hsl({}, 100%, {}%)".format(self.hue_1, self.bright_1))
            draw.line([(split_width, j), (width - 1, j)], fill="hsl({}, 100%, {}%)".format(self.hue_2, self.bright_2))
            new_perc_complete = trunc(100 * j / height)
            if new_perc_complete > percent_complete:
                percent_complete = new_perc_complete
                print(percent_complete)

        img.save(f'output_images/straws-{self.bright_1:.1f}_{self.bright_2:.1f}_{self.hue_1:.1f}_{self.hue_2:.1f}_{self.xition_start:.1f}_{self.xition_stop:.1f}.png')
