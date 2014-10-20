from matplotlib import pyplot
from mandel import calc_mandelset


def plot():
    ranges = {'min_x': -2, 'max_x': 1, 'min_y': -1.5, 'max_y': 1.5}
    mandelbrot = calc_mandelset(**ranges)
    
    pyplot.imshow(mandelbrot, cmaps='spectral')
    pyplot.show()
