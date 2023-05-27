import pygcurse
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, K_TAB, K_ESCAPE
import random
import sys

########################################################################################################################

CELL_WIDTH = 6
CELL_HEIGHT = 6
HORIZONTAL_CELLS_NUMBER = 7
VERTICAL_CELLS_NUMBER = 7

BLUE = (0, 0, 128)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

########################################################################################################################


class Canva:

    def __init__(self):

        self.win = pygcurse.PygcurseWindow(CELL_WIDTH * HORIZONTAL_CELLS_NUMBER,
                                           CELL_HEIGHT * VERTICAL_CELLS_NUMBER,
                                           fullscreen=False)
        pygame.display.set_caption('CELLS')
        self.win.autowindowupdate = False
        self.win.autoupdate = False

    def fill_poly(self, x, y, width, height, color):
        for i in range(y, y + height):
            for j in range(x, x + width):
                self.win.paint(j, i, color)

########################################################################################################################


class ImpossibleBeautyShowElements(Canva):

    def stage_one(self):
        """ Show twisted cells picture """
        for i in range(VERTICAL_CELLS_NUMBER):
            for z in range(CELL_HEIGHT):
                for j in range(HORIZONTAL_CELLS_NUMBER):
                    for w in range(CELL_WIDTH + random.randint(0, 3)):

                        self.win.cursor = (j * CELL_WIDTH + w, i * CELL_HEIGHT + z)
                        if (i+j) % 2 == 0:
                            self.win.paint(j * CELL_WIDTH + w + random.randint(0, 1),
                                           i * CELL_HEIGHT + z + random.randint(0, 1),
                                           GREEN)
                        else:
                            self.win.paint(j * CELL_WIDTH + w + random.randint(0, 3),
                                           i * CELL_HEIGHT + z + random.randint(0, 3),
                                           BLUE)
        self.win.update()

    def stage_two(self):
        """ Show distorted square cells picture """

        distort_x = [random.randint(-2, 2) for _ in range(HORIZONTAL_CELLS_NUMBER)]
        distort_y = [random.randint(-2, 2) for _ in range(VERTICAL_CELLS_NUMBER)]

        # Distortion sums correction
        if sum(distort_x) != 0:
            ptr = random.randint(0, HORIZONTAL_CELLS_NUMBER - 1)
            distort_x[ptr] = distort_x[ptr] - sum(distort_x)
        if sum(distort_y) != 0:
            ptr = random.randint(0, VERTICAL_CELLS_NUMBER - 1)
            distort_y[ptr] = distort_y[ptr] - sum(distort_y)

        for i in range(VERTICAL_CELLS_NUMBER):
            for j in range(VERTICAL_CELLS_NUMBER):

                delta_x = sum(distort_x[0:j])
                delta_y = sum(distort_y[0:i])

                if (i + j) % 2 == 0:

                    self.fill_poly(j * CELL_WIDTH + delta_x,
                                   i * CELL_HEIGHT + delta_y,
                                   CELL_WIDTH + distort_x[j],
                                   CELL_HEIGHT + distort_y[i],
                                   BLUE)
                else:

                    self.fill_poly(j * CELL_WIDTH + delta_x,
                                   i * CELL_HEIGHT + delta_y,
                                   CELL_WIDTH + distort_x[j],
                                   CELL_HEIGHT + distort_y[i],
                                   GREEN)
        self.win.update()

    def add_sparks_over(self):
        """ Place yellow sparks over green-blue cells """
        for i in range(VERTICAL_CELLS_NUMBER):
            for j in range(VERTICAL_CELLS_NUMBER):
                self.fill_poly(j * CELL_WIDTH + 2,
                               i * CELL_HEIGHT + 2,
                               1,
                               1,
                               YELLOW)
        self.win.update()

########################################################################################################################


def main():

    obj = ImpossibleBeautyShowElements()

    # Show initial picture
    obj.stage_one()

    # Handle keyboard input
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    obj.stage_two()
                    obj.win.update()

                elif event.key == K_TAB:
                    obj.add_sparks_over()
                    obj.win.update()

                elif event.key == K_ESCAPE:
                    sys.exit()

########################################################################################################################


if __name__ == '__main__':
    main()
