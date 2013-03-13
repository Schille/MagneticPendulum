def calcPendulumPath(myCoords,double friction, double lenght, double mass, float propconst, float gr, int magnets, posmagnets ):
    double myX,double myY,double myXdot,double myYdot = myCoords 
    
    cdef double xdotdot = - (friction * myXdot) - ((gr / lenght) * myX) \
     - ((propconst / mass) * calcMagenticPotentialsToX(myX,myY, magnets,posmagnets))
    
    cdef double ydotdot = - (friction * myYdot) - ((gr / lenght) * myY) \
    - ((propconst / mass) * calcMagenticPotentialsToY(myX,myY, magnets,posmagnets))
        
    return [myXdot,myYdot, xdotdot, ydotdot]

def calcMagenticPotentialsToX( double myX, double myY, int magnets, posmagnets):
    cdef double result = 0
    for i from 0 <= i < magnets:
        result += ((myX - posmagnets[i][0])**2 + (myY - posmagnets[i][1])**2 \
                    + (0.25)**2)**(-3./2.) * (myX - posmagnets[i][0])
    #print("X: " + str(result))q
    return result

def calcMagenticPotentialsToY(double myX,double myY,int magnets, posmagnets):
    cdef double result = 0
    for i from 0 <= i < magnets:
        result += ((myX - posmagnets[i][0])**2 + (myY - posmagnets[i][1])**2 \
                   + (0.25)**2)**(-3./2.) * (myY - posmagnets[i][1])
    #print("Y: " + str(result))
    return result
