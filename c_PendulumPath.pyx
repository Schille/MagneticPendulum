def calcPendulumPath(double x,double y ,double xdot,double ydot,double friction, double lenght, double mass, float propconst, float gr, int magnets,double x1,double y1,double x2, double y2, double x3,double y3 ):

    
    cdef double xdotdot = - (friction * xdot) - ((gr / lenght) * x) \
     - ((propconst / mass) * (((x - x1)**2 + (y - y1)**2 \
                   + (0.25)**2)**(-3./2.) * (x - x1) + \
        ((x - x2)**2 + (y - y2)**2 \
                   + (0.25)**2)**(-3./2.) * (x - x2) + \
        ((x - x3)**2 + (y - y3)**2 \
                   + (0.25)**2)**(-3./2.) * (x - x3)))
    
    cdef double ydotdot = - (friction * ydot) - ((gr / lenght) * y) \
    - ((propconst / mass) * (((x - x1)**2 + (y - y1)**2 \
                   + (0.25)**2)**(-3./2.) * (y - y1) + \
        ((x - x2)**2 + (y - y2)**2 \
                   + (0.25)**2)**(-3./2.) * (y - y2) + \
        ((x - x3)**2 + (y - y3)**2 \
                   + (0.25)**2)**(-3./2.) * (y - y3)))
        
    return [xdot,ydot, xdotdot, ydotdot]

