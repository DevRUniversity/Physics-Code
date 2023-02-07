import random

from matplotlib import pyplot as plt
import math
import time
seconds_of_computation_time = 600 #Ten Minutes
Gravitational_constant = 0.00000000006674
bounds_of_calculation_left = -4000000
bounds_of_calculation_right = 4000000
speed_of_light = 299792458
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
    schwartzchild_radius = 0
    color = "black"

    def __init__(self, x, y,v_x,v_y,inMass, inColor):
        self.x_cord = x
        self.y_cord = y
        self.x_velocity = v_x
        self.y_velocity = v_y
        self.mass = inMass
        self.color = inColor
        self.schwartzchild_radius = 2*Gravitational_constant*self.mass/(speed_of_light**2)
        if(self.schwartzchild_radius < 2): #2 Meters is arbitrary, but for what we are looking at most objects are probably wider than 2 meters. The idea is that if they are sufficently close they combine.
            self.schwartzchild_radius = 2

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

    def distance_from(self, distance_x, distance_y):
        magnitude = ((abs(distance_x - self.x_cord) ** 2) + (abs(distance_y - self.y_cord) ** 2)) ** 0.5
        return magnitude

    def add_mass(self, newMass):
        self.mass = self.mass + newMass


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

def calculate_marker_size(mass):
    markersize = (int(mass/10000000000000)) + 1
    if(markersize > 15):
        markersize = 15
    return markersize

def get_random(lR,rR):
    return random.randrange(lR,rR,1)

def animate_and_update(grav_list,ListOfCoords2D):
    # Mention x and y limits to define their range
    plt.clf()
    plt.xlim(bounds_of_calculation_left, bounds_of_calculation_right)
    plt.ylim(bounds_of_calculation_left, bounds_of_calculation_right)
    for i in range(0, len(grav_list)):
        grav_list[i].update_positon()  # called here to avoid strange issues with the order in which calculations are made
        ListOfCoords2D[(i*2)].append(grav_list[i].x_cord) #every grav obj has two entries in ListOfCords2D, when i is odd, we get the x cord
        ListOfCoords2D[(i*2)+1].append(grav_list[i].y_cord) #when its even we get the y cord. We multiply i by 2 as shown to do this.

        #building out the 'old' points
        xCords = []
        yCords = []
        for j in range(len(ListOfCoords2D[(i*2)])-15,len(ListOfCoords2D[(i*2)])-1):
            if(j>=0):
                xCords.append(ListOfCoords2D[(i*2)][j])
                yCords.append(ListOfCoords2D[(i*2)+1][j])
        # xCord.append(grav_list[i].x_cord)
        # yCord.append(grav_list[i].y_cord)
        # Ploting graph

        markersize = calculate_marker_size(grav_list[i].mass)
        plt.plot(xCords, yCords, color=grav_list[i].color,marker=".", markersize=markersize)
        #plt.plot(xCords, yCords, color="white",markersize = 50)
    plt.pause(0.01)

#Create and add gravitational objects here
GravObj1 = Gravitational_Object(get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,2989000000,"magenta") #Asteroid size
GravObj2 = Gravitational_Object(get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,2989000000,"magenta") #Asteroid size
GravObj3 = Gravitational_Object(get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,2989000000,"magenta") #Asteroid size
GravObj4 = Gravitational_Object(get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,2989000000,"magenta") #Asteroid size
GravObj5 = Gravitational_Object(get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,2989000000,"magenta") #Asteroid size
GravObj6 = Gravitational_Object(get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,2989000000,"magenta") #Asteroid size
GravObj7 = Gravitational_Object(get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,998999000000000,"green") #Planet Like
GravObj8 = Gravitational_Object(get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,998999000000000,"green") #Planet Like
GravObj9 = Gravitational_Object(-9000000,-4000000,40000,18500,10000000000,"cyan") #Interstellar Object
GravObj10 = Gravitational_Object(3000000,-3000000,4000,4000,10000,"red") #Spacecraft
GravObj11 = Gravitational_Object(get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,999999999980000000,"blue") #Gas Giant
GravObj12 = Gravitational_Object(get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right),get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,get_random(bounds_of_calculation_left,bounds_of_calculation_right)/1000,999999999980000000,"blue") #Gas Giant
GravObjSun1 = Gravitational_Object(800000,800000,-7000,0,2989000000000000000000000,"gold") #Sun in this system
GravObjSun2 = Gravitational_Object(-800000,-800000,7000,0,2989000000000000000000000,"gold") #Sun in this system
#GravObj11 = Gravitational_Object(50000,50000,-1,0,99999999999999999999999999999999,"black") #Blackhole
ListOfGravitationalObjects.append(GravObj1)
ListOfGravitationalObjects.append(GravObj2)
ListOfGravitationalObjects.append(GravObj3)
ListOfGravitationalObjects.append(GravObj4)
ListOfGravitationalObjects.append(GravObj5)
ListOfGravitationalObjects.append(GravObj6)
ListOfGravitationalObjects.append(GravObj7)
ListOfGravitationalObjects.append(GravObj8)
ListOfGravitationalObjects.append(GravObj9)
ListOfGravitationalObjects.append(GravObj10)
ListOfGravitationalObjects.append(GravObj11)
ListOfGravitationalObjects.append(GravObj12)
ListOfGravitationalObjects.append(GravObjSun1)
ListOfGravitationalObjects.append(GravObjSun2)

# GravObj1 = Gravitational_Object(1,1,1,-1,2989000000000000000000000,"gold") #Sun in this system
# GravObj2 = Gravitational_Object(0,1000000,-3500,3000,2989000000,"magenta") #Asteroid size
# GravObj3 = Gravitational_Object(0,1500000,-2000,3000,2989000000,"magenta") #Asteroid size
# GravObj4 = Gravitational_Object(1000000,0,5400,6000,2989000000,"magenta") #Asteroid size
# GravObj5 = Gravitational_Object(1500000,0,3000,9000,2989000000,"magenta") #Asteroid size
# GravObj6 = Gravitational_Object(1230000,0,7730,-3705,2989000000,"magenta") #Asteroid size
# GravObj7 = Gravitational_Object(4000000,4000000,-7700,-2000,998999000000000,"green") #Planet Like
# GravObj8 = Gravitational_Object(-4000000,-4000000,7700,2000,998999000000000,"green") #Planet Like
# GravObj9 = Gravitational_Object(-9000000,-4000000,40000,18500,10000000000,"cyan") #Interstellar Object
# GravObj10 = Gravitational_Object(3000000,-3000000,4000,4000,10000,"red") #Spacecraft
# GravObj11 = Gravitational_Object(4000000,-4000000,1000,10500,999999999980000000,"blue") #Gas Giant
# GravObj12 = Gravitational_Object(-4000000,4000000,1000,-10500,999999999980000000,"blue") #Gas Giant
# #GravObj11 = Gravitational_Object(50000,50000,-1,0,99999999999999999999999999999999,"black") #Blackhole
# ListOfGravitationalObjects.append(GravObj1)
# ListOfGravitationalObjects.append(GravObj2)
# ListOfGravitationalObjects.append(GravObj3)
# ListOfGravitationalObjects.append(GravObj4)
# ListOfGravitationalObjects.append(GravObj5)
# ListOfGravitationalObjects.append(GravObj6)
# ListOfGravitationalObjects.append(GravObj7)
# ListOfGravitationalObjects.append(GravObj8)
# ListOfGravitationalObjects.append(GravObj9)
# ListOfGravitationalObjects.append(GravObj10)
# ListOfGravitationalObjects.append(GravObj11)
# ListOfGravitationalObjects.append(GravObj12)

plt.xlim(bounds_of_calculation_left, bounds_of_calculation_right)
plt.ylim(bounds_of_calculation_left, bounds_of_calculation_right)
print("Type \'Y\' to initiate the program:")
firstPass = True
ListOfCoords2D = setup(ListOfCoords2D, ListOfGravitationalObjects)
elapsed_milliseconds = 0
initial_milliseconds = current_milli_time()
counter = 0
while(elapsed_milliseconds / 1000 < seconds_of_computation_time):
    plt.xlim(bounds_of_calculation_left, bounds_of_calculation_right)
    plt.ylim(bounds_of_calculation_left, bounds_of_calculation_right)
    if(int(elapsed_milliseconds / 1000) % 10 == 0):
        print(str(elapsed_milliseconds/ 10 / seconds_of_computation_time) + "% Done with Simulation" )
    PreviousGravObjs = ListOfGravitationalObjects.copy()
    for objN1 in ListOfGravitationalObjects:
        for objN2 in ListOfGravitationalObjects:
            if(objN1 != objN2):
                if(objN2.distance_from(objN1.x_cord,objN1.y_cord) <= objN1.schwartzchild_radius):
                    objN1.add_mass(objN2.mass)
                    ListOfGravitationalObjects.remove(objN2)
                else:
                    objN1.accelerate_this_by(distance_x = objN2.x_cord,distance_y = objN2.y_cord,mass_two = objN2.mass)
    animate_and_update(ListOfGravitationalObjects,ListOfCoords2D)
    if(firstPass):
        while (input() != "Y"):
            pass
        initial_milliseconds = current_milli_time() #First tick
        firstPass = False # No longer the first tick
    elapsed_milliseconds = current_milli_time() - initial_milliseconds
    #print(str(elapsed_milliseconds / 1000) + "of Computer Time Used")
plt.show()