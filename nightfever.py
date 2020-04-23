import straws_screen
import gravity_screen
import diagon_screen

# 3440 x 1440
WIDTH = 3440
HEIGHT = 1440

#my_screen = straws_screen.StrawsScreen();
my_screen = gravity_screen.GravityScreen();
#my_screen = diagon_screen.DiagonScreen();

my_screen.draw_screen(WIDTH, HEIGHT)
