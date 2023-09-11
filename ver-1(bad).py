# ---------------------------------------------------------------------------- #
#                                     SETUP                                    #
# ---------------------------------------------------------------------------- #

import cmath
import matplotlib as mpl
import matplotlib.pyplot as plt
from itertools import product


# ---------------------------------------------------------------------------- #
#                                   FUNCTIONS                                  #
# ---------------------------------------------------------------------------- #

def mandelbrotCheck(c):
    zList = [0]
    for i in range(0, 2001):
        complexC = (zList[i]**2)+c
        if cmath.polar(complexC)[0] >= 2:
            return False
        else:
            zList.append(complexC)
    return True

def graphVals(x1,x2,step):
    xList = []
    yList = []
    for a, b in product(range(x1,x2+6,step),range(x1,x2+6,step)):
        z = complex(a/x2,b/x2)
        if mandelbrotCheck(z):
            xList.append(a/x2)
            yList.append(b/x2)
    return(xList,yList)


# ---------------------------------------------------------------------------- #
#                                    SCRIPT                                    #
# ---------------------------------------------------------------------------- #

xVals, yVals = graphVals(-200,100,1)

plt.xticks([])
plt.yticks([])
plt.scatter(xVals,yVals)
plt.savefig(f'./figs/v1-qual{300}_iter{2000}.png')
plt.show()


# ----------------------------------- TO DO ---------------------------------- #
# numpy array [?]
# itertools [x]
# functools [o]
# imshow [o]
# pillow [o]
