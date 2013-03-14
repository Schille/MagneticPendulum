from ClusterQueueManager import ClusterQueueManager
import Parameter
import time
from multiprocessing import Manager, Process

def startClient():
    import Simulation
    manager = ClusterQueueManager()
    manager.connect()
    manager.clientStart()
    all_coordinates = manager.getCoordinatesQueue()
    all_values = manager.getValuesQueue()
    lock = manager.getCoordinatesLock()
    localCoordinates = manager.Queue()
    localvalues = manager.Queue()
    workerRunning = manager.Value('i', 0)
    
    while not all_coordinates.empty():
        lock.acquire()
        fetchCoordinates(localCoordinates, all_coordinates)
        lock.release()
        
        while workerRunning.value < Parameter.MAX_PROCESSES:
            Process(target=Simulation.workerThread,args=(localCoordinates, workerRunning, localvalues)).start()
        
        while localCoordinates.qsize() > 20:
            while not localvalues.empty():
                all_values.put(localvalues.get())
            time.sleep(5)
    return 0
        
            
def fetchCoordinates(myLocalQueue, myCoordinatesQueue):
    count = 0
    while (count < Parameter.CHUNKSIZE and not myCoordinatesQueue.empty()):
        myLocalQueue.put(myCoordinatesQueue.get())
        count += 1