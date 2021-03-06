from multiprocessing.managers import BaseManager
from multiprocessing import Manager
import Parameter

class ClusterQueueManager(BaseManager):
    
    def __init__(self):
        BaseManager.__init__(self,address=(Parameter.SERVER, Parameter.PORT), authkey=Parameter.PASSWORD)
        self._manager = Manager()
        self._coordinates = self._manager.Queue()
        self._values = self._manager.Queue()
        self._lock = self._manager.Lock()
        self._clientCounter = self._manager.Value('i', 0)
        self.register('clientStart', self.addClient)
        self.register('clientDone', self.removeClient)
        self.register('getCoordinatesLock', self.getCoordinatesLock)
        self.register('getCoordinatesQueue', self.getCoordinates)
        self.register('getValuesQueue', self.getValues)

    def getCoordinatesLock(self):
        return self._lock

    def getCoordinates(self):
        return self._coordinates
    
    def getValues(self):
        return self._values
    
    def addClient(self):
        self._clientCounter.set(self._clientCounter.get() + 1)
        print("A client has been connected. Now {0} clients working.".format(self._clientCounter.get()))
    
    def removeClient(self):
        self._clientCounter.set(self._clientCounter.get() - 1)
        print("A client has been disconnected. Now {0} client(s) working.".format(self._clientCounter.get()))
        
    def getRunningClients(self):
        return self._clientCounter.get()    