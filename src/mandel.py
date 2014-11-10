#!/usr/bin/env python3
import sys
import pygame
import datetime
import argparse
import mandely
from pygame.locals import *
import numpy as np
from timeit import default_timer as timer
# from numba import autojit


# @autojit
def mandel(x, y, max_iters):
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if abs(z) >= 3.5:
            return i  # 発散しない

    return max_iters  # 発散


# @autojit
def create_fractal(min_x, max_x, min_y, max_y, image, screen, iters):
    start = timer()
    print("%f < x < %f, %f < y < %f" % (min_x, max_x, min_y, max_y))
    print("Mandelbrot set plotting...")
    height = image.shape[0]
    width = image.shape[1]
    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height
    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            # res = mandel(real, imag, iters)
            res = mandely.mandel(real, imag, iters)  # Cython
            if res < iters:
                color = (0, (res * 10) % 255, 255)
            else:
                color = (0, 0, 0)  # マンデルブロ集合に属している
            plot_mandel(x, y, color, screen)
    dt = timer() - start
    print("Mandel created in %f s" % dt)


def plot_mandel(x, y, color, screen):
    pygame.draw.line(screen, color, (x, y), (x, y))


def main(width, height, min_x, max_x, min_y, max_y, iters):
    screen_size = width, height
    # min_x, max_x = -2.0, 1.0
    # min_y, max_y = -1.5, 1.5
    # iters = 30               # 反復回数
    zooming = 1.5            # ズーム率
    pygame.init()
    screen = pygame.display.set_mode(
        screen_size, HWSURFACE | DOUBLEBUF | RESIZABLE)
    pygame.display.set_caption(sys.argv[0] + " "
                               + str(width) + " x " + str(height))
    image = np.zeros((height, width), dtype=np.uint8)
    
    create_fractal(min_x, max_x, min_y, max_y, image, screen, iters)
    sysfont = pygame.font.SysFont(None, (int)((width * height) / 25000))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Exiting...")
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    print("Exiting...")
                    sys.exit()
                elif event.key == K_s:
                    print("Saving the screen")
                    pygame.image.save(screen, datetime.datetime.now().strftime('screenshot_%Y-%m-%d_%H:%M:%S.%f.png'))
                elif event.key == K_r:
                    print("Resetting...")
                    min_x, max_x = -2.0, 1.0
                    min_y, max_y = -1.5, 1.5
                    create_fractal(min_x, max_x, min_y, max_y,
                                   image, screen, iters)
                elif event.key == K_i:
                    # Zoom in
                    min_x /= zooming
                    max_x /= zooming
                    min_y /= zooming
                    max_y /= zooming
                    print("Zoom in")
                    create_fractal(min_x, max_x, min_y, max_y,
                                   image, screen, iters)
                elif event.key == K_o:
                # Zoom out
                    min_x *= zooming
                    max_x *= zooming
                    min_y *= zooming
                    max_y *= zooming
                    print("Zoom out")
                    create_fractal(min_x, max_x, min_y, max_y,
                                   image, screen, iters)
                elif event.key == K_UP or event.key == K_k:
                    # 半分上に行く
                    height = max_y - min_y
                    min_y -= height / 2
                    max_y -= height / 2
                    print("Shift up half screen")
                    print("height: %f width: %f" % (height, width))
                    create_fractal(min_x, max_x, min_y, max_y,
                                   image, screen, iters)
                elif event.key == K_DOWN or event.key == K_j:
                    # 半分下に行く
                    height = max_y - min_y
                    min_y += height / 2
                    max_y += height / 2
                    print("Shift down half screen")
                    print("height: %f width: %f" % (height, width))
                    create_fractal(min_x, max_x, min_y, max_y,
                                   image, screen, iters)
                elif event.key == K_LEFT or event.key == K_h:
                    # 半分左に行く
                    width = max_x - min_x
                    min_x -= width / 2
                    max_x -= width / 2
                    print("Shift left")
                    print("height: %f width: %f" % (height, width))
                    create_fractal(min_x, max_x, min_y, max_y,
                                   image, screen, iters)
                elif event.key == K_RIGHT or event.key == K_l:
                    # 半分左に行く
                    width = max_x - min_x
                    min_x += width / 2
                    max_x += width / 2
                    print("Shift Right")
                    print("height: %f width: %f" % (height, width))
                    create_fractal(min_x, max_x, min_y, max_y,
                                   image, screen, iters)

                zahyo = "{0} < x < {1}, {2} < y < {3}".format(min_x, max_x, min_y, max_y)
                st = sysfont.render(zahyo, True, (255, 255, 255))
                screen.blit(st, (20, 30))
                pygame.display.update()


if __name__ == "__main__":
    description = "This program is plotting mandelbrot set \
    using Pygame and Numpy"
    '''
    How to control: (Keyboard Shortcut)
    * Zoom in     : i
    * Zoom out    : o
    * Shift up    : up arrow key or k
    * Shift down  : down arrow key or j
    * Shift left  : left arrow key or h
    * Shift right : right arrow key or l
    * Save screen : s
    * Exit        : q
    '''    
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--width', type=int, default=720,
                        help="スクリーンの幅 デフォルト値:720")
    parser.add_argument('--height', type=int, default=480,
                        help="スクリーンの高さ デフォルト値:480")

    parser.add_argument('--minx', type=float, default=-2.0,
                        help="xの最小値 デフォルト値:2.0")
    parser.add_argument('--maxx', type=float, default=1.0,
                        help="xの最大値 デフォルト値:1.0")
    parser.add_argument('--miny', type=float, default=-1.5,
                        help="yの最小値 デフォルト値:-1.5")
    parser.add_argument('--maxy', type=float, default=1.5,
                        help="yの最大値 デフォルト値:1.5")
    parser.add_argument('--iters', type=int, default=30,
                        help="反復回数 デフォルト値:30回"
                        )
    args = parser.parse_args()
    main(args.width, args.height, args.minx, args.maxx, args.miny, args.maxy, args.iters)
