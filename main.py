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

# head -> last, tail -> first
body = [
    (COLUMNS // 2, ROWS // 2),
    (COLUMNS // 2 - 1, ROWS // 2),
    (COLUMNS // 2 - 2, ROWS // 2),
]

SNAKE_BODY_COLOR = (64, 109, 240, 255)
SNAKE_HEAD_COLOR = (43, 73, 171, 255)


def reset_snake_body():
    global body
    body = [(COLUMNS // 2, ROWS // 2)]


def draw_snake():
    # draw snake body
    for i in range(len(body) - 1):
        draw_rectangle(body[i][0] * TILE_X, body[i][1] * TILE_Y, TILE_X, TILE_Y, SNAKE_BODY_COLOR)

    # draw snake head
    draw_rectangle(body[len(body) - 1][0] * TILE_X, body[len(body) - 1][1] * TILE_Y, TILE_X, TILE_Y, SNAKE_HEAD_COLOR)


def move_snake():
    body_len = len(body)
    if movement["DOWN"]:
        body.append((body[body_len - 1][0], body[body_len - 1][1] + 1))
        body.pop(0)

    elif movement["UP"]:
        body.append((body[body_len - 1][0], body[body_len - 1][1] - 1))
        body.pop(0)

    elif movement["RIGHT"]:
        body.append((body[body_len - 1][0] + 1, body[body_len - 1][1]))
        body.pop(0)

    elif movement["LEFT"]:
        body.append((body[body_len - 1][0] - 1, body[body_len - 1][1]))
        body.pop(0)

    if not ((0 <= body[body_len - 1][0] <= COLUMNS - 1) and (0 <= body[body_len - 1][1] <= ROWS - 1)):
        reset_snake_body()


def key_detection():
    if is_key_pressed(KEY_UP) or is_key_pressed(KEY_W):
        if not movement["DOWN"]:
            movement["UP"] = True
            movement["DOWN"] = False
            movement["LEFT"] = False
            movement["RIGHT"] = False
    if is_key_pressed(KEY_DOWN) or is_key_pressed(KEY_S):
        if not movement["UP"]:
            movement["UP"] = False
            movement["DOWN"] = True
            movement["LEFT"] = False
            movement["RIGHT"] = False
    if is_key_pressed(KEY_LEFT) or is_key_pressed(KEY_A):
        if not movement["RIGHT"]:
            movement["UP"] = False
            movement["DOWN"] = False
            movement["LEFT"] = True
            movement["RIGHT"] = False
    if is_key_pressed(KEY_RIGHT) or is_key_pressed(KEY_D):
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
            draw_rectangle_lines(j * TILE_X, i * TILE_Y, TILE_X, TILE_Y, LIGHTGRAY)


generate_grid()

init_window(SCREEN_WIDTH, SCREEN_HEIGHT,
            'raylib [other] example - Snake')

set_target_fps(10)

while not window_should_close():
    begin_drawing()

    clear_background(WHITE)

    draw_grid()
    key_detection()
    move_snake()
    draw_snake()

    end_drawing()

close_window()
