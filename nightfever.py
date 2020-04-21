from math import trunc, sqrt
from random import random, randrange

from PIL import Image, ImageDraw, ImageColor, ImageFilter

import straws_screen
import gravity_screen
import diagon_screen

# 3440 x 1440
WIDTH = 3440
HEIGHT = 1440

gravity_screen.draw_gravity_screen(WIDTH, HEIGHT)
#straws_screen.draw_straws_screen(WIDTH, HEIGHT)
#diagon_screen.draw_diagon_screen(WIDTH, HEIGHT)
