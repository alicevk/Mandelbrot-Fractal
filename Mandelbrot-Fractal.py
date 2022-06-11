import cmath
import matplotlib as mpl
import matplotlib.pyplot as plt

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
    for a in range(x1,x2+6,step):
        for b in range(x1,x2+6, step):
            z = complex(a/x2,b/x2)
            if mandelbrotCheck(z):
                xList.append(a/x2)
                yList.append(b/x2)
    return(xList,yList)

xVals, yVals = graphVals(-200,100,1)

plt.scatter(xVals,yVals)
plt.show()


# ----- TO DO:
# itertools
# functools
# imshow
# pillow
