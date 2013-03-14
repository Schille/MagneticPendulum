from multiprocessing.managers import BaseManager
from ClusterQueueManager import ClusterQueueManager
import Parameter
import time
import Image
import sys


        
def startServer():
    print('MagneticPendulum  -Cluster/Server')
    print('--------------------------------------------')
    print('Image resolution: {0}x{0} Output: {1}'.format(Parameter.RESOLUTION, Parameter.IMG_NAME))
    print('============================================')
    print('Now waiting to have some working clients.')
    import Simulation
    manager = ClusterQueueManager()
    data = []
    coordinates = manager.getCoordinates()
    values = manager.getValues()
    im= Image.new('RGB', (Parameter.RESOLUTION, Parameter.RESOLUTION))
    pixel = [] + [0]*(Parameter.RESOLUTION**2)
    Simulation.createAllCoordinates(coordinates, data)
    start = time.time()
    manager.start()
    while not coordinates.empty():
        while manager.getRunningClients() > 0:
            if not values.empty():
                print("Receiving values...")
                Simulation.drawImage(im, data, pixel, values)
            time.sleep(Parameter.REPAINT)
        time.sleep(.5)
    print("Coordinates are now completely distributed.")
    
    while manager.getRunningClients() > 0:
        time.sleep(Parameter.REPAINT)
        print('Waiting for {0} clients to be done'.format(manager.getRunningClients()))
    Simulation.drawImage(im, data, pixel, values)
    print('Image succeeded. Time consumed: {0:.2f}s'.format((time.time() - start)))
    print('Exiting...')
    sys.exit(0)
