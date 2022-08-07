"""

raylib [other] example - Snake

"""
from pyray import *
from raylib import *
from raylib.colors import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
ROWS = 20
COLUMNS = 20
TILE_X = SCREEN_WIDTH // COLUMNS
TILE_Y = SCREEN_WIDTH // ROWS

grid = []

movement = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}


def key_detection():
    if is_key_down(KEY_UP) or is_key_down(KEY_W):
        if not movement["DOWN"]:
            movement["UP"] = True
            movement["DOWN"] = False
            movement["LEFT"] = False
            movement["RIGHT"] = False
    elif is_key_down(KEY_DOWN) or is_key_down(KEY_S):
        if not movement["UP"]:
            movement["UP"] = False
            movement["DOWN"] = True
            movement["LEFT"] = False
            movement["RIGHT"] = False
    elif is_key_down(KEY_LEFT) or is_key_down(KEY_A):
        if not movement["RIGHT"]:
            movement["UP"] = False
            movement["DOWN"] = False
            movement["LEFT"] = True
            movement["RIGHT"] = False
    elif is_key_down(KEY_RIGHT) or is_key_down(KEY_D):
        if not movement["LEFT"]:
            movement["UP"] = False
            movement["DOWN"] = False
            movement["LEFT"] = False
            movement["RIGHT"] = True


def generate_grid():
    for i in range(ROWS):
        for j in range(COLUMNS):
            grid.append([])
            grid[i].append(0)


def draw_grid():
    for i in range(ROWS):
        for j in range(COLUMNS):
            draw_rectangle_lines(j * TILE_X, i * TILE_Y, TILE_X, TILE_Y, WHITE)


generate_grid()

init_window(SCREEN_WIDTH, SCREEN_HEIGHT,
            'raylib [other] example - Snake')

set_target_fps(60)

while not window_should_close():
    begin_drawing()

    clear_background(BLACK)

    draw_grid()
    key_detection()

    end_drawing()
    print(movement)
close_window()
