from ClusterQueueManager import ClusterQueueManager
import Parameter

class ClusterClient():
    
    def __init__(self):
        self.__connectToServer()


    def __connectToServer(self):
        manager = ClusterQueueManager(address=(Parameter.SERVER, Parameter.PORT),\
                                   authkey=Parameter.PASSWORD)

def startClient():
    manager = Manager()
    workerRunning = manager.Value('i', 0)
    
