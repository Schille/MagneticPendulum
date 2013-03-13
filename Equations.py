import numpy as np
from scipy import constants
from scipy.integrate import odeint
import Parameter
import c_PendulumPath

friction = Parameter.FRICTION
lenght = Parameter.T_LENGHT
mass = Parameter.MASS
propconst = Parameter.PROPOTIONAL_CONST
gr = constants.g
magnets = 3
x1 = Parameter.MAGNETS[0][0]
y1 = Parameter.MAGNETS[0][1]
x2 = Parameter.MAGNETS[1][0]
y2 = Parameter.MAGNETS[1][1]
x3 = Parameter.MAGNETS[2][0]
y3 = Parameter.MAGNETS[2][1]


def pendulumPath(myCoords,t):
    x, y , xdot, ydot = myCoords

    myXdot, myYdot, xdotdot, ydotdot = c_PendulumPath.calcPendulumPath(x, y , xdot, ydot, friction, lenght,\
                                   mass, propconst, gr, magnets, x1,y1,x2,y2,x3,y3)
    
    return np.array([myXdot,myYdot, xdotdot, ydotdot])
    
    """
    xdotdot = - (Parameter.FRICTION * myXdot) - ((constants.g / Parameter.T_LENGHT) * myX) \
     - ((Parameter.PROPOTIONAL_CONST / Parameter.MASS) * calcMagenticPotentialsToX(myX,myY))
    
    ydotdot = - (Parameter.FRICTION * myYdot) - ((constants.g / Parameter.T_LENGHT) * myY) \
    - ((Parameter.PROPOTIONAL_CONST / Parameter.MASS) * calcMagenticPotentialsToY(myX,myY))
    """
    
    
    
 

def calcMagenticPotentialsToX(myX, myY):
    result = 0
    for i in range(0,3):
        result += ((myX - Parameter.MAGNETS[i][0])**2 + (myY - Parameter.MAGNETS[i][1])**2 \
                    + (0.25)**2)**(-3./2.) * (myX - Parameter.MAGNETS[i][0])
    #print("X: " + str(result))q
    return result

def calcMagenticPotentialsToY(myX, myY):
    result = 0
    for i in range(0,3):
        result += ((myX - Parameter.MAGNETS[i][0])**2 + (myY - Parameter.MAGNETS[i][1])**2 \
                   + (0.25)**2)**(-3./2.) * (myY - Parameter.MAGNETS[i][1])
    #print("Y: " + str(result))
    return result
        
def runPendulum(myX, myY):
    time = np.linspace(0,Parameter.STEP_WIDE, Parameter.STEP_COUNT)
    atol, rtol = 1e-6, 1e-6
    result = odeint(pendulumPath, [myX,myY,0,0], time, atol=atol, rtol=rtol)
    magnetID = nearMagnet(result[-1, :2][0], result[-1, :2][1])
    if magnetID == 0:
        #print("Magnet Red")
        return (255,0,0)
    elif magnetID == 1:
        #print("Magnet Green")
        return (0,255,0)
    elif magnetID == 2:
        #print("Magnet Blue")
        return (0,0,255)
    else:
        #print("No Magnet")
        return (255,255,255)
        

def nearMagnet(myX, myY):
    for i in range(0, 3):
        cmpX = np.abs(myX - Parameter.MAGNETS[i][0])
        cmpY = np.abs(myY - Parameter.MAGNETS[i][1])
        if cmpX <= Parameter.MAGNET_EPSILON and cmpY <= Parameter.MAGNET_EPSILON:
            return i   
