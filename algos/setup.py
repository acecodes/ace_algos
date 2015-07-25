from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='Algorithms converted into Cython (compiled) format',
    ext_modules=cythonize("PythonCython.pyx"),
)
