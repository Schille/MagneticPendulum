from multiprocessing.managers import BaseManager
from multiprocessing import Manager


class ClusterQueueManager(BaseManager):
    
    
    def __init__(self, myMode):
        self.clientsRunning = 0
        self._manager = Manager()
        self._coordinates = Manager.Queue()
        self._values = Manager.Queue()
        self.register('getCoordinatesQueue', self.getCoordinatesQueue)
        self.register('getValesQueue', self.getCoordinatesQueue)
    
        if myMode == 'Server':
            self.register('clientRun', self.selfe.addClient)
            self.register('clientDone', self.removeClient)
        else:
            self.register('clientRun')
            self.register('clientDone')
        
    
    def getCoordinatesQueue(self):
        return self._coordinates
    
    def getValuesQueue(self):
        return self._values
    
    def addClient(self):
        self.clientsRunning += 1
    
    def removeClient(self):
        self.clientsRunning -= 1
    
    