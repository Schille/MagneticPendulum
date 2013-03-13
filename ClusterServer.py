'''
Created on 13.03.2013

@author: RStein
'''
from multiprocessing.managers import BaseManager
from ClusterQueueManager import ClusterQueueManager
import Parameter


class ServerManager(BaseManager):
   
        
    def registerClient(self):
        self.clients += 1
        
    def unregisterClient(self):
        self.clients -= 1

  
    def __setUp_Server(self):
        manager = ClusterQueueManager(address=(Parameter.SERVER, Parameter.PORT),\
                                   authkey=Parameter.PASSWORD)
        
        manager.register("registerClient",registerClient)
        manager.register("unregisterClient", unregisterClient)
        server = manager.get_server()
        server.start()
        
        
    def __init__(self):
        self.clients = 0
        self.__setUp_Server()
        
        
        