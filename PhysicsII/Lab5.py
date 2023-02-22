import numpy as np
import matplotlib.pyplot as plt

# define charges and their positions here

#charges = [(1.0, [1.0, 0.0]),(1.0, [-1.0, 0.0])]
charges = []
for i in range (-50,50):
  prepackaged_list = (1.0, [0.0, i/10])
  charges.append(prepackaged_list)
prepackaged_list = (-25.0, [-10.0, 0])
charges.append(prepackaged_list)
prepackaged_list = (-5.0, [-4, 5])
charges.append(prepackaged_list)
prepackaged_list = (-5.0, [-4, 4])
charges.append(prepackaged_list)
prepackaged_list = (5.0, [-6, 5])
charges.append(prepackaged_list)
prepackaged_list = (5.0, [-6, 4])
charges.append(prepackaged_list)

xlist = np.linspace(-15.0, 15.0, 100) # Create 1-D arrays for x,y dimensions
ylist = np.linspace(-15.0, 15.0, 100)

X,Y = np.meshgrid(xlist, ylist) # Create 2-D grid xlist,ylist values

# create arrays for Ex, Ey and electric potential V and fill them with zeros
EX=np.zeros(len(X))
EY=np.zeros(len(X))
V=np.zeros(len(X))

# apply superposition
for C in charges:
  R=((X-C[1][0])**2+(Y-C[1][1])**2)**(1/2)
  EX=EX+C[0]*(X-C[1][0])/R**3
  EY=EY+C[0]*(Y-C[1][1])/R**3
  V=V+C[0]/R


plt.figure() # Create a new figure window
plt.axis('equal') # set aspect ratio

# plot electric potential using filled contours
levels=np.linspace(np.min(V), np.max(V), 21)
CS1=plt.contourf(X, Y, V ,levels,cmap=plt.cm.jet)
plt.colorbar(CS1, shrink=0.8)
plt.xlabel("Position in x direction")
plt.ylabel("Position in y direction")

# plot field lines
plt.streamplot(X, Y, EX, EY, color=V, linewidth=2, cmap=plt.cm.magma)
plt.show()

