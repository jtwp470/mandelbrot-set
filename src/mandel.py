import numpy as np
import pylab
from timeit import default_timer as timer


SCREEN_SIZE = (1024, 1536)


def mandel(x, y, max_iters=30):
    """
    マンデルブロ集合の計算回数を返す
    max_iter が返ってくれば発散しないことになりマンデルブロ集合に属す
    """
    c, z, iter = complex(x, y), complex(0, 0), 0
    for iter in range(max_iters):
        z = z*z + c
        if abs(z) > 3.5:  # 発散した
            return iter

    return max_iters


def create_mandelplot(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pix_x = (max_x - min_x) / width
    pix_y = (max_y - min_y) / height

    for x in range(width):
        real = min_x + x * pix_x
        for y in range(height):
            imag = min_y + y * pix_y
            color = mandel(real, imag, iters)
            image[y, x] = color


def main():
    #    r = {'min_x': -1, 'max_x': 2, 'min_y': -1.5, 'max_y': 1.5}
    image = np.zeros(SCREEN_SIZE, dtype=np.uint8)
    start = timer()
    #    create_mandelplot(-1, 2, -1.5, 1.5, image, 30)
    create_mandelplot(-1, 1, -0.55, 0.55, image, 30)
    dt = timer() - start
    print("Running time: " + str(dt) + " s")
    pylab.imshow(image)
    pylab.show()
    

if __name__ == "__main__":
    main()
