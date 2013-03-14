from ClusterQueueManager import ClusterQueueManager
import Parameter
import time
from multiprocessing import Manager, Process

def startClient():
    import Simulation
    manager = ClusterQueueManager()
    localManager = Manager()
    manager.connect()
    manager.clientStart()
    all_coordinates = manager.getCoordinatesQueue()
    all_values = manager.getValuesQueue()
    lock = manager.getCoordinatesLock()
    localCoordinates = localManager.Queue()
    localvalues = localManager.Queue()
    workerRunning = localManager.Value('i', 0)
    
    while not all_coordinates.empty():
        lock.acquire()
        fetchCoordinates(localCoordinates, all_coordinates)
        lock.release()
        
        while workerRunning.get() < Parameter.MAX_PROCESSES:
            Process(target=Simulation.workerThread,args=(localCoordinates, workerRunning, localvalues)).start()
            time.sleep(0.5)
        
        while localCoordinates.qsize() > 5:
            while not localvalues.empty():
                all_values.put(localvalues.get())
        time.sleep(1)
        
    while workerRunning.get():
        print("Waiting for {0} worker to be done.". format(str(workerRunning.get())))
        time.sleep(1)
    
    while not localvalues.empty():
        all_values.put(localvalues.get())
        
    manager.clientDone()
    return 0
        
            
def fetchCoordinates(myLocalQueue, myCoordinatesQueue):
    print("Fetching coordinates")
    count = 0
    while (count < Parameter.CHUNKSIZE and not myCoordinatesQueue.empty()):
        myLocalQueue.put(myCoordinatesQueue.get())
        count += 1
    print("Fetching of {0} coordinates done.".format(count))