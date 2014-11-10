from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("mandely", ["mandely.pyx"]),
]

setup(
    name = "Mandelbrot calc on Cython",
    cmdclass = {"build_ext": build_ext},
    ext_modules = ext_modules,
)
