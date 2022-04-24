from matplotlib import pyplot as plt
import math
import time
seconds_of_computation_time = 90
Gravitational_constant = 0.00000000006674
bounds_of_calculation_left = -50000
bounds_of_calculation_right = 50000
ListOfGravitationalObjects = []
newX = []
newY = []
oldX = []
oldY = []
ListOfCoords2D = []

class Gravitational_Object:
    x_cord = 0 #meters
    y_cord = 0 #meters
    x_velocity = 0
    y_velocity = 0
    mass = 1 #kg
    color = "black"

    def __init__(self, x, y,v_x,v_y,inMass, inColor):
        self.x_cord = x
        self.y_cord = y
        self.x_velocity = v_x
        self.y_velocity = v_y
        self.mass = inMass
        self.color = inColor

    def accelerate_this_by(self,distance_x,distance_y,mass_two):
        magnitude = ((abs(distance_x - self.x_cord) ** 2) + (abs(distance_y - self.y_cord) ** 2)) ** 0.5
        acceleration = (Gravitational_constant*mass_two)/(magnitude**2)
        x_unit_component_of_velocity_times_acceleration = float(distance_x - self.x_cord )/ magnitude * acceleration
        y_unit_component_of_velocity_times_acceleration = float(distance_y - self.y_cord )/ magnitude * acceleration
        self.x_velocity = self.x_velocity + x_unit_component_of_velocity_times_acceleration
        self.y_velocity = self.y_velocity + y_unit_component_of_velocity_times_acceleration

    def update_positon(self):
        self.x_cord = self.x_cord + self.x_velocity
        self.y_cord = self.y_cord + self.y_velocity

def current_milli_time():
    return round(time.time() * 1000)

def setup(ListOfCoords2D, grav_list):
    newListOfCords = ListOfCoords2D
    for i in range(0, len(grav_list)):
        tempListX = []
        tempListY = []
        tempListX.append(grav_list[i].x_cord)
        tempListY.append(grav_list[i].y_cord)

        newListOfCords.append(tempListX)
        newListOfCords.append(tempListY)
    return newListOfCords

def animate_and_update(grav_list,ListOfCoords2D):
    # Mention x and y limits to define their range
    plt.xlim(bounds_of_calculation_left, bounds_of_calculation_right)
    plt.ylim(bounds_of_calculation_left, bounds_of_calculation_right)
    for i in range(0, len(grav_list)):
        grav_list[i].update_positon()  # called here to avoid strange issues with the order in which calculations are made
        ListOfCoords2D[(i*2)].append(grav_list[i].x_cord) #every grav obj has two entries in ListOfCords2D, when i is odd, we get the x cord
        ListOfCoords2D[(i*2)+1].append(grav_list[i].y_cord) #when its even we get the y cord. We multiply i by 2 as shown to do this.

        #building out the 'old' points
        xCords = []
        yCords = []
        for j in range(0,len(ListOfCoords2D[(i*2)])-5):
            if(j>=0):
                xCords.append(ListOfCoords2D[(i*2)][j])
                yCords.append(ListOfCoords2D[(i*2)+1][j])
        # xCord.append(grav_list[i].x_cord)
        # yCord.append(grav_list[i].y_cord)
        # Ploting graph
        plt.plot(ListOfCoords2D[(i*2)], ListOfCoords2D[(i*2)+1], color=grav_list[i].color,markersize=40)
        plt.plot(xCords, yCords, color="white",markersize = 39)
    plt.pause(0.0001)

#Create and add gravitational objects here
GravObj1 = Gravitational_Object(1,1,1,-1,29890000000000000000,"gold")
GravObj2 = Gravitational_Object(-1000,20000,-300,-50,298900000,"blue")
GravObj3 = Gravitational_Object(1000,-5000,-500,-70,10000,"green")
GravObj4 = Gravitational_Object(2000,-10000,-200,-50,100,"red")
GravObj5 = Gravitational_Object(-50000,-10000,500,-50,100000,"cyan")
ListOfGravitationalObjects.append(GravObj1)
ListOfGravitationalObjects.append(GravObj2)
ListOfGravitationalObjects.append(GravObj3)
ListOfGravitationalObjects.append(GravObj4)
ListOfGravitationalObjects.append(GravObj5)


ListOfCoords2D = setup(ListOfCoords2D, ListOfGravitationalObjects)
elapsed_milliseconds = 0
initial_milliseconds = current_milli_time()
counter = 0
while(elapsed_milliseconds / 1000 < seconds_of_computation_time):
    if(int(elapsed_milliseconds / 1000) % 10 == 0):
        print(str(elapsed_milliseconds/ 10 / seconds_of_computation_time) + "% Done with Simulation" )
    PreviousGravObjs = ListOfGravitationalObjects.copy()
    for objN1 in ListOfGravitationalObjects:
        for objN2 in ListOfGravitationalObjects:
            if(objN1 != objN2):
                objN1.accelerate_this_by(distance_x = objN2.x_cord,distance_y = objN2.y_cord,mass_two = objN2.mass)
    animate_and_update(ListOfGravitationalObjects,ListOfCoords2D)

    elapsed_milliseconds = current_milli_time() - initial_milliseconds
    #print(str(elapsed_milliseconds / 1000) + "of Computer Time Used")
plt.show()