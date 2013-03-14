import numpy as np
import Parameter
import argparse
import time
import Client
import Equations as calc
import signal
import sys
import Standalone
import ClusterServer



def signal_handler(signal, frame):
    print('Calculation interrupted')
    sys.exit(0)


def createAllCoordinates(coordinates, data):
    x = Parameter.INITIAL_DEFLECTION_X
    y = Parameter.INITIAL_DEFLECTION_Y
    data = np.zeros((Parameter.RESOLUTION,Parameter.RESOLUTION), dtype=np.uint8)
    counter = 0
    for row in data:
        for column in row:
            coordinates.put((x, y, counter))
            counter += 1
            x = x + Parameter.STEP_SIZE
        x = Parameter.INITIAL_DEFLECTION_X
        y = y - Parameter.STEP_SIZE
    

def workerThread(myCoordinates, myWorkerRunning, myPixel):
    myWorkerRunning.value += 1
    if myCoordinates.empty():
        myWorkerRunning.value -= 1
        return
    else:
        while not myCoordinates.empty():
            coord = myCoordinates.get() 
            print('Calculation for: x={0} y={1}'.format(coord[0], coord[1]))
            color = calc.runPendulum(coord[0], coord[1])
            myPixel.put((coord[2],color))
            myPixel.task_done()
            myCoordinates.task_done()
        myWorkerRunning.value -= 1
    return 0


def fetchValues(pixel, myValues):
    for i in range(0,myValues.qsize()):
        entry = myValues.get()
        pixel[entry[0]] = entry[1]
        

def drawImage(im, data, pixel, myValues):
    fetchValues(pixel, myValues)
    if data is not None:
        im.putdata(pixel)
        im.save(Parameter.IMG_NAME)
    
    

        
    
    
  
 
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--client", help="starts an client instance", action="store_true")
    parser.add_argument("-s", "--server", help="starts an server instance, which also paints the output",\
                        action="store_true")
    args = parser.parse_args()
    
    if args.client:
        Client.startClient()
    elif args.server:
        ClusterServer.startServer()
    else:
        Standalone.startStandalone()

