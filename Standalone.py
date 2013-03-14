from multiprocessing import Manager, Process
import Parameter
import time
import sys
import Image

def startStandalone():
    import Simulation
    print('MagneticPendulum  -Standalone')
    print('--------------------------------------------')
    print('Image resolution: {0}x{0} Output: {1}'.format(Parameter.RESOLUTION, Parameter.IMG_NAME))
    print('Working with {0} sub-processes in total.'.format(Parameter.MAX_PROCESSES))
    print('============================================')
    start = time.time()
    im= Image.new('RGB', (Parameter.RESOLUTION, Parameter.RESOLUTION))
    data = []
    pixel = [] + [0]*(Parameter.RESOLUTION**2)
    manager = Manager()
    coordinates = manager.Queue()
    values = manager.Queue()
    workerRunning = manager.Value('i', 0)
    Simulation.createAllCoordinates(coordinates, data) 
    while workerRunning.get() < Parameter.MAX_PROCESSES:
        Process(target=Simulation.workerThread,args=(coordinates, workerRunning, values)).start()
        time.sleep(1)
    while workerRunning.value > 0:
        Simulation.drawImage(im, data, pixel, values)
        time.sleep(Parameter.REPAINT)
    Simulation.drawImage(im, data, pixel, values)
    print('Image succeeded. Time consumed: {0:.2f}s'.format((time.time() - start)))
    print('Exiting...')
    sys.exit(0)     