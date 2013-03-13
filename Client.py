from ClusterQueueManager import ClusterQueueManager
import Parameter

class ClusterClient():
    
    def __init__(self):
        self.__connectToServer()


    def __connectToServer():
        manager = ClusterQueueManager(address=(Parameter.SERVER, Parameter.PORT),\
                                   authkey=Parameter.PASSWORD)
        manager.connect()