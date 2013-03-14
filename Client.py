from ClusterQueueManager import ClusterQueueManager
import Parameter
import time
from multiprocessing import Manager, Process

def startClient():
    print('MagneticPendulum  -Cluster/Client')
    print('--------------------------------------------')
    print('Connecting to server: {0} on port {1}'.format(Parameter.SERVER, Parameter.PORT))
    print('Working with {0} sub-processes in total.'.format(Parameter.MAX_PROCESSES))
    print('============================================')
    import Simulation
    manager = ClusterQueueManager()
    localManager = Manager()
    try:
        manager.connect()
    except:
        print("Could not connect to server, review settings!")
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
            if workerRunning.get() < localCoordinates.qsize():
                Process(target=Simulation.workerThread,args=(localCoordinates, workerRunning, localvalues)).start()
            else:
                break
            time.sleep(0.5)
    
        while not localCoordinates.empty():
            while not localvalues.empty():
                all_values.put(localvalues.get())
        time.sleep(1)
        
    while workerRunning.get() > 0:
        print("Waiting for {0} worker to be done.". format(str(workerRunning.get())))
        time.sleep(1)
    
    while not localvalues.empty():
        all_values.put(localvalues.get())
        
    manager.clientDone()
    print("Client Done.")
    return 0
        
            
def fetchCoordinates(myLocalQueue, myCoordinatesQueue):
    print("Fetching coordinates")
    count = 0
    while (count < Parameter.CHUNKSIZE and not myCoordinatesQueue.empty()):
        myLocalQueue.put(myCoordinatesQueue.get())
        count += 1
    print("Fetching of {0} coordinates done.".format(count))