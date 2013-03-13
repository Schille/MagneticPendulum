from multiprocessing.managers import BaseManager
from multiprocessing import Manager


class ClusterQueueManager(BaseManager):
    
    def __init__(self):
    _manager = Manager()
    _coordinates = Manager.Queue()
    _values = Manager.Queue()
    self.register('getCoordinatesQueue', getCoordinatesQueue)
    self.register('getValesQueue', getCoordinatesQueue)
    
    
    def getCoordinatesQueue(self):
        return self._coordinates
    
    def getValuesQueue(self):
        return self._values