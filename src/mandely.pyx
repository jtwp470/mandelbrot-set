# mandely.pyx
# cython: profile=True

import cython

@cython.profile(False)
def mandel(double x, double y, int max_iter=30):
    cdef double z_real = 0., z_imag = 0.
    cdef int i

    for i in range(0, max_iter):
        z_real, z_imag = (z_real * z_real - z_imag * z_imag + x,
                          2*z_real * z_imag + y)
        if (z_real * z_real + z_imag * z_imag) >= 3.5 * 3.5:
            return i
    return max_iter
