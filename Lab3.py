import numpy as np
import matplotlib.pyplot as plt

# Create 1-D arrays for x,y dimensions

xlist = np.linspace(-10.0, 10.0, 100) 
ylist = np.linspace(-10.0, 10.0, 100)

# Create 2-D grid xlist,ylist values

X,Y = np.meshgrid(xlist, ylist) 

EX,EY = np.meshgrid(xlist, ylist) 

'''
Triple apostrophes mark a block comment. 
EX and EY are the components of a vector field
E is its magnitude
'''

"""
FIELD ONE
"""
# EX=1*Y # x-comp
# EY=-1*X # y-comp
# E=np.sqrt(EX**2+EY**2) # magnitude 
"""
FIELD TWO
"""
# EX=(1/np.sqrt(2))*(X/X) # x-comp
# EY=(-1/np.sqrt(2))*(Y/Y) # y-comp
# E=np.sqrt(EX**2+EY**2) # magnitude 
"""
FIELD THREE
"""
# EX=(X/np.sqrt(2)) # x-comp
# EY=(Y/np.sqrt(2)) # y-comp
# E=np.sqrt(EX**2+EY**2) # magnitude 
"""
FIELD FOUR
"""
# EX=-1*Y # x-comp
# EY=1*X # y-comp
# E=np.sqrt(EX/EX) # magnitude  
"""
FIELD FIVE
"""
# EX=X/X # x-comp
# EY=Y/Y # y-comp
# E=(X + Y)**2 # magnitude 
"""
FIELD SIX
# """
# EX=X # x-comp
# EY=Y # y-comp
# E=np.sqrt(EX**2+EY**2) # magnitude 









# plot magnitude of E using filled contours

levels=np.linspace(np.min(E), np.max(E)+0.1, 20)
CS1=plt.contourf(X, Y, E ,levels,cmap=plt.cm.jet)
plt.colorbar(CS1, shrink=0.8)

# plot field lines
plt.streamplot(X, Y, EX, EY, color=E, linewidth=1, cmap=plt.cm.magma)

plt.axis('equal')
plt.show()

  
