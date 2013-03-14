from multiprocessing.managers import BaseManager
from ClusterQueueManager import ClusterQueueManager
import Parameter
import time
import Image
import sys


        
def startServer():
    import Simulation
    manager = ClusterQueueManager(address=(Parameter.SERVER, Parameter.PORT),\
                                   authkey=Parameter.PASSWORD)
    manager.start()
    data = []
    coordinates = manager.getCoordinates()
    im= Image.new('RGB', (Parameter.RESOLUTION, Parameter.RESOLUTION))
    pixel = [] + [0]*(Parameter.RESOLUTION**2)
    Simulation.createAllCoordinates(coordinates, data)
    values = manager.getValuesQueue() 
    start = time.time()
    while not coordinates.empty():
        Simulation.drawImage(im, data, pixel, values)
        time.sleep(Parameter.REPAINT)
    Simulation.drawImage(im, data, pixel, values)
    print('Image succeeded. Time consumed: {0:.2f}s'.format((time.time() - start)))
    print('Exiting...')
    sys.exit(0)
