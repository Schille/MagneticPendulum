from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
  name = 'PendulumPath',
  ext_modules=[
    Extension('c_PendulumPath', ['c_PendulumPath.pyx'])
    ],
  cmdclass = {'build_ext': build_ext}
)
