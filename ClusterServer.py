'''
Created on 13.03.2013

@author: RStein
'''
from multiprocessing.managers import BaseManager
from ClusterQueueManager import ClusterQueueManager
import Parameter


class ServerManager(BaseManager):
    def __setUp_Server(self):
        manager = ClusterQueueManager(address=(Parameter.SERVER, Parameter.PORT),\
                                   authkey=Parameter.PASSWORD)
        
        server = manager.get_server()
        manager.start()
        
        
    def __init__(self):
        self.clients = 0
        self.__setUp_Server()
        
        
        