import numpy as np

MAGNETS = np.array([[0,0.8,-0.25],
                    [(2*np.sqrt(3))/5,-0.4,-0.25],
                    [-(2*np.sqrt(3))/5,-0.4,-0.25]])
T_LENGHT = 11.
FRICTION = 0.4
PROPOTIONAL_CONST = 5.
MASS = 1.


RESOLUTION = 100    #Resolution in pixel
STEP_SIZE = 2.8/RESOLUTION      #stepsize for deflections
STEP_COUNT = 100
STEP_WIDE = 99
MAGNET_EPSILON = 0.04

MAX_PROCESSES = 3
SERVER = '192.168.1.3'
PORT = 5005
PASSWORD = 'abc'.encode(encoding='utf_8', errors='strict')
CHUNKSIZE = 200

REPAINT = 20

DEFLECTIONS = 10000

IMG_NAME = 'output.png'

INITIAL_DEFLECTION_X = -1.4
INITIAL_DEFLECTION_Y = 1.4
