import numpy as np

MAGNETS = np.array([[0,0.8,-0.25],
                    [(2*np.sqrt(3))/5,-0.4,-0.25],
                    [-(2*np.sqrt(3))/5,-0.4,-0.25]])
T_LENGHT = 11.
FRICTION = 0.4
PROPOTIONAL_CONST = 5.
MASS = 1.


RESOLUTION = 2000         #Resolution in pixel
STEP_SIZE = 2.8/RESOLUTION      #stepsize for deflections
STEP_COUNT = 100
STEP_WIDE = 99
MAGNET_EPSILON = 0.04

MAX_PROCESSES = 5
SERVER = '127.0.0.1'
PORT = 5000
PASSWORD = 'abc'.encode(encoding='utf_8', errors='strict')
DEFLECTIONS = 10000

IMG_NAME = 'output.png'

INITIAL_DEFLECTION_X = -1.4
INITIAL_DEFLECTION_Y = 1.4
