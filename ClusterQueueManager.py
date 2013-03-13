from multiprocessing.managers import BaseManager
from multiprocessing import Manager
import Parameter

import time



class ClusterQueueManager(BaseManager):
    clientsRunning = 0 
    def __init__(self, myMode=''):
        BaseManager.__init__(self,address=(Parameter.SERVER, Parameter.PORT), authkey=Parameter.PASSWORD)
        self._manager = Manager()
        self._coordinates = self._manager.Queue()
        self._values = self._manager.Queue()
        ClusterQueueManager.register('getCoordinatesQueue', self.getCoordinatesQueue)
        ClusterQueueManager.register('getValesQueue', self.getCoordinatesQueue)
    
        if myMode == 'Server':
            print('Server')
            self.register('clientStart', self.addClient)
            self.register('clientDone', self.removeClient)
        else:
            self.register('clientStart')
            self.register('clientDone')
            
        
    
    def getCoordinatesQueue(self):
        return self._coordinates
    
    def getValuesQueue(self):
        return self._values

 
    def addClient(self):
        print('added client')
        self.clientsRunning += 1
    
    def removeClient(self):
        self.clientsRunning -= 1
    